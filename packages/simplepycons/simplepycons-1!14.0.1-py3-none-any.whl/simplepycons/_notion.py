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


class NotionIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "notion"

    @property
    def original_file_name(self) -> "str":
        return "notion.svg"

    @property
    def title(self) -> "str":
        return "Notion"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Notion</title>
     <path d="M4.459 4.208c.746.606 1.026.56 2.428.466l13.215-.793c.28
 0 .047-.28-.046-.326L17.86 1.968c-.42-.326-.981-.7-2.055-.607L3.01
 2.295c-.466.046-.56.28-.374.466zm.793 3.08v13.904c0 .747.373 1.027
 1.214.98l14.523-.84c.841-.046.935-.56.935-1.167V6.354c0-.606-.233-.933-.748-.887l-15.177.887c-.56.047-.747.327-.747.933zm14.337.745c.093.42
 0 .84-.42.888l-.7.14v10.264c-.608.327-1.168.514-1.635.514-.748
 0-.935-.234-1.495-.933l-4.577-7.186v6.952L12.21 19s0
 .84-1.168.84l-3.222.186c-.093-.186
 0-.653.327-.746l.84-.233V9.854L7.822
 9.76c-.094-.42.14-1.026.793-1.073l3.456-.233 4.764
 7.279v-6.44l-1.215-.139c-.093-.514.28-.887.747-.933zM1.936
 1.035l13.31-.98c1.634-.14 2.055-.047 3.082.7l4.249
 2.986c.7.513.934.653.934 1.213v16.378c0 1.026-.373 1.634-1.68
 1.726l-15.458.934c-.98.047-1.448-.093-1.962-.747l-3.129-4.06c-.56-.747-.793-1.306-.793-1.96V2.667c0-.839.374-1.54
 1.447-1.632z" />
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
