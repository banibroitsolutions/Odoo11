

from odoo import models, api, fields


class PayslipLateCheckIn(models.Model):
    _inherit = 'hr.payslip'

    late_check_in_ids = fields.Many2many('late.check_in')

    @api.model
    def get_inputs(self, contracts, date_from, date_to):
        """
        function used for writing late check-in record in payslip
        input tree.

        """
        res = super(PayslipLateCheckIn, self).get_inputs(contracts, date_to, date_from)
        late_check_in_type = self.env.ref('br_employee_late_check_in.late_check_in')
        contract = self.contract_id
        late_check_in_id = self.env['late.check_in'].search([('employee_id', '=', self.employee_id.id),
                                                             ('date', '<=', self.date_to),
                                                             ('date', '>=', self.date_from),
                                                             ('state', '=', 'approved'),
                                                             ])
        amount = late_check_in_id.mapped('amount')
        cash_amount = sum(amount)
        if late_check_in_id:
            self.late_check_in_ids = late_check_in_id
            input_data = {
                'name': late_check_in_type.name,
                'code': late_check_in_type.code,
                'amount': cash_amount,
                'contract_id': contract.id,
            }
            res.append(input_data)
        return res

    def action_payslip_done(self):
        """
        function used for marking deducted Late check-in
        request.

        """
        for recd in self.late_check_in_ids:
            recd.state = 'deducted'
        return super(PayslipLateCheckIn, self).action_payslip_done()
