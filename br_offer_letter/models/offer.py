from odoo import api, fields, models, SUPERUSER_ID
from odoo.tools.translate import _
from odoo.exceptions import UserError
import base64

class OfferBr(models.Model):
    _name = "br.offer"

    name = fields.Char('Number', default='/', store=True)
    employee = fields.Char('Employee', store=True,required=True)
    application = fields.Many2one('hr.applicant', 'Application', store=True)
    offer_date = fields.Date('Offer Date', default=fields.Date.today, store=True)
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency',related='company_id.currency_id')
    monthly_sal = fields.Float('Monthly Salary', store=True)
    prepaid_by = fields.Many2one('res.users', 'Prepaid By', store=True, default=lambda self: self.env.uid)
    prepaid_date = fields.Date('Prepaid Date', default=fields.Date.today, store=True)
    msg_body = fields.Html('Body',store=True)
    status = fields.Selection(
        [('new', 'New'), ('in_progress', 'In Progress'), ('given_to', 'Given To Employee'), ('done', 'Done')], 'Status',
        default='new', store=True)

    @api.model
    def create(self, vals):
        obj = super(OfferBr, self).create(vals)
        if obj.name == '/':
            number = self.env['ir.sequence'].get('br.offer.letter') or '/'
            obj.write({'name': number})
        return obj

    def in_progress(self):
        self.write({'status':'in_progress'})

    def get_done(self):
        self.write({'status':'done'})
        if self.application.id:
           self.application.write({'is_offered':True})

    def give_to(self):
        if self.application.email_from == False:
           raise UserError(_("Please ensure the applicant's mail"))
        report_template_id = self.env.ref('br_offer_letter.br_offer_letter_report_id').render_qweb_pdf(self.id)
        data_record = base64.b64encode(report_template_id[0])
        ir_values = {
           'name': "Customer Report",
           'type': 'binary',
           'datas': data_record,
           'store_fname': data_record,
           'mimetype': 'application/x-pdf',
        }
        data_id = self.env['ir.attachment'].create(ir_values)
        template = self.env.ref('br_offer_letter.br_offer_letter_mail')[0]
        template.attachment_ids = [(6, 0, [data_id.id])]
        template.send_mail(self.id, force_send=True)
        template.attachment_ids = [(3, data_id.id)]
        self.write({'status': 'given_to'})
        return True

    def action_done_cr(self):
        self.application.write({'offer_letter_id':self.id})
        return {'type': 'ir.actions.act_window_close'}

class OfferBrApplicants(models.Model):
    _inherit = "hr.applicant"

    offer_letter_id = fields.Many2one('br.offer','Offer Letter',readonly=True)
    is_offered = fields.Boolean("Is Offered",stored=True)

    def create_offer_ltr(self):
        return {'type': 'ir.actions.act_window',
                'name': _('Create Job Offer Request'),
                'res_model': 'br.offer',
                'target': 'new',
                'view_id': self.env.ref('br_offer_letter.view_offer_letter_cr').id,
                'view_mode': 'form',
                'context': {'default_employee': self.partner_name,'default_application': self.id}
                }