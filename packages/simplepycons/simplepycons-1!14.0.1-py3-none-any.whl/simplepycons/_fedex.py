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


class FedexIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fedex"

    @property
    def original_file_name(self) -> "str":
        return "fedex.svg"

    @property
    def title(self) -> "str":
        return "FedEx"

    @property
    def primary_color(self) -> "str":
        return "#4D148C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FedEx</title>
     <path d="M22.498 14.298c-.016-.414.345-.751.75-.755a.745.745 0 0
 1 .752.755.755.755 0 0
 1-.751.745c-.395.002-.759-.346-.751-.745zm.759-.083c.067-.02.164-.042.162-.13.007-.09-.086-.133-.162-.134h-.163v.263c0
 .001.165-.002.163.001zm-.163.107v.418h-.14v-.91h.327c.156-.021.294.092.286.253a.218.218
 0 0 1-.156.19c.162.083.108.322.173.467h-.156a2.355 2.355 0 0
 1-.04-.205c-.018-.093-.047-.229-.17-.213h-.124zm.76-.024a.603.603 0 0
 0-.605-.632c-.338-.012-.62.302-.605.632a.619.619 0 0 0 .605.622.61.61
 0 0 0 .605-.622zm-5.052-.579l-.878
 1.008h-1.306l1.559-1.745-1.56-1.75h1.355l.902.997.878-.998h1.306l-1.543
 1.743 1.559
 1.753h-1.371l-.901-1.008zm-4.703-.352v-.827h1.904v-1.506l1.724
 1.948-1.724 1.941v-1.556h-1.904zm1.56
 1.36h-3.2V9.044h3.224v1.024H13.77v1.163h1.888v.958h-1.904v1.522h1.904v1.016zm-5.705-.655c-.54.017-.878-.552-.877-1.04-.01-.507.307-1.123.878-1.105.579-.025.871.6.845
 1.103.023.501-.29 1.062-.846 1.042zM4.743
 12.41c.076-.358.403-.67.78-.663a.788.788 0 0 1
 .803.663H4.743zm15.182.564l1.815-2.047h-2.125l-.74.844-.763-.844h-4.037v-.548h1.912V8.741H10.84v2.58c-.362-.448-.981-.559-1.526-.492-.782.123-1.427.762-1.634
 1.514-.254-.958-1.179-1.588-2.157-1.554-.781.009-1.6.365-1.987
 1.071v-.818h-1.87v-.9h2.043v-1.4H0v6.287h1.666v-2.644h1.666a7.59 7.59
 0 0 0-.082.622c-.013 1.232 1.042 2.27 2.274 2.236a2.204 2.204 0 0 0
 2.157-1.432H6.254c-.14.268-.441.38-.73.36-.457.009-.83-.417-.829-.86h2.914c.083
 1.027.988 1.966 2.043 1.947a1.53 1.53 0 0 0
 1.19-.639v.41h7.215l.754-.86.754.86h2.192l-1.832-2.055z" />
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
