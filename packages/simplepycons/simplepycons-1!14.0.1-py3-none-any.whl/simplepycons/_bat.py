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


class BatIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bat"

    @property
    def original_file_name(self) -> "str":
        return "bat.svg"

    @property
    def title(self) -> "str":
        return "bat"

    @property
    def primary_color(self) -> "str":
        return "#31369E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>bat</title>
     <path d="M8.3258 5.8712a.165.165 0 0 0-.0828.0227L.1628
 10.6287a.3292.3292 0 0 0 0 .5682c.7296.4273 1.5858.9285 2.9645
 1.736l.0003-.0002c.1766.1035.3639.2134.6667.3907.3059.1792
 1.5546.9292 1.8978 1.1352a.172.172 0 0 0
 .1758.0011l3.2446-1.892a.145.145 0 0 0 .072-.126.146.146 0 0
 0-.0725-.1259c-.4119-.2378-1.2937-.7475-1.625-.9419l-.7927-.4647c.4232-.2457
 1.222-.7063 1.5211-.8811a.558.558 0 0 0 .2767-.4819V6.0368a.1657.1657
 0 0 0-.1663-.1656m7.3487 0a.1653.1653 0 0
 0-.1664.1656v3.5094a.558.558 0 0 0 .2765.4819c.2955.1725 1.2455.7276
 1.5145.8847l-3.1644 1.8562a.246.246 0 0 1-.3706-.212V8.2744a.19.19 0
 0 0-.0917-.1626.19.19 0 0
 0-.1863-.0063c-.1207.0626-1.0953.5325-1.5392.7464-.6352-.292-1.2494-.5767-1.4327-.672-.059-.0306-.126-.0214-.1865.0063-.0496.0228-.0915.0962-.0915.1627v4.208c0
 .0883.0109.3806-.304.5623L6.638 15.0234l5.3628 3.1054s9.5549-5.5958
 11.8364-6.9318a.3295.3295 0 0 0
 0-.5682l-2.8146-1.6493.0003-.0002-.2142-.1252-.002-.0014-5.0493-2.9587a.165.165
 0 0 0-.0827-.0227z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/sharkdp/bat/blob/018a48262'''

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
