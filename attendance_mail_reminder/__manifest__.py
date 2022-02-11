# -*- coding: utf-8 -*-
###################################################################################
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Cybrosys Technologies (<https://www.cybrosys.com>).#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################

{
    'name': "Attendance Mail Reminder",
    'version': "13.0.1.0.0",
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://www.banibro.com',
	'license': "AGPL-3",
	'email': "support@banibro.com",
    'summary': '''Automatic Mail for Check-In & Check-Out Reminder''',
    'description': '''Automatic Mail for Check-In & Check-Out Reminder''',
    'category': "hr",
    'depends': ['mail','hr'],
    'license': 'AGPL-3',
    'data': [
            'data/attendance_mail_hr_action_data.xml',
             ],
    'demo': [],
    'images': ['attendance_mail_reminder/static/description/icon.png'],
    'installable': True,
    'auto_install': False
	'price': 10,
    'currency': 'USD'
}
