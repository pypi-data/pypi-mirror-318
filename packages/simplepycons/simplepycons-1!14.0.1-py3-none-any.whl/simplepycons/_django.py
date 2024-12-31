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


class DjangoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "django"

    @property
    def original_file_name(self) -> "str":
        return "django.svg"

    @property
    def title(self) -> "str":
        return "Django"

    @property
    def primary_color(self) -> "str":
        return "#092E20"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Django</title>
     <path d="M11.146
 0h3.924v18.166c-2.013.382-3.491.535-5.096.535-4.791
 0-7.288-2.166-7.288-6.32 0-4.002 2.65-6.6 6.753-6.6.637 0 1.121.05
 1.707.203zm0 9.143a3.894 3.894 0 00-1.325-.204c-1.988 0-3.134
 1.223-3.134 3.365 0 2.09 1.096 3.236 3.109 3.236.433 0 .79-.025
 1.35-.102V9.142zM21.314 6.06v9.098c0 3.134-.229 4.638-.917 5.937-.637
 1.249-1.478 2.039-3.211 2.905l-3.644-1.733c1.733-.815 2.574-1.53
 3.109-2.625.561-1.121.739-2.421.739-5.835V6.059h3.924zM17.39.021h3.924v4.026H17.39z"
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
        return '''https://www.djangoproject.com/community/logos'''

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
