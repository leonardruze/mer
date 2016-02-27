# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
import time

from openerp.osv import fields, osv
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp

class mrp_operator_tasks_mer(osv.osv_memory):

    _name = 'mrp.operator.tasks'
    _description = 'Tasks of operators'
    _columns = {
        'task_id': fields.many2one('operator.tasks', 'Task'),
        'operator_id': fields.many2one('hr.employee', 'Operator'),
        'hours': fields.float('Hours'),
        'lot_id': fields.many2one('stock.production.lot', 'Lot'),
        'mrp_production_id': fields.many2one('mrp.production', 'Production ID')
    }
    
mrp_operator_tasks_mer()