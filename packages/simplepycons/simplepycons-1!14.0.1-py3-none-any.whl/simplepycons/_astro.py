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


class AstroIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "astro"

    @property
    def original_file_name(self) -> "str":
        return "astro.svg"

    @property
    def title(self) -> "str":
        return "Astro"

    @property
    def primary_color(self) -> "str":
        return "#BC52EE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Astro</title>
     <path d="M8.358 20.162c-1.186-1.07-1.532-3.316-1.038-4.944.856
 1.026 2.043 1.352 3.272 1.535 1.897.283 3.76.177
 5.522-.678.202-.098.388-.229.608-.36.166.473.209.95.151 1.437-.14
 1.185-.738 2.1-1.688 2.794-.38.277-.782.525-1.175.787-1.205.804-1.531
 1.747-1.078 3.119l.044.148a3.158 3.158 0 0 1-1.407-1.188 3.31 3.31 0
 0
 1-.544-1.815c-.004-.32-.004-.642-.048-.958-.106-.769-.472-1.113-1.161-1.133-.707-.02-1.267.411-1.415
 1.09-.012.053-.028.104-.045.165h.002zm-5.961-4.445s3.24-1.575
 6.49-1.575l2.451-7.565c.092-.366.36-.614.662-.614.302 0
 .57.248.662.614l2.45 7.565c3.85 0 6.491 1.575 6.491
 1.575L16.088.727C15.93.285 15.663 0 15.303 0H8.697c-.36
 0-.615.285-.784.727l-5.516 14.99z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
