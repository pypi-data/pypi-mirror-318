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


class MtaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mta"

    @property
    def original_file_name(self) -> "str":
        return "mta.svg"

    @property
    def title(self) -> "str":
        return "MTA"

    @property
    def primary_color(self) -> "str":
        return "#0039A6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MTA</title>
     <path d="M15.171
 10.07l-1.293-.109v6.861l-1.926.34-.004-7.371-1.637-.145V6.944l4.86.85zm3.668
 5.884l-1.142.198-.134-1-1.113.145-.14 1.1-1.473.26 1.458-8.651
 1.385.24zm-1.48-2.492l-.305-2.642h-.068l-.31 2.682zM10.991 24c6.59 0
 11.932-5.373 11.932-12 0-6.628-5.342-12-11.932-12C6.86 0 3.22 2.112
 1.077 5.323l3.307.583.91 6.965c.003-.012.066-.004.066-.004l.998-6.615
 3.309.58v10.735l-2.089.367V13.32s.078-1.987.032-2.327c0
 0-.09.002-.092-.005l-1.246 7.18-2.075.366L2.672
 10.8l-.092-.007c-.032.28.112 2.707.112 2.707v5.298l-1.364.24C3.498
 22.044 7.016 24 10.991 24z" />
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
