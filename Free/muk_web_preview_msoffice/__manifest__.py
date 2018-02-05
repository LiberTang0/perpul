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

{
    "name": "MuK Preview MS Office",
    "summary": """MS Office Preview""",
    "description": """ 
        Extendes the Preview Dialog to support MS Office files.
        Currently the following file extensions are supported:
            - Word (*.doc | *.docx, application/msword)
            - Excel (*.xls | *.xlsx, application/msexcel)
            - PowerPoint (*.ppt | *.pptx, application/mspowerpoint)
    """,
    "version": "11.0.1.1.0",
    "category": "Extra Tools",
    "license": "AGPL-3",
    "website": "http://www.mukit.at",
    "author": "MuK IT",
    "contributors": [
        "Mathias Markl <mathias.markl@mukit.at>",
    ],
    "depends": [
        "muk_web_preview",
    ],
    "data": [
        "template/assets.xml",
    ],
    "demo": [
        "demo/preview_office_demo.xml",
    ],
    "qweb": [
        "static/src/xml/*.xml",
    ],
    "images": [
        'static/description/banner.png'
    ],
    "external_dependencies": {
        "python": [
            'requests',
            'cachetools',
            'pdfconv'
        ],
        "bin": [],
    },
    "application": False,
    "installable": True,
    
}    