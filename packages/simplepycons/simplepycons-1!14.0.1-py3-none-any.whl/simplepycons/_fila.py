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


class FilaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fila"

    @property
    def original_file_name(self) -> "str":
        return "fila.svg"

    @property
    def title(self) -> "str":
        return "Fila"

    @property
    def primary_color(self) -> "str":
        return "#002D62"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fila</title>
     <path d="M8.814 8.027c-.614 0-1.113.498-1.113 1.113v5.72a1.113
 1.113 0 0 0 2.226
 0V9.14c0-.614-.498-1.113-1.113-1.113m-2.849.078H1.113a1.113 1.113 0 0
 0 0 2.226h4.852a1.113 1.113 0 0 0 0-2.226m17.411 4.417L21.03
 8.705c-.275-.444-.65-.658-1.125-.658-.488 0-.904.229-1.162.658l-2.715
 4.5c-.186.308-.4.436-.753.436h-2.019a.275.275 0 0
 1-.285-.284V9.102c0-.613-.497-1.075-1.11-1.075-.614 0-1.11.463-1.11
 1.076v5.215c0 .784.774 1.544 1.544 1.544h4.064c.576 0 .963-.42
 1.292-.996l2.114-3.627c.018-.04.053-.091.093-.091.043 0
 .07.051.091.088l1.384
 2.22c.058.094.069.141.032.225-.033.077-.108.093-.23.093h-1.943a1.044
 1.044 0 1 0 0 2.088h3.17c.77 0 1.638-.734 1.638-1.693
 0-.608-.117-.822-.624-1.647M5.431 10.954H1.113c-.615
 0-1.113.498-1.113 1.113v2.715a1.113 1.113 0 1 0 2.226
 0v-1.268c0-.185.15-.334.334-.334h2.87a1.113 1.113 0 0 0 0-2.226" />
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
