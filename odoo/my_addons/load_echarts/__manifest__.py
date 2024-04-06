# -*- coding: utf-8 -*-
{
    'name': '引入echarts样式',
    'version': '1.0',
    'category': '引入echarts样式',
    'summary': '引入echarts样式',
    'author': 'Qin',
    'depends': ['base', 'web'],
    'data': [
        'views/home_view.xml',
        'security/ir.model.access.csv',
        'views/school_view.xml',


    ],

    'assets': {
            'web.assets_backend': [
                'load_echarts/static/src/js/*.js',
                'load_echarts/static/src/**/*',
                
            ],
        },
'images': [
        'load_echarts/static/src/**/*.jpg',
        'load_echarts/static/src/**/*.png',
        'load_echarts/static/src/**/*.gif',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
