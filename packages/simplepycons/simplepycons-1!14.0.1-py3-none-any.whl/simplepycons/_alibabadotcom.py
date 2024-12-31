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


class AlibabadotcomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "alibabadotcom"

    @property
    def original_file_name(self) -> "str":
        return "alibabadotcom.svg"

    @property
    def title(self) -> "str":
        return "Alibaba.com"

    @property
    def primary_color(self) -> "str":
        return "#FF6A00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Alibaba.com</title>
     <path d="M14.391 16.22c-.963.044-.865-.459-.302-1.234 1.32-1.768
 3.82-4.236
 3.906-5.982.151-2.283-2.143-3.026-4.501-3.004-1.645.022-3.344.492-4.501.906C5
 8.315 2.489 10.576.909 13.076-.768 15.554-.216 17.923 3.322
 18c2.716-.109 4.48-.862 6.32-1.802.01 0-5.086
 1.453-6.958.383l-.008-.002c-.193-.11-.404-.264-.457-.683-.012-.885
 1.46-1.802 2.283-2.097v-1.533a5.374 5.374 0 0 0 1.955.366 5.378 5.378
 0 0 0
 3.472-1.265c.037.13.056.278.044.447h.371c.048-.394-.172-.706-.172-.706-.333-.529-.915-.52-.915-.52s.315.137.529.466a4.953
 4.953 0 0 1-4.665.932l1.21-1.2-.336-.874c2.435-.852 4.48-1.507
 7.812-2.085l-.746-.624.389-.24c2.01.568 3.325.985 3.253 2.051a2.672
 2.672 0 0 1-.202.611c-.584 1.158-2.326 3.09-3.029 3.898-.465.535-.92
 1.06-1.245 1.562-.335.503-.54.971-.551 1.42.043 3.504 10.334-1.64
 12.324-3.003-2.943 1.266-6.113 2.489-9.609 2.718Z" />
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
