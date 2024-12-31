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


class BasecampIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "basecamp"

    @property
    def original_file_name(self) -> "str":
        return "basecamp.svg"

    @property
    def title(self) -> "str":
        return "Basecamp"

    @property
    def primary_color(self) -> "str":
        return "#1D2D35"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Basecamp</title>
     <path d="M12.6516 22.453c-4.0328
 0-7.575-1.5542-10.244-4.4946a1.11 1.11 0 0 1-.219-1.1338c.7008-1.8884
 2.5935-6.2808 5.0205-6.2948h.0125c1.219 0 2.1312.9655 2.8648
 1.7412.2192.2324.555.5875.7818.7611.5656-.5587 1.6775-2.4158
 2.5422-4.2779.259-.5567.9203-.7985
 1.4765-.5402.557.2584.7988.919.5404 1.4762-2.6217 5.6503-4.019
 5.6503-4.478 5.6503-1.022
 0-1.7628-.7843-2.4791-1.5422-.3208-.339-.9878-1.045-1.2482-1.045h-.0004c-.5665.095-1.8085
 2.0531-2.6966 4.2034 2.1925 2.1722 4.9232 3.2726 8.1266 3.2726 4.3955
 0 7.683-1.1964
 9.0996-3.2953-.4888-5.585-3.5642-13.1634-9.0996-13.1634-4.6855
 0-8.2152 3.264-10.4915
 9.7007-.205.579-.8416.8828-1.4187.6776-.5789-.2047-.882-.8398-.6776-1.4185
 2.624-7.421 6.859-11.1833 12.5878-11.1833 7.4826 0 10.9304 9.5613
 11.3458 15.588a1.1154 1.1154 0 0 1-.1456.6314c-1.7407 3.0221-5.7182
 4.6864-11.2002 4.6864Z" />
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
