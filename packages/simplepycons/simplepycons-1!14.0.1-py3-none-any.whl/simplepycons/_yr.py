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


class YrIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "yr"

    @property
    def original_file_name(self) -> "str":
        return "yr.svg"

    @property
    def title(self) -> "str":
        return "Yr"

    @property
    def primary_color(self) -> "str":
        return "#00B9F1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Yr</title>
     <path d="M18.412 9.764c.295.257.464.558.474
 1.085-.003.567-.184.96-.454
 1.234-.275.271-.667.452-1.234.454h-1.885c-.292.001-.573.103-.839.2l-.13.047v-2.479a.982.982
 0 0 1 .97-.969h1.708c.605 0 1.09.177 1.39.428zM24 12c0 6.627-5.372
 12-12 12-6.627 0-12-5.373-12-12C0 5.372 5.373 0 12 0c6.628 0 12 5.372
 12 12zM11.148 7.709H9.231l-.002 3.133c-.036 1.168-1.13 1.546-2.001
 1.558-.995-.014-2.044-.566-2.044-2.083V7.709H3.293v2.608c0 1.184.409
 2.195 1.184 2.925.701.66 1.662 1.031 2.712 1.049h.078c.705-.013
 1.741-.473 1.942-.879v.863c0 1.144-1.455 1.89-1.847
 2.086l.028.034a.3059.3059 0 0 0-.01.005l-.018.009 1.218
 1.473.18-.101h-.001c.797-.445 2.38-1.33 2.389-3.717V7.709zm7.14
 6.621a3.427 3.427 0 0 0 1.514-.876c.664-.661 1.026-1.597
 1.022-2.604.01-1.047-.45-1.988-1.176-2.578-.723-.597-1.655-.874-2.625-.875h-1.709c-1.6047.0033-2.9047
 1.3033-2.908 2.908v7.176h1.938v-2.036a.982.982 0 0 1
 .97-.969h.772l2.085
 2.554.146.18c.158.151.365.25.596.27v.001h.042a.283.283 0 0 0 .08
 0h1.147l.003-1.567s-.473.132-.826-.246c-.415-.444-1.071-1.338-1.071-1.338z"
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
