from odoo import models, fields, api
from datetime import datetime


class hr_warning(models.Model):
    _name = 'hr.warning'
    # _inherit = ['mail.thread', 'mail.activity.mixin']


    title = fields.Char()
    employee = fields.Many2one("hr.employee",string="Employee",required = True)
    department = fields.Many2one("hr.department", string="Department",related='employee.department_id')
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    current_date=fields.Date('current date',default=datetime.today())
    company_id=fields.Many2one('res.company', string='company',related='employee.company_id')
    
    notes = fields.Text(string="Note")
    
    state = fields.Selection([('draft', 'Draft'),('first_warning', 'First Warning'),('second_warning', 'Second Warning'),('third_warning', 'Third Warning'),('fired', 'Fired')], string = "Status", readonly = True, default='draft',inverse='_inverse_state')
    
    
    @api.model
    def _company_get(self):
        return self.env["res.company"].browse(self.env.company.id)
    

    def _inverse_state(self):
 
        if self.state == 'second_warning':

            template_id = self.env.ref('hr_warning.second_warning_mail').id
            template = self.env['mail.template'].browse(template_id)
            template.send_mail(self.id, force_send=True)
            

        if self.state == 'third_warning':

            template_id = self.env.ref('hr_warning.third_warning_mail').id
            template = self.env['mail.template'].browse(template_id)
            template.send_mail(self.id, force_send=True)

        if self.state == 'fired':

            template_id = self.env.ref('hr_warning.fired_mail').id
            template = self.env['mail.template'].browse(template_id)
            template.send_mail(self.id, force_send=True)
            # self.env['hr.employee'].update({"active": False})
            
    
   
    
    
    def button_draft(self):
             
        template_id = self.env.ref('hr_warning.reset_mail').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
        
        return self.write({"state": "draft"})

    def button_first_warning(self):
        template_id = self.env.ref('hr_warning.first_warning_mail').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
        # self.env['hr.employee'].browse(self._context.get("employee.name")).update({'archive': True})
       
        # for rec in self:
            
            # rec.employee.fired = True
                # # Removing and deactivating user
            # if rec.employee.user_id:
                # rec.employee.user_id.active = False
                # rec.employee.user_id = None
        
        return self.write({"state": "first_warning"})
        
    # def button_draft(self,values):
        # record = super(hrresignation, self).write(values)
        # if 'state' in values and values['state'] == 'draft':
            # if values.get('employee') and values.get('department'):
                # self.env['hr.resignation'].create({
                 # 'employee_id': values['employee'],
                 # 'department_id': values['department'],
                 # })
        # return record
        
    # def button_second_warning(self):
        # return self.write({"state": "second_warning"})
        
    # def button_third_warning(self):
        # return self.write({"state": "third_warning"})
        # {'type':'ir.actions.act_window',
                 # 're_model': 'second_warning.wizard',
                 # 'view_mode' : 'form',
                 # 'target' : 'new'}
        
    def button_fired(self):
        # template_id = self.env.ref('hr_warning.fired_mail').id
        # template = self.env['mail.template'].browse(template_id)
        # template.send_mail(self.id, force_send=True)
        vals = { 'employee_id':self.employee.id,
            'expected_revealing_date':self.current_date,
            'reason':self.notes,
            'resignation_type':'fired',
            'notice_period':'immediate',
            'state':'draft'
        }
        self.env['hr.resignation'].create(vals) 
        return self.write({"state": "fired"})
        
        
    # def update_employee_status(self):
        # resignation = self.env['hr.warning'].search([('state', '=', 'first_warning')])
        # for rec in resignation:
            
            # rec.employee.active = False
            # # Changing fields in the employee table with respect to resignation
            
            # rec.employee.fired = True
                # # Removing and deactivating user
            # if rec.employeeuser_id:
                # rec.employee.user_id.active = False
                # rec.employee.user_id = None    
    # @api.model
    # def button_draft(self):
        # res = super(hr_warning, self).button_draft()
        # template_id = self.env.ref('hr_warning.reset_mail').id
        # template = self.env['mail.template'].browse(template_id)
        # template.send_mail(self.id, force_send=True)
        # return result 
    
        
    # @api.model
    # def button_first_warning(self):
        # res = super(hr_warning, self).button_first_warning()
        # template_id = self.env.ref('hr_warning.first_warning_mail').id
        # template = self.env['mail.template'].browse(template_id)
        # template.send_mail(self.id, force_send=True)
        # return result 
        
    # @api.model
    # def button_second_warning(self):
        # res = super(hr_warning, self).button_second_warning()
        # template_id = self.env.ref('hr_warning.second_warning_mail').id
        # template = self.env['mail.template'].browse(template_id)
        # template.send_mail(self.id, force_send=True)
        # return result
        
    # @api.model
    # def button_third_warning(self):
        # res = super(hr_warning, self).button_third_warning()
        # template_id = self.env.ref('hr_warning.third_warning_mail').id
        # template = self.env['mail.template'].browse(template_id)
        # template.send_mail(self.id, force_send=True)
        # return result
        
        
    # @api.model
    # def button_fired(self):
        # res = super(hr_warning, self).button_fired
        # template_id = self.env.ref('hr_warning.fired_mail').id
        # template = self.env['mail.template'].browse(template_id)
        # template.send_mail(self.id, force_send=True)
        # return result
    
   

   
        
    # def button_first_warning(self):
        # res = super(hr_warning,self).button_first_warning()
        # self.env['hr.employee'].browse(self._context.get("active_ids")).update({'archive': True})
        # return res
        
# class HrEmployee(models.Model):
    # _inherit = 'hr.employee'
    
    
    # active = fields.Boolean('Active', related='resource_id.active', default=True, store=True, readonly=False)
    
    # # fired = fields.Boolean(string="Fired", default=False, store=True, help="If checked then employee has fired")
    
# class hrresignation(models.Model):
    # _inherit = 'hr.resignation'
    
    
    
    # joined_date = fields.Date(string="Join Date", required=False, readonly=True, related="employee_id.joining_date",
                              # help='Joining date of the employee.i.e Start date of the first contract')
                              
    
    