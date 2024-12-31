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


class BvgIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bvg"

    @property
    def original_file_name(self) -> "str":
        return "bvg.svg"

    @property
    def title(self) -> "str":
        return "BVG"

    @property
    def primary_color(self) -> "str":
        return "#F0D722"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>BVG</title>
     <path d="M17.25 1.11c3.647 0 6.478 2.886 6.73 6.447.151 2.21-.535
 4.019-2.158 5.674l-3.601
 3.655-.154.157-.078.079-.214.217-.214.217a18348.219 18348.219 0 0
 1-4.951 5.019c-.074.074-.323.302-.576.315h-.023c-.272
 0-.534-.24-.6-.315l-4.89-4.958-.129-.13-.257-.261-.214-.218A5994.604
 5994.604 0 0 1 2.2 13.23C.554 11.576-.13 9.768.02 7.557.27 3.997
 3.103 1.11 6.75 1.11c2.353 0 3.704 1.416 5.25 3.027 1.536-1.61
 2.897-3.027 5.25-3.027zm-4.02 6.48c-.26 0-.446.174-.511.48l-.6
 3.092c-.043.294-.097.642-.12.87a5.71 5.71 0 0
 0-.12-.87l-.663-3.093c-.065-.36-.283-.48-.534-.48-.392
 0-.577.35-.479.763l1.013 4.193c.098.414.305.642.784.642.414 0
 .664-.228.762-.686l.948-4.214c.087-.425-.153-.697-.48-.697zm2.995-.033c-1.274
 0-2.101.85-2.101 2.832 0 1.884.37 2.787 2.003 2.787 1.013 0 1.48-.348
 1.48-1.143v-1.634c0-.337-.107-.479-.412-.479h-.904c-.294
 0-.436.142-.436.414 0 .25.163.392.436.392h.305v1.568a1.015 1.015 0 0
 1-.35.044c-.73 0-1.077-.349-1.077-1.873 0-1.634.414-2.004
 1.035-2.004.468 0 .697.163.925.163a.439.439 0 0 0
 .294-.762c-.305-.24-.925-.305-1.198-.305Zm-8.091.065H7.056a.42.42 0 0
 0-.436.414v4.716c0 .283.185.37.436.37h.99c1.406 0 1.721-.784
 1.732-1.655 0-.556-.272-1.177-1.056-1.22.719-.153.904-.664.904-1.242
 0-.718-.196-1.383-1.492-1.383zm-.185 3.018c.686 0
 .74.37.74.86v.02c-.002.45-.074.852-.664.852h-.37v-1.733h.294zm.022-2.265c.577
 0
 .664.207.664.762v.071l-.001.03c-.01.325-.087.682-.718.682h-.25V8.374h.305z"
 />
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
        yield from [
            "Berliner Verkehrsbetriebe",
        ]
