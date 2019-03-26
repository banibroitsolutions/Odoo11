# -*- coding: utf-8 -*-

import datetime
from datetime import datetime, timedelta
from odoo import SUPERUSER_ID
from odoo import api, fields, models, _
import calendar

class SalemReminder(models.Model):
    _inherit = "sale.order"

    mails = fields.Char("Mails",readonly=True, default='sending')

    @api.model
    def _cron_sale_change(self):
        su_id = self.env['res.partner'].browse(SUPERUSER_ID)
        for task in self.env['sale.order'].search([('user_id', '!=', None),('mails', '=', 'sending')]):
            today = datetime.now().date()
            updated = datetime.strptime(task.create_date,"%Y-%m-%d %H:%M:%S").date()			
            
            if updated == today and task:
                template_id = self.env['ir.model.data'].get_object_reference(
                                                      'sale_reminder',
                                                      'email_template_sale_change_reminder')[1]
                if template_id:
                    email_template_obj = self.env['mail.template'].browse(template_id)
                    values = email_template_obj.generate_email(task.id, fields=None)
                    values['email_from'] = su_id.email
                    values['email_to'] = task.user_id.employee_ids.parent_id.work_email
                    values['res_id'] = False
                    mail_mail_obj = self.env['mail.mail']
                    msg_id = mail_mail_obj.create(values)
                    if msg_id:
                       
                       msg_id.send()
                       task.write({'mails':'sent',})
        return True


