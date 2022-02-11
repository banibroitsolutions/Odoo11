import datetime
from datetime import datetime, timedelta
from odoo import SUPERUSER_ID
from odoo import api, fields, models, _
import calendar
import base64
import re

class TimesheetReminder(models.Model):
    _inherit = "hr.employee"

    @api.model
    def _cron_timesheet_in_mail(self):
        su_id = self.env['res.partner'].browse(SUPERUSER_ID)
        for task in self.env['hr.employee'].search([]):
            if task.user_id.login:
                curr = datetime.now().strftime('%Y-%m-%d')
                rms_list_in = []
                time_env = self.env['account.analytic.line'].search([('employee_id','=',task.id),('date','=',curr)],limit=1)

                for rms in task.attendance_ids:
                    check_in = datetime.strptime(str(rms.check_in), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
                    # check_out = datetime.strptime(rms.check_out, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
                    if check_in == curr:
                        rms_list_in.append(rms.id)
                time_msg = "This is a reminder for you have not recorded your today's timesheet.So please record your today's timesheet."
                if rms_list_in and not time_env:
                    mail_body = ('\
<p style="margin: 0px 0px 9px 0px; font-size: 13px; font-family: &quot;Lucida Grande&quot;, Helvetica, Verdana, Arial, sans-serif">Dear %s,</p>\
<p style="margin: 0px 0px 9px 4px; font-size: 13px; font-family: &quot;Lucida Grande&quot;, Helvetica, Verdana, Arial, sans-serif">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;%s</p>\
<p style="margin: 0px 0px 9px 0px; font-size: 13px; font-family: &quot;Lucida Grande&quot;, Helvetica, Verdana, Arial, sans-serif">Date:&nbsp;<b><font>%s</font></b>,</p>\
<br/><br/><p style="margin: 0px 0px 9px 86px; font-size: 14px; font-family: &quot;Lucida Grande&quot;, Helvetica, Verdana, Arial, sans-serif"><b>Note-This is a auto generated mail. Please do not reply</b>,</p>') % (
                    task.name, time_msg, curr)

                    #server_id = self.env['ir.mail_server'].search([('name', '=', 'Attendance Server')]).id
                    mail_values_approval = {'email_to': task.work_email,
                                            'email_cc': task.parent_id.work_email, 'subject': 'Timesheet Reminder',
                                            'body_html': mail_body, 'notification': True, 'auto_delete':True}
                    mail = self.env['mail.mail'].create(mail_values_approval)
                    mail.send()

        return True