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


class JapanAirlinesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "japanairlines"

    @property
    def original_file_name(self) -> "str":
        return "japanairlines.svg"

    @property
    def title(self) -> "str":
        return "Japan Airlines"

    @property
    def primary_color(self) -> "str":
        return "#C00000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Japan Airlines</title>
     <path d="M11.1381.0342a11.9956 11.9956 0 0 0-8.789 4.8388 9.3446
 9.3446 0 0 0 1.3511 7.8206.014.014 0 1 1-.0219.0172A8.229 8.229 0 0 1
 1.598 6.0554c0-.0152-.0116-.019-.0188-.0078A11.8789 11.8789 0 0 0
 .3624 9.0653a8.7616 8.7616 0 0 0 2.421 5.3574.015.015 0 0
 1-.0188.0234A7.1718 7.1718 0 0 1 .125
 10.4023c0-.0152-.0195-.0152-.0203 0a12.1316 12.1316 0 0 0-.0578
 2.6552 7.2198 7.2198 0 0 0 2.193
 3.1536c.0159.0144.0003.0353-.0157.0265a6.5064 6.5064 0 0
 1-1.954-1.7806c-.0072-.0112-.0204-.0074-.0172.0062a11.9956 11.9956 0
 0 0 23.4805 0c0-.0136-.0092-.0174-.0172-.0062a6.5008 6.5008 0 0
 1-1.9555 1.7806c-.0176.0088-.0316-.0121-.0156-.0265a7.223 7.223 0 0 0
 2.196-3.1536h.0125a12.1284 12.1284 0 0
 0-.0593-2.6552c0-.0152-.0171-.0152-.0203 0a7.1742 7.1742 0 0 1-2.6397
 4.0438.015.015 0 0 1-.0187-.0234 8.7576 8.7576 0 0 0 2.4194-5.3574
 11.8789 11.8789 0 0
 0-1.2167-3.0177c-.008-.0112-.022-.0074-.0188.0078a8.2322 8.2322 0 0
 1-2.079 6.6554.0145.0145 0 1 1-.0233-.0172 9.3422 9.3422 0 0 0
 1.3526-7.8206A11.9956 11.9956 0 0 0 11.138.0342zm.0438.3108a7.7212
 7.7212 0 0 1 6.2383 13.1733l-.0016.0016c-2.4535
 2.3871-6.1174.8622-5.7448-2.0695.2863-2.26 3.0575-4.5112
 5.156-5.7323a.016.016 0 0 0
 0-.0266c-.2751-.2623-.8466-.8526-1.2136-1.2964a2.4127 2.4127 0 0
 0-3.8549.0672l-6.0321.5591a.0188.0188 0 0 0 0
 .0375l6.4663.3749c1.1468.0647 1.5207 1.1057.4155 1.943-4.1073
 3.1133-4.8401 6.4075-3.9189 9.0186a.0171.0171 0 0 1-.0312.014 5.3045
 5.3045 0 0 1-.8138-1.8758A7.7212 7.7212 0 0 1 11.1818.345ZM9.12
 17.3357h1.6353l-.8746 2.2804a2.1952 2.1952 0 0 1-2.3382 1.262 5.3005
 5.3005 0 0 1-1.1387-.1124l.2796-.7279c.7485.0872 1.3905.0216
 1.6416-.6326zm3.8658 0h1.4635l.328
 3.43h-1.6369l-.025-.678H11.638l-.5435.678h-1.351l2.7395-3.1754a.7005.7005
 0 0 1 .503-.2546zm3.5456 0h1.6353l-1.0387
 2.7037h2.079l-.2796.7263h-3.7112zm-3.4707.998-.8793 1.0965h.92z" />
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
