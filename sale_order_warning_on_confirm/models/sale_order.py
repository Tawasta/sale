# -*- coding: utf-8 -*-
from odoo import models, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()

        for record in self:
            for line in record.order_line:
                product = line.product_id

                if product.sale_line_warn == 'block':
                    raise UserError(
                        _("Product '%s' can not be used: %s") %
                        (product.name, product.sale_line_warn_msg)
                    )

        return res
