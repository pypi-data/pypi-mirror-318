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


class ThirdwebIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "thirdweb"

    @property
    def original_file_name(self) -> "str":
        return "thirdweb.svg"

    @property
    def title(self) -> "str":
        return "thirdweb"

    @property
    def primary_color(self) -> "str":
        return "#F213A4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>thirdweb</title>
     <path d="M24 13.5937c-.1163.393-.2906.7639-.4387 1.143a870.5395
 870.5395 0 0 1-1.2935
 3.2333c-.0994.2468-.2005.4931-.2971.7412a.9115.9115 0 0
 1-.8479.5725.912.912 0 0
 1-.8442-.5778c-1.9393-4.8534-3.1898-7.9705-5.1009-12.7515a.9012.9012
 0 0 1 .0322-.76.898.898 0 0 1
 .6024-.4628c.0174-.004.0343-.0099.0517-.0151h4.2467c.0134.004.026.0093.0395.0122a.9061.9061
 0 0 1 .6613.5671c.2472.6211.4947 1.2404.7426 1.858a8310.711 8310.711
 0 0 1 1.945 4.8654c.1702.4274.3597.8472.4991
 1.2862zm-19.0021-8.88c.0482.0135.0965.0251.1435.0414a.8605.8605 0 0 1
 .5434.506 910.6628 910.6628 0 0 1 1.2551 3.1326c.6288 1.57 1.255
 3.1412 1.8857 4.7105a.9012.9012 0 0 1 0 .6987c-.6574 1.6411-1.3168
 3.2814-1.9757 4.9219a.8993.8993 0 0
 1-.3286.4067c-.308.2088-.7209.2057-1.0283-.0032a.9163.9163 0 0
 1-.3423-.4344c-.394-.9997-.796-1.9966-1.1947-2.9946-1.078-2.727-2.17-5.4485-3.2582-8.1715-.208-.52-.4144-1.041-.6253-1.5604-.1912-.449.009-.9714.451-1.1768a1.736
 1.736 0 0 1 .2376-.0768zm7.6272
 0c.147.0306.2856.0924.4067.1811a.9537.9537 0 0 1 .3005.4117c.8137
 2.0331 1.6242 4.0675 2.44 6.0998.2243.5613.4474 1.1232.6752
 1.6833a.931.931 0 0 1 0 .7244l-1.9571
 4.8823c-.1296.3231-.3643.524-.7095.5764-.4295.0646-.8136-.1473-.9687-.524-.9815-2.4381-1.9539-4.8798-2.9293-7.3203-.5451-1.3667-1.091-2.7331-1.6376-4.0991-.1813-.4536-.3568-.9095-.5462-1.3596a.9105.9105
 0 0 1 .0264-.7696.9072.9072 0 0 1
 .607-.4724c.0157-.0034.0308-.0093.0459-.014Z" />
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
