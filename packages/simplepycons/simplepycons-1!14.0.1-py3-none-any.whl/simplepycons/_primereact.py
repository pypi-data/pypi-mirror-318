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


class PrimereactIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "primereact"

    @property
    def original_file_name(self) -> "str":
        return "primereact.svg"

    @property
    def title(self) -> "str":
        return "PrimeReact"

    @property
    def primary_color(self) -> "str":
        return "#03C4E8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PrimeReact</title>
     <path d="M12.01 0c-1.212 0-2.297.62-2.903 1.66l-1.52
 2.608H4.303A3.287 3.287 0 0 0 1.43 5.911a3.226 3.226 0 0 0 0
 3.285l1.642 2.819-1.646 2.825a3.202 3.202 0 0 0 0 3.261 3.265 3.265 0
 0 0 2.851 1.631h2.925l.865.856L9.09 22.34A3.322 3.322 0 0 0 11.991
 24c1.211 0 2.296-.62 2.902-1.66l.816-1.4 1.22-1.208h2.77a3.287 3.287
 0 0 0 2.87-1.643c.6-1.028.6-2.256 0-3.285l-1.642-2.82
 1.646-2.824a3.202 3.202 0 0 0 0-3.261 3.265 3.265 0 0
 0-2.851-1.631H16.43L14.91 1.66A3.322 3.322 0 0 0 12.01 0Zm0 .719c.948
 0 1.798.486 2.273 1.3l1.31 2.249H8.425l1.31-2.248A2.603 2.603 0 0 1
 12.01.719Zm.33 4.265v7.74h.962l5.904-2.174.014-.057.87 1.492-1.33
 2.282.171-3.173-1.51.543-1.51 1.494-1.237-.27.962
 1.357v4.212l1.452-1.296-.708
 1.216v.001l-.744.622v.654l-.412.708V14.49l-1.098-1.63-.687.407h-2.746l-.687-.407-1.098
 1.63v6.101l-.412-.706v-.912l-1.036-.867-.729-1.25 1.765
 1.574v-4.212l.961-1.358-1.236.271-1.51-1.494-1.511-.543.188
 3.455-1.477-2.534.942-1.617.122-.208.088.36 5.904
 2.174h.824V4.985Zm1.512 0h.412l.96 2.17
 1.935-.2.237.406-2.452.192zm-3.985.001h.412L9.187
 7.552l-2.556-.205.072-.124.001.001.163-.28
 2.04.21Zm-5.565.001h2.867L5.831 7.282l-1.592-.127.49 2.018-1.237
 2.124-1.433-2.46a2.52 2.52 0 0 1 0-2.567 2.568 2.568 0 0 1
 2.243-1.284Zm12.547 0h2.873c.928 0 1.759.476 2.223 1.272a2.497 2.497
 0 0 1 0 2.543l-1.437 2.466-1.042-1.789.563-2.323-1.833.143Zm3.659
 7.718 1.433 2.46a2.52 2.52 0 0 1 0 2.566 2.567 2.567 0 0 1-2.243
 1.283h-2.277V18zm-17.016.03 3.22 5.525v.754H4.277a2.545 2.545 0 0
 1-2.223-1.27 2.497 2.497 0 0 1 0-2.544z" />
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
