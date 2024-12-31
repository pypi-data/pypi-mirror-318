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


class UnicodeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "unicode"

    @property
    def original_file_name(self) -> "str":
        return "unicode.svg"

    @property
    def title(self) -> "str":
        return "Unicode"

    @property
    def primary_color(self) -> "str":
        return "#5455FE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Unicode</title>
     <path d="M.2 0a.2.2 0 00-.2.2v23.6c0 .11.09.2.2.2h23.6a.2.2 0
 00.2-.2V.2a.2.2 0 00-.2-.2H.2zm19.488 5.27A1.312 1.312 0 0121
 6.582a1.312 1.312 0 01-1.313 1.313 1.312 1.312 0 01-1.31-1.313 1.312
 1.312 0 011.31-1.312zM3.15 6.05h1.996c.102 0 .153.05.153.151v7.49c0
 .912.222 1.644.666 2.188.444.546 1.121.816 2.033.816.38 0 .729-.048
 1.047-.15.316-.102.59-.272.824-.506.234-.236.419-.546.553-.932.134-.386.2-.869.2-1.453V6.223c0-.014.003-.024.005-.035l-.006-.004c0-.09.045-.133.133-.133h2.682c.076
 0 .126.01.152.027.026.018.05.054.076.104.228.418.499.906.809
 1.464.31.558.629 1.14.959 1.749l.998 1.843c.334.62.647 1.206.94
 1.758.291.552.549 1.045.77 1.475.223.432.39.768.505
 1.008h.02c0-.126-.005-.27-.01-.428a25.728 25.728 0
 01-.02-.57c-.006-.223-.014-.493-.02-.81-.008-.315-.01-.696-.01-1.14v-3.21c0-.103.056-.153.17-.153H20.6c.114
 0 .171.058.171.172v9.03c0 .113-.063.17-.189.17h-2.414c-.114
 0-.198-.046-.248-.134a173.907 173.907 0 00-1.623-3.021 232.322
 232.322 0 01-2.121-3.946 96.063 96.063 0 01-.883-1.718 37.59 37.59 0
 01-.371-.768v4.815c0 .888-.13 1.643-.39 2.271-.26.628-.611
 1.141-1.055 1.541a4.112 4.112 0 01-1.588.873 6.848 6.848 0
 01-1.97.277 6.42 6.42 0 01-2.032-.304 4.196 4.196 0
 01-1.559-.903c-.43-.4-.76-.903-.988-1.511-.228-.608-.342-1.325-.342-2.149v-7.64c0-.114.05-.172.152-.172Z"
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
        return '''https://commons.wikimedia.org/wiki/File:New_U'''

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
