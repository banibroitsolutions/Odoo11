

from odoo import api, models


class ProductCatalogueReport(models.AbstractModel):
    """ Model to contain the information related to printing the information about
    the products"""

    _name = "report.br_product_catalogue.report_product_catalog"

    @api.model
    def _get_report_values(self, docids, data=None):
        """Get the report values.
                        :param : model
                        :param : docids
                        :param : data
                        :return : data
                        :return : Product template records"""
        product = self.env['product.template'].browse(docids)
        return {
            'data': data,
            'docs': product,
        }