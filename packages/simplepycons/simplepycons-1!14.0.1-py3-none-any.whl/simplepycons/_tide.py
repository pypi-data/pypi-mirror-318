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


class TideIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tide"

    @property
    def original_file_name(self) -> "str":
        return "tide.svg"

    @property
    def title(self) -> "str":
        return "Tide"

    @property
    def primary_color(self) -> "str":
        return "#4050FB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tide</title>
     <path d="M18.694
 12.509h3.393c-.206-.846-.883-1.272-1.647-1.272-.883 0-1.5.48-1.746
 1.272zm1.746 4.48c-2.238 0-3.679-1.57-3.679-3.648 0-2.024 1.501-3.662
 3.693-3.662 2.211 0 3.546 1.532 3.546 3.569 0
 .273-.027.626-.027.672h-5.346c.206.886.87 1.465 1.853 1.465.844 0
 1.461-.366 1.853-.932l1.421.872c-.677 1.025-1.76 1.665-3.314
 1.665m-6.179-3.634a1.89 1.89 0 00-1.906-1.884c-1.036 0-1.84.846-1.84
 1.884 0 1.052.804 1.884 1.84 1.884 1.09 0 1.906-.832
 1.906-1.884zm-.026 2.956c-.492.386-1.256.613-2.046.613a3.546 3.546 0
 01-3.533-3.569c0-2.024 1.62-3.608 3.533-3.608.79 0 1.554.246
 2.046.626v-2.91h1.892v9.368h-1.892v-.52M7.796
 9.814H5.904v7.01h1.892v-7.01m-2.922 0v1.697H2.91v2.816c0
 .626.285.872.93.872H4.88v1.625H3.706c-1.853
 0-2.69-.832-2.69-2.404v-2.91H0V9.814a1.01 1.01 0
 001.01-1.012V8.01h1.892v1.804h1.972m3.124-1.657c0 .632-.511
 1.145-1.142 1.145-.63 0-1.142-.513-1.142-1.145 0-.633.511-1.145
 1.142-1.145a1.135 1.135 0 011.142 1.145Z" />
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
