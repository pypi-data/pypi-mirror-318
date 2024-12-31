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


class UberEatsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ubereats"

    @property
    def original_file_name(self) -> "str":
        return "ubereats.svg"

    @property
    def title(self) -> "str":
        return "Uber Eats"

    @property
    def primary_color(self) -> "str":
        return "#06C167"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Uber Eats</title>
     <path d="M0 2.8645v4.9972c0 1.8834 1.3315 3.1297 3.0835
 3.1297a2.9652 2.9652 0 0 0
 2.1502-.876v.7425H6.445V2.8645H5.223v4.9339c0 1.2642-.8696
 2.1198-1.9954
 2.122-1.1386-.0023-1.997-.834-1.997-2.122V2.8645zm7.3625
 0v7.9934h1.163v-.7318a2.9915 2.9915 0 0 0 2.1177.876c1.714.048
 3.1295-1.3283 3.1295-3.0429s-1.4155-3.091-3.1295-3.0429a2.9674 2.9674
 0 0 0-2.107.876V2.8645zm9.8857 2.0561c-1.6752-.0074-3.0369
 1.3492-3.0356 3.0245 0 1.7366 1.3732 3.0373 3.1537 3.0373a3.123 3.123
 0 0 0 2.5578-1.2438l-.8495-.6177a2.0498 2.0498 0 0
 1-1.7083.8585c-.9763.0126-1.8147-.6915-1.971-1.6553h4.818v-.379c0-1.734-1.254-3.0238-2.9638-3.0245zm6.1632.0667a1.5943
 1.5943 0 0
 0-1.376.7657v-.7186h-1.163v5.8235h1.1741V7.5465c0-.9023.5581-1.4847
 1.3268-1.4847h.4949V4.9886c-.1576.0013-.3186-.0009-.4568-.0013zm-6.2034.944a1.844
 1.844 0 0 1 1.8337 1.486H15.424a1.844 1.844 0 0 1
 1.784-1.486zm-6.6589.0056c1.1223-.0084 2.0365.8992 2.0364
 2.0215-.0026 1.1203-.914 2.0258-2.0343 2.021a2.0151 2.0151 0 0
 1-1.4159-.5987A2.0152 2.0152 0 0 1 8.55 7.9592a2.0152 2.0152 0 0 1
 .5838-1.422 2.0152 2.0152 0 0 1 1.4153-.6003zM0
 12.9864v7.9716h5.7222v-1.3666H1.5458v-1.971h4.0647v-1.314H1.5458v-1.9556h4.1764v-1.3644zm14.5608.4097v1.6861h-1.1519v1.338h1.1545v3.143c0
 .7927.5712 1.4209 1.6005 1.4209h1.6425L17.8 19.646h-1.1412c-.3482
 0-.5714-.1509-.5714-.464v-2.7683H17.8v-1.3316h-1.7062v-1.686zm-5.2974
 1.5275c-1.7348-.0103-3.141 1.4035-3.1214 3.1382.0196 1.7346 1.4575
 3.1163 3.1915 3.0668a2.9915 2.9915 0 0 0
 1.912-.6655v.532h1.5175v-5.9129h-1.509v.5257a3.0047 3.0047 0 0
 0-1.9205-.6835c-.0244-.0007-.0492-.0006-.0701-.0008zm11.771.0077c-1.5855
 0-2.7002.6437-2.7002 1.8854 0 .8607.6132 1.4213 1.936
 1.695l1.4478.3286c.5694.1095.7224.2585.7224.4906 0
 .3701-.438.6022-1.1279.6022-.876
 0-1.3774-.1907-1.5723-.8477h-1.533c.219 1.2307 1.1563 2.05 3.0484
 2.05h.0022c1.752 0 2.7422-.819 2.7422-1.9534
 0-.8059-.5847-1.4084-1.8089-1.6668l-1.2943-.2605c-.7511-.1358-.988-.2738-.988-.5454
 0-.357.3616-.5757 1.0295-.5757.7227 0 1.2527.1925
 1.406.8473h1.5175c-.0854-1.2286-.9899-2.0497-2.8273-2.0497zM9.467
 16.1815c1.0092.0096 1.8188.8369 1.8067 1.8461.0014 1.0046-.8198
 1.816-1.8243
 1.8025-1.0075-.0048-1.8203-.8256-1.8155-1.833.0048-1.0076.8255-1.8204
 1.833-1.8156z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://assets.uber.com/d/k4nuxdZ8MC7E/user-g'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://assets.uber.com/d/k4nuxdZ8MC7E/logos/'''

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
