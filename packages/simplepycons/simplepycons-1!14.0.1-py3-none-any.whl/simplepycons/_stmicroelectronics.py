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


class StmicroelectronicsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "stmicroelectronics"

    @property
    def original_file_name(self) -> "str":
        return "stmicroelectronics.svg"

    @property
    def title(self) -> "str":
        return "STMicroelectronics"

    @property
    def primary_color(self) -> "str":
        return "#03234B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>STMicroelectronics</title>
     <path d="M 23.818 5.61 L 6.402 5.61 C 5.125 5.609 3.968 6.362
 3.452 7.529 L 0.014 15.811 C -0.036 15.931 0.052 16.063 0.182 16.061
 L 8.046 16.061 C 8.601 16.061 8.848 15.523 8.412 15.093 L 5.524
 12.388 C 4.008 10.9 4.658 7.45 7.81 7.45 L 23.206 7.45 C 23.283 7.451
 23.352 7.402 23.378 7.329 L 23.987 5.857 C 23.996 5.835 24.001 5.811
 24 5.787 C 23.997 5.689 23.917 5.61 23.818 5.61 M 22.082 9.826 L
 19.126 9.826 C 18.932 9.825 18.756 9.94 18.681 10.118 L 15.369 18.118
 C 15.355 18.144 15.347 18.173 15.347 18.202 C 15.348 18.302 15.429
 18.383 15.529 18.381 L 16.632 18.381 C 17.93 18.387 19.105 17.613
 19.612 16.418 L 22.244 10.063 C 22.252 10.042 22.257 10.019 22.257
 9.996 C 22.253 9.902 22.176 9.828 22.082 9.826 M 16.271 10.005 C
 16.271 9.905 16.189 9.825 16.089 9.825 L 7.706 9.825 C 7.251 9.825
 6.853 10.38 7.335 10.825 L 10.104 13.404 C 10.104 13.404 11.224
 14.437 10.984 15.916 C 10.778 17.219 9.889 18.016 9.241 18.302 C
 9.208 18.31 9.196 18.351 9.219 18.376 C 9.23 18.387 9.246 18.392
 9.261 18.388 L 12.489 18.388 C 12.683 18.39 12.859 18.275 12.934
 18.095 L 16.256 10.068 C 16.266 10.049 16.271 10.027 16.271 10.005"
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
