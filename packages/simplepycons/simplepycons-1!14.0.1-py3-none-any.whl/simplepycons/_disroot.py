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


class DisrootIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "disroot"

    @property
    def original_file_name(self) -> "str":
        return "disroot.svg"

    @property
    def title(self) -> "str":
        return "Disroot"

    @property
    def primary_color(self) -> "str":
        return "#50162D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Disroot</title>
     <path d="M3.976 2.856C2.321 3.296.603 4.491.122
 5.536c-.144.315-.164.885-.04 1.133.178.35.343.384 1.387.24.817-.11
 1.085-.117 1.985-.055 1.106.076 1.594.213 1.882.522.172.179 3.75
 9.033 3.813 9.418.11.694-.234 1.312-1.189
 2.143-.797.687-.927.907-.824 1.381.151.666.508.982 1.113.982.508 0
 2.095-.268 3.297-.55 3.476-.817 6.437-1.923 8.504-3.173 1.944-1.168
 3.25-2.555 3.765-3.984.15-.433.178-.618.185-1.326
 0-.975-.11-1.38-.536-1.958-.858-1.16-1.8-2.005-3.338-2.988-2.96-1.902-3.778-2.294-6.67-3.215-2.521-.803-5.358-1.318-7.728-1.394-1.017-.027-1.147-.02-1.752.144zm9.411
 6.526c1.477.563 2.823 1.47 4.554 3.07.838.777 1.024 1.072 1.058
 1.732.076 1.23-.597 2.033-2.088
 2.507-.708.22-2.191.536-2.253.474-.02-.014
 0-.13.041-.254.048-.13.062-.447.048-.749-.027-.433-.096-.68-.364-1.319-.179-.433-.708-1.91-1.175-3.283l-.851-2.5.22.047c.123.028.487.151.81.275z"
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
