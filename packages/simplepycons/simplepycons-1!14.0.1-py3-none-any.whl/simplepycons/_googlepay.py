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


class GooglePayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlepay"

    @property
    def original_file_name(self) -> "str":
        return "googlepay.svg"

    @property
    def title(self) -> "str":
        return "Google Pay"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Pay</title>
     <path d="M3.963 7.235A3.963 3.963 0 00.422 9.419a3.963 3.963 0
 000 3.559 3.963 3.963 0 003.541 2.184c1.07 0 1.97-.352
 2.627-.957.748-.69 1.18-1.71 1.18-2.916a4.722 4.722 0
 00-.07-.806H3.964v1.526h2.14a1.835 1.835 0 01-.79
 1.205c-.356.241-.814.379-1.35.379-1.034
 0-1.911-.697-2.225-1.636a2.375 2.375 0 010-1.517c.314-.94 1.191-1.636
 2.225-1.636a2.152 2.152 0 011.52.594l1.132-1.13a3.808 3.808 0
 00-2.652-1.033zm6.501.55v6.9h.886V11.89h1.465c.603 0 1.11-.196
 1.522-.588a1.911 1.911 0 00.635-1.464 1.92 1.92 0 00-.635-1.456 2.125
 2.125 0 00-1.522-.598zm2.427.85a1.156 1.156 0 01.823.365 1.176 1.176
 0 010 1.686 1.171 1.171 0 01-.877.357H11.35V8.635h1.487a1.156 1.156 0
 01.054 0zm4.124 1.175c-.842
 0-1.477.308-1.907.925l.781.491c.288-.417.68-.626 1.175-.626a1.255
 1.255 0 01.856.323 1.009 1.009 0
 01.366.785v.202c-.34-.193-.774-.289-1.3-.289-.617
 0-1.11.145-1.479.434-.37.288-.554.677-.554 1.165a1.476 1.476 0 00.525
 1.156c.35.308.785.463 1.305.463.61 0 1.098-.27
 1.465-.81h.038v.655h.848v-2.909c0-.61-.19-1.09-.568-1.44-.38-.35-.896-.525-1.551-.525zm2.263.154l1.946
 4.422-1.098 2.38h.915L24 9.963h-.965l-1.368
 3.391h-.02l-1.406-3.39zm-2.146 2.368c.494 0 .88.11 1.156.33 0
 .372-.147.696-.44.973a1.413 1.413 0 01-.997.414 1.081 1.081 0
 01-.69-.232.708.708 0
 01-.293-.578c0-.257.12-.47.363-.647.24-.173.54-.26.9-.26Z" />
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
