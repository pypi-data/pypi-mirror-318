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


class LeptosIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "leptos"

    @property
    def original_file_name(self) -> "str":
        return "leptos.svg"

    @property
    def title(self) -> "str":
        return "Leptos"

    @property
    def primary_color(self) -> "str":
        return "#EF3939"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Leptos</title>
     <path d="M10.097 17.876A6.207 6.207 0 0 1 5.834 12c0-3.393
 2.773-6.166 6.166-6.166.248 0 .517.021.766.042a9.896 9.896 0 0 1
 1.49-2.504 3.575 3.575 0 0
 1-.85-2.296c0-.331.042-.662.146-.993A19.487 19.487 0 0 0 12 0C5.38 0
 0 5.38 0 12c0 4.366 2.338 8.172 5.814 10.283l.124-.062a8.434 8.434 0
 0 0 4.159-4.345Zm6.848-14.979c.662 0 1.262-.352 1.593-.952v-.02a12.32
 12.32 0 0 0-3.269-1.49v.02a1.851 1.851 0 0 0-.124.642c0 .993.807 1.8
 1.8 1.8ZM19.924 3c-.662 1.014-1.758 1.634-2.98 1.634a3.54 3.54 0 0
 1-.806-.103 3.153 3.153 0 0 1-.476-.145 8.75 8.75 0 0 0-1.22
 1.945c2.275.993 3.724 3.186 3.724 5.669 0 3.393-2.773 6.166-6.166
 6.166h-.145a10.374 10.374 0 0 1-4.117 5.048C9.062 23.71 10.51 24 12
 24c6.62 0 12-5.38 12-12 0-3.58-1.572-6.807-4.076-9Zm-8.848 4.67a4.428
 4.428 0 1 0 1.849 8.661 4.428 4.428 0 1 0-1.85-8.66z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/leptos-rs/leptos/blob/6fac'''

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
