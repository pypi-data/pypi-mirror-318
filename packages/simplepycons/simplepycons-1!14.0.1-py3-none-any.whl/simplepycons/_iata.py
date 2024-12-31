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


class IataIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "iata"

    @property
    def original_file_name(self) -> "str":
        return "iata.svg"

    @property
    def title(self) -> "str":
        return "Iata"

    @property
    def primary_color(self) -> "str":
        return "#004E81"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Iata</title>
     <path d="M3.417 19.695l.98-4.885H5.99l-.973
 4.884zm4.808-1.6h1.012l-.26-1.792zm-2.235 1.6l2.412-4.885h1.57l.99
 4.884H9.487l-.088-.58H7.827l-.25.58zm6.439
 0l.547-3.674h-1.394l.238-1.233h4.28l-.237 1.233h-1.327L14
 19.695zm5.354-1.6h1.012l-.26-1.792zm-2.23 1.6l2.407-4.885h1.57l.99
 4.884h-1.487l-.073-.58h-1.57l-.25.58zM24 9.289h-7.495c-.276
 1.372-1.228 2.517-3.125 3.308.215.652.95 1.255 1.714 1.255h4.066c.62
 0 1.112-.52 1.31-.94h-4.13c-.254-.044-.265-.25-.01-.271h4.06c.524 0
 1-.448 1.276-.935h-4.73c-.237-.04-.237-.238 0-.277h4.77c.48 0
 .918-.558 1.1-.934h-5.232c-.26-.033-.26-.277 0-.282H22.9c.415 0
 .819-.454 1.1-.924zm-24 0h7.495c.27 1.372 1.228 2.517 3.12
 3.308-.216.652-.952 1.255-1.715 1.255H4.84c-.62
 0-1.112-.52-1.311-.94h4.13c.25-.044.266-.25.01-.271H3.608c-.525
 0-1-.448-1.272-.935H7.07c.238-.04.238-.238 0-.277H2.3c-.481
 0-.918-.558-1.1-.934h5.232c.26-.033.26-.277 0-.282H1.106c-.42
 0-.824-.454-1.106-.924zm9.569-4.114c.277.238.586.448.918.58.282-.553.675-1.028
 1.129-1.45a4.05 4.05 0 0 0-2.047.87zM8.242 7.902h1.67a5.358 5.358 0 0
 1 .454-1.91 4.021 4.021 0 0 1-1.002-.63 3.83 3.83 0 0 0-1.122
 2.54zm3.628-1.567V7.9H10.2a4.62 4.62 0 0 1 .414-1.815c.399.143.83.237
 1.256.25zm2.56-1.161a3.346 3.346 0 0 1-.917.58 5.243 5.243 0 0
 0-1.134-1.443 3.993 3.993 0 0 1 2.052.863zM15.754 7.9h-1.665a5.096
 5.096 0 0 0-.442-1.91c.354-.165.69-.375.984-.63a3.723 3.723 0 0 1
 1.123 2.54zM12.14 6.335V7.9h1.66c0-.631-.155-1.234-.415-1.815a4.017
 4.017 0 0 1-1.245.25zm-2.571
 4.57c.277-.216.597-.454.918-.57.299.559.67 1.018 1.129 1.433a4.05
 4.05 0 0 1-2.047-.863zM8.242 8.173h1.67c.039.69.182 1.3.454
 1.924a4.202 4.202 0 0 0-1.002.625 3.864 3.864 0 0 1-1.122-2.55zm3.628
 1.57v-1.57H10.2c.01.63.154 1.255.414 1.814.399-.144.83-.232
 1.256-.244zm2.56 1.162a3.41 3.41 0 0 0-.917-.57 5.113 5.113 0 0
 1-1.134 1.433 4.088 4.088 0 0 0 2.052-.863zm1.323-2.732h-1.665a5.075
 5.075 0 0 1-.442 1.924c.354.166.674.366.984.625a3.806 3.806 0 0 0
 1.123-2.55zm-3.612 1.57v-1.57h1.66c0 .63-.155 1.244-.415 1.814a4.01
 4.01 0 0 0-1.245-.244zm-.271-5.276a4.387 4.387 0 0 0-1.123
 1.382c.36.122.74.222 1.123.222zm.27 0c.444.365.847.846 1.113
 1.382a3.26 3.26 0 0 1-1.112.222zm-.27 7.146a4.23 4.23 0 0
 1-1.123-1.388c.36-.128.74-.2 1.123-.2zm.27.01c.444-.37.847-.867
 1.113-1.4a3.715 3.715 0 0 0-1.112-.197z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:IATAl'''

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
