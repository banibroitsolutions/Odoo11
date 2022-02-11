from odoo import models, fields, api


class hr_warning_second_wizard(models.TransientModel):
    _name = "second_warning.wizard"
    
    
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    
    
    def update_second(self):
        
        self.env['hr.warning'].browse(self._context.get("active_ids")).update({'start_date':self.start_date})
        self.env['hr.warning'].browse(self._context.get("active_ids")).update({'end_date':self.end_date})
        self.env['hr.warning'].browse(self._context.get("active_ids")).update({"state": "second_warning"})
        # template_id = self.env.ref('hr_warning.second_warning_mail').id
        # template = self.env['mail.template'].browse(template_id)
        # template.send_mail(self.id, force_send=True)
        return True
        
        
class hr_warning_third_wizard(models.TransientModel):
    _name = "third_warning.wizard"
    
    
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    
    
    def update_third(self):
        
        self.env['hr.warning'].browse(self._context.get("active_ids")).update({'start_date':self.start_date})
        self.env['hr.warning'].browse(self._context.get("active_ids")).update({'end_date':self.end_date})
        self.env['hr.warning'].browse(self._context.get("active_ids")).update({"state": "third_warning"})
        # template_id = self.env.ref('hr_warning.third_warning_mail').id
        # template = self.env['mail.template'].browse(template_id)
        # template.send_mail(self.id, force_send=True)
        return True