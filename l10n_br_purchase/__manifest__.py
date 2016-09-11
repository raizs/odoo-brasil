# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2009  Renato Lima - Akretion                                  #
#                                                                             #
#This program is free software: you can redistribute it and/or modify         #
#it under the terms of the GNU Affero General Public License as published by  #
#the Free Software Foundation, either version 3 of the License, or            #
#(at your option) any later version.                                          #
#                                                                             #
#This program is distributed in the hope that it will be useful,              #
#but WITHOUT ANY WARRANTY; without even the implied warranty of               #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
#GNU Affero General Public License for more details.                          #
#                                                                             #
#You should have received a copy of the GNU Affero General Public License     #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
###############################################################################

{
    'name': 'Brazilian Localization Purchase',
    'description': 'Brazilian Localization for Purchase',
    'license': 'AGPL-3',
    'category': 'Localisation',
    'author': 'Akretion, OpenERP Brasil',
    'website': 'http://openerpbrasil.org',
    'version': '10.0.1.0.0',
    'depends': [
        'purchase',
        'l10n_br_stock',
    ],
    'data': [
        'views/purchase.xml',
        'security/ir.model.access.csv',
    ],
    'test': [
        'test/purchase_order_demo.yml'
    ],
    'auto_install': False,
}