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


class NuxtIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nuxt"

    @property
    def original_file_name(self) -> "str":
        return "nuxt.svg"

    @property
    def title(self) -> "str":
        return "Nuxt"

    @property
    def primary_color(self) -> "str":
        return "#00DC82"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nuxt</title>
     <path d="M13.4642 19.8295h8.9218c.2834 0
 .5618-.0723.8072-.2098a1.5899 1.5899 0 0 0 .5908-.5732 1.5293 1.5293
 0 0 0 .216-.783 1.529 1.529 0 0 0-.2167-.7828L17.7916 7.4142a1.5904
 1.5904 0 0 0-.5907-.573 1.6524 1.6524 0 0 0-.807-.2099c-.2833
 0-.5616.0724-.807.2098a1.5904 1.5904 0 0 0-.5907.5731L13.4642
 9.99l-2.9954-5.0366a1.5913 1.5913 0 0 0-.591-.573 1.6533 1.6533 0 0
 0-.8071-.2098c-.2834 0-.5617.0723-.8072.2097a1.5913 1.5913 0 0
 0-.591.573L.2168 17.4808A1.5292 1.5292 0 0 0 0
 18.2635c-.0001.2749.0744.545.216.783a1.59 1.59 0 0 0
 .5908.5732c.2454.1375.5238.2098.8072.2098h5.6003c2.219 0 3.8554-.9454
 4.9813-2.7899l2.7337-4.5922L16.3935 9.99l4.3944 7.382h-5.8586ZM7.123
 17.3694l-3.9083-.0009 5.8586-9.8421 2.9232 4.921-1.9572 3.2892c-.7478
 1.1967-1.5972 1.6328-2.9163 1.6328z" />
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
        yield from [
            "Nuxt.js",
        ]
