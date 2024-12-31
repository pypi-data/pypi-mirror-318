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


class SamsungIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "samsung"

    @property
    def original_file_name(self) -> "str":
        return "samsung.svg"

    @property
    def title(self) -> "str":
        return "Samsung"

    @property
    def primary_color(self) -> "str":
        return "#1428A0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Samsung</title>
     <path d="M19.8166 10.2808l.0459
 2.6934h-.023l-.7793-2.6934h-1.2837v3.3925h.8481l-.0458-2.785h.023l.8366
 2.785h1.2264v-3.3925zm-16.149 0l-.6418
 3.427h.9284l.4699-3.1175h.0229l.4585
 3.1174h.9169l-.6304-3.4269zm5.1805 0l-.424
 2.6132h-.023l-.424-2.6132H6.5788l-.0688
 3.427h.8596l.023-3.0832h.0114l.573
 3.0831h.8711l.5731-3.083h.023l.0228
 3.083h.8596l-.0802-3.4269zm-7.2664
 2.4527c.0343.0802.0229.1949.0114.2522-.0229.1146-.1031.2292-.3324.2292-.2177
 0-.3438-.126-.3438-.3095v-.3323H0v.2636c0 .7679.6074.9971
 1.2493.9971.6189 0 1.1346-.2178 1.2149-.7794.0458-.298.0114-.4928
 0-.5616-.1605-.722-1.467-.9283-1.5588-1.3295-.0114-.0688-.0114-.1375
 0-.1834.023-.1146.1032-.2292.3095-.2292.2063 0
 .321.126.321.3095v.2063h.8595v-.2407c0-.745-.6762-.8596-1.1576-.8596-.6074
 0-1.1117.2063-1.2034.7564-.023.149-.0344.2866.0114.4585.1376.7106
 1.364.9169 1.5358 1.3524m11.152
 0c.0343.0803.0228.1834.0114.2522-.023.1146-.1032.2292-.3324.2292-.2178
 0-.3438-.126-.3438-.3095v-.3323h-.917v.2636c0 .7564.596.9857
 1.2379.9857.6189 0 1.1232-.2063 1.2034-.7794.0459-.298.0115-.4814
 0-.5616-.1375-.7106-1.4327-.9284-1.5243-1.318-.0115-.0688-.0115-.1376
 0-.1835.0229-.1146.1031-.2292.3094-.2292.1948 0
 .321.126.321.3095v.2063h.848v-.2407c0-.745-.6647-.8596-1.146-.8596-.6075
 0-1.1004.1948-1.192.7564-.023.149-.023.2866.0114.4585.1376.7106
 1.341.9054 1.513 1.3524m2.8882.4585c.2407 0
 .3094-.1605.3323-.2522.0115-.0343.0115-.0917.0115-.126v-2.533h.871v2.4642c0
 .0688 0 .1948-.0114.2292-.0573.6419-.5616.8482-1.192.8482-.6303
 0-1.1346-.2063-1.192-.8482
 0-.0344-.0114-.1604-.0114-.2292v-2.4642h.871v2.533c0 .0458 0
 .0916.0115.126 0 .0917.0688.2522.3095.2522m7.1518-.0344c.2522 0
 .3324-.1605.3553-.2522.0115-.0343.0115-.0917.0115-.126v-.4929h-.3553v-.5043H24v.917c0
 .0687 0 .1145-.0115.2292-.0573.6303-.596.8481-1.2034.8481-.6075
 0-1.1461-.2178-1.2034-.8481-.0115-.1147-.0115-.1605-.0115-.2293v-1.444c0-.0574.0115-.172.0115-.2293.0802-.6419.596-.8482
 1.2034-.8482s1.1347.2063
 1.2034.8482c.0115.1031.0115.2292.0115.2292v.1146h-.8596v-.1948s0-.0803-.0115-.1261c-.0114-.0802-.0802-.2521-.3438-.2521-.2521
 0-.321.1604-.3438.2521-.0115.0458-.0115.1032-.0115.1605v1.5702c0
 .0458 0 .0916.0115.126 0 .0917.0917.2522.3323.2522" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.samsung.com/us/about-us/brand-ide'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.samsung.com/us/about-us/brand-ide'''

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
