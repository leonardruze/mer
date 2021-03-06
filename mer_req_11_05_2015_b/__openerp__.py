# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 Humanytek (<http://humanytek.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Mercurio: req_11_05_2015_b',
    'version': '1.0',
    'sequence': 1,
    'category': 'Custom',
    'complexity': 'easy',
    'sumary': 'req_11_05_2015_b',
    'description': """
Customizations in Manufacturing / Products

Details:
--------
* Add menu: Manufacturing / Products / Product Variants
* Add field: campo incoming_qty
* Add field: campo outgoing_qty
    """,
    'author': 'Humanytek',
    'website': 'https://github.com/humanytek/mer',
    'depends': [
        'base',
        'mrp',
    ],
    'data': [
        # Security and groups
    
        # Data
        
        # Views
        'view/product_variants.xml',
        
        # Other views
        
        # Wizard
        
        # Reports
    ],
    'demo_xml': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
