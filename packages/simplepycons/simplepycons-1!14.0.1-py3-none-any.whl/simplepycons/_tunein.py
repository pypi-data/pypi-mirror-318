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


class TuneinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tunein"

    @property
    def original_file_name(self) -> "str":
        return "tunein.svg"

    @property
    def title(self) -> "str":
        return "TuneIn"

    @property
    def primary_color(self) -> "str":
        return "#14D8CC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TuneIn</title>
     <path d="M7.66 11.398v.742c0 .105-.11.105-.11.105h-.847s-.11
 0-.11.11v4.03c0 .11-.105.11-.105.11h-.855c-.106
 0-.106-.11-.106-.11v-4.03s0-.11-.109-.11h-.844c-.105
 0-.105-.105-.105-.105v-.742c0-.106.105-.106.105-.106H7.66v.106m15.458-7.52H12.301c-.68
 0-.836.16-.836.816v2.414c0 .493 0 .493-.492.493H.813C.137 7.6 0 7.737
 0 8.425v5.41c0 1.754 0 3.508.023 5.266 0 .922.102 1.02 1.04
 1.02H9.89c.664 0 1.32.01
 1.984-.01.48-.006.669-.202.669-.682v-2.56c0-.468
 0-.468.469-.468h10.195c.633 0
 .793-.152.793-.78V4.736c0-.7-.164-.86-.883-.86zm-11.64 14.625c0
 .5-.013.5-.525.5-3.148 0-6.293 0-9.445.008-.32
 0-.43-.078-.43-.418.016-3.16.008-6.324
 0-9.48-.008-.34.086-.446.442-.446 3.187.012 6.363.008 9.55.008.117 0
 .23.015.4.023 0 .18 0 .32.01.442-.003 3.113-.003 6.242-.003
 9.363zm7.69-5.844c0 .102-.104.102-.104.102h-2.57c-.106
 0-.106-.102-.106-.102v-.72c0-.1.105-.1.105-.1h.617s.102 0
 .102-.102V8.659s0-.101-.102-.101h-.515c-.102
 0-.102-.102-.102-.102v-.82c0-.106.102-.106.102-.106h2.367c.102 0
 .102.106.102.106v.715c0 .105-.102.105-.102.105h-.516s-.101
 0-.101.102v3.074s0 .105.1.105h.618c.106 0 .106.102.106.102z" />
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
