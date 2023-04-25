

from odoo import models, fields, api, _
from odoo.exceptions import Warning, UserError


class InvoiceInherit(models.Model):
    _inherit = "account.move"

    @api.model
    def _default_show_sign(self):
        return self.env['ir.config_parameter'].sudo().get_param(
            'br_digital_signature.show_digital_sign_invoice')

    @api.model
    def _default_enable_sign(self):
        return self.env['ir.config_parameter'].sudo().get_param(
            'br_digital_signature.enable_options_invoice')

    @api.model
    def _default_show_sign_bill(self):
        return self.env['ir.config_parameter'].sudo().get_param(
            'br_digital_signature.show_digital_sign_bill')

    digital_sign = fields.Binary(string='Signature')
    sign_by = fields.Char(string='Signed By')
    designation = fields.Char(string='Designation')
    sign_on = fields.Datetime(string='Signed On')
    show_signature = fields.Boolean('Show Signature',
                                    default=_default_show_sign,
                                    compute='_compute_show_signature')
    show_sign_bill = fields.Boolean('Show Signature',
                                    default=_default_show_sign_bill,
                                    compute='_compute_show_sign_bill')
    enable_others = fields.Boolean(default=_default_enable_sign,
                                   compute='_compute_enable_others')

    def action_post(self):
        res = super(InvoiceInherit, self).action_post()
        if self.env[
            'ir.config_parameter'].sudo().get_param(
            'br_digital_signature.confirm_sign_invoice') and self.digital_sign is False:
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

    def _compute_show_sign_bill(self):
        show_sign_bill = self._default_show_sign_bill()
        for record in self:
            record.show_sign_bill = show_sign_bill
