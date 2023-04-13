
from odoo import api, fields, models


class PartnerEmailSMSHistory(models.Model):
    _inherit = 'res.partner'

    def action_view_partner_sms(self):
        self.ensure_one()
        action = self.env.ref('sms.sms_sms_action').read()[0]
        action['domain'] = [
            ('partner_id', '=', self.id)]
        return action

    def sent_email_history(self):
        action = self.env.ref('mail.action_view_mail_mail')
        result = action.read()[0]
        result['domain'] = [('email_from', 'ilike', self.email)]
        return result

    def received_email_history(self):
        action = self.env.ref('mail.action_view_mail_mail')
        result = action.read()[0]
        result['domain'] = ['|', ('email_to', '=', self.email), ('recipient_ids', '=', self.email)]
        return result


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sms_history = fields.Boolean('SMS History', config_parameter='br_partner_emails_history.default_sms_history', default=False)