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


class RedsysIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "redsys"

    @property
    def original_file_name(self) -> "str":
        return "redsys.svg"

    @property
    def title(self) -> "str":
        return "Redsys"

    @property
    def primary_color(self) -> "str":
        return "#DC7C26"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Redsys</title>
     <path d="M11.626 24c-3.989-.108-7.476-2.03-9.89-5.873A10.9 10.9 0
 0 1 .17 13.959a12.4 12.4 0 0 1 .239-4.996c.44-1.711 1.275-3.197
 2.339-4.58.075-.099.169-.263.314-.174.098.061.023.207-.019.324-.473
 1.36-.46 2.756.225 3.984.783 1.411 1.964 2.438 3.67 2.705 1.636.258
 3.07-.211 4.21-1.317 1.378-1.34 1.95-2.99
 1.415-4.946-.285-1.036-.768-1.922-1.612-2.578-1.092-.848-2.33-1.26-3.722-1.12-.098.01-.225.08-.267-.056s.103-.14.187-.178A11.9
 11.9 0 0 1 12.071 0c1.74.01 3.427.384 5.006 1.125 2.152 1.008 3.91
 2.498 5.133 4.552a12.4 12.4 0 0 1 1.688 4.93c.154 1.313.08 2.584-.188
 3.863-.333 1.575-.942 3.028-1.875 4.34-.853 1.2-1.851 2.241-3.103
 3.052-.998.647-2.025 1.177-3.16 1.538-1.115.356-2.245.544-3.946.595z"
 />
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
