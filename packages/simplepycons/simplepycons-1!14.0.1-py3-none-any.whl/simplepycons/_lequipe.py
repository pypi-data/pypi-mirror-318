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


class LequipeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lequipe"

    @property
    def original_file_name(self) -> "str":
        return "lequipe.svg"

    @property
    def title(self) -> "str":
        return "L'Équipe"

    @property
    def primary_color(self) -> "str":
        return "#E42829"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>L'Équipe</title>
     <path d="m6.109 9.885-.132.301H5l-.258.612h.399l-1.32
 3.092h2.398l.265-.611H5.312l.454-1.051h1.172l.234-.557H6.008l.375-.866h1.164l.258-.611H6.711l.133-.309h-.735Zm3.575.27c-1.223.008-1.74.891-2.024
 1.492-.811 1.722.479 2.232.773 2.285.168.031.505.031.674
 0l.107.183h.635l-.215-.328c.475-.03 1.034-.678
 1.278-1.195.245-.518.962-2.397-1.228-2.437Zm11.449.012-.269.63h.437l-1.317
 3.077h2.422l.242-.551h-1.234l.461-1.078h1.235l.242-.567h-1.235l.383-.885h1.226l.274-.626h-2.867Zm-17.828.004-.27.625h.415c-.087.211-.192.477-.34.805.828-.195
 1.249-.844 1.359-1.43H3.305Zm-2.109.001-.266.619h.398L0
 13.89h2.445l.258-.603H1.539l1.336-3.115H1.196Zm10.749.009-.266.61h.415l-.766
 1.804c-.312.682.141 1.31 1.149 1.318 1.038.009 1.39-.636
 1.5-.904l1.203-2.828h-.664l-1.203
 2.798c-.211.413-1.149.376-.883-.153l1.133-2.645h-1.618Zm5.688.008-.27.603h.426l-1.313
 3.098h1.212l.546-1.29h1.203c.571 0 .974-.562
 1.164-1.051.196-.502.063-1.36-.718-1.36h-2.25Zm-2.031.001-.258.605h.351l-1.32
 3.103h1.211l1.601-3.708h-1.585Zm-5.918.555c.279-.012.553.172.448.431l-.842
 1.972-.191-.312-.467.259.115.175c-.406
 0-.336-.335-.237-.525l.734-1.715a.487.487 0 0 1
 .44-.285Zm9.308.047h.36c.304 0
 .124.61.07.719-.055.108-.211.471-.446.471h-.5l.516-1.19Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:L_Equ'''

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
