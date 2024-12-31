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


class BigbasketIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bigbasket"

    @property
    def original_file_name(self) -> "str":
        return "bigbasket.svg"

    @property
    def title(self) -> "str":
        return "bigbasket"

    @property
    def primary_color(self) -> "str":
        return "#A5CD39"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>bigbasket</title>
     <path d="M11.543 12.989a3.352 3.352 0 0 0-.871-1.375 2.251 2.251
 0 0 0-1.474-.503 2.276 2.276 0 0 0-1.541.536 2.953 2.953 0 0 0-.973
 1.375 5.609 5.609 0 0 0-.335 1.845 5.42 5.42 0 0 0 .335
 1.809c.192.548.528 1.034.973 1.407.441.339.985.516 1.541.503a2.08
 2.08 0 0 0 1.945-1.072h-.002a4.92 4.92 0 0 0 .67-2.649 6.477 6.477 0
 0 0-.268-1.876zM20.381.033H3.587A3.584 3.584 0 0 0 0 3.585V20.38a3.59
 3.59 0 0 0 3.587 3.586h16.794c1.986 0 3.601-1.6
 3.619-3.586V3.585A3.614 3.614 0 0 0 20.381.033zM10.64
 3.034h1.911v5.744a3.47 3.47 0 0 0-1.911-.584v-5.16zm-.438 17.93a5.586
 5.586 0 0 1-2.278-.369 3.522 3.522 0 0 1-1.174-.804 4.18 4.18 0 0
 1-.335-.536l-.033-.134v.302C6.281 21.266 3.4 20.931 3.4
 20.931V3.034h3.15v7.442h.034a3.675 3.675 0 0 1 1.541-1.309 4.825
 4.825 0 0 1 2.079-.435 4.197 4.197 0 0 1 2.649.871 5.263 5.263 0 0 1
 1.675 2.278v-.001c.372.951.565 1.963.569 2.984a8.418 8.418 0 0 1-.571
 2.984 5.47 5.47 0 0 1-1.675 2.278 4.161 4.161 0 0
 1-2.649.838zm9.828-3.111a5.47 5.47 0 0 1-1.675 2.278 4.173 4.173 0 0
 1-2.649.838 5.587 5.587 0 0 1-2.278-.37 4.85 4.85 0 0
 1-.362-.186c.444-.36.837-.778 1.168-1.245.353.127.726.189 1.101.185
 2.38 0 3.15-2.502 3.15-4.484 0-1.96-.721-4.523-3.15-4.523a3.058 3.058
 0 0 0-1.021.163 6.349 6.349 0 0
 0-1.017-1.166c.107-.063.218-.121.331-.176a4.72 4.72 0 0 1 6.403
 2.715l-.001.004c.373.951.566 1.963.571 2.984a8.409 8.409 0 0 1-.571
 2.983z" />
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
