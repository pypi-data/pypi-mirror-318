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


class BeijingSubwayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "beijingsubway"

    @property
    def original_file_name(self) -> "str":
        return "beijingsubway.svg"

    @property
    def title(self) -> "str":
        return "Beijing Subway"

    @property
    def primary_color(self) -> "str":
        return "#004A9D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Beijing Subway</title>
     <path d="M10.729
 23.936c-2.182-.257-4.152-1.048-5.948-2.389-.586-.437-1.636-1.465-2.11-2.064-1.11-1.404-1.854-2.957-2.313-4.828-.303-1.232-.41-2.309-.335-3.35.069-.955.409-2.437.811-3.536.371-1.014
 1.151-2.382 1.864-3.269a15.51 15.51 0 0 1 1.55-1.593C6.625.878
 9.607-.14 12.69.026 15.358.17 17.738 1.1 19.738 2.78c1.904 1.6 3.36
 3.801 3.883
 5.869.067.263.113.486.104.495-.009.009-.636.022-1.392.03l-1.375.014-.132-.342c-.674-1.738-2.194-3.564-3.948-4.743-.806-.541-1.555-.874-2.296-1.021-2.136-.424-4.15-.276-5.829.428C6.21
 4.576 4.078 6.948 3.317 9.559c-.222.761-.274 1.185-.273 2.199.002
 1.29.139 2.128.549 3.365.497 1.499 1.083 2.438 2.198 3.525 1.249
 1.216 2.839 2.146 4.121 2.407 1.463.299 3.868.029 5.887-.662
 1.911-.654 3.511-2.086 4.6-4.116.21-.391.681-1.508.682-1.615
 0-.045-.076-.05-.437-.03-.241.014-1.02.025-1.731.025h-1.294l-.017.088c-.01.048-.047.245-.082.438-.103.558-.273
 1.029-.615 1.705l-.319.63-9.514.02V6.445h9.488l.203.316c.591.922.914
 2.116 1.049 3.885.022.288.04.713.04.944v.42H24v.247c0 .372-.105
 1.39-.195 1.887-.529 2.932-1.96 5.434-4.086 7.148-1.853 1.493-3.982
 2.387-6.306
 2.647-.648.072-2.063.07-2.684-.003zm3.64-8.802c.163-.171.404-.539.537-.82.112-.235.123-.295.123-.632
 0-.36-.006-.384-.164-.701-.091-.18-.26-.44-.378-.577l-.214-.25.125-.153c.238-.291.308-.401.459-.711.369-.76.232-1.527-.382-2.131l-.187-.184-2.305-.025-2.306-.026.01
 3.13.01 3.129 2.277.02c1.252.011 2.28.024
 2.285.029s.054-.039.11-.098z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://zh.wikipedia.org/wiki/File:Beijing_Su'''

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
