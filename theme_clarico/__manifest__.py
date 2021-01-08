{
    'name': 'Theme Wonder',
    'category': 'Theme/eCommerce',
    'summary': 'Fully Responsive Odoo Theme suitable for eCommerce Businesses',
    'author': 'Bansi',

    'depends': [
        'website_theme_install',
        'website_sale_wishlist',
        'website_sale',
        'website_sale_stock',
        'emipro_theme_base',
    ],
    'data': [
        'templates/assets.xml',
        'templates/theme_customise_option.xml',
        'templates/customize.xml',

        'templates/header.xml',
        'templates/footer.xml',
        # 'templates/menu_config.xml',
    ],

    'installable': True,
    'auto_install': False,
}
