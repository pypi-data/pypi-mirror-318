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


class PipedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "piped"

    @property
    def original_file_name(self) -> "str":
        return "piped.svg"

    @property
    def title(self) -> "str":
        return "Piped"

    @property
    def primary_color(self) -> "str":
        return "#F84330"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Piped</title>
     <path d="M9.947 22.915c0 .6-1.207 1.085-2.7 1.085-1.492
 0-2.698-.485-2.698-1.085s1.206-1.086 2.699-1.086c1.492 0 2.699.485
 2.699 1.086zm-.018-.906V.789S9.593.58 9.06.33A7.333 7.333 0 0 0
 8.1.07 8.257 8.257 0 0 0 6.986 0a8.07 8.07 0 0 0-1.043.144 6.31 6.31
 0 0 0-.786.272A5.819 5.819 0 0 0 4.56.79v21.223c.609-.462 1.668-.684
 2.687-.684 1.015 0 2.072.22 2.68.68zm1.906-17.195c.66 0 1.192-1
 1.192-2.237S12.494.34 11.835.34c-.66 0-1.192 1-1.192 2.237s.533 2.237
 1.192 2.237zm.045 4.488c-.66 0-1.192 1.102-1.192 2.464 0 1.363.533
 2.465 1.192 2.465.66 0 1.192-1.102 1.192-2.465
 0-1.362-.532-2.464-1.192-2.464zm7.556-2.16a12.19 12.19 0 0
 0-.142-1.026 12.28 12.28 0 0 0-.27-.994 12.027 12.027 0 0
 0-.388-.939c-.151-.293-.315-.58-.492-.859a10.837 10.837 0 0
 0-.578-.76 10.181 10.181 0 0 0-.647-.65 9.626 9.626 0 0 0-1.412-.941
 9.61 9.61 0 0 0-1.412-.492 10.987 10.987 0 0 0-.65-.102 6.299 6.299 0
 0 0-.626-.053c.433.486.708 1.294.708 2.25 0 1-.3 1.836-.767
 2.313.224.041.575.163.708.212.215.096.432.211.641.344.356.258.543.471.73.77.263.474.31.856.247
 1.287-.135.651-.495 1.035-.937 1.33a4.3 4.3 0 0
 1-.623.297c-.087.026-.438.13-.694.158.453.521.74 1.418.74 2.48 0
 1.042-.278 1.923-.716 2.448.114-.002.22-.003.35-.007.414-.037.9-.107
 1.395-.207.314-.085.862-.25 1.531-.55a8.856 8.856 0 0 0
 1.422-.996c.213-.214.415-.438.605-.673a8.95 8.95 0 0 0
 .504-.782c.145-.285.275-.577.39-.876.102-.308.19-.626.262-.951.058-.33.1-.664.129-1.003.02-.343-.001-.686-.008-1.028z"
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
        return '''https://github.com/TeamPiped/Piped/blob/71a37'''

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
