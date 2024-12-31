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


class SwarmIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "swarm"

    @property
    def original_file_name(self) -> "str":
        return "swarm.svg"

    @property
    def title(self) -> "str":
        return "Swarm"

    @property
    def primary_color(self) -> "str":
        return "#FFA633"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Swarm</title>
     <path d="M16.358 1.216c-1.82.023-4.234 2.581-2.57
 6.704.018.034.08.17.091.204h.003c5.172-2.298 4.45-6.287
 3.112-6.8a1.71 1.71 0 0 0-.636-.108zM4.001
 2.768c-1.867.027-3.392.81-3.874 2.06-.91 2.365 3.07 7.996 12.229
 3.93l.004-.003a5.53 5.53 0 0 1-.16-.362C10.193 4.303 6.73 2.728 4
 2.768zM15.51 9.432l-.138.034a7.08 7.08 0 0
 0-2.153.951c-.949.624-1.786 1.549-2.147
 2.641-.097.295-.17.618-.194.928a9.153 9.153 0 0 0 .77 4.451 9.165
 9.165 0 0 0 2.681 3.46c.686.544 1.92.887 2.93.887.949 0 1.884-.282
 2.725-.71.262-.133.841-.494.879-.52a3.847 3.847 0 0
 1-1.378-.663c-1.447-1.107-2.594-2.595-3.409-4.423-.826-1.854-1.163-3.73-1.002-5.575a3.813
 3.813 0 0 1 .436-1.46zm3.498.026c-.868 0-1.704.722-1.783 1.623-.132
 1.503.166 3.033.824 4.51.648 1.453 1.567 2.683 2.749 3.586a1.73 1.73
 0 0 0 1.06.346c.677 0 1.353-.36 1.621-1.002a6.74 6.74 0 0
 0-.068-5.356 6.75 6.75 0 0 0-3.891-3.618 1.508 1.508 0 0
 0-.512-.089zm-10.05 5.498a28.722 28.722 0 0 0-2.175
 4.098c-.023.054-.378.932-.483 1.205a.676.676 0 0 0 .384.86c.273.107
 1.164.43 1.22.449a28.93 28.93 0 0 0 4.453 1.12 11.15 11.15 0 0
 1-2.442-3.48 11.136 11.136 0 0 1-.958-4.252z" />
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
