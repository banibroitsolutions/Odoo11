

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    show_product_image_in_sale_report = fields.Boolean(string="Show Product Image", default=False)

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].sudo().set_param('br_sale_product_image.show_product_image_in_sale_report',
                                                         self.show_product_image_in_sale_report)
        res = super(ResConfigSettings, self).set_values()
        return res

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        param = self.env['ir.config_parameter'].sudo().get_param(
            'br_sale_product_image.show_product_image_in_sale_report',
            self.show_product_image_in_sale_report)
        res.update(
            show_product_image_in_sale_report=param
        )
        return res
