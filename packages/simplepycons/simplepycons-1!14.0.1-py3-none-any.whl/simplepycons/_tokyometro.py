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


class TokyoMetroIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tokyometro"

    @property
    def original_file_name(self) -> "str":
        return "tokyometro.svg"

    @property
    def title(self) -> "str":
        return "Tokyo Metro"

    @property
    def primary_color(self) -> "str":
        return "#149DD3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tokyo Metro</title>
     <path d="M11.9832 18.2104c2.86.006 4.04-.949
 4.043-2.392.003-1.7021-1.694-3.7822-2.923-5.0732 2.318-2.082
 5.3251-3.622 6.5082-2.432 1.367 1.367.02 5.418-3.2131 9.8922l4.26
 1.222c3.6132-6.4301 4.3802-12.7603 1.8901-14.4733-1.946-1.329-6.8521
 1.337-10.5502 4.721-3.6871-3.398-8.5802-6.08-10.5323-4.759-2.5
 1.704-1.748 8.0372 1.841 14.4803l4.2662-1.207C4.35 13.7033 3.02
 9.6482 4.393 8.285c1.184-1.185 4.1861.365 6.5002 2.4561-1.237
 1.286-2.9431 3.36-2.9451 5.0621-.003 1.444 1.176 2.402 4.035
 2.408zm.004-2.34c-.947-.001-1.745-.242-1.743-1.0501 0-.748.637-1.88
 1.75-3.106 1.11 1.23 1.739 2.364 1.738 3.113-.001.807-.8 1.045-1.745
 1.044z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Tokyo'''

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
