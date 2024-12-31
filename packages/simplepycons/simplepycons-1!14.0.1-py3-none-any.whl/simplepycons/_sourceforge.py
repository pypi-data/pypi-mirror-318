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


class SourceforgeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sourceforge"

    @property
    def original_file_name(self) -> "str":
        return "sourceforge.svg"

    @property
    def title(self) -> "str":
        return "SourceForge"

    @property
    def primary_color(self) -> "str":
        return "#FF6600"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SourceForge</title>
     <path d="M9.998 1.4648c-.088 0-.1761.0395-.2402.1036L.1016
 11.2148c-.1361.1281-.1361.3444 0 .4805l9.1523
 9.1348c.064.072.1522.1054.2402.1054.0881 0
 .1743-.0414.2383-.1054l1.3692-1.3848c.136-.128.136-.3444
 0-.4805l-7.172-7.1738a.4682.4682 0
 010-.664l9.0782-9.0782c.1201-.12.1123-.2728.0723-.377-.04-.096-.1444-.207-.3125-.207H9.998zm4.5313
 1.5918c-.088 0-.1762.0415-.2402.1055l-1.3926
 1.3926c-.1361.128-.1361.3444 0 .4805l7.1719
 7.1816c.088.088.1367.208.1367.3281 0
 .1201-.0487.24-.1367.3281l-9.0782
 9.0782c-.12.12-.1123.2728-.0722.377.04.096.1443.207.3125.207v-.0079H14c.088
 0
 .1762-.0316.2402-.0957l9.6563-9.6543c.072-.064.1035-.1521.1035-.2402
 0-.088-.0395-.1762-.1035-.2402l-9.127-9.1348c-.064-.072-.1521-.1055-.2402-.1055zM11.4336
 6.213c-.1125.005-.2164.1007-.211.2383.1442 2.2176-2.6425
 2.7635-2.6425 6.246v.0235c0 2.1216 1.6026 3.8418 3.58 3.8418 1.9775 0
 3.5782-1.7202
 3.5782-3.8418v-.0234c0-.9848-.3679-1.9225-.7442-2.627-.072-.136-.2896-.087-.2656.041.6725
 2.9943-1.0156 4.8507-1.0156 2.545
 0-3.931-1.3943-5.7162-2.1309-6.3887a.2072.2072 0 00-.1484-.0547Z" />
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
