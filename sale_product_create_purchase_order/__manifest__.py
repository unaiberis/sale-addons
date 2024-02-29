# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Sale Product Create Purchase Order",
    "version": "16.0.1.0.0",
    "category": "Hidden",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "https://github.com/avanzosc/sale-addons",
    "depends": [
        "product",
        "purchase",
        "sale",
        "sale_order_shorcut_line"
    ],
    "excludes": [],
    "data": [
        "views/sale_order_views.xml",
        "views/sale_order_line_views.xml",
    ],
    "installable": True,
}