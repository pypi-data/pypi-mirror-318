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


class PlaystationPortableIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "playstationportable"

    @property
    def original_file_name(self) -> "str":
        return "playstationportable.svg"

    @property
    def title(self) -> "str":
        return "PlayStation Portable"

    @property
    def primary_color(self) -> "str":
        return "#003791"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PlayStation Portable</title>
     <path d="M0
 9.93v.296h7.182v1.626H.001v2.217h.295v-1.921h7.182V9.93zm11.29
 0v3.844H7.478v.296h4.124v-3.844h3.813V9.93zm5.233
 0v.296h7.182v1.626h-7.182v2.217h.296v-1.921H24V9.93z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:PSP_L'''

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
        yield from [
            "PSP",
        ]
