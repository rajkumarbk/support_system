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
        'views/views.xml',
        'views/templates.xml',
        'views/ticket_view.xml',
        'views/ticket_raise.xml',
        'views/ticket_list.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'support_sys/static/src/components/**/*.js',
            'support_sys/static/src/components/**/*.xml',
            # 'support_sys/static/src/scss/**/*.scss',
            # 'support_sys/static/src/components/chart_renderer/chart_renderer.js',
            # 'support_sys/static/src/components/chart_renderer/chart_renderer.xml',
            # 'support_sys/static/src/components/kpi_card/kpi_card.js'
            # 'support_sys/static/src/components/kpi_card/kpi_card.xml'


        ]
    }
}
