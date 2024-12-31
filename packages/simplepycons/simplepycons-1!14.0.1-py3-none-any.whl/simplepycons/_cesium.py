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


class CesiumIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cesium"

    @property
    def original_file_name(self) -> "str":
        return "cesium.svg"

    @property
    def title(self) -> "str":
        return "Cesium"

    @property
    def primary_color(self) -> "str":
        return "#6CADDF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cesium</title>
     <path d="M23.0283 10.216c-.3959 0-.7785.22-1.0792.6168l-3.7755
 4.994c-.625.8275-1.5128 1.3012-2.4355 1.3012h-.0143c-.9236
 0-1.8115-.4737-2.4355-1.3012l-3.7754-4.994c-.2998-.3969-.6823-.6168-1.0802-.6168-.3949
 0-.7795.22-1.0781.6168l-3.7765 4.994c-.621.8204-1.4996 1.294-2.414
 1.3012C3.088 21.186 7.2113 24 12.0004 24 18.6268 24 24 18.6276 24
 12.001c0-.4705-.0338-.9308-.086-1.382-.2638-.2598-.5697-.403-.8857-.403m-7.019-2.5972c-.6936
 0-1.2542-.5616-1.2542-1.2541s.5606-1.2541 1.2541-1.2541c.6925 0
 1.254.5616 1.254 1.254s-.5615 1.2542-1.254 1.2542M12.0005 0C5.3732 0
 0 5.3714 0 12.001c0 1.0536.1504 2.0704.406
 3.0463.2272.175.4788.2762.7366.2762.3979 0 .7804-.2189
 1.0812-.6138l3.7754-4.996c.623-.8285 1.5129-1.3021 2.4335-1.3021.9226
 0 1.8095.4736 2.4355 1.3021l3.6323
 4.8037.1565.1923c.2997.3939.6812.6107 1.074.6138.3918-.003.7743-.22
 1.072-.6138l.1595-.1923 3.6323-4.8037c.624-.8285 1.5118-1.3021
 2.4335-1.3021.1462 0 .2935.0163.4367.0388C21.9522 3.5557 17.3922 0
 12.0005 0" />
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
