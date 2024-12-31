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


class CbcIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cbc"

    @property
    def original_file_name(self) -> "str":
        return "cbc.svg"

    @property
    def title(self) -> "str":
        return "CBC"

    @property
    def primary_color(self) -> "str":
        return "#E60505"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CBC</title>
     <path d="M12 0c-1.5673 0-2.9376.8395-3.6855
 2.0938l7.369.0019C14.9357.8402 13.5676 0 12 0zm0 2.7676c-2.3692
 0-4.291 1.9188-4.291
 4.287h8.5781c0-2.3682-1.9191-4.287-4.2871-4.287zm-4.9531.209c-2.2507
 0-4.0762 1.8241-4.0762
 4.0742h4.0762V2.9766zm9.9043.002v4.0722l4.0722.002c0-2.2501-1.8234-4.0743-4.0722-4.0743zM7.0469
 7.709c-2.3698 0-4.289 1.9224-4.289 4.291 0 2.368 1.9189 4.2871 4.289
 4.2871V7.709zm9.9043 0v8.5781c2.3682 0 4.291-1.9191 4.291-4.2871
 0-2.3686-1.9228-4.291-4.291-4.291zm-4.9551.002C9.6278 7.711 7.709
 9.6316 7.709 12c0 2.3686 1.9188 4.2871 4.287 4.2871 2.3684 0
 4.2892-1.9185 4.2892-4.2871
 0-2.3683-1.9208-4.289-4.2891-4.289zm-9.9004.6035C.8399 9.062 0
 10.4327 0 12c0 1.5666.8398 2.9364 2.0938 3.6855l.0019-7.371zm19.8086
 0 .002 7.371C23.1595 14.9364 24 13.5666 24
 12c0-1.5673-.8402-2.9379-2.0957-3.6855zM7.0469 16.9492l-4.0742.002c0
 2.2491 1.8222 4.0703 4.0742 4.0703v-4.0723zm9.9043 0v4.0703c2.2485 0
 4.0722-1.8189 4.0722-4.0683l-4.0722-.002zm-9.2422.002c0 2.3692 1.9218
 4.289 4.291 4.289 2.368 0 4.2871-1.9198 4.2871-4.289H7.709zm.5488
 4.9531C9.0061 23.1592 10.3755 24 11.9434 24c1.5672 0 2.9366-.8408
 3.6855-2.0957H8.258z" />
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
            "Canadian Broadcasting Company",
        ]
