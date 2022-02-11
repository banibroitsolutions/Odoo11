# -*- coding: utf-8 -*-

import datetime
from datetime import datetime, timedelta, date
from odoo import SUPERUSER_ID
from odoo import api, fields, models, _
import calendar
import base64
import re

class AttendenceReminder(models.Model):
    _inherit = "hr.employee"

    #test_field = fields.Text("Test Field")
    
    @api.model
    def attendance_in_mail(self):
        # global leaves and 2nd saturday filter
        sat = []
        test = []
        global_leave = []
        year=date.today().year 
        month=date.today().month
        dt=date(year,month,1)    
        first_w=dt.isoweekday()  
        saturday2=14-first_w
        saturday4=28-first_w
        dt=date(year,month,saturday2)
        dt_2 =date(year,month,saturday4)
        first_sat = datetime.strptime(str(dt), '%Y-%m-%d').strftime('%Y-%m-%d')
        sat.append(first_sat)
        fouth_sat = datetime.strptime(str(dt_2), '%Y-%m-%d').strftime('%Y-%m-%d')
        sat.append(fouth_sat)
        #global leave
        glob_leave = self.env['resource.calendar.leaves'].search([])
        for lev in glob_leave:
            gl_lev = datetime.strptime(str(lev.date_from), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
            global_leave.append(gl_lev)
        su_id = self.env['res.partner'].browse(SUPERUSER_ID)
        for task in self.env['hr.employee'].search([('user_id', '!=', None)]):
            if task.user_id.login:
                curr = datetime.now().strftime('%Y-%m-%d')
                sun = datetime.today().strftime('%A')
                rms_list_in = []               
                if (curr not in sat) and (curr not in global_leave) and (sun != 'Sunday'):
                    for rms in task.attendance_ids:
                        check_in = datetime.strptime(str(rms.check_in), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
                        if check_in == curr:
                           rms_list_in.append(rms.id)
                        att = 'This is a reminder for you have not check-out yet.so please make sure that.'
                    if not rms_list_in:
                        mail_body = ('\
<p style="margin: 0px 0px 9px 0px; font-size: 13px; font-family: &quot;Lucida Grande&quot;, Helvetica, Verdana, Arial, sans-serif">Dear %s,</p>\
<p style="margin: 0px 0px 9px 0px; font-size: 13px; font-family: &quot;Lucida Grande&quot;, Helvetica, Verdana, Arial, sans-serif">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;This is a reminder for you have not check-in yet.so please make sure your todays presence.</p>\
<p style="margin: 0px 0px 9px 0px; font-size: 13px; font-family: &quot;Lucida Grande&quot;, Helvetica, Verdana, Arial, sans-serif">Date:&nbsp;<b><font style="background-color: rgb(179, 94, 155);">%s</font></b>,</p>') % (task.name,curr)
                        mail_values_approval = {'email_to':task.user_id.login ,'subject': 'Attendance Check-in Reminder','body_html': mail_body,'notification': True}          
                        mail = self.env['mail.mail'].create(mail_values_approval)
                        mail.send()
        return True

    @api.model
    def attendance_out_mail(self):
        test1 = []
        su_id = self.env['res.partner'].browse(SUPERUSER_ID)
        for task in self.env['hr.employee'].search([('user_id', '!=', None)]):
            if task.user_id.login:
                curr = datetime.now().strftime('%Y-%m-%d')
                rms_list_in = []               
                rms_list_out = []
                for rms in task.attendance_ids:
                    check_in = datetime.strptime(str(rms.check_in), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
                #check_out = datetime.strptime(rms.check_out, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
                    if rms.check_out:
                        check_out = datetime.strptime(str(rms.check_out), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
                        if check_out == curr:
                            rms_list_out.append(rms.id)
                    else:
                        if check_in == curr:
                            rms_list_in.append(rms.id)
               
                if rms_list_in:
                   test1.append(task.user_id.login)
                   mail_body = ('\
<p style="margin: 0px 0px 9px 0px; font-size: 13px; font-family: &quot;Lucida Grande&quot;, Helvetica, Verdana, Arial, sans-serif">Dear %s,</p>\
<p style="margin: 0px 0px 9px 0px; font-size: 13px; font-family: &quot;Lucida Grande&quot;, Helvetica, Verdana, Arial, sans-serif">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;This is a reminder for you have not check-out yet.so please make sure that.</p>\
<p style="margin: 0px 0px 9px 0px; font-size: 13px; font-family: &quot;Lucida Grande&quot;, Helvetica, Verdana, Arial, sans-serif">Date:&nbsp;<b><font style="background-color: rgb(179, 94, 155);">%s</font></b>,</p>') % (task.name,curr)
            
                   mail_values_approval = {'email_to':task.user_id.login ,'subject': 'Attendance Check-out Reminder','body_html': mail_body,'notification': True}          
                   mail = self.env['mail.mail'].create(mail_values_approval)
                   mail.send()
        return True
