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


class MercedesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mercedes"

    @property
    def original_file_name(self) -> "str":
        return "mercedes.svg"

    @property
    def title(self) -> "str":
        return "Mercedes"

    @property
    def primary_color(self) -> "str":
        return "#242424"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mercedes</title>
     <path d="M12 0c6.623 0 12 5.377 12 12s-5.377 12-12 12S0 18.623 0
 12 5.377 0 12 0zM3.245 17.539A10.357 10.357 0 0012 22.36c3.681 0
 6.917-1.924 8.755-4.821L12 14.203zm10.663-6.641l7.267 5.915A10.306
 10.306 0 0022.36
 12c0-5.577-4.417-10.131-9.94-10.352zm-2.328-9.25C6.057 1.869 1.64
 6.423 1.64 12c0 1.737.428 3.374 1.185 4.813l7.267-5.915z" />
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
