# -*- coding: utf-8 -*-
from odoo import models, fields


class EmployeeTimesheet(models.TransientModel):
    _name = 'timesheet.wizard'

    employee = fields.Many2one('res.users', string="Employee", required=True)
    from_date = fields.Date(string="Starting Date")
    to_date = fields.Date(string="Ending Date")

    def print_timesheet(self):
        """Redirects to the report with the values obtained from the wizard
        'data['form']': name of employee and the date duration"""
        data = {
            'start_date': self.from_date,
            'end_date': self.to_date,
            'employee': self.employee.id
        }
        return self.env.ref('br_employee_timesheet_report.action_report_print_timesheets').report_action(self, data=data)

