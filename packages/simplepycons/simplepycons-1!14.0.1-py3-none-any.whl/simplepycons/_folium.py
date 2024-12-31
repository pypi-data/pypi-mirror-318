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


class FoliumIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "folium"

    @property
    def original_file_name(self) -> "str":
        return "folium.svg"

    @property
    def title(self) -> "str":
        return "Folium"

    @property
    def primary_color(self) -> "str":
        return "#77B829"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Folium</title>
     <path d="M9.209
 17.302v.558h-.558v-.558h.558zm-1.116-.558v.558h.558v-.558h-.558zm1.116
 1.116v.558h.558v-.558h-.558zm-1.674-1.674v.558h.558v-.558h-.558zm2.232
 2.233v.558h.558v-.558h-.558zm.559-4.466v.558h.558v-.558h-.558zM9.767
 2.791v.558h.558v-.558h-.558zm.559 5.581v.558h.558v-.558h-.558zm0
 10.605v.558h.558v-.558h-.558zm-2.233-7.256v-.558h-.558v.558h.558zm1.116-4.465v-.558h-.558v.558h.558zm-.558-.558V6.14h-.558v.558h.558zm1.116
 1.116v-.558h-.558v.558h.558zM8.093 6.14v-.559h-.558v.559h.558zm1.116
 6.697v-.558h-.558v.558h.558zm1.117
 1.116v-.558h-.559v.558h.559zm-1.675-1.674v-.558h-.558v.558h.558zm1.116
 1.116v-.558h-.558v.558h.558zm.559-5.023v-.558h-.559v.558h.559zM6.977
 18.977v.558h.558v-.558h-.558zm1.116-15.07h-.558v.558h.558v-.558zm0
 16.186v.558h.558v-.558h-.558zm-.558-3.907v-.558h-.558v-4.465h.558v-.558h-.558V5.581h.558V4.465h-.558v.558h-.558v13.953h.558v-2.791h.558zm0
 3.349v.558h.558v-.558h-.558zm1.116 1.116v.558h.558v-.558h-.558zm1.675
 1.675v.558h.558v-.558h-.558zm-.559-.559v.558h.558v-.558h-.558zm-.558-.558v.558h.558v-.558h-.558zm1.117-19.535h-.559v.558h.558v-.558zm0
 1.675v.558h.558v-.558h-.558zm-.559-1.116h-.558v.558h.558v-.558zm1.117-1.117h-.558v.558h.558v-.558zM9.209
 2.791h-.558v.558h.558v-.558zm-.558.558h-.558v.558h.558v-.558zm5.023
 15.628h.558v-.558h-.558v.558zm.559-16.186h-.558v.558h.558v-.558zm0
 15.628h.558v-.559h-.558v.559zm-1.117
 1.116h.558v-.558h-.558v.558zm2.233-7.256h-.558v.558h.558v-.558zm.558
 4.465h.558v-.558h-.558v.558zm-1.116
 1.116h.558v-.558h-.558v.558zm.558-.558h.558v-.558h-.558v.558zm-1.675-3.349h-.558v.558h.558v-.558zm.559-.558h-.558v.558h.558v-.558zm.558-6.139h-.558v.558h.558v-.558zm.558-.558h-.558v.558h.558v-.558zm.558-.558h-.558v.558h.558V6.14zm-2.233-2.791h-.558v.558h.558v-.558zm1.117
 9.488h-.558v.558h.558v-.558zm1.116-1.116h-.558v.558h.558v-.558zm-1.674-3.907h-.558v.558h.558v-.558zm-.559.558h-.558v.558h.558v-.558zm-.558
 14.512h.558v-.558h-.558v.558zm1.675-1.675h.558v-.558h-.558v.558zm-.558.558h.558v-.558h-.558v.558zm1.674-10.046h.558v-.558h-.558v.558zm-.558
 8.93h.558v-.558h-.558v.558zm.558-.558h.558v-.558h-.558v.558zm1.116-15.07v-.558h-.558v1.116h.558v5.023h-.558v.558h.558v4.465h-.558v.558h.558v2.791h.558V5.023h-.558zm-.558
 14.512h.558v-.558h-.558v.558zm-2.791
 2.791h.558v-.558h-.558v.558zm2.791-17.861v-.558h-.558v.558h.558zm-.558-.558v-.558h-.558v.558h.558zm-.558-.558v-.558h-.558v.558h.558zm.558
 2.791h.558v-.559h-.558v.559zm-2.233-4.466v-.558h-.558v.558h.558zm1.117
 1.117v-.558h-.558v.558h.558zm-2.233
 17.302h.558v-.558h-.558V15.07h.558v-.558h-.558V9.488h.558V8.93h-.558V4.465h.558v-.558h-.558V1.116h.558V.558h-.558V0h-1.116v.558h-.558v.558h.558v2.791h-.558v.558h.558V8.93h-.558v.558h.558v5.023h-.558v.558h.558v4.465h-.558v.558h.558v2.791h-.558v.558h.558V24h1.116v-.558h.558v-.558h-.558v-2.791zm1.675-17.86v-.559h-.558v.558h.558z"
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
        return '''https://python-visualization.github.io/folium'''

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
