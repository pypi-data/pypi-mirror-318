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


class AppveyorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "appveyor"

    @property
    def original_file_name(self) -> "str":
        return "appveyor.svg"

    @property
    def title(self) -> "str":
        return "AppVeyor"

    @property
    def primary_color(self) -> "str":
        return "#00B3E0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AppVeyor</title>
     <path d="M 12,0 C 18.6,0 24,5.4 24,12 24,18.6 18.6,24 12,24
 5.4,24 0,18.6 0,12 0,5.4 5.4,0 12,0 Z m 2.94,14.34 C 16.26,12.66
 16.08,10.26 14.4,9 12.78,7.74 10.38,8.04 9,9.72 7.68,11.4 7.86,13.8
 9.54,15.06 c 1.68,1.26 4.08,0.96 5.4,-0.72 z m -6.42,7.8 c 0.72,0.3
 2.28,0.6 3.06,0.6 l 5.22,-7.56 c 1.68,-2.52 1.26,-5.94 -1.08,-7.8
 -2.1,-1.68 -5.04,-1.62 -7.14,0 l -7.26,5.58 c 0.18,1.92 0.72,2.88
 0.72,2.94 l 4.14,-4.5 c -0.3,1.98 0.42,4.02 2.1,5.28 1.44,1.14
 3.18,1.44 4.86,1.08 z" />
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
