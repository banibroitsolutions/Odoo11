

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    insurance_id = fields.Many2one('insurance.details', string='Insurance')
    claim_id = fields.Many2one('claim.details', string='Insurance')
