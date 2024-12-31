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


class AllegroIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "allegro"

    @property
    def original_file_name(self) -> "str":
        return "allegro.svg"

    @property
    def title(self) -> "str":
        return "Allegro"

    @property
    def primary_color(self) -> "str":
        return "#FF5A00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Allegro</title>
     <path d="M4.59 7.981a.124.124 0 0 0-.122.124v5.917a.124.124 0 0 0
 .124.124h.72a.124.124 0 0 0 .124-.124h-.002V8.105a.124.124 0 0
 0-.124-.124Zm1.691 0a.124.124 0 0 0-.124.124v5.917a.124.124 0 0 0
 .124.124h.72a.124.124 0 0 0 .123-.124V8.105a.124.124 0 0
 0-.122-.124Zm12.667 1.776a1.868 1.868 0 0 0-1.317.532 1.674 1.674 0 0
 0-.531 1.254v2.48a.124.124 0 0 0 .123.123h.72a.124.124 0 0 0
 .124-.124v-2.427c0-.752.5-1.113 1.314-.946a.13.13 0 0 0
 .168-.142v-.495c0-.13-.014-.18-.1-.208a2.794 2.794 0 0
 0-.501-.047Zm-4.626 0a2.193 2.193 0 0 0-1.732.849 2.355 2.355 0 0 0 0
 2.678 2.13 2.131 0 0 0 1.732.849 2.21 2.21 0 0 0 1.234-.372v.53c0
 .717-.627.848-1.03.873a4.73 4.73 0 0 1-.826-.045c-.11-.017-.188
 0-.188.119v.636a.109.109 0 0 0 .114.103c.933.08 1.56.064
 2.032-.206a1.537 1.537 0 0 0 .69-.875 2.928 2.928 0 0 0
 .117-.874v-2.077h.002a2.245 2.245 0 0 0-.412-1.34 2.193 2.193 0 0
 0-1.733-.848Zm-12.255.002a2.903 2.903 0 0 0-1.465.39.092.092 0 0
 0-.045.08l.038.63a.112.112 0 0 0 .185.065c.627-.387 1.38-.459
 1.764-.265a.67.67 0 0 1 .335.605v.092H1.832c-.45 0-1.83.167-1.83
 1.434v.014a1.229 1.229 0 0 0 .45 1.017 1.768 1.768 0 0 0
 1.118.32h2.118a.124.124 0 0 0
 .124-.125v-2.51l-.002.004c0-.57-.127-1.004-.402-1.303-.274-.3-.827-.45-1.34-.45zm7.707
 0c-1.28 0-1.84.858-2.02 1.585a2.44 2.44 0 0 0-.074.6 2.277 2.277 0 0
 0 .412 1.338 2.198 2.198 0 0 0 1.733.85c.691.024 1.153-.093
 1.506-.294a.196.196 0 0 0
 .084-.212v-.558c0-.114-.069-.167-.167-.098a2.185 2.185 0 0
 1-1.393.334 1.14 1.14 0 0 1-1.118-1.016h2.845a.117.117 0 0 0
 .117-.116c.05-.778-.175-2.413-1.925-2.413Zm12.08 0a2.193 2.193 0 0
 0-1.731.848 2.275 2.275 0 0 0-.412 1.34 2.275 2.275 0 0 0 .412 1.339
 2.193 2.193 0 0 0 3.465 0 2.277 2.277 0 0 0 .412-1.34 2.277 2.277 0 0
 0-.412-1.339 2.193 2.193 0 0 0-1.733-.848Zm-7.532.833c1.157 0 1.196
 1.18 1.196 1.351 0 .171-.039 1.351-1.196 1.351-.517
 0-.89-.378-1.047-.849a1.552 1.552 0 0 1 0-1.004c.157-.47.53-.849
 1.047-.849zm-4.546.004a.86.86 0 0 1 .91.922H8.754a.968.968 0 0 1
 1.024-.922zm12.078 0c.515-.012.89.378 1.048.848a1.553 1.553 0 0 1 0
 1.003v.002c-.158.47-.531.837-1.048.848-.518.012-.89-.378-1.047-.848a1.552
 1.552 0 0 1 0-1.005c.158-.47.53-.837 1.047-.848zM1.89
 12.121h.99v1.246H1.63a.773.773 0 0 1-.444-.156.492.492 0 0
 1-.21-.412c0-.226.153-.678.914-.678z" />
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
