

from odoo import models, fields, api, _


class ChecklistStage(models.Model):
    _inherit = "project.task.type"

    is_checklist = fields.Boolean(string='Checklist Task')


class ChecklistActivityStages(models.Model):
    _name = 'checklist.activity.stages'

    stage_name = fields.Char(string='Stage')
    sequence = fields.Char(string='sequence')
