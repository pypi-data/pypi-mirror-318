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


class GoogleTasksIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googletasks"

    @property
    def original_file_name(self) -> "str":
        return "googletasks.svg"

    @property
    def title(self) -> "str":
        return "Google Tasks"

    @property
    def primary_color(self) -> "str":
        return "#2684FC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Tasks</title>
     <path d="M11.383.617C5.097.617 0 5.714 0 12c0 6.286 5.097 11.383
 11.383 11.383 6.286 0 11.38-5.097 11.38-11.383a11.34 11.34 0 0
 0-.878-4.389l-3.203 3.203c.062.387.1.782.1 1.186a7.398 7.398 0 1
 1-7.4-7.398c1.499 0 2.889.448 4.054 1.214l2.857-2.857a11.325 11.325 0
 0 0-6.91-2.342zm9.674.756c-.292 0-.583.112-.805.334-2.97 2.965-5.934
 5.934-8.9 8.902L9.596 8.854a1.139 1.139 0 0 0-1.61 0l-1.775
 1.773a1.139 1.139 0 0 0 0 1.61l4.166 4.163a1.421 1.421 0 0 0 2.012
 0L23.666 5.121a1.136 1.136 0 0 0 0-1.61l-1.805-1.804a1.136 1.136 0 0
 0-.804-.334z" />
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
