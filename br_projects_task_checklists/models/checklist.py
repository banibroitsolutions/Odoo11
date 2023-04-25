

from odoo import models, fields, api, _


class TaskChecklist(models.Model):
    _name = 'task.checklist'

    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    project_id = fields.Many2one('project.project', string='Project')
    task_ids = fields.Many2one('project.task', string='Task')

    checklist_ids = fields.One2many('checklist.item', 'checklist_id',
                                    string='CheckList Items', required=True)


class ChecklistItem(models.Model):
    _name = 'checklist.item'
    _description = 'Checklist Item'

    name = fields.Char(required=True)
    sequence = fields.Integer(default=1)
    description = fields.Char()
    projects_id = fields.Many2one('project.task')
    checklist_id = fields.Many2one('task.checklist')
    state = fields.Selection(
        string='Status', required=True, readonly=True, copy=False,
        tracking=True, selection=[
            ('todo', 'To Do'),
            ('in_progress', 'In Progress'),
            ('done', 'Done'),
            ('cancel', 'Cancelled'),
        ], default='todo', )

    def approve_and_next(self):
        self.state = 'in_progress'

    def mark_completed(self):
        self.state = 'done'

    def mark_canceled(self):
        self.state = 'cancel'

    def reset_stage(self):
        self.state = 'todo'


class ChecklistProgress(models.Model):
    _inherit = 'project.task'

    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')
    progress = fields.Float(compute='_compute_progress', string='Progress in %')
    checklist_id = fields.Many2one('task.checklist')
    checklists = fields.One2many('checklist.item', 'projects_id',
                                 string='CheckList Items', required=True)

    @api.onchange('checklist_id')
    def _onchange_project_id(self):
        self.checklists = []
        checklist = self.env['task.checklist'].search(
            [('name', '=', self.checklist_id.name)])
        for rec in checklist:
            self.checklists += rec.checklist_ids

    def _compute_progress(self):
        for rec in self:
            total_completed = 0
            for activity in rec.checklists:
                if activity.state in ['cancel', 'done', 'in_progress']:
                    total_completed += 1
            if total_completed:
                rec.progress = float(total_completed) / len(
                    rec.checklists) * 100
            else:
                rec.progress = 0.0
