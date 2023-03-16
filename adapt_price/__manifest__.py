# -*- coding: utf-8 -*-
# More info at https://www.odoo.com/documentation/master/reference/module.html

{
    "name": "Price adaptater for Waligali",
    'version': '1.0',
    'author': "Delarbre Louis",
    'description': """
    module to adapt price's product from an excel sheet
    """,
    "depends": [
        "base",
        "product"
    ],
    "data": [
        'security/ir.model.access.csv',
        "views/adaptor_product_view.xml",
        "views/adaptor_resume_view.xml",
        "views/adaptor_menus.xml",
        "report/adaptor_reports.xml",
        "report/adaptor_report_views.xml",
    ],
    "application": True,
}
