

from odoo import api, models, fields, _


class IrModelFields(models.Model):
    """Adding a new field to understand the dynamically created fields."""

    _inherit = 'ir.model.fields'

    is_dynamic = fields.Boolean(string="Dynamic Field")
