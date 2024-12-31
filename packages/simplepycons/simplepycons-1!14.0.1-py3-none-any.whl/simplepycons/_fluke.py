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


class FlukeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fluke"

    @property
    def original_file_name(self) -> "str":
        return "fluke.svg"

    @property
    def title(self) -> "str":
        return "Fluke"

    @property
    def primary_color(self) -> "str":
        return "#FFC20E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fluke</title>
     <path d="M20.603 12.656h-.092v-.131h.08c.065 0 .078.013.078.065 0
 .04-.026.066-.066.066zm.263.013c0
 .157-.118.288-.276.288s-.275-.13-.275-.288c0-.158.105-.276.262-.289.17
 0 .289.118.289.289zm-.118.197-.105-.17c.052-.014.091-.053.091-.106
 0-.079-.052-.118-.13-.118h-.145v.394h.066v-.17h.065l.105.17h.053zM24
 8.393v7.214H0V8.393h24zM6.44
 11.567H4.222V11.2h2.203v-.498H3.633v2.308h.59v-.892h2.216v-.55zm2.819.866H7.384v-1.731h-.577v2.308h2.452v-.577zm3.462-1.731h-.577v1.77h-2.02v-1.77h-.576v1.875c.039.42.432.433.432.433h2.308s.38-.013.433-.433v-1.875zm3.568
 2.308-1.837-1.18
 1.745-1.128h-1.023l-1.299.8v-.8h-.577v2.308h.577v-.866l1.377.866h1.037zm3.239-2.308h-2.912v2.308h2.912v-.538h-2.335v-.328h2.335v-.537h-2.335v-.355h2.335v-.55zm1.403
 1.967a.347.347 0 0 0-.34-.341.347.347 0 0 0-.342.34c0
 .184.158.342.341.342a.347.347 0 0 0 .341-.341z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.fluke.com/en-us/fluke/fluke-terms'''
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
