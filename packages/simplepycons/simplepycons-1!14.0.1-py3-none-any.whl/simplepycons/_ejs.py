#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class EjsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ejs"

    @property
    def original_file_name(self) -> "str":
        return "ejs.svg"

    @property
    def title(self) -> "str":
        return "EJS"

    @property
    def primary_color(self) -> "str":
        return "#B4CA65"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>EJS</title>
     <path d="m8.291 5.696-1.258-1.58 1.668-1.55 1.258 1.58-1.668
 1.55zm2.34 2.048.205-1.55-5.412-.03-.204 1.55 3.945.022L7.8
 17.852l-.839.77-.405-.004c.385.403.803.81 1.236 1.214l1.378-1.265
 1.458-10.823h.004zm-6.757 7.254s2.925-.468 3.54.38c0
 0-1.756-2.925-4.184-2.925 0-.074-.098-1.353
 5.146-2.609l.206-1.53c-8.346 1.108-14.287 4.322.265 13.12 0
 0-5.675-4.71-4.973-6.436zM13 6.223 11.216 7.86l-.526 4.037 1.316
 1.638 5.675.058.556.702-.38
 2.633-.713.685-.018.017h2.193l.556-4.037-1.345-1.638-5.646-.058-.556-.702.351-2.633.731-.702
 5.032.058.556.673-.176
 1.229h1.55l.264-1.902-1.317-1.667-6.318-.03zm2.882
 11.908.545-.523-4.305-.035-.965-1.17-1.258 1.17 1.346 1.667 6.318.03
 1.22-1.139h-2.901zM13.13 8.965a103.16 103.16 0 0 1
 4.624-.554l-4.145-.048-.457.44-.022.162zm8.026-1.156-.025.179-.018.132c.92-.07
 1.87-.139 2.887-.2 0 0-1.113-.067-2.844-.11zM1.914 18.392l1.404 1.784
 2.66.02c-1.292-.875-2.393-1.708-3.296-2.499l-.768.695z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/mde/ejs-site/blob/dd845093'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
