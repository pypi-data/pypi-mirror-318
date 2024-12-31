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


class LiberapayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "liberapay"

    @property
    def original_file_name(self) -> "str":
        return "liberapay.svg"

    @property
    def title(self) -> "str":
        return "Liberapay"

    @property
    def primary_color(self) -> "str":
        return "#F6C915"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Liberapay</title>
     <path d="M2.32 0A2.321 2.321 0 0 0 0 2.32v19.36A2.321 2.321 0 0 0
 2.32 24h19.36A2.32 2.32 0 0 0 24 21.68V2.32A2.32 2.32 0 0 0 21.68
 0zm9.208 3.98l-2.27 9.405a2.953 2.953 0 0 0-.073.539.853.853 0 0 0
 .09.432.7.7 0 0 0 .334.302c.157.077.378.126.661.147l-.49 2.008c-.772
 0-1.38-.1-1.82-.3-.441-.203-.757-.477-.947-.826a2.391 2.391 0 0
 1-.278-1.2c.005-.452.068-.933.188-1.445l2.074-8.67zm3.9 3.888c.61 0
 1.135.092 1.576.277.44.185.802.438 1.085.76.283.32.493.696.629
 1.126.136.43.204.89.204 1.379v.001c0 .794-.13 1.52-.392 2.179a5.16
 5.16 0 0 1-1.086 1.706 4.84 4.84 0 0 1-1.665
 1.118c-.648.267-1.353.4-2.114.4-.37 0-.74-.033-1.11-.098l-.735
 2.956H9.403l2.71-11.298c.435-.13.934-.248 1.494-.351a10.045 10.045 0
 0 1 1.821-.155zm-.31 2.041a4.67 4.67 0 0 0-.98.098l-1.143
 4.752c.185.044.413.065.685.065.425 0 .812-.079 1.16-.237a2.556 2.556
 0 0 0 .89-.661c.244-.283.435-.623.571-1.02a4.03 4.03 0 0 0
 .204-1.315c0-.468-.104-.865-.31-1.192-.207-.326-.566-.49-1.077-.49z"
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
