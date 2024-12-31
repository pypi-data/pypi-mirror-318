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


class MaptilerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "maptiler"

    @property
    def original_file_name(self) -> "str":
        return "maptiler.svg"

    @property
    def title(self) -> "str":
        return "MapTiler"

    @property
    def primary_color(self) -> "str":
        return "#323357"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MapTiler</title>
     <path d="m7.794 1.655 4.188 4.188 4.204-4.204A6.13 6.13 0 0 0 12
 0a6.136 6.136 0 0 0-4.204 1.655ZM3.25 6.197 7.455 1.99l4.19
 4.19-4.206 4.207Zm-.315 8.697 4.168-4.168-2.889-2.89-1.298-1.299a6.19
 6.19 0 0 0 .02 8.357zm14.728-5.64 3.073-3.073-4.208-4.207-4.207 4.207
 4.207 4.206Zm-6.015 6.013L7.44 11.061l-4.172 4.172 4.206
 4.208zm5.216-4.543 4.185 4.185a6.18 6.18 0 0 0 .02-8.387l-4.205
 4.202zm-2.448 6.639 2.093 2.092 4.207-4.206-4.188-4.188-4.207
 4.206zM11.968 24a3007.16 3007.16 0 0 0 4.2-4.208l-4.187-4.188-4.17
 4.174c1.386 1.407 2.773 2.813 4.157 4.222Z" />
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
