# -*- coding: utf-8 -*-
{
    'name': "Hello World",

    'summary': "Say Hello",
    'description': """
        Say Hellow to the world
    """,

    'version': '0.1',
    'depends': ['web', 'contacts', 'base_geolocalize'],
    'data': [

        "views/data.xml",
    ],
    'assets': {
        'web.assets_backend': [
            '/hello_world_view/static/src/js/hello_world_view.js',
            '/hello_world_view/static/src/scss/hello_world_view.scss',

        ],
    },
    'qweb': [],
    'installable': True,
    'auto_install': True
}