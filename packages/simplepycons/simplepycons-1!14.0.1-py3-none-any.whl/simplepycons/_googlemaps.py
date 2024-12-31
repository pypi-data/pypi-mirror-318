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


class GoogleMapsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlemaps"

    @property
    def original_file_name(self) -> "str":
        return "googlemaps.svg"

    @property
    def title(self) -> "str":
        return "Google Maps"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Maps</title>
     <path d="M19.527 4.799c1.212 2.608.937 5.678-.405 8.173-1.101
 2.047-2.744 3.74-4.098 5.614-.619.858-1.244 1.75-1.669
 2.727-.141.325-.263.658-.383.992-.121.333-.224.673-.34
 1.008-.109.314-.236.684-.627.687h-.007c-.466-.001-.579-.53-.695-.887-.284-.874-.581-1.713-1.019-2.525-.51-.944-1.145-1.817-1.79-2.671L19.527
 4.799zM8.545 7.705l-3.959 4.707c.724 1.54 1.821 2.863 2.871
 4.18.247.31.494.622.737.936l4.984-5.925-.029.01c-1.741.601-3.691-.291-4.392-1.987a3.377
 3.377 0 0
 1-.209-.716c-.063-.437-.077-.761-.004-1.198l.001-.007zM5.492
 3.149l-.003.004c-1.947 2.466-2.281 5.88-1.117
 8.77l4.785-5.689-.058-.05-3.607-3.035zM14.661.436l-3.838
 4.563a.295.295 0 0 1 .027-.01c1.6-.551 3.403.15 4.22
 1.626.176.319.323.683.377 1.045.068.446.085.773.012 1.22l-.003.016
 3.836-4.561A8.382 8.382 0 0 0 14.67.439l-.009-.003zM9.466
 5.868L14.162.285l-.047-.012A8.31 8.31 0 0 0 11.986 0a8.439 8.439 0 0
 0-6.169 2.766l-.016.018 3.665 3.084z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Googl'''

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
