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


class SailsdotjsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sailsdotjs"

    @property
    def original_file_name(self) -> "str":
        return "sailsdotjs.svg"

    @property
    def title(self) -> "str":
        return "Sails.js"

    @property
    def primary_color(self) -> "str":
        return "#14ACC2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sails.js</title>
     <path d="M2.23828 24S-6.9375 9.39844 11.9375
 0v24H2.23828M14.85938 24V9.125s3.01171 4.91406 9.1328 14.875h-9.1328"
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
