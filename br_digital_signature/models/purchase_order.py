

from odoo import models, fields, api, _
from odoo.exceptions import Warning, UserError


class PurchaseOrderInherit(models.Model):
    _inherit = "purchase.order"

    @api.model
    def _default_show_sign(self):
        return self.env['ir.config_parameter'].sudo().get_param(
            'br_digital_signature.show_digital_sign_po')

    @api.model
    def _default_enable_sign(self):
        return self.env['ir.config_parameter'].sudo().get_param(
            'br_digital_signature.enable_options_po')

    digital_sign = fields.Binary(string='Signature')
    sign_by = fields.Char(string='Signed By')
    designation = fields.Char(string='Designation')
    sign_on = fields.Datetime(string='Signed On')
    show_signature = fields.Boolean('Show Signature',
                                    default=_default_show_sign,
                                    compute='_compute_show_signature')
    enable_others = fields.Boolean(default=_default_enable_sign,
                                   compute='_compute_enable_others')

    def button_confirm(self):
        res = super(PurchaseOrderInherit, self).button_confirm()
        if self.env[
            'ir.config_parameter'].sudo().get_param(
            'br_digital_signature.confirm_sign_po') and self.digital_sign is False:
            raise UserError(_("Signature is missing"))

        return res

    def _compute_show_signature(self):
        show_signature = self._default_show_sign()
        for record in self:
            record.show_signature = show_signature

    def _compute_enable_others(self):
        enable_others = self._default_enable_sign()
        for record in self:
            record.enable_others = enable_others
