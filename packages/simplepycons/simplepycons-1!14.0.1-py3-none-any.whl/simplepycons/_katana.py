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


class KatanaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "katana"

    @property
    def original_file_name(self) -> "str":
        return "katana.svg"

    @property
    def title(self) -> "str":
        return "Katana"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Katana</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0zm.016
 22.762H12c-5.95-.009-10.765-4.84-10.756-10.789.009-5.95 4.839-10.766
 10.789-10.757 5.943.009 10.756 4.829 10.756 10.773 0 5.95-4.823
 10.773-10.773 10.773zm9.475-10.857a5.562 5.562 0 0 1-9.142 3.214
 6.331 6.331 0 0 0 3.251-2.062l.104.169c.339.584.568 1.226.676
 1.893a6.281 6.281 0 0 0-.349-2.656 6.328 6.328 0 0 0-8.94-8.63 5.563
 5.563 0 0 1 7.418 6.256 6.334 6.334 0 0 0-3.425-1.762l.093-.175a5.53
 5.53 0 0 1 1.304-1.533 6.31 6.31 0 0 0-2.122 1.636 6.327 6.327 0 0
 0-3.016 12.044 5.564 5.564 0 0 1 1.713-9.562 6.33 6.33 0 0 0 .185
 3.818h-.186a5.535 5.535 0 0 1-1.98-.36 6.295 6.295 0 0 0 2.471 1.025
 6.328 6.328 0 0 0 8.513 2.758 6.319 6.319 0 0 0
 3.432-6.073zm-11.018-1.443a5.582 5.582 0 0 1 3.6.998 5.584 5.584 0 0
 1-2.667 2.618 5.57 5.57 0 0 1-.933-3.616z" />
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
