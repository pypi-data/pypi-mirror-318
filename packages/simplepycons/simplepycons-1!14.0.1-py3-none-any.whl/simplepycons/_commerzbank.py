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


class CommerzbankIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "commerzbank"

    @property
    def original_file_name(self) -> "str":
        return "commerzbank.svg"

    @property
    def title(self) -> "str":
        return "Commerzbank"

    @property
    def primary_color(self) -> "str":
        return "#FFCC33"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Commerzbank</title>
     <path d="M6.277 1.538a.018.018 0 0 0-.012.007l-4.74 8.21-1.398
 2.418c.446.774.794 1.353 1.22 2.09.671 1.164 1.548 1.597 3.13
 1.889a12.9 12.9 0 0 1 .697-1.392l2.783-4.824 2.786-4.826c.404-.702
 1.296-2.143
 2.57-2.965-.04.025-.07.059-.109.085.07-.047.137-.094.209-.136.46-.278.98-.467
 1.413-.515.339-.038 1.465-.041
 2.74-.041zm11.59.505c-1.048-.008-1.462.007-2.545.008-1.39
 0-2.381.887-3.083 1.773.372.493.68.971.863 1.288a13357.605 13357.605
 0 0 0 5.571 9.648c.404.7 1.209 2.196 1.284 3.71.029.574-.079
 1.165-.265 1.592-.131.3-.652 1.207-1.256 2.253L24
 12.678v-.008a.013.013 0 0 0-.002-.005zM.001 8.163l.095 4.946L0
 8.163zm.093 4.946 1.132 1.964 4.264 7.384a.015.015 0 0 0
 .012.005h12.265c.446-.779.664-1.147
 1.311-2.282.709-1.242.278-2.681-.037-3.472-.618.076-1.18.093-1.547.093H6.35c-.809
 0-2.505-.05-3.853-.741-.513-.263-.972-.65-1.248-1.027-.176-.238-.625-1.003-1.156-1.924z"
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
        return '''https://commons.wikimedia.org/wiki/Category:C'''

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
