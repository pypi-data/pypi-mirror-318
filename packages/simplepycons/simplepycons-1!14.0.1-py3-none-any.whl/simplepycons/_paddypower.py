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


class PaddyPowerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "paddypower"

    @property
    def original_file_name(self) -> "str":
        return "paddypower.svg"

    @property
    def title(self) -> "str":
        return "Paddy Power"

    @property
    def primary_color(self) -> "str":
        return "#004833"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Paddy Power</title>
     <path d="M15.014 3.713a18.383 18.383 0 0
 0-1.626.084c-.816.082-1.714.245-2.53.408l.57 6.368.246 1.96.654 6.857
 1.55-.083 1.796-.162v-.082l-.408-4.081v-.573a19.201 19.201 0 0 0
 2.04-.408 10.164 10.164 0 0 0 1.633-.816 5.257 5.257 0 0 0
 1.714-2.041 6.53 6.53 0 0 0 .409-2.774 4.751 4.751 0 0 0-2.858-4.082
 7.347 7.347 0 0 0-2.694-.572 18.383 18.383 0 0
 0-.496-.003zm-10.775.98a18.383 18.383 0 0 0-1.626.085A14.026 14.026 0
 0 0 0 5.105l.572 6.366.163 1.96.654 6.857 1.551-.082
 1.795-.164-.327-4.081v-.571a19.197 19.197 0 0 0 2.041-.408 10.164
 10.164 0 0 0 1.633-.817 5.257 5.257 0 0 0 1.714-2.04 5.967 5.967 0 0
 0 .408-2.695A4.653 4.653 0 0 0 7.43 5.267a7.347 7.347 0 0 0-2.695-.57
 18.383 18.383 0 0 0-.496-.004zM15.1 6.731a1.233 1.233 0 0 1 .085.006
 3.265 3.265 0 0 1 1.468.325 2.065 2.065 0 0 1 1.062 1.633 2.596 2.596
 0 0 1-.164 1.143 1.861 1.861 0 0 1-.571.817 2.449 2.449 0 0
 1-1.306.572 1.78 1.78 0 0 1-.653.081l-.409-4.49a1.233 1.233 0 0 1
 .488-.087zm-10.942.98a1.233 1.233 0 0 1 .17.005 3.265 3.265 0 0 1
 1.47.327 2.065 2.065 0 0 1 1.06 1.633 4.947 4.947 0 0 1-.163 1.143
 1.861 1.861 0 0 1-.573.816 2.449 2.449 0 0 1-1.305.57 1.78 1.78 0 0
 1-.653.082l-.408-4.49a1.233 1.233 0 0 1 .402-.086zm17.801 7.27A2.04
 2.04 0 1 0 24 17.023a2.04 2.04 0 0 0-2.04-2.04z" />
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
