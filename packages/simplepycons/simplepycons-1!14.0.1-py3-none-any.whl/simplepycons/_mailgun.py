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


class MailgunIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mailgun"

    @property
    def original_file_name(self) -> "str":
        return "mailgun.svg"

    @property
    def title(self) -> "str":
        return "Mailgun"

    @property
    def primary_color(self) -> "str":
        return "#F06B66"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mailgun</title>
     <path d="M11.837 0c6.602 0 11.984 5.381 11.984 11.994-.017
 2.99-3.264 4.84-5.844 3.331a3.805 3.805 0 0
 1-.06-.035l-.055-.033-.022.055c-2.554 4.63-9.162
 4.758-11.894.232-2.732-4.527.46-10.313 5.746-10.416a6.868 6.868 0 0 1
 7.002 6.866 1.265 1.265 0 0 0 2.52
 0c0-5.18-4.197-9.38-9.377-9.387C4.611 2.594.081 10.41 3.683
 16.673c3.238 5.632 11.08 6.351 15.289 1.402l1.997 1.686A11.95 11.95 0
 0 1 11.837 24C2.6 23.72-2.87 13.543 1.992 5.684A12.006 12.006 0 0 1
 11.837 0Zm0 7.745c-3.276-.163-5.5 3.281-4.003 6.2a4.26 4.26 0 0 0
 4.014 2.31c3.276-.171 5.137-3.824 3.35-6.575a4.26 4.26 0 0
 0-3.36-1.935Zm0 2.53c1.324 0 2.152 1.433 1.49 2.58a1.72 1.72 0 0
 1-1.49.86 1.72 1.72 0 1 1 0-3.44Z" />
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
