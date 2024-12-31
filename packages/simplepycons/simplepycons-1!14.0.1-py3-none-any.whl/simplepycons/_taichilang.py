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


class TaichiLangIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "taichilang"

    @property
    def original_file_name(self) -> "str":
        return "taichilang.svg"

    @property
    def title(self) -> "str":
        return "Taichi Lang"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Taichi Lang</title>
     <path d="M15.526 4.6782c-.0196 1.6052-.8167 2.8963-2.211
 3.8542-1.2176.8371-2.47 1.627-3.6316 2.5398-1.8976 1.4954-3.1392
 3.4337-3.1784 5.9263-.0415 2.7115 1.1753 4.7975 3.4344
 6.274.0415.0276.0888.0502.1302.0756.2.123.3637.3055.2197.5237-.0698.1033-.3273.1542-.4728.115-1.2168-.2975-2.3856-.731-3.4556-1.395-3.462-2.1486-5.484-5.2623-5.9517-9.318C-.2542
 7.4683 3.1934 2.0903 8.6833.3542c1.3558-.4313 2.7224-.5266
 4.0731.0422 1.7223.72 2.8257 2.3806 2.7697 4.2818Zm8.1462
 9.2648c-.0276 1.0699-.328 2.2693-1.4445
 3.1115-1.3004.9805-2.9755.9165-3.9981-.1483a2.8359 2.8359 0 0
 1-.6444-1.0809 2.9144 2.9144 0 0 1-.12-1.2546 2.8788 2.8788 0 0 1
 .4334-1.1856 2.8439 2.8439 0 0 1
 .8976-.8786c.1389-.0873.2807-.171.4218-.2524 1.1674-.6582
 1.6925-1.6889 1.731-3.0053a1.9547 1.9547 0 0 1
 .0895-.3804c.131.056.28.0836.3884.1709 1.4336 1.126 2.2453 2.8148
 2.2453 4.9037z" />
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
