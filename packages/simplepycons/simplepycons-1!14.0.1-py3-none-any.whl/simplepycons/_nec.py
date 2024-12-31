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


class NecIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nec"

    @property
    def original_file_name(self) -> "str":
        return "nec.svg"

    @property
    def title(self) -> "str":
        return "NEC"

    @property
    def primary_color(self) -> "str":
        return "#1414A0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NEC</title>
     <path d="M21.496 8.8a13.892 13.892 0 0
 0-2.453.198c-.6.11-1.165.223-1.693.57-.807.526-1.076 1.49-1.086
 2.394-.012.98.283 2.06 1.21 2.54.735.384 1.537.552 2.355.624
 1.397.118 2.792.1
 4.171-.09v-.98c-1.04.19-2.107.31-3.184.152-1.652-.24-1.93-1.473-1.93-2.286
 0-.451.06-.987.482-1.526.676-.865 2.667-.956 4.55-.59V8.95a22.777
 22.777 0 0 0-2.422-.15zm-12.812.197v4.446c.03.744.295 1.518 1.834
 1.581 1.814.075 3.54.045 5.334-.024v-.896c-.89.014-3.487.001-3.65
 0-.704-.042-.973-.256-.998-.837a32.12 32.12 0 0
 1-.02-1.055h4.177v-.834h-4.176V9.851h4.582v-.854zM0
 8.997v5.999h1.146v-4.254l3.383 3.764c.41.404.763.478
 1.122.49h2.015V8.997h-1.15v4.397l-3.39-3.757c-.232-.227-.753-.64-1.194-.64z"
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
        return '''https://commons.wikimedia.org/wiki/File:NEC_l'''

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
