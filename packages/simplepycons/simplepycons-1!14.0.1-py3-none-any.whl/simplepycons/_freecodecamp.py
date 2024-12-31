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


class FreecodecampIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "freecodecamp"

    @property
    def original_file_name(self) -> "str":
        return "freecodecamp.svg"

    @property
    def title(self) -> "str":
        return "freeCodeCamp"

    @property
    def primary_color(self) -> "str":
        return "#0A0A23"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>freeCodeCamp</title>
     <path d="M19.885 3.906a.621.621 0
 00-.354.12c-.08.08-.161.196-.161.313 0 .2.236.474.673.923 1.822 1.754
 2.738 3.903 2.732 6.494-.007 2.867-.97 5.17-2.844
 6.954-.394.353-.556.63-.557.867 0
 .116.08.237.16.353.076.08.237.162.353.162.434 0 1.04-.512 1.833-1.509
 1.542-1.89 2.24-3.978
 2.279-6.824.036-2.847-.857-4.777-2.603-6.77-.63-.712-1.153-1.082-1.511-1.083zm-15.769.002c-.358
 0-.882.37-1.51 1.083C.858 6.984-.035 8.914.001 11.761c.04 2.846.737
 4.933 2.28 6.824.791.997 1.398 1.51 1.832 1.509a.573.573 0
 00.352-.162c.08-.116.16-.237.16-.353
 0-.237-.162-.514-.556-.866-1.873-1.785-2.837-4.087-2.844-6.955-.006-2.591.91-4.74
 2.732-6.494.437-.449.674-.722.673-.923
 0-.117-.08-.233-.161-.313a.621.621 0 00-.354-.12zm7.056.895s.655
 2.081-2.649 6.727c-3.156 4.433 1.045 7.15 1.432
 7.386-.281-.18-2.001-1.5.402-5.423.466-.77 1.076-1.47 1.834-3.041 0 0
 .67.946.32 2.998-.523 3.101 2.271 2.214 2.314 2.257.976 1.15-.808
 3.17-.917 3.233-.108.061 5.096-3.13 1.399-7.935-.253.253-.582
 1.442-1.267 1.266-.684-.174 2.125-3.494-2.868-7.468zM9.955
 18.916c.023.016.038.024.038.024l-.038-.024z" />
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
