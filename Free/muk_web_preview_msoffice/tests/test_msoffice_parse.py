# -*- coding: utf-8 -*-

###################################################################################
#
#    Copyright (C) 2017 MuK IT GmbH
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

import os
import base64
import logging
import unittest

from urllib.parse import urlunparse
from urllib.parse import urlparse
from urllib.parse import parse_qsl
from urllib.parse import urlencode
from contextlib import closing

from flectra import _
from flectra.tests import common

from flectra.addons.muk_web_preview_mail.controllers import main

_path = os.path.dirname(os.path.dirname(__file__))
_logger = logging.getLogger(__name__)

class MSOfficeParseTestCase(common.HttpCase):
    
    at_install = False
    post_install = True
    
    def setUp(self):
        super(MSOfficeParseTestCase, self).setUp()
        self.sample_msoffice_attachment = self.browse_ref('muk_web_preview_msoffice.msoffice_attachment_demo')

    def tearDown(self):
        super(MSOfficeParseTestCase, self).tearDown()
        
    def test_parse_msoffice(self):
        self.authenticate('admin', 'admin')
        url = "/web/preview/converter/msoffice"
        params = {'url': "/web/content?id={}".format(
           self.sample_msoffice_attachment.id
        )}
        url_parts = list(urlparse(url))
        query = dict(parse_qsl(url_parts[4]))
        query.update(params)
        url_parts[4] = urlencode(query)
        url = urlunparse(url_parts)
        self.url_open(url)              