# -*- encoding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2015 Datamatic All Rights Reserved.
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licensse/>.
#
##############################################################################
{
    'name': 'Sequencias para documentos',
    'version': '1.0',
    'category': 'Accounting & Finance',
    'description': """
Este módulo crea las secuencias internas para los documentos descritos a continuacion
======================================================================

Crea Numeración de sequencias para los siguientes documentos:
-----------------------------------------------------------
    * Factura
    * Nota de Crédito
    * Contado
    * Devolución Contado
    * Remito
    """,
    'author': 'Felipe Ferreira',
    'website': 'https://www.datamatic.com.uy',
    'depends': ['base'],
    "data":["views/sequences.xml"],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
