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


class AviraIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "avira"

    @property
    def original_file_name(self) -> "str":
        return "avira.svg"

    @property
    def title(self) -> "str":
        return "Avira"

    @property
    def primary_color(self) -> "str":
        return "#E02027"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Avira</title>
     <path d="M24 23.414a.586.586 0 0 1-.586.587H.585A.586.586 0 0 1 0
 23.414V.586c0-.324.262-.587.585-.587h22.829c.325 0
 .586.263.586.587v22.828Zm-4.971-9.675-.04-.044-1.323 1.256a.925.925 0
 0 1-1.342 1.272 1.234 1.234 0 0 1-.118-.122l-3.56-3.753
 4.857-4.609c-3.034-2.858-7.795-2.984-10.765-.111-2.969 2.874-3.337
 7.527-.539 10.838l5.106-4.845 3.748 3.952a2.777 2.777 0 0 0 1.995.74
 2.681 2.681 0 0 0 1.772-.742c.559-.526.894-1.272.887-2.022a2.702
 2.702 0 0 0-.678-1.81Zm-4.573-5.55-7.65 7.259c-2.576-4.553
 2.815-10.009 7.65-7.259Z" />
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
