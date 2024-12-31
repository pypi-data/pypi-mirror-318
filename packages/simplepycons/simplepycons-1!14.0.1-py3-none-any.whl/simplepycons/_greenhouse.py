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


class GreenhouseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "greenhouse"

    @property
    def original_file_name(self) -> "str":
        return "greenhouse.svg"

    @property
    def title(self) -> "str":
        return "Greenhouse"

    @property
    def primary_color(self) -> "str":
        return "#24A47F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Greenhouse</title>
     <path d="M16.279 7.13c0 1.16-.49 2.185-1.293 2.987-.891.891-2.184
 1.114-2.184 1.872 0 1.025 1.65.713 3.231 2.295 1.048 1.047 1.694 2.43
 1.694 4.034C17.727 21.482 15.187 24 12 24c-3.187
 0-5.727-2.518-5.727-5.68 0-1.607.646-2.989 1.694-4.036 1.582-1.582
 3.23-1.27 3.23-2.295
 0-.758-1.292-.98-2.183-1.872-.802-.802-1.293-1.827-1.293-3.03 0-2.318
 1.895-4.19 4.212-4.19.446 0 .847.067 1.181.067.602 0
 .914-.268.914-.691 0-.245-.112-.557-.112-.891 0-.758.647-1.382
 1.427-1.382s1.404.646 1.404 1.426c0 .825-.647 1.204-1.137
 1.382-.401.134-.713.312-.713.713 0 .758 1.382 1.493 1.382 3.61zm-.446
 11.19c0-2.206-1.627-3.99-3.833-3.99-2.206 0-3.833 1.784-3.833 3.99 0
 2.184 1.627 3.989 3.833 3.989 2.206 0 3.833-1.808 3.833-3.99zM14.518
 7.086c0-1.404-1.136-2.562-2.518-2.562S9.482 5.682 9.482 7.086 10.618
 9.65 12 9.65s2.518-1.159 2.518-2.563z" />
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
