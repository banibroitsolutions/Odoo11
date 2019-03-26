# -*- coding: utf-8 -*-


from odoo import api, fields, models, _, exceptions

class project_task(models.Model):
    _inherit = 'sale.order.line'

    
    

    @api.multi
    def check_values(self,values):
        self.ensure_one()
        te = self.env['sale.order.line']
        inv_obj = te.create({'name':self.name,
			'order_id':self.order_id.id,
			'product_id':self.product_id.id,
			'product_uom_qty':self.product_uom_qty,
			'price_unit':self.price_unit,
			'price_subtotal':self.price_subtotal,
			'tax_id': [(6, 0, self.tax_id.ids)],
			'layout_category_id':self.layout_category_id.id,
			'qty_delivered': self.qty_delivered,
			'qty_invoiced': self.qty_invoiced,
			'product_uom': self.product_uom.id,
			'discount': self.discount,
			'price_total': self.price_total,
			
			})        
        return inv_obj


