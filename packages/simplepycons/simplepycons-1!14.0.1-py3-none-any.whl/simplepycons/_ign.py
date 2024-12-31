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


class IgnIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ign"

    @property
    def original_file_name(self) -> "str":
        return "ign.svg"

    @property
    def title(self) -> "str":
        return "IGN"

    @property
    def primary_color(self) -> "str":
        return "#BF1313"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>IGN</title>
     <path d="M5.38 7.66c.59-.9 1.359-1.67
 2.26-2.26.13-1.18.31-2.26.52-3.21a10.602 10.602 0 0 0-6 6c.95-.22
 2.03-.39 3.21-.52m10.97-2.3v.02c.9.59 1.67 1.37 2.27 2.27 1.18.13
 2.26.31 3.21.52a10.632 10.632 0 0 0-6.02-6.01c.22.95.4 2.02.54
 3.2m-8.7
 13.26c-.9-.59-1.67-1.37-2.27-2.27h-.03c-1.19-.14-2.26-.32-3.19-.54
 1.07 2.75 3.26 4.95 6.01
 6.02-.22-.95-.39-2.03-.52-3.21m11-2.27h-.03c-.59.9-1.37 1.67-2.27
 2.27v.03c-.14 1.17-.32 2.25-.54 3.19a10.593 10.593 0 0 0
 6.03-6.03c-.94.22-2 .4-3.19.54M10.04.01h3.9c.85 1.85 1.2 4.59 1.3
 5.52.04.22.06.43.06.63L12 9.12 8.7
 6.16c0-.17.02-.35.05-.55.1-.95.43-3.75 1.29-5.61M8.7 17.84c0
 .17.02.35.05.55.1.95.43 3.75 1.29 5.61h3.9c.85-1.84 1.2-4.59
 1.3-5.52.04-.22.06-.43.06-.64L12 14.88l-3.3 2.96ZM6.16 8.69c-.17
 0-.35.02-.55.05-.95.12-3.75.45-5.61 1.31v3.9c1.84.85 4.59 1.19 5.52
 1.3.22.04.43.06.64.06l2.95-3.3-2.95-3.3v-.02ZM24
 10.03c-1.86-.86-4.66-1.19-5.61-1.29-.2-.03-.38-.05-.55-.05l-2.96 3.3
 2.96 3.3c.2 0 .41-.02.64-.06.93-.11 3.68-.45 5.52-1.3v-3.9Z" />
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
