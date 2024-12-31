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


class GoogleEarthIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googleearth"

    @property
    def original_file_name(self) -> "str":
        return "googleearth.svg"

    @property
    def title(self) -> "str":
        return "Google Earth"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Earth</title>
     <path d="M12 0c-1.326 0-2.597.22-3.787.613 4.94-1.243 8.575 1.72
 11.096 5.606 1.725 2.695 2.813 2.83 4.207 2.412A11.956 11.956 0 0012
 0zM7.658 2.156c-1.644.019-3.295.775-4.931 2.207A11.967 11.967 0 000
 12c.184-2.823 2.163-5.128 4.87-5.07 2.104.044 4.648 1.518 7.13 5.289
 4.87 7.468 10.917 5.483 11.863 1.51.081-.566.137-1.14.137-1.729
 0-.176-.02-.347-.027-.521-1.645 1.725-4.899
 2.35-8.264-2.97-2.59-4.363-5.31-6.383-8.05-6.353zM3.33
 13.236c-1.675.13-2.657 1.804-2.242 3.756A11.955 11.955 0 0012
 24c4.215 0 7.898-2.149 10.037-5.412v-.043c-2.836 3.49-8.946
 4.255-13.855-2.182-1.814-2.386-3.544-3.228-4.852-3.127Z" />
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
