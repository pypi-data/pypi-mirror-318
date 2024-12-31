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


class ItchdotioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "itchdotio"

    @property
    def original_file_name(self) -> "str":
        return "itchdotio.svg"

    @property
    def title(self) -> "str":
        return "Itch.io"

    @property
    def primary_color(self) -> "str":
        return "#FA5C5C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Itch.io</title>
     <path d="M3.13 1.338C2.08 1.96.02 4.328 0 4.95v1.03c0 1.303 1.22
 2.45 2.325 2.45 1.33 0 2.436-1.102 2.436-2.41 0 1.308 1.07 2.41 2.4
 2.41 1.328 0 2.362-1.102 2.362-2.41 0 1.308 1.137 2.41 2.466
 2.41h.024c1.33 0 2.466-1.102 2.466-2.41 0 1.308 1.034 2.41 2.363 2.41
 1.33 0 2.4-1.102 2.4-2.41 0 1.308 1.106 2.41 2.435 2.41C22.78 8.43 24
 7.282 24
 5.98V4.95c-.02-.62-2.082-2.99-3.13-3.612-3.253-.114-5.508-.134-8.87-.133-3.362
 0-7.945.053-8.87.133zm6.376 6.477a2.74 2.74 0 0
 1-.468.602c-.5.49-1.19.795-1.947.795a2.786 2.786 0 0
 1-1.95-.795c-.182-.178-.32-.37-.446-.59-.127.222-.303.412-.486.59a2.788
 2.788 0 0 1-1.95.795c-.092 0-.187-.025-.264-.052-.107 1.113-.152
 2.176-.168 2.95v.005l-.006 1.167c.02 2.334-.23 7.564 1.03 8.85
 1.952.454 5.545.662 9.15.663 3.605 0 7.198-.21 9.15-.664 1.26-1.284
 1.01-6.514
 1.03-8.848l-.006-1.167v-.004c-.016-.775-.06-1.838-.168-2.95-.077.026-.172.052-.263.052a2.788
 2.788 0 0
 1-1.95-.795c-.184-.178-.36-.368-.486-.59-.127.22-.265.412-.447.59a2.786
 2.786 0 0 1-1.95.794c-.76 0-1.446-.303-1.948-.793a2.74 2.74 0 0
 1-.468-.602 2.738 2.738 0 0 1-.463.602 2.787 2.787 0 0
 1-1.95.794h-.16a2.787 2.787 0 0 1-1.95-.793 2.738 2.738 0 0
 1-.464-.602zm-2.004 2.59v.002c.795.002 1.5 0 2.373.953.687-.072
 1.406-.108 2.125-.107.72 0 1.438.035 2.125.107.873-.953 1.578-.95
 2.372-.953.376 0 1.876 0 2.92 2.934l1.123 4.028c.832 2.995-.266
 3.068-1.636
 3.07-2.03-.075-3.156-1.55-3.156-3.025-1.124.184-2.436.276-3.748.277-1.312
 0-2.624-.093-3.748-.277 0 1.475-1.125 2.95-3.156
 3.026-1.37-.004-2.468-.077-1.636-3.072l1.122-4.027c1.045-2.934
 2.545-2.934 2.92-2.934zM12 12.714c-.002.002-2.14 1.964-2.523
 2.662l1.4-.056v1.22c0 .056.56.033 1.123.007.562.026 1.124.05
 1.124-.008v-1.22l1.4.055C14.138 14.677 12 12.713 12 12.713z" />
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
