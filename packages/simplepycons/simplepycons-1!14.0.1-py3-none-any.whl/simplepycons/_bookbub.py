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


class BookbubIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bookbub"

    @property
    def original_file_name(self) -> "str":
        return "bookbub.svg"

    @property
    def title(self) -> "str":
        return "BookBub"

    @property
    def primary_color(self) -> "str":
        return "#F44336"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>BookBub</title>
     <path d="M0 20V4h5.4c1.6 0 2.8.3 3.8 1 .9.7 1.4 1.6 1.4 2.7 0
 .8-.3 1.6-.8 2.3-.6.7-1.3 1.2-2.2 1.4 1.1.1 2 .6 2.7 1.3.7.7 1 1.6 1
 2.6 0 1.4-.5 2.6-1.5 3.4-1 .9-2.4 1.3-4.1 1.3H0zM3 6.4v4.2h1.7c.8 0
 1.5-.2 1.9-.6.4-.4.7-1 .7-1.7 0-1.3-.9-1.9-2.7-1.9H3zM3 13v4.7h2.1c.9
 0 1.6-.2 2.1-.6.5-.5.8-1.1.8-1.9C8 13.7 7 13 5 13H3zm9.7 7V4h5.4c1.6
 0 2.8.3 3.8 1 .9.7 1.4 1.6 1.4 2.7 0 .8-.3 1.6-.8 2.3-.6.7-1.3
 1.2-2.2 1.4 1.1.1 2 .6 2.7 1.3.7.7 1 1.6 1 2.6 0 1.4-.5 2.6-1.5 3.4-1
 .9-2.4 1.3-4.1 1.3h-5.7zm3-13.6v4.2h1.7c.8 0 1.5-.2 1.9-.6s.7-1
 .7-1.7c0-1.3-.9-1.9-2.7-1.9h-1.6zm0 6.6v4.7h2.1c.9 0 1.6-.2
 2.1-.6.5-.4.7-1 .7-1.8 0-1.5-1-2.3-3-2.3h-1.9z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://insights.bookbub.com/bookbub-follow-b'''

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
