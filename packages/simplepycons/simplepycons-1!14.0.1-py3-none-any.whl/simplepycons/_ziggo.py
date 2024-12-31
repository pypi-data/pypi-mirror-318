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


class ZiggoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ziggo"

    @property
    def original_file_name(self) -> "str":
        return "ziggo.svg"

    @property
    def title(self) -> "str":
        return "Ziggo"

    @property
    def primary_color(self) -> "str":
        return "#F48C00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ziggo</title>
     <path d="M18.555 18.69a3 3 0 0 0-2.52-2.865h-6.3l7.26-6.945a2.145
 2.145 0 0 0 .495-2.34 2.1 2.1 0 0 0-2.205-1.23h-9a2.79 2.79 0 0 0
 2.19 2.895h5.175L6 15.375a2.01 2.01 0 0 0-.42 2.13 1.965 1.965 0 0 0
 2.115 1.185zM2.85 18.6a2.535 2.535 0 0 0 2.55 2.535h13.2a2.536 2.537
 0 0 0 2.55-2.535V7.92A2.865 2.865 0 0 1 24 5.31V18.6a5.385 5.385 0 0
 1-5.4 5.4H5.4A5.385 5.385 0 0 1 0 18.6V5.4A5.385 5.385 0 0 1 5.4
 0h13.2a5.595 5.595 0 0 1 2.07.405A5.235 5.235 0 0 1 22.635 1.8a1.5
 1.5 0 0 1 .42 1.005 1.41 1.41 0 0 1-.42 1.02 1.5 1.5 0 0 1-2.025
 0A2.685 2.685 0 0 0 19.59 3a2.43 2.43 0 0 0-.99-.195H5.4A2.505 2.505
 0 0 0 2.865 5.4z" />
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
