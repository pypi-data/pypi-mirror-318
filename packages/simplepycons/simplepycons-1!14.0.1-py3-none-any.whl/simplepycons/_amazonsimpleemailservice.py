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


class AmazonSimpleEmailServiceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "amazonsimpleemailservice"

    @property
    def original_file_name(self) -> "str":
        return "amazonsimpleemailservice.svg"

    @property
    def title(self) -> "str":
        return "Amazon Simple Email Service"

    @property
    def primary_color(self) -> "str":
        return "#DD344C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Amazon Simple Email Service</title>
     <path d="M11.9996 0C5.3833 0 0 5.3834 0 11.9998c0 2.5316.7813
 4.9544 2.2599 7.0051l.6955-.5014C1.5827 16.5993.8571 14.3505.8571
 11.9998.8571 5.856 5.856.8572 12.0004.8572c6.144 0 11.1425 4.999
 11.1425 11.1426 0 2.3508-.7256 4.5995-2.0983
 6.5037l.6955.5014C23.2187 16.9542 24 14.5314 24 11.9998 24 5.3834
 18.6163 0 11.9996 0zM6 16.7142a.4285.4285 0 0
 0-.4286.4285v1.7598c-.9643.2048-1.7143 1.0822-1.7143 2.0974 0
 1.1615.9815 2.143 2.1429 2.143s2.1429-.9815
 2.1429-2.143c0-1.0152-.75-1.8926-1.7143-2.0974v-1.3312h5.1428v2.1883c-.9643.2049-1.7143
 1.0822-1.7143 2.0975C9.8571 23.0186 10.8386 24 12 24s2.1429-.9814
 2.1429-2.1429c0-1.0153-.75-1.8926-1.7143-2.0975v-2.1883h5.1428v1.3312c-.9643.2048-1.7143
 1.0822-1.7143 2.0974 0 1.1615.9815 2.143 2.1429 2.143s2.1429-.9815
 2.1429-2.143c0-1.0152-.75-1.8926-1.7143-2.0974v-1.7598A.4285.4285 0 0
 0 18 16.7142h-5.5714v-2.5715H18c.237 0
 .4286-.192.4286-.4286V5.9997A.4285.4285 0 0 0 18 5.571H6a.4285.4285 0
 0 0-.4286.4286v7.7144c0
 .2366.1916.4286.4286.4286h5.5714v2.5715H6zm1.2857 4.2857c0 .697-.5889
 1.2858-1.2857 1.2858s-1.2857-.5889-1.2857-1.2858c0-.6968.5889-1.2857
 1.2857-1.2857S7.2857 20.3031 7.2857 21zm12 0c0 .697-.5889
 1.2858-1.2857 1.2858s-1.2857-.5889-1.2857-1.2858c0-.6968.5889-1.2857
 1.2857-1.2857s1.2857.5889 1.2857 1.2857zm-1.7143-8.248L14.259
 9.7703l3.3124-2.8389v5.8205zm-.7298-6.3236-4.842
 4.1499-4.8412-4.15h9.6832zm-10.413.5031L9.741 9.7707 6.4286
 12.752V6.9314zm.6878 6.3541 3.2807-2.9525 1.3239 1.135a.4253.4253 0 0
 0 .2786.1032.4253.4253 0 0 0 .2785-.1033l1.3243-1.1349 3.2812
 2.9525H7.1164zM12 20.5714c.6968 0 1.2857.5888 1.2857 1.2857 0
 .6969-.5889 1.2857-1.2857
 1.2857s-1.2857-.5888-1.2857-1.2857c0-.6969.5889-1.2857
 1.2857-1.2857z" />
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
            "AWS SES",
        ]
