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


class BitcoinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bitcoin"

    @property
    def original_file_name(self) -> "str":
        return "bitcoin.svg"

    @property
    def title(self) -> "str":
        return "Bitcoin"

    @property
    def primary_color(self) -> "str":
        return "#F7931A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bitcoin</title>
     <path d="M23.638 14.904c-1.602 6.43-8.113 10.34-14.542 8.736C2.67
 22.05-1.244 15.525.362 9.105 1.962 2.67 8.475-1.243 14.9.358c6.43
 1.605 10.342 8.115 8.738
 14.548v-.002zm-6.35-4.613c.24-1.59-.974-2.45-2.64-3.03l.54-2.153-1.315-.33-.525
 2.107c-.345-.087-.705-.167-1.064-.25l.526-2.127-1.32-.33-.54
 2.165c-.285-.067-.565-.132-.84-.2l-1.815-.45-.35
 1.407s.975.225.955.236c.535.136.63.486.615.766l-1.477
 5.92c-.075.166-.24.406-.614.314.015.02-.96-.24-.96-.24l-.66 1.51
 1.71.426.93.242-.54 2.19 1.32.327.54-2.17c.36.1.705.19 1.05.273l-.51
 2.154 1.32.33.545-2.19c2.24.427 3.93.257
 4.64-1.774.57-1.637-.03-2.58-1.217-3.196.854-.193 1.5-.76
 1.68-1.93h.01zm-3.01 4.22c-.404 1.64-3.157.75-4.05.53l.72-2.9c.896.23
 3.757.67 3.33 2.37zm.41-4.24c-.37
 1.49-2.662.735-3.405.55l.654-2.64c.744.18 3.137.524 2.75 2.084v.006z"
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
