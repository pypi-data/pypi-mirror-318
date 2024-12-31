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


class AkauntingIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "akaunting"

    @property
    def original_file_name(self) -> "str":
        return "akaunting.svg"

    @property
    def title(self) -> "str":
        return "Akaunting"

    @property
    def primary_color(self) -> "str":
        return "#6DA252"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Akaunting</title>
     <path d="M15.146 18.673a7.352 7.352 0 0 1-3.148.704 7.344 7.344 0
 0 1-4.538-1.561l-3.013 3.511A11.956 11.956 0 0 0 11.998 24c1.913 0
 3.721-.448 5.326-1.244l-2.178-4.083Zm4.229
 2.792V24h4.623V12c0-6.627-5.372-12-12-12C5.473 0 .165 5.208.002
 11.693h4.626a7.377 7.377 0 1 1 11.034 6.711l2.177 4.081a12 12 0 0 0
 1.536-1.02ZM7.016 17.44a7.352 7.352 0 0 1-2.389-5.165H.002a11.97
 11.97 0 0 0 4.002 8.675l3.012-3.51Z" />
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
