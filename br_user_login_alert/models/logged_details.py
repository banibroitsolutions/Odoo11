
from odoo import models, fields


class ResUsersInherit(models.Model):
    _inherit = 'res.users'

    last_logged_ip = fields.Char(string='IP')
    last_logged_browser = fields.Char(string='Browser')
    last_logged_os = fields.Char(string='OS')
