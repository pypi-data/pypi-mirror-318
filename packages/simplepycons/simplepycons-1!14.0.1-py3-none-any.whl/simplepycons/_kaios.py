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


class KaiosIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kaios"

    @property
    def original_file_name(self) -> "str":
        return "kaios.svg"

    @property
    def title(self) -> "str":
        return "KaiOS"

    @property
    def primary_color(self) -> "str":
        return "#6F02B5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>KaiOS</title>
     <path d="M17.3419.0001a3.6735 3.6735 0 0 0-3.647 3.6735 3.6727
 3.6727 0 0 0 3.6735 3.6734 3.6735 3.6735 0 1
 0-.0265-7.3469zM4.6233.16a2.7459 2.7459 0 0 0-2.7475
 2.7473v18.167a2.7474 2.7474 0 1 0 5.4942 0V2.9071A2.749 2.749 0 0 0
 4.6233.16zm6.9494 7.2078a2.729 2.729 0 0 0-2.237 4.2947l7.8107
 11.1541a2.729 2.729 0 1 0 4.4706-3.1307L13.8062 8.5311a2.729 2.729 0
 0 0-2.2335-1.1634z" />
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
