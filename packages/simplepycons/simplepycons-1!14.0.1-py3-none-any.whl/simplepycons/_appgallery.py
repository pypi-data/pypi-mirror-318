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


class AppgalleryIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "appgallery"

    @property
    def original_file_name(self) -> "str":
        return "appgallery.svg"

    @property
    def title(self) -> "str":
        return "AppGallery"

    @property
    def primary_color(self) -> "str":
        return "#FF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AppGallery</title>
     <path d="M6.734 0C1.804 0 0 1.803 0 6.733v10.535C0 22.198 1.803
 24 6.734 24h10.529C22.193 24 24 22.197 24 17.268V6.733C24 1.803
 22.197 0 17.266 0zM8 4h.565A3.439 3.439 0 0 0 12 7.435 3.439 3.439 0
 0 0 15.435 4H16c0 2.206-1.794 4-4 4S8 6.206 8 4zm6.468 8h.52l.713
 2.16.696-2.158h.66l-1.092 3.14h-.532l-.714-2.063-.714
 2.063h-.528l-1.095-3.14h.678l.694 2.158zm6.236
 0h.629v3.138h-.629zM2.666
 12h.638v1.267h1.439V12h.637v3.142h-.637v-1.276h-1.44v1.276h-.637zm5.668
 0h.637v1.772c0 .9-.496 1.417-1.36 1.417-.856
 0-1.347-.507-1.347-1.39v-1.797H6.9v1.775c0 .524.255.805.719.805.46 0
 .714-.273.714-.784zm2.344 0h.563l1.378
 3.14h-.668l-.282-.654H10.23l-.286.654h-.651zm6.893.002h2.312v.572H18.2v.643h1.16v.573H18.2v.777h1.744v.573H17.57zm-6.623.793-.48
 1.124h.964z" />
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
            "HUAWEI AppGallery",
        ]
