from odoo import api, fields, models, SUPERUSER_ID
from odoo.tools.translate import _
from odoo.exceptions import UserError, ValidationError
import base64

class InterviewReviewsBr(models.Model):
    _name = "br.interview.review"

    name = fields.Char('Interview',related='interview_id.name', store=True)
    rev_type = fields.Many2one('br.review.type','Review Type', store=True,required=True)
    interview_id = fields.Many2one('br.interview', 'Interview', store=True)
    rating = fields.Integer("Rating",store=True)
    interviewer_ids = fields.Many2many('res.users', 'review_int_ids_rel', 'review_id1', 'review_id2',
                                       string='Interviewers')
    interviewer = fields.Many2one('res.users','Interviewer',store=True)

    @api.onchange('rev_type','rating')
    def _domain_interviewer(self):
        for record in self:
            record['interviewer_ids'] = record.interview_id.interviewer_ids

    @api.constrains('rating')
    def _check_rating(self):
        for record in self:
            if record.rating > 10:
               raise ValidationError("Rating should be less than 10")

class InterviewBrType(models.Model):
    _name = "br.review.type"

    name = fields.Char('Name', store=True)
    code = fields.Char('Code', store=True)

class InterviewBr(models.Model):
    _name = "br.interview"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Interview"

    name = fields.Char('Interview', default='/', store=True)
    applicant = fields.Char('Applicant', store=True,required=True)
    application = fields.Many2one('hr.applicant', 'Application', store=True)
    schedule_date = fields.Datetime('Schedule Date', default=lambda self: fields.datetime.now(), store=True)
    degree = fields.Many2one('hr.recruitment.degree','Degree',related='application.type_id')
    applied_job = fields.Many2one('hr.job', 'Applied Job', related='application.job_id')
    interviewer_ids = fields.Many2many('res.users','reviewer_ids_rel','reviewer_id1','reviewer_id2',string='Interviewers')
    review_ids = fields.One2many('br.interview.review','interview_id','Review')
    performance = fields.Char("Performance:",compute='_get_performance',store=True)
    review_summ = fields.Text("Review Summary",store=True)
    status = fields.Selection(
        [('new', 'Draft'), ('start', 'Start'), ('stop', 'Stop'), ('cancel', 'Cancelled')], 'Status',
        default='new', store=True)

    @api.model
    def create(self, vals):
        obj = super(InterviewBr, self).create(vals)
        if obj.name == '/':
            number = self.env['ir.sequence'].get('br.interview') or '/'
            obj.write({'name': number})
            obj.activity_system_manager()
        return obj

    @api.depends('review_ids')
    def _get_performance(self):
        performance = 0
        for recs in self.review_ids:
            performance += recs.rating
        calc_perc = (performance/(len(self.review_ids)*10))*100 if len(self.review_ids) != 0 else 0
        self.update({'performance':" ".join(['%s'%int(calc_perc),"%"])})

    def activity_system_manager(self):
        act_env = self.env['mail.activity']
        interview_id = self.env['ir.model'].search([('model','=','br.interview')]).id
        for recs in self.interviewer_ids:
            act_env.create({'activity_type_id':4,'summary':'Activity For Interview','date_deadline':self.schedule_date.date(),'user_id':recs.id,'note':'Notification for Scheduled Interview','res_model_id':interview_id,'res_id':self.id})
        return True

    def interview_start(self):
        self.write({'status':'start'})

    def interview_stop(self):
        print("vamk review %s"%len(self.review_ids))
        if len(self.review_ids) == 0:
           raise UserError(_("Please give the review"))
        self.write({'status':'stop'})

    def interview_draft(self):
        self.write({'status':'new'})

    def interview_cancelled(self):
        self.write({'status':'cancel'})

    def action_done_cr(self):
        self.application.write({'interview_id':self.id})
        return {'type': 'ir.actions.act_window_close'}

class InterviewBrApplicants(models.Model):
    _inherit = "hr.applicant"

    interview_count = fields.Integer('Interviews',compute='_get_interview_cnt',readonly=True)
    interview_id = fields.Many2one('br.interview','Interview Id', readonly=True)
    interview_st = fields.Selection([('new', 'Draft'), ('start', 'Start'), ('stop', 'Stop'), ('cancel', 'Cancelled')],'Interview Status',related='interview_id.status')

    @api.depends('interview_count')
    def _get_interview_cnt(self):
        for record in self:
            record['interview_count'] = len(self.env['br.interview'].search([('application','=',record.id)]))

    def create_interview(self):
        return {'type': 'ir.actions.act_window',
                'name': _('Create Interview'),
                'res_model': 'br.interview',
                'target': 'new',
                'view_id': self.env.ref('br_interview_process.view_interview_cr').id,
                'view_mode': 'form',
                'context': {'default_applicant': self.partner_name,'default_application': self.id}
                }

    def action_applications_interview(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Interview',
            'view_mode': 'tree,form',
            'res_model': 'br.interview',
            'domain': [('application', '=', self.id)],
            'context': "{'create': False}"
        }