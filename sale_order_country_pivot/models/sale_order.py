from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    partner_country_id = fields.Many2one(
        related="partner_id.country_id",
        string="Customer Country",
        store=True,
    )
    partner_state_id = fields.Many2one(
        related="partner_id.state_id",
        string="Customer State",
        store=True,
    )
