

from odoo import models, fields, api, _


class ResConfigurationInherit(models.TransientModel):
    _inherit = 'res.config.settings'

    show_digital_sign_po = fields.Boolean(
        config_parameter='br_digital_signature.show_digital_sign_po')
    enable_options_po = fields.Boolean(
        config_parameter='br_digital_signature.enable_options_po')
    confirm_sign_po = fields.Boolean(
        config_parameter='br_digital_signature.confirm_sign_po')
    show_digital_sign_inventory = fields.Boolean(
        config_parameter='br_digital_signature.show_digital_sign_inventory')
    enable_options_inventory = fields.Boolean(
        config_parameter='br_digital_signature.enable_options_inventory')
    sign_applicable = fields.Selection([
        ('picking_operations', 'Picking Operations'),
        ('delivery', 'Delivery Slip'), ('both', 'Both'),
    ], string="Sign Applicable inside",
        default="picking_operations",
        config_parameter='br_digital_signature.sign_applicable')
    confirm_sign_inventory = fields.Boolean(
        config_parameter='br_digital_signature.confirm_sign_inventory')
    show_digital_sign_invoice = fields.Boolean(
        config_parameter='br_digital_signature.show_digital_sign_invoice')
    enable_options_invoice = fields.Boolean(
        config_parameter='br_digital_signature.enable_options_invoice')
    confirm_sign_invoice = fields.Boolean(
        config_parameter='br_digital_signature.confirm_sign_invoice')
    show_digital_sign_bill = fields.Boolean(
        config_parameter='br_digital_signature.show_digital_sign_bill')
