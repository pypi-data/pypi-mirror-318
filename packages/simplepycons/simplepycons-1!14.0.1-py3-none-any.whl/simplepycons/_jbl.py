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


class JblIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jbl"

    @property
    def original_file_name(self) -> "str":
        return "jbl.svg"

    @property
    def title(self) -> "str":
        return "JBL"

    @property
    def primary_color(self) -> "str":
        return "#FF3300"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>JBL</title>
     <path d="M0 5.2645l2.0221 4.5892 2.0217-4.5892zm2.0221
 7.601c.6982 0 1.2656-.5655 1.2656-1.2606
 0-.6985-.5674-1.2618-1.2656-1.2618-.7003 0-1.2661.5633-1.2661 1.2618
 0 .6951.5658 1.2607 1.2661 1.2607zm-1.0937 3.361c0 .9572.862 2.509
 3.3142 2.509 2.4529 0 3.3154-1.1872 3.3154-2.509V5.2645H5.3693l.0011
 11.3428c0 .6196-.5037 1.1392-1.1261 1.1392-.6231
 0-1.1279-.5045-1.1279-1.124l-.0016-2.3108H.9284zm8.2885
 2.3119V5.2645h4.3745c.8441 0 2.187.693 2.187 2.1628v2.2611c0
 .6612-.5798 1.8328-1.4412 1.8328.8614 0 1.4412.7422 1.4412
 1.3045v3.9788c0 .6767-.5463 1.7339-2.187 1.7339zm3.3802-7.559c.7955 0
 .9944-.134.9944-2.2147
 0-2.0801-.199-2.246-.9944-2.246h-1.1948v4.4575zm.9944 3.8108c0-2.0812
 0-2.6906-.8636-2.6906h-1.3256v5.3482l1.3255.0027c.8636 0
 .8636-.5807.8636-2.6603zm3.779 3.7482H24v-4.2267h-2.1886l.0016
 2.3107c0 .6196-.5047 1.1241-1.1273 1.1241-.622
 0-1.1273-.5045-1.1273-1.124V5.2644h-2.188Z" />
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
