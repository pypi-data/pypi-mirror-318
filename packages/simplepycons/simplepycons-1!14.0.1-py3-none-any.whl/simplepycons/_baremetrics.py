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


class BaremetricsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "baremetrics"

    @property
    def original_file_name(self) -> "str":
        return "baremetrics.svg"

    @property
    def title(self) -> "str":
        return "Baremetrics"

    @property
    def primary_color(self) -> "str":
        return "#6078FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Baremetrics</title>
     <path d="M22.109 7.951l1.485 2.464a3.507 3.507 0 010 3.275l-4.505
 7.717a3.333 3.333 0 01-2.94 1.793H7.83a3.335 3.335 0
 01-2.94-1.793l-1.555-2.632 6.139-5.695 4.447 2.578a1.093 1.093 0
 001.456-.198zm-13.39.628L1.99 16.15.406 13.725a3.495 3.495 0
 010-3.27L5.158 2.59A3.338 3.338 0 018.1.8h8.008c1.228 0 2.357.687
 2.942 1.79l1.616 2.722-6.017 5.592-4.432-2.574a1.098 1.098 0
 00-1.499.248z" />
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
