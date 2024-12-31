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


class OpenzeppelinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "openzeppelin"

    @property
    def original_file_name(self) -> "str":
        return "openzeppelin.svg"

    @property
    def title(self) -> "str":
        return "OpenZeppelin"

    @property
    def primary_color(self) -> "str":
        return "#4E5EE4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OpenZeppelin</title>
     <path d="M22.783 24H9.317l2.196-3.69a5.23 5.23 0 0 1
 4.494-2.558h6.775ZM1.217 0h21.566l-3.718 6.247H1.217ZM9.76 9.763a5.73
 5.73 0 0 1 4.92-2.795h4.01L8.498 24h-7.26Z" />
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
