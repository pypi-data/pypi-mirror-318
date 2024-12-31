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


class TheIrishTimesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "theirishtimes"

    @property
    def original_file_name(self) -> "str":
        return "theirishtimes.svg"

    @property
    def title(self) -> "str":
        return "The Irish Times"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>The Irish Times</title>
     <path d="M9.636 4.093V8.33h.42c.18-1.156.614-2.047
 1.3-2.67.487-.448 1.27-.672 2.35-.672h1.197V17.22c0 .79-.043
 1.28-.127
 1.465-.116.263-.272.45-.473.557-.277.165-.642.246-1.096.246h-.518v.417h8.26v-.417h-.517c-.443
 0-.793-.077-1.049-.228-.256-.15-.428-.327-.516-.528-.088-.203-.131-.706-.131-1.512V4.988h1.197c.743
 0 1.264.07 1.56.208.532.254.95.595 1.256 1.023.305.427.584 1.13.834
 2.11H24V4.093zM7.74 19.488c-.438
 0-.787-.076-1.044-.227-.259-.15-.43-.328-.519-.529-.088-.202-.132-.705-.132-1.512V6.778c0-.79.041-1.278.127-1.464.114-.264.272-.45.472-.559.277-.162.641-.244
 1.096-.244h.519v-.418H0v.418h.521c.441 0 .79.076
 1.05.227.258.15.43.329.515.53.085.2.129.705.129 1.51v10.444c0
 .79-.044 1.279-.128
 1.465-.109.263-.264.45-.463.557-.28.164-.647.245-1.103.245H0v.418h8.26v-.418h-.52Z"
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
