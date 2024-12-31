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


class HoudiniIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "houdini"

    @property
    def original_file_name(self) -> "str":
        return "houdini.svg"

    @property
    def title(self) -> "str":
        return "Houdini"

    @property
    def primary_color(self) -> "str":
        return "#FF4713"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Houdini</title>
     <path d="M0 19.635V24h3.824A8.662 8.662 0 0 1 0
 19.635zm16.042-4.555c0-4.037-3.253-7.92-8.111-8.089C4.483 6.873 1.801
 8.136 0 10.005v4.209c1.224-3.549 4.595-5.158 7.419-5.128 3.531.041
 6.251 2.703 6.275 5.72 0 2.878-1.183 4.992-4.436
 5.516-1.774.296-4.548-.754-4.436-3.434.065-1.381 1.138-2.162
 2.366-2.106-1.207 1.618.39 2.801 1.52 2.561a2.51 2.51 0 0 0
 1.966-2.502c0-1.017-.958-2.662-3.333-2.6-2.936.068-4.785 2.183-4.85
 4.797-.071 3.28 3.007 5.457 6.174 5.483 4.633.059 7.395-2.984
 7.377-7.441zM0 0v6.906a12.855 12.855 0 0 1 7.931-2.609c6.801 0 11.134
 4.762 11.131 10.765 0 4.17-1.946 7.308-4.995 8.938H24V0H0z" />
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
