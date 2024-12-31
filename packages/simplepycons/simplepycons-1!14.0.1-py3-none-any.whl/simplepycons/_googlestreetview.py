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


class GoogleStreetViewIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlestreetview"

    @property
    def original_file_name(self) -> "str":
        return "googlestreetview.svg"

    @property
    def title(self) -> "str":
        return "Google Street View"

    @property
    def primary_color(self) -> "str":
        return "#FEC111"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Street View</title>
     <path d="M12.571 5.714a5.714 5.714 0 1 1 11.43 0 5.714 5.714 0 0
 1-11.43 0zm2.264 5.165l-3.502 3.502c2.015-1.488 4.48-2.31 6.953-2.31
 1.155 0 2.307.182 3.428.53v-1.709a6.176 6.176 0 0 1-3.428 1.037 6.177
 6.177 0 0 1-3.45-1.05zm6.88 11.407V13.12a11.074 11.074 0 0 0-3.43-.55
 11.25 11.25 0 0 0-6.731 2.265c-.425.34-.697.863-.697 1.45V24H20a1.72
 1.72 0 0 0 1.714-1.714zM13.12 9.165L.001 22.285V4a1.72 1.72 0 0 1
 1.713-1.714h11.394a6.176 6.176 0 0 0-1.037 3.428c0 1.276.388 2.463
 1.05 3.45zm-5.246-1.95a2.7 2.7 0 0
 0-.077-.644h-2.94v1.142h1.69c.001.303-.228.755-.625
 1.025-.258.176-.606.298-1.066.298-.818 0-1.512-.552-1.76-1.295a1.887
 1.887 0 0 1 0-1.196c.248-.743.942-1.295 1.76-1.295.6 0 .987.268
 1.19.458l.913-.889A3.018 3.018 0 0 0 4.857 4a3.143 3.143 0 1 0 0
 6.287c.848 0 1.563-.279
 2.083-.759.593-.547.935-1.356.935-2.313zm2.482
 9.07c0-.511.17-.995.471-1.399L1.714 24h8.643v-7.714z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://developers.google.com/streetview/read'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://developers.google.com/streetview/read'''

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
