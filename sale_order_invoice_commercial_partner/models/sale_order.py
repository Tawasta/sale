# -*- coding: utf-8 -*-


from odoo import api, models


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.model
    def create(self, vals):

        if vals['team_id'] == \
            self.env.ref('sales_team.salesteam_website_sales').id:
                vals['partner_invoice_id'] = \
                    self.env['res.partner'].browse(
                        vals['partner_invoice_id']). \
                            commercial_partner_id.id

        res = super(SaleOrder, self).create(vals)

        return res
