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


class EbayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ebay"

    @property
    def original_file_name(self) -> "str":
        return "ebay.svg"

    @property
    def title(self) -> "str":
        return "eBay"

    @property
    def primary_color(self) -> "str":
        return "#E53238"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>eBay</title>
     <path d="M6.056 12.132v-4.92h1.2v3.026c.59-.703 1.402-.906
 2.202-.906 1.34 0 2.828.904 2.828 2.855 0
 .233-.015.457-.06.668.24-.953 1.274-1.305 2.896-1.344.51-.018
 1.095-.018 1.56-.018v-.135c0-.885-.556-1.244-1.53-1.244-.72
 0-1.245.3-1.305.81h-1.275c.136-1.29 1.5-1.62 2.686-1.62 1.064 0
 1.995.27 2.415 1.02l-.436-.84h1.41l2.055 4.125 2.055-4.126H24l-3.72
 7.305h-1.346l1.07-2.04-2.33-4.38c.13.255.2.555.2.93v2.46c0
 .346.01.69.04 1.005H16.8a6.543 6.543 0
 01-.046-.765c-.603.734-1.32.96-2.32.96-1.48 0-2.272-.78-2.272-1.695
 0-.15.015-.284.037-.405-.3 1.246-1.36 2.086-2.767 2.086-.87
 0-1.694-.315-2.2-.93 0
 .24-.015.494-.04.734h-1.18c.02-.39.04-.855.04-1.245v-1.05h-4.83c.065
 1.095.818 1.74 1.853 1.74.718 0 1.355-.3 1.568-.93h1.24c-.24
 1.29-1.61 1.725-2.79 1.725C.95 15.009 0 13.822 0
 12.232c0-1.754.982-2.91 3.116-2.91 1.688 0 2.93.886 2.94
 2.806v.005zm9.137.183c-1.095.034-1.77.233-1.77.95 0 .465.36.97
 1.305.97 1.26 0 1.935-.69 1.935-1.814v-.13c-.45
 0-.99.006-1.484.022h.012zm-6.06 1.875c1.11 0 1.876-.806
 1.876-2.02s-.768-2.02-1.893-2.02c-1.11 0-1.89.806-1.89 2.02s.765 2.02
 1.875 2.02h.03zm-4.35-2.514c-.044-1.125-.854-1.546-1.725-1.546-.944
 0-1.694.474-1.815 1.546z" />
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
