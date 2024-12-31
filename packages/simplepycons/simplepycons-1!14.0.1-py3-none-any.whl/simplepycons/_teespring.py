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


class TeespringIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "teespring"

    @property
    def original_file_name(self) -> "str":
        return "teespring.svg"

    @property
    def title(self) -> "str":
        return "Teespring"

    @property
    def primary_color(self) -> "str":
        return "#ED2761"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Teespring</title>
     <path d="M15.78 8.348c-.77 0-1.396.615-1.396 1.37 0 1.075.406
 2.058 1.075 2.813.277.312.598.584.956.807a5 5 0 0 0
 .736-3.874c-.005-.029-.013-.058-.02-.087a1.392 1.392 0 0
 0-1.35-1.029zm-8.612 3.958c.138.366.317.712.533
 1.032.356-.223.678-.495.955-.807a4.221 4.221 0 0 0
 1.076-2.813c0-.755-.626-1.37-1.397-1.37-.65 0-1.195.438-1.35
 1.029-.006.029-.015.057-.02.086a5.002 5.002 0 0 0 .205
 2.843zm15.501-.67L24 12.29a5.873 5.873 0 0 1-5.243 3.18 5.958 5.958 0
 0 1-1.926-.32 6.745 6.745 0 0 1-4.774 1.963 6.742 6.742 0 0
 1-4.774-1.964 5.943 5.943 0 0 1-1.926.32A5.87 5.87 0 0 1 0
 12.054l1.362-.595a4.38 4.38 0 0 0 3.995 2.549c.324 0
 .641-.036.946-.102a6.45 6.45 0 0 1-.945-3.367 6.512 6.512 0 0 1
 .19-1.554c.328-1.208 1.45-2.098
 2.786-2.098l.079.002c.08.002.162.008.242.016 1.444.157 2.565 1.357
 2.565 2.814 0 1.958-.999 3.687-2.522 4.724a5.244 5.244 0 0 0 3.36
 1.21 5.247 5.247 0 0 0
 3.358-1.21c-1.523-1.037-2.522-2.767-2.522-4.724 0-1.458 1.122-2.658
 2.564-2.814.08-.008.16-.014.242-.016l.08-.002a2.877 2.877 0 0 1 2.832
 2.286 6.478 6.478 0 0 1-.8 4.733c.305.066.62.102.945.102 1.71 0
 3.191-.967 3.91-2.372z" />
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
