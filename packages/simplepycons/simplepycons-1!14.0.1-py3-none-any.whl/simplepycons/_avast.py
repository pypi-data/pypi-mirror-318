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


class AvastIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "avast"

    @property
    def original_file_name(self) -> "str":
        return "avast.svg"

    @property
    def title(self) -> "str":
        return "Avast"

    @property
    def primary_color(self) -> "str":
        return "#FF7800"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Avast</title>
     <path d="M10.2941 2.991a3.0286 3.0286 0 0 1 4.4499 1.2039l7.0018
 14.8042a11.937 11.937 0 0 0 2.2539-6.9131C24.0464 5.4569 18.7112.047
 12.0834.0004 5.4556-.0463.047 5.2889.0004 11.9167a11.9356 11.9356 0 0
 0 2.2213 7.0344l.2813-.0613
 4.5692-1.008c.1287-.0286.1967.1454.084.2127L3.3736 20.337a11.9563
 11.9563 0 0 0 8.5431 3.6625c3.76.0267 7.1258-1.68
 9.3444-4.3705L9.8095 7.5735a3.0272 3.0272 0 0 1 .4846-4.5826zm2.1493
 13.6089-7.3731.64a1.302 1.302 0 1 1 .1866-2.5666l7.2031
 1.6972c.1287.0314.114.2174-.0166.2294zM9.03 10.116l8.9404
 7.2324c.102.0827.01.2447-.1133.198L7.1035 13.4713a1.9593 1.9593 0 1 1
 1.9266-3.3552z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://press.avast.com/media-materials#logos'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://press.avast.com/media-materials#logos'''

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
