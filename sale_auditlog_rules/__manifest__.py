##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2019 Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

{
    'name': "Futural Log Rules - Sales",
    'summary': "Audit log rules for sales",
    'description': "Log rules for Futural ERP Sale",
    'author': 'Oy Tawasta Technologies Ltd.',
    'license': 'AGPL-3',
    'website': "https://tawasta.fi",
    'category': 'Logging',
    'application': False,
    'installable': True,
    'version': '12.0.1.0.0',
    'depends': [
        'sale_management',
        'auditlog',
    ],
    'data': [
        'data/rules.xml'
    ],
    'demo': [],
}
