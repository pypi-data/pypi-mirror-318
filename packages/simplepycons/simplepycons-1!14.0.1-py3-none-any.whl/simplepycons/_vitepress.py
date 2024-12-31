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


class VitepressIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vitepress"

    @property
    def original_file_name(self) -> "str":
        return "vitepress.svg"

    @property
    def title(self) -> "str":
        return "VitePress"

    @property
    def primary_color(self) -> "str":
        return "#5C73E7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>VitePress</title>
     <path d="M17.029.0014a1.8382 1.8382 0 0 0-.1875.0176L4.0845
 1.8334C3.0779 1.9767 2.3767 2.9196 2.518 3.939l2.5604 18.457c.1415
 1.0193 1.0735 1.7292 2.08 1.586l12.757-1.8165c1.0066-.1433
 1.7078-1.0861 1.5664-2.1054L18.9215 1.6049C18.7889.6493 17.961-.035
 17.029.0014Zm.127.9316c.4271.027.7915.3549.8534.8008l2.5604
 18.457c.0707.5097-.28.9812-.7831 1.0528L7.0296
 23.058c-.5033.0717-.9683-.2833-1.039-.793L3.4302
 3.81c-.0707-.5097.2799-.9811.7832-1.0528L16.9704.9408A.9066.9066 0 0
 1 17.156.933zm-3.6443 5.3541L9.9668 7.5215a.1364.1364 0 0
 0-.0898.1406l.3183
 3.8692c.0075.0911.0994.1497.1836.1171l.9824-.3789c.092-.0355.1894.0373.1836.1368l-.0898
 1.539c-.006.1036.1005.1763.1933.1328l.5997-.2812c.093-.0435.1976.031.1914.1347l-.1465
 2.418c-.0092.1513.195.2037.2578.0664l.041-.0918
 2.123-6.4238c.0355-.1076-.0658-.2104-.1718-.1738l-1.0176.3515c-.0955.033-.1917-.0491-.1777-.1504l.3437-2.4902a.1368.1368
 0 0
 0-.1426-.1562c-.016-.001-.0422.0084-.037.0058zm2.8223.7988a.2717.2717
 0 0 0-.0801.0137L14
 7.8496l-.0762.5606.4551-.1563c.5074-.1627.973.2955.8106.8027l-2.131
 6.4493-.0526.1171c-.1268.2776-.4416.4304-.7383.3516-.2904-.077-.4911-.353-.4727-.6562l.1094-1.8086c-.5057.2578-.9731-.1473-.9473-.5938l.0567-.9765-.4532.1757c-.4144.1536-.8298-.1366-.8632-.543L9.453
 8.5997l-3.0625-.123c-.2294-.0093-.3635.2552-.2226.4394l6.291
 8.2305c.1293.169.391.1302.4668-.0684l3.668-9.6191c.072-.1889-.0765-.377-.2598-.373z"
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
        return '''https://github.com/vuejs/vitepress/blob/f7aef'''

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
