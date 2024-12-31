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


class EcovacsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ecovacs"

    @property
    def original_file_name(self) -> "str":
        return "ecovacs.svg"

    @property
    def title(self) -> "str":
        return "Ecovacs"

    @property
    def primary_color(self) -> "str":
        return "#1E384B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ecovacs</title>
     <path d="M19.066,19.071L19.065,19.07C17.256,20.88 14.755,22
 11.994,22C9.233,22 6.732,20.88 4.924,19.07L4.924,19.071C4.743,18.89
 4.492,18.779 4.217,18.779C3.956,18.779 3.722,18.879
 3.543,19.041C3.343,19.223 3.217,19.485 3.217,19.779C3.217,20.049
 3.325,20.295 3.499,20.475L3.51,20.485L3.521,20.496C5.692,22.661
 8.686,24 11.994,24C15.3,24 18.295,22.662
 20.466,20.498L20.48,20.484L20.491,20.472C20.665,20.293 20.772,20.048
 20.772,19.779C20.772,19.485 20.645,19.223 20.445,19.041C20.267,18.879
 20.031,18.779 19.773,18.779C19.496,18.779 19.247,18.89
 19.066,19.071ZM15.394,14L11.395,14C10.29,14 9.395,13.105
 9.395,12C9.395,10.896 10.29,10.001
 11.395,10.001L15.394,10.001L16.794,8L11.395,8C9.185,8 7.394,9.791
 7.394,12C7.394,14.209 9.185,16
 11.395,16L16.794,16L15.394,14ZM14.994,11L14.963,11.001L14.963,11L11.994,11C11.441,11
 10.995,11.448 10.995,12C10.995,12.553 11.441,13
 11.994,13L14.963,13L14.963,12.998L14.994,13C15.546,13 15.994,12.553
 15.994,12C15.994,11.448 15.546,11 14.994,11ZM11.977,0C8.68,0.003
 5.69,1.339 3.523,3.497C3.342,3.677 3.228,3.926
 3.228,4.202C3.227,4.496 3.353,4.758 3.553,4.941C3.73,5.103
 3.966,5.204 4.225,5.205C4.501,5.206 4.751,5.094
 4.933,4.915L4.933,4.914L4.934,4.913C6.748,3.107 9.25,1.994
 12.011,2C14.772,2.007 17.27,3.13
 19.075,4.945L19.075,4.944C19.256,5.125 19.505,5.239
 19.781,5.24C20.041,5.24 20.277,5.14 20.455,4.978C20.656,4.796
 20.783,4.535 20.783,4.242C20.784,3.965 20.673,3.716
 20.493,3.536L20.492,3.534L20.491,3.533C18.325,1.357 15.328,0.007
 12.015,0L11.977,0Z" />
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
