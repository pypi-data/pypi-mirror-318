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


class CoinmarketcapIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "coinmarketcap"

    @property
    def original_file_name(self) -> "str":
        return "coinmarketcap.svg"

    @property
    def title(self) -> "str":
        return "CoinMarketCap"

    @property
    def primary_color(self) -> "str":
        return "#17181B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CoinMarketCap</title>
     <path d="M20.738
 14.341c-.419.265-.912.298-1.286.087-.476-.27-.738-.898-.738-1.774v-2.618c0-1.264-.5-2.164-1.336-2.407-1.416-.413-2.482
 1.32-2.882 1.972l-2.498
 4.05v-4.95c-.028-1.14-.398-1.821-1.1-2.027-.466-.135-1.161-.081-1.837.953l-5.597
 8.987A9.875 9.875 0 0 1 2.326 12c0-5.414 4.339-9.818 9.672-9.818
 5.332 0 9.67 4.404 9.67 9.818.004.018.002.034.003.053.05 1.049-.29
 1.883-.933 2.29zm3.08-2.34-.001-.055C23.787 5.353 18.497 0 11.997 0
 5.48 0 .177 5.383.177 12c0 6.616 5.303 12 11.82 12 2.991 0
 5.846-1.137 8.037-3.2.435-.41.46-1.1.057-1.541a1.064 1.064 0 0
 0-1.519-.059 9.56 9.56 0 0 1-6.574 2.618c-2.856
 0-5.425-1.263-7.197-3.268l5.048-8.105v3.737c0 1.794.696 2.374 1.28
 2.544.584.17 1.476.054 2.413-1.468.998-1.614 2.025-3.297
 3.023-4.88v2.276c0 1.678.672 3.02 1.843 3.68 1.056.597 2.384.543
 3.465-.14 1.312-.828 2.018-2.354 1.944-4.193z" />
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
