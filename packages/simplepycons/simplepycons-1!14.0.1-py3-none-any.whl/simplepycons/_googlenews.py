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


class GoogleNewsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlenews"

    @property
    def original_file_name(self) -> "str":
        return "googlenews.svg"

    @property
    def title(self) -> "str":
        return "Google News"

    @property
    def primary_color(self) -> "str":
        return "#174EA6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google News</title>
     <path d="M21.2666 21.2a.6141.6141 0 0
 1-.6128.6128H3.3446a.614.614 0 0 1-.6128-.6128V8.1153a.6141.6141 0 0
 1 .6128-.6128h17.3091a.6141.6141 0 0 1
 .6128.6128V21.2zm-3.0315-3.4196v-1.1957a.0803.0803 0 0
 0-.0803-.0803h-5.3725v1.3619h5.3725a.0817.0817 0 0 0
 .0804-.083l-.0001-.0029zm.8171-2.5875v-1.2012a.0803.0803 0 0
 0-.079-.0817h-6.191v1.3619h6.1896a.079.079 0 0 0
 .0804-.0776v-.0041.0027zm-.8171-2.5875v-1.2066a.0803.0803 0 0
 0-.0803-.0803h-5.3725v1.3619h5.3725a.0816.0816 0 0 0
 .0803-.079v.004zM8.1492 14.0448v1.2257h1.7704c-.1457.749-.8049
 1.2924-1.7704
 1.2924-1.0906-.0405-1.9418-.9574-1.9013-2.048.0384-1.0338.8676-1.8629
 1.9013-1.9013a1.77 1.77 0 0 1 1.2529.4903l.9342-.9329a3.1405 3.1405 0
 0 0-2.1871-.8525c-1.8051 0-3.2684 1.4633-3.2684 3.2684 0 1.8051
 1.4633 3.2684 3.2684 3.2684 1.8889 0 3.1323-1.3278
 3.1323-3.1976a3.941 3.941 0 0 0-.0518-.6183l-3.0805.0054zM2.2701
 7.6537a.6156.6156 0 0 1 .6128-.6128h12.1545l-1.2692-3.4904a.5952.5952
 0 0 0-.7436-.3827L.3676 7.7749a.5938.5938 0 0 0-.3228.7749l2.2253
 6.112V7.6537za.6156.6156 0 0 1
 .6128-.6128h12.1545l-1.2692-3.4904a.5952.5952 0 0 0-.7436-.3827L.3676
 7.7749a.5938.5938 0 0 0-.3228.7749l2.2253
 6.112V7.6537zm21.3116-.3105l-8.803-2.3683.7517
 2.0659h5.5836a.6141.6141 0 0 1
 .6128.6128v8.7948l2.2471-8.3659a.5923.5923 0 0
 0-.3922-.7393zm-4.4955-1.6738V2.7946a.6101.6101 0 0
 0-.6115-.6074H5.5236a.6101.6101 0 0
 0-.6156.6046v2.8368l8.3904-3.0519a.5937.5937 0 0 1 .7422.3895l.5447
 1.498 4.5009 1.2052z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://partnermarketinghub.withgoogle.com/br'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://partnermarketinghub.withgoogle.com/br'''

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
