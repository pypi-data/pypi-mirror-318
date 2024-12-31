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


class ActivisionIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "activision"

    @property
    def original_file_name(self) -> "str":
        return "activision.svg"

    @property
    def title(self) -> "str":
        return "Activision"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Activision</title>
     <path d="M1.88 8.91L0
 14.284h.985l.27-.718h1.252l.269.718h.985zm3.224.359l-.537.984h2.15v4.03H7.7v-4.03h1.522l1.882
 4.837 1.791-4.837h4.567l-.537-.984H12.18l-1.074 2.865L9.94
 9.269zm16.21 1.163v3.762h.986v-1.523l1.7
 1.702v-3.76h-.896v1.342zm-15.94.09c-1.075 0-1.881.807-1.881 1.881 0
 1.075.806 1.88 1.88 1.88.448 0 .895-.179 1.164-.447L6
 12.94c-.18.18-.358.27-.627.27a.897.897 0 0
 1-.895-.896c0-.448.358-.896.895-.896.18 0
 .448.089.537.268l.627-.715c-.27-.269-.716-.448-1.164-.448zm7.522
 0v3.672h.985v-3.671zm2.148 0c-.358 0-.804.18-.804.896 0 .896 1.074
 1.433.985 1.792-.09.179-.27.178-.359.178h-.626v.806h1.074c.448 0
 .895-.269.895-.806 0-.985-1.253-1.611-.984-1.97
 0-.09.178-.09.178-.09h.628v-.805zm1.255 0v3.672h.984v-3.671zm3.045
 0c-1.075 0-1.88.807-1.88 1.881 0 .985.805 1.88 1.88 1.88 1.074 0
 1.88-.805 1.88-1.88
 0-1.074-.806-1.88-1.88-1.88zm-11.016.09v3.672h.986v-3.672zm11.016.896c.448
 0 .895.358.895.895a.897.897 0 0 1-.895.896c-.538
 0-.985-.358-.896-.896
 0-.448.358-.895.896-.895zm-17.464.178l.27.896h-.54z" />
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
