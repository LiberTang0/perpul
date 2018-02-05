# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2017-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Niyas Raphy(<https://www.cybrosys.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from flectra.addons.web.controllers import main
from flectra.http import request
from flectra.exceptions import Warning
import flectra
import flectra.modules.registry
from flectra.tools.translate import _
from flectra import http


class Home(main.Home):

    @http.route('/web/login', type='http', auth="public")
    def web_login(self, redirect=None, **kw):
        main.ensure_db()
        request.params['login_success'] = False
        if request.httprequest.method == 'GET' and redirect and request.session.uid:
            return http.redirect_with_hash(redirect)

        if not request.uid:
            request.uid = flectra.SUPERUSER_ID

        values = request.params.copy()
        try:
            values['databases'] = http.db_list()
        except flectra.exceptions.AccessDenied:
            values['databases'] = None
        if request.httprequest.method == 'POST':
            old_uid = request.uid
            ip_address = request.httprequest.environ['REMOTE_ADDR']
            if request.params['login']:
                user_rec = request.env['res.users'].sudo().search([('login', '=', request.params['login'])])
                if user_rec.allowed_ips:
                    ip_list = []
                    for rec in user_rec.allowed_ips:
                        ip_list.append(rec.ip_address)
                    if ip_address in ip_list:
                        uid = request.session.authenticate(request.session.db, request.params['login'], request.params['password'])
                        if uid is not False:
                                request.params['login_success'] = True
                                if not redirect:
                                    redirect = '/web'
                                return http.redirect_with_hash(redirect)
                        request.uid = old_uid
                        values['error'] = _("Wrong login/password")
                    request.uid = old_uid
                    values['error'] = _("Not allowed to login from this IP")
                else:
                    uid = request.session.authenticate(request.session.db, request.params['login'],
                                                       request.params['password'])
                    if uid is not False:
                        request.params['login_success'] = True
                        if not redirect:
                            redirect = '/web'
                        return http.redirect_with_hash(redirect)
                    request.uid = old_uid
                    values['error'] = _("Wrong login/password")

        return request.render('web.login', values)
