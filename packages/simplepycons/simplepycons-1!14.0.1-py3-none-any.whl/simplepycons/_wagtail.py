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


class WagtailIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wagtail"

    @property
    def original_file_name(self) -> "str":
        return "wagtail.svg"

    @property
    def title(self) -> "str":
        return "Wagtail"

    @property
    def primary_color(self) -> "str":
        return "#43B1B0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wagtail</title>
     <path d="M16.1812 0c-2.641 0-4.11 1.969-4.732 3.313L4.0175
 16.9734l2.0979-.3927L2.2627 24l2.688-.4822 2.0433-5.8379c5.8146 0
 13.279-2.0877 12.2382-9.9063 0
 0-.634-3.151-4.7436-2.3013-.4163-1.4205-.3419-2.4749.5662-3.4343
 1.2487-1.3192 3.1822-.5958 3.1822-.5958l.002-1.0877C17.5596.0565
 16.9059 0 16.1813 0zm2.417 2.5229a.4955.4955 0 1 0 0 .991.4955.4955 0
 0 0 0-.991zm1.502 1.029l-1.2918 1.5742h2.9289zM16.374
 8.3422l.3033.0105-.0407.5502-.0374.2886c-.0144.1048-.0252.2188-.051.3388l-.0737.383-.1068.4193c-.0422.1448-.0937.2935-.1428.4484a14.128
 14.128 0 0
 1-.1863.4678l-.1128.2374-.0574.1207-.066.1184-.1343.2399c-.0502.0778-.1008.1563-.152.2354l-.0772.119-.0853.1146c-.0578.0762-.1137.1546-.1741.2303-.1258.1472-.2494.2993-.3902.438-.1335.1453-.2843.2754-.4312.4097l-.231.19c-.0764.0644-.1598.12-.2393.1803-.3235.2336-.6618.4464-1.01.626-.3473.1805-.697.3432-1.0442.4767-.3467.1351-.686.2538-1.0122.3513-.3253.1004-.6363.1829-.9243.2547-.5762.1422-1.061.2393-1.4002.3065l-.5337.1026.531-.1155c.3374-.0754.8196-.184
 1.391-.3397.2855-.0785.5935-.1682.9148-.276.3223-.1047.6567-.2308.9972-.373.3413-.1407.6833-.31
 1.0217-.4962.3392-.1853.6668-.4028.9782-.6391.0764-.0611.1567-.1172.2298-.182l.2212-.191c.1401-.1346.2841-.2646.4104-.4091.1337-.138.2499-.2887.3685-.4341.0567-.0747.109-.1521.1632-.2271l.08-.1128.0719-.1168.1413-.231.1241-.2348.0609-.1155.0526-.118.1033-.2314c.061-.1552.1165-.3078.1688-.4556.0438-.1509.09-.2953.1274-.436l.0934-.4074.0623-.3721c.0223-.1163.03-.2273.0415-.3291.0108-.102.0208-.1956.0296-.2803l.0267-.5345Z"
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
        return '''https://github.com/wagtail/wagtail/blob/e3e46
e23b780aa2b1b521de081cb81872f77466d/wagtail/admin/static_src/wagtailad'''

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
