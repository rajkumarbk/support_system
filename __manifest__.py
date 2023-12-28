# -*- coding: utf-8 -*-
{
    'name': "support_sys",
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,
    'sequence': 1,

    # any module necessary for this one to work correctly
    'depends': ['base','web','sale','board'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/homepage.xml',
        'views/views.xml',
        'views/email_template.xml',
        'views/expense.xml',
        'views/ticket_history.xml',
        'views/new_ticket.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'support_sys/static/src/components/*/.js',
            'support_sys/static/src/components/*/.xml',
            # 'support_sys/static/src/scss/*/.scss',
            # 'support_sys/static/src/components/chart_renderer/chart_renderer.js',
            # 'support_sys/static/src/components/chart_renderer/chart_renderer.xml',
            # 'support_sys/static/src/components/kpi_card/kpi_card.js'
            # 'support_sys/static/src/components/kpi_card/kpi_card.xml'
        ],


        'web.assets_frontend': [
            'support_sys/static/src/css/nepali.datepicker.v4.0.1.min.css',
        ]

    }
}