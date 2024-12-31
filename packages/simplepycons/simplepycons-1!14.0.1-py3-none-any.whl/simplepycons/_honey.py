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


class HoneyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "honey"

    @property
    def original_file_name(self) -> "str":
        return "honey.svg"

    @property
    def title(self) -> "str":
        return "Honey"

    @property
    def primary_color(self) -> "str":
        return "#FF6801"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Honey</title>
     <path d="M9.416 5.59c.04-.994.254-2.312.909-3.091.922-1.09
 2.794-.914 3.102.658.146.767-.054 1.708-.402 2.367-.734 1.439-2.1
 2.622-3.636 3.026.013-.901 0-2.071.027-2.96zm12.54
 13.904c-.775.901-1.764 1.6-2.714
 1.56-1.07-.04-.963-1.372-.963-2.124v-3.16c.014-.605.014-1.21-.053-1.802-.174-1.761-1.204-3.173-3.142-3.307-3.37-.135-4.706
 3.132-5.695 5.821v-5.89c2.94-.456 7.02-2.11
 7.14-5.875.2-6.4-10.563-6.629-10.523 1.426.014.618.014 1.802.014
 2.42-1.445-.215-2.608-2.34-3.143-3.604a.35.35 0 0 0-.427-.215C.43
 5.27.137 7.407 1.5 8.86c1.124 1.197 2.915 1.654 4.493 1.735-.013
 4.664-.013 7.542-.013 12.194.067.66.962.835 1.484.848.588.013
 1.684-.16 1.738-.928.187-2.286 2.125-9.036 4.76-9.036.613 0
 .908.403.908.995v5.5c0 2.286 1.284 3.818 3.623 3.832 2.073 0
 3.891-1.72 4.8-3.698.281-.632-.922-1.278-1.337-.807z" />
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
