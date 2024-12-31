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


class WolframIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wolfram"

    @property
    def original_file_name(self) -> "str":
        return "wolfram.svg"

    @property
    def title(self) -> "str":
        return "Wolfram"

    @property
    def primary_color(self) -> "str":
        return "#DD1100"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wolfram</title>
     <path d="M20.105 12.001l3.307-3.708-4.854-1.059.495-4.944-4.55
 1.996L12 0 9.495 4.287 4.947 2.291l.494 4.944L.587 8.289l3.305
 3.707-3.305 3.713 4.854 1.053-.5 4.945 4.553-1.994L12 24l2.504-4.287
 4.55 1.994-.495-4.938 4.854-1.06-3.308-3.708zm1.605
 2.792l-2.861-.982-1.899-2.471 2.526.942 2.234
 2.511zm.459-6.096l-2.602 2.918-3.066-1.141 1.844-2.612
 3.824.835zm-4.288-1.324l-1.533 2.179.088-3.162 1.788-2.415-.343
 3.398zm-3.304-2.399l3.091-1.354L15.9 5.998l-2.943 1.049
 1.62-2.073zm1.187 1.772l-.096 3.652-3.341 1.12V7.969l3.437-1.223zM12
 1.308l1.969 3.371L12 7.199l-1.971-2.521L12 1.308zM9.423 4.974l1.619
 2.072-2.948-1.048L6.332 3.62l3.091 1.354zm2.245
 2.995v3.549l-3.335-1.12-.102-3.652 3.437 1.223zM7.564 6.39l.086
 3.162-1.532-2.179-.341-3.397L7.564 6.39zM1.83 8.692l3.824-.83 1.839
 2.612-3.065 1.136L1.83 8.692zm2.694 3.585l2.526-.937-1.9
 2.471-2.861.977 2.235-2.511zm-2.093 3.159l2.929-1
 3.045.896-2.622.837-3.352-.733zm3.28 5.212l.392-3.896 3.111-.982.082
 3.31-3.585 1.568zm3.691-5.708l-3.498-1.03 2.226-2.892 3.335
 1.126-2.063 2.796zm2.266 7.191l-1.711-2.934-.066-2.771 1.777
 2.597v3.108zm-1.73-6.8L12 12.532l2.063 2.799L12
 18.336l-2.062-3.005zm4.104 3.866l-1.715 2.934v-3.107l1.782-2.597-.067
 2.77zm-1.514-7.052l3.341-1.126 2.221 2.892-3.499
 1.03-2.063-2.796zm2.175 6.935l.077-3.31 3.116.982.386
 3.901-3.579-1.573zm3.514-2.912l-2.625-.837 3.049-.896 2.928
 1.003-3.352.73z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://company.wolfram.com/press-center/wolf'''

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
