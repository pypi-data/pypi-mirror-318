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


class TablecheckIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tablecheck"

    @property
    def original_file_name(self) -> "str":
        return "tablecheck.svg"

    @property
    def title(self) -> "str":
        return "TableCheck"

    @property
    def primary_color(self) -> "str":
        return "#7935D2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TableCheck</title>
     <path d="M10.9139 3.8281 7.24817.16392C7.1253.04109
 6.87835-.00105 6.71331.04109 3.75313 1.36028 1.37926 3.71815.04078
 6.66865a.44898.44898 0 0 0 .12408.53464L3.8294
 10.8675c.12408.124.37103.0819.41199-.1228a7.90878 7.90878 0 0 1
 2.21626-4.33041 7.91452 7.91452 0 0 1 4.33216-2.21532c.1651 0
 .247-.24684.1241-.37087Zm9.2661 7.0803
 3.6658-3.66417c.1229-.12282.165-.36967.1228-.53463-1.3199-2.95848-3.6788-5.33089-6.6303-6.6685a.44958.44958
 0 0 0-.2884-.0297.44942.44942 0 0 0-.2465.15252L13.1377
 3.8281c-.1241.12282-.0819.37087.1229.41181a7.91473 7.91473 0 0 1
 4.3322 2.21532 7.90904 7.90904 0 0 1 2.2162 4.33037c0
 .1638.2482.2468.371.1228Zm3.6658 5.887L20.18
 13.0903c-.1228-.1228-.3698-.0819-.4119.124-.5349 3.3355-3.1707
 6.0099-6.5485 6.5457-.2048.041-.2879.2878-.1229.4118l3.6658
 3.663c.1228.124.3698.165.5348.124 2.9486-1.3214 5.3084-3.6802
 6.6304-6.6275.1241-.2059.0831-.4118-.0819-.5359ZM3.8306 13.0903.16366
 16.7954c-.12408.1241-.16504.3709-.12408.5359 1.32198 2.9473 3.68175
 5.3061 6.63037 6.6275a.44874.44874 0 0 0 .28924.0296.44923.44923 0 0
 0
 .24682-.1536l3.66569-3.663c.1229-.124.082-.3708-.124-.4118-1.64103-.2653-3.15679-1.0404-4.33223-2.2153a7.90877
 7.90877 0 0
 1-2.21625-4.3304c0-.1649-.24695-.2468-.37103-.124h.00241Z" />
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
