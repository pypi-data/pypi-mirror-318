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


class TubiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tubi"

    @property
    def original_file_name(self) -> "str":
        return "tubi.svg"

    @property
    def title(self) -> "str":
        return "Tubi"

    @property
    def primary_color(self) -> "str":
        return "#7408FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tubi</title>
     <path d="M16.696 15.272v-.752c.4.548 1.107.917 1.934.917 1.475 0
 2.28-.956 2.28-2.865 0-1.714-.893-2.858-2.235-2.858-.851
 0-1.55.347-1.979.908v-2.06h-2.674v6.71zm1.57-2.614c0 .827-.337
 1.275-.827 1.275-.486 0-.837-.452-.837-1.275s.342-1.28.837-1.28c.495
 0 .828.452.828 1.28zM6.94 9.988v3.6c0 1.236.754 1.841 1.955 1.841.959
 0 1.625-.396 2.028-1.064v.91h2.597V9.989h-2.675v3.14c0
 .493-.346.693-.666.693-.321 0-.568-.192-.568-.655V9.989Zm14.39
 0H24v5.276h-2.67ZM6.553 11.136c0 .781-.635 1.415-1.42 1.415-.783
 0-1.419-.634-1.419-1.415 0-.782.636-1.415 1.42-1.415.784 0 1.42.633
 1.42 1.415zM3.49 9.702v2.668c.005.653.327.924.976.924.225 0
 .526-.053.672-.166v1.931c-.49.243-.869.378-1.535.378 0 0-.069
 0-.18-.006l-.003.006c-1.614
 0-2.51-1.035-2.482-2.686v-.47H0V9.99h.92V8.563h2.569Z" />
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
