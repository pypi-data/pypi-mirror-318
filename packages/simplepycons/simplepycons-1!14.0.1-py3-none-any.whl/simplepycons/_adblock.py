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


class AdblockIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "adblock"

    @property
    def original_file_name(self) -> "str":
        return "adblock.svg"

    @property
    def title(self) -> "str":
        return "AdBlock"

    @property
    def primary_color(self) -> "str":
        return "#F40D12"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AdBlock</title>
     <path d="M7.775 0a1.8 1.8 0 0 0-1.273.527L.528 6.503A1.8 1.8 0 0
 0 0 7.775v8.45c0 .478.19.936.528 1.274l5.974 5.974A1.8 1.8 0 0 0
 7.775 24h8.45a1.8 1.8 0 0 0 1.273-.527l5.975-5.974A1.8 1.8 0 0 0 24
 16.225v-8.45a1.8 1.8 0 0 0-.527-1.272L17.498.527A1.8 1.8 0 0 0 16.225
 0zm4.427 3c1.02 0 .958 1.108.958 1.108v6.784s-.009.218.16.218c.188 0
 .175-.226.175-.226l-.002-5.63s-.05-.986.959-.986c1.01 0
 .97.983.97.983v7.621s.014.158.141.158c.127 0
 .944-2.122.944-2.122s.451-1.497
 2.576-1.1c.038.008-.167.688-.167.688l-2.283 6.556S15.69 20.7 11.714
 20.7c-5.044 0-4.808-5.407-4.814-5.405V7.562s-.016-.99.897-.99c.858 0
 .849.99.849.99l.007 3.583s-.004.172.167.172c.16 0
 .141-.172.141-.172l.01-5.926s-.055-1.162.966-1.162c1.04 0 .983
 1.142.983 1.142v5.611s-.005.204.152.204c.168 0
 .154-.206.154-.206l.01-6.693S11.18 3 12.202 3Z" />
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
