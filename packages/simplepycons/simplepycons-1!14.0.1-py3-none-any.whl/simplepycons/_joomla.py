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


class JoomlaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "joomla"

    @property
    def original_file_name(self) -> "str":
        return "joomla.svg"

    @property
    def title(self) -> "str":
        return "Joomla"

    @property
    def primary_color(self) -> "str":
        return "#5091CD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Joomla</title>
     <path d="M16.719 14.759L14.22 17.26l-2.37 2.37-.462.466c-1.368
 1.365-3.297 1.83-5.047 1.397-.327 1.424-1.604 2.49-3.13 2.49C1.438
 23.983 0 22.547 0 20.772c0-1.518 1.055-2.789
 2.469-3.123-.446-1.76.016-3.705 1.396-5.08l.179-.18 2.37
 2.37-.184.181c-.769.779-.769 2.024 0 2.789.771.78 2.022.78 2.787
 0l.465-.465 2.367-2.371 2.502-2.506 2.368 2.372zm.924
 6.652c-1.822.563-3.885.12-5.328-1.318l-.18-.185
 2.365-2.369.18.184c.771.768 2.018.768 2.787 0
 .765-.765.769-2.01-.004-2.781l-.466-.465-2.365-2.37-2.502-2.503
 2.37-2.369 2.499 2.505 2.367 2.37.464.464c1.365 1.36 1.846 3.278
 1.411 5.021 1.56.224 2.759 1.56 2.759 3.18 0 1.784-1.439 3.21-3.209
 3.21-1.545 0-2.851-1.096-3.135-2.565l-.013-.009zM6.975
 9.461l2.508-2.505 2.37-2.369.462-.461C13.74 2.7 15.772 2.251 17.58
 2.79c.212-1.561 1.555-2.775 3.179-2.775 1.772 0 3.211 1.437 3.211
 3.209 0 1.631-1.216 2.978-2.79 3.186.519 1.799.068 3.816-1.35
 5.234l-.182.184-2.369-2.369.184-.184c.769-.77.769-2.016
 0-2.783-.766-.766-2.011-.768-2.781.003l-.462.461-2.37 2.369-2.505
 2.502-2.37-2.366zm-2.653 2.647l-.461-.462C2.43 10.215 1.986 8.17
 2.529 6.358 1.1 6.029.03 4.754.03 3.224.03 1.454 1.47.015
 3.24.015c1.596 0 2.92 1.166 3.17 2.691 1.73-.405 3.626.065 4.979
 1.415l.184.185-2.37 2.37-.183-.181c-.77-.765-2.016-.765-2.785
 0-.771.781-.77 2.025-.005 2.79l.465.466 2.37 2.369 2.505 2.505-2.367
 2.37-2.51-2.505-2.371-2.37v-.012z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://docs.joomla.org/Joomla:Brand_Identity'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://docs.joomla.org/Joomla:Brand_Identity'''

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
