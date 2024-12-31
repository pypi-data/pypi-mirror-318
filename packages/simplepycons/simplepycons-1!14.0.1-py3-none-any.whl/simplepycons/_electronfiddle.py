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


class ElectronFiddleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "electronfiddle"

    @property
    def original_file_name(self) -> "str":
        return "electronfiddle.svg"

    @property
    def title(self) -> "str":
        return "Electron Fiddle"

    @property
    def primary_color(self) -> "str":
        return "#E79537"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Electron Fiddle</title>
     <path d="M8 0c-.6312 0-1.1429.5117-1.1429
 1.1429v13.8583c-1.9716.5075-3.4285 2.2973-3.4285 4.4274C3.4286
 21.9533 5.4753 24 8 24c2.5247 0 4.5714-2.0467 4.5714-4.5714
 0-2.1301-1.4569-3.92-3.4285-4.4274v-4.7155h4.7346c.541 0
 .9796-.5117.9796-1.1428
 0-.6312-.4386-1.1429-.9796-1.1429H9.143V2.2857h10.2857c.6312 0
 1.1428-.5117 1.1428-1.1428C20.5714.5117 20.0598 0 19.4286 0Zm0
 17.1429c1.2624 0 2.2857 1.0233 2.2857 2.2857 0 1.2623-1.0233
 2.2857-2.2857 2.2857-1.2624 0-2.2857-1.0234-2.2857-2.2857 0-1.2624
 1.0233-2.2857 2.2857-2.2857z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/electron/fiddle/blob/19360'''

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
