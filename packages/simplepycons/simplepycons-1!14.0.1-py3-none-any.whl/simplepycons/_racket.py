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


class RacketIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "racket"

    @property
    def original_file_name(self) -> "str":
        return "racket.svg"

    @property
    def title(self) -> "str":
        return "Racket"

    @property
    def primary_color(self) -> "str":
        return "#9F1D20"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Racket</title>
     <path d="M12 0a11.95 11.95 0 0 0-4.104.721c4.872 2.556 11.316
 10.893 13.547 18.686A11.957 11.957 0 0 0 24
 12c0-6.627-5.373-12-12-12zM4.093 2.974A11.971 11.971 0 0 0 0 12c0
 3.026 1.12 5.789 2.968 7.9 1.629-4.894 4.691-9.611
 7.313-12.246-1.872-2.016-3.968-3.618-6.188-4.68zm2.276 19.625A11.947
 11.947 0 0 0 12 24c2.092 0 4.059-.536
 5.772-1.478-.987-4.561-2.851-8.739-5.28-12.147-2.597 2.8-5.186
 7.702-6.123 12.224z" />
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
