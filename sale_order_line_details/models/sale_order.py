# -*- coding: utf-8 -*-
from odoo import models, api


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.multi
    def action_sale_order_lines(self):
        action = self.env.ref(
            'sale_order_line_details.action_sale_order_lines').read()[0]

        return action
