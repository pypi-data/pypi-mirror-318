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


class IcomoonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "icomoon"

    @property
    def original_file_name(self) -> "str":
        return "icomoon.svg"

    @property
    def title(self) -> "str":
        return "IcoMoon"

    @property
    def primary_color(self) -> "str":
        return "#825794"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>IcoMoon</title>
     <path d="M12 0C10.34 0 8.79 .313 7.34 .938A12 12 0 0 0 3.5 3.5A12
 12 0 0 0 .937 7.34C.313 8.79 0 10.34 0 12C0 13.66 .313 15.21 .938
 16.66A12 12 0 0 0 3.5 20.5A12 12 0 0 0 7.34 23.06C8.79 23.69 10.34 24
 12 24C13.66 24 15.21 23.69 16.66 23.06A12 12 0 0 0 20.5 20.5A12 12 0
 0 0 23.06 16.66C23.69 15.21 24 13.66 24 12C24 10.34 23.69 8.79 23.06
 7.34A12 12 0 0 0 20.5 3.5A12 12 0 0 0 16.66 .937C15.21 .313 13.66 0
 12 0M8.88 1.5A11.65 11.65 0 0 1 11.37 3.42A12.31 12.31 0 0 1 13.27
 5.87C13.8 6.77 14.2 7.73 14.5 8.77C14.78 9.8 14.93 10.88 14.93
 12S14.78 14.2 14.5 15.23A11.71 11.71 0 0 1 13.27 18.13A12.31 12.31 0
 0 1 11.37 20.58C10.62 21.33 9.79 21.96 8.88 22.5A11.91 11.91 0 0 1
 6.42 20.58A12.31 12.31 0 0 1 4.5 18.13A11.71 11.71 0 0 1 3.31
 15.23A11.63 11.63 0 0 1 2.86 12C2.86 10.88 3 9.8 3.31 8.77A11.71
 11.71 0 0 1 4.5 5.87A12.31 12.31 0 0 1 6.42 3.42C7.17 2.67 8 2.04
 8.88 1.5M8.86 9.23C8.09 9.23 7.44 9.5 6.9 10.04A2.67 2.67 0 0 0 6.09
 12C6.09 12.77 6.36 13.42 6.9 13.96C7.44 14.5 8.09 14.77 8.86
 14.77C9.63 14.77 10.28 14.5 10.82 13.96C11.36 13.42 11.63 12.77 11.63
 12S11.36 10.58 10.82 10.04A2.67 2.67 0 0 0 8.86 9.23Z" />
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
