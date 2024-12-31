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


class ThunderbirdIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "thunderbird"

    @property
    def original_file_name(self) -> "str":
        return "thunderbird.svg"

    @property
    def title(self) -> "str":
        return "Thunderbird"

    @property
    def primary_color(self) -> "str":
        return "#0A84FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Thunderbird</title>
     <path d="M9.948 4.444h-.005c-1.92.788-2.126 2.55-1.817
 3.499v.02C9.236 7.18 10.658 6.76 12 6.76c3.26 0 5.902 2.156 5.902
 4.815 0 2.66-2.643 4.816-5.902
 4.816l-.083-.002c-.155-.006-.354-.013-.435.118-.096.156.116.397.238.536
 1.274 1.441 3.123 1.622 3.608
 1.67l.076.008c-4.281.414-9.304-2.32-9.306-7.076 0-1.12.414-2.073
 1.075-2.83l-.005-.002h-.003C7.31 6.38 6.376 3.47 4.629
 2.898c-.124-.04-.246.054-.262.183-.23 1.924-.727 2.59-1.264 3.31-.805
 1.08-1.39 2.328-1.365 3.698a10.99 10.99 0 0
 1-.705-1.91c-.024-.09-.17-.365-.333-.272-.13.072-.227.274-.296.485A12.137
 12.137 0 0 0 0 11.489c0 6.536 5.475 12 12 12 6.627 0 12-5.372 12-12
 0-2.526-.781-4.87-2.115-6.805l.167-.002c.518 0 1.024.045
 1.51.129-.734-.816-1.724-1.475-2.877-1.904a8.54 8.54 0 0 1
 2.494-.495c-1.426-1.166-3.508-1.9-5.827-1.9-3.355 0-6.648 1.29-7.404
 3.93zm.682 9.166c-.87-.905-3.473-3.91-3.473-3.91l.202.01 4.075
 3.042c.305.223.74.22 1.043-.004l3.996-3.034.212-.018s-2.518
 2.935-3.483
 3.9c-.964.968-1.703.919-2.572.014zm2.774-10.083s.055.625-.576.824c-.722.227-1.042-.38-1.042-.38s.09-.417.676-.61c.626-.206.942.166.942.166z"
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
        yield from []
