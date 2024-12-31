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


class AlliedmoddersIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "alliedmodders"

    @property
    def original_file_name(self) -> "str":
        return "alliedmodders.svg"

    @property
    def title(self) -> "str":
        return "AlliedModders"

    @property
    def primary_color(self) -> "str":
        return "#1578D3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AlliedModders</title>
     <path d="M.588 1.077A.615.615 0 0 0 0 1.69v20.617c0
 .34.275.615.615.615h8.309c.34 0 .615-.275.615-.615v-1.746l.647
 1.94a.615.615 0 0 0 .584.421h6.77a.615.615 0 0 0
 .585-.427l.035-.11c.04.307.3.537.61.537h4.615c.34 0
 .615-.275.615-.615V8.153a.615.615 0 0
 0-.447-.592l-4.307-1.23a.615.615 0 0 0-.744.37l-1.887
 4.907v-5.55a.615.615 0 0 0-.443-.593l-3.385-.98a.615.615 0 0
 0-.787.59v6.15l-2.809-7.48a.615.615 0 0 0-.408-.375l-8-2.272a.615.615
 0 0 0-.195-.021zm.027.613l8 2.272 4 10.652v-9.54L16
 6.058v8.865l3.076-8 4.309
 1.231v14.154H18.77v-2.463h1.845v-7.076l-3.076 9.54h-6.77L6.155
 8.46v11.078h2.77v2.77H.615zm.615.816V21.69h7.08v-1.537H6.154a.615.615
 0 0 1-.615-.615V8.46c.002-.698.979-.855 1.2-.194l4.474
 13.424h5.877l2.94-9.111c.215-.668 1.201-.513 1.2.19v7.075c0
 .34-.275.615-.615.616h-1.23v1.23h3.385V8.616l-3.32-.947-2.876
 7.474c-.245.635-1.188.46-1.19-.22V6.52l-2.154-.625v8.719c0
 .685-.95.857-1.19.217L8.147 4.467zm5.54 9.747l2.224
 6.67c-.734-.01-1.485 0-2.224 0zM20 16.683v2.546h-.822Z" />
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
