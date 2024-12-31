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


class TurborepoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "turborepo"

    @property
    def original_file_name(self) -> "str":
        return "turborepo.svg"

    @property
    def title(self) -> "str":
        return "Turborepo"

    @property
    def primary_color(self) -> "str":
        return "#EF4444"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Turborepo</title>
     <path d="M6.155 12.058c0 .503.095.967.285
 1.392.19.424.447.793.771 1.106.324.313.699.56
 1.123.738.437.168.895.252 1.375.252.481 0 .934-.084 1.359-.252a3.578
 3.578 0 0 0 1.14-.738 3.37 3.37 0 0 0 1.073-2.498 3.371 3.371 0 0
 0-1.073-2.498 3.356 3.356 0 0 0-1.14-.721 3.463 3.463 0 0
 0-1.359-.269c-.48 0-.938.09-1.374.269-.425.167-.8.408-1.124.72a3.52
 3.52 0 0 0-.771 1.107 3.37 3.37 0 0 0-.285 1.392Zm-3.437
 0c0-.939.173-1.81.52-2.616a6.524 6.524 0 0 1 1.441-2.13 6.503 6.503 0
 0 1 2.197-1.408c.86-.346 1.805-.52 2.833-.52 1.018 0 1.957.174
 2.817.52a6.47 6.47 0 0 1 2.213 1.409 6.542 6.542 0 0 1 1.979 4.745c0
 .939-.173 1.816-.52 2.632a6.45 6.45 0 0 1-1.459 2.113 6.678 6.678 0 0
 1-2.213 1.425c-.86.335-1.8.503-2.817.503-1.028
 0-1.973-.168-2.833-.503a6.717 6.717 0 0 1-2.197-1.425 6.572 6.572 0 0
 1-1.442-2.113 6.663 6.663 0 0
 1-.52-2.632ZM10.144.008c-2.76-.096-5.52.76-7.805 2.569l1.523.857C5.67
 2.1 7.955 1.53 10.144 1.625V.007Zm8.09 3.616C16.331 1.625 13.856.388
 11.191.102V1.72a10.725 10.725 0 0 1 5.901 3.046l1.142-1.142Zm3.427
 7.805c-.095-2.475-1.047-4.95-2.665-7.043l-1.142 1.142c1.332 1.808
 2.094 3.807 2.189 5.9h1.618Zm-2.665 8.185c1.618-2.094 2.57-4.568
 2.665-7.043h-1.618c-.095 2.094-.857 4.093-2.19 5.901l1.143
 1.142Zm-7.805 4.284c2.57-.286 5.14-1.523
 7.043-3.522l-1.142-1.142c-1.618 1.713-3.712 2.76-5.901
 3.046v1.618Zm-8.852-2.475a11.867 11.867 0 0 0 7.805
 2.57v-1.618c-2.19.095-4.378-.476-6.282-1.809l-1.523.857Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/vercel/turborepo/blob/7312'''

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
