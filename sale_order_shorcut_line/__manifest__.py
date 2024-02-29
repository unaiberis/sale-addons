# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Sale Order Shorcut Line",
    "version": "16.0.1.0.0",
    "category": "Hidden",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "https://github.com/avanzosc/sale-addons",
    "depends": [
        "sale",
        "sales_team"
    ],
    "excludes": [],
    "data": [
        "security/ir.model.access.csv",
        "wizard/wiz_change_sequence_in_sale_line_views.xml",
        "wizard/wiz_duplicate_sale_line_views.xml",
        "views/sale_order_views.xml",
        "views/sale_order_line_views.xml",
    ],
    "installable": True,
}