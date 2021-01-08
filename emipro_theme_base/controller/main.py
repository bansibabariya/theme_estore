# -*- coding: utf-8 -*-
"""
    This file is used for create and inherit the core controllers
"""
import datetime
import json
from datetime import timedelta, date
from odoo.http import request, Controller, route
from odoo.tools.safe_eval import safe_eval
from werkzeug.exceptions import NotFound
from odoo.exceptions import UserError
from odoo.addons.auth_signup.models.res_users import SignupError
import werkzeug

from odoo import http
import odoo
import logging
from odoo.tools.translate import _
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.sale.controllers.variant import VariantController
from odoo.addons.website.controllers.main import QueryURL
from odoo.addons.website_sale.controllers.main import TableCompute
from odoo.addons.website_sale_wishlist.controllers.main import WebsiteSale
from odoo.addons.website_sale_wishlist.controllers.main import WebsiteSaleWishlist
from psycopg2 import Error


_logger = logging.getLogger(__name__)

class EmiproThemeBase(http.Controller):

    @http.route('/get_test_homepage_data', type='json', auth="user")
    def get_homepage_test_data(self):
        response = http.Response(template="theme_clarico_vega.js_home_page_1_test")
        return response.render()



