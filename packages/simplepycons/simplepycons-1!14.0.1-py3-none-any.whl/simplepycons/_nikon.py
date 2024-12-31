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


class NikonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nikon"

    @property
    def original_file_name(self) -> "str":
        return "nikon.svg"

    @property
    def title(self) -> "str":
        return "Nikon"

    @property
    def primary_color(self) -> "str":
        return "#FFE100"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nikon</title>
     <path d="M8.267 8.681c-.69 0-1.054.463-1.054.873 0
 .144.032.653.949.653.762 0 1.057-.488 1.057-.854
 0-.244-.2-.672-.952-.672zm-6.87.215L0 15.146h1.72c.194-1
 .455-2.056.711-3.138l1.206 3.136H5.27L6.681 8.9H5l-.715
 3.176-1.18-3.18Zm8.587.004L8.6 15.144h1.663l.558-2.375.703
 2.375h1.705l-.707-2.508 1.715-2.08h-1.91l-1.38 1.664.743-3.32zm6.608
 1.465c-2.582 0-2.962 2.01-3.034 2.379-.19.93.02 2.137 1.235
 2.457.8.21 2.051.187 2.855-.47.736-.6 1.1-1.619
 1.088-2.575-.012-.92-.79-1.791-2.144-1.791zm6.193.072c-.573.038-1.156.35-1.486.807.044-.188.088-.404.14-.658h-1.7l-.999
 4.558h1.695l.563-2.586c.104-.476.488-.68.826-.591.146.04.35.15.281.548l-.574
 2.63h1.674l.767-3.51a.96.96 0 0 0-.627-1.14 1.594 1.594 0 0
 0-.56-.058zm-15.66.121-1.02 4.586h1.676l1.022-4.586zm9.23
 1.104c.372-.002.472.218.44.426-.09.545-.245 1.081-.362
 1.539-.082.254-.321.4-.601.4-.286
 0-.458-.178-.432-.406.04-.384.286-1.357.356-1.549.12-.334.451-.408.6-.41z"
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
