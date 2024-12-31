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


class NbbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nbb"

    @property
    def original_file_name(self) -> "str":
        return "nbb.svg"

    @property
    def title(self) -> "str":
        return "NBB"

    @property
    def primary_color(self) -> "str":
        return "#FF7100"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NBB</title>
     <path d="M2.714 11.176h.02l.167 4.327h2.105L6.5 8.482H4.652l-.915
 4.288h-.02L3.63 8.482H1.495L0
 15.503h1.79zm7.254.649l.01-.02c.462-.098 1.219-.481
 1.453-1.583.248-1.16-.362-1.74-1.59-1.74H7.007l-1.494 7.02h2.94c1.209
 0 2.153-.619 2.458-2.025.295-1.416-.549-1.613-.944-1.652zm-1.052
 1.504c-.099.462-.354.757-.787.757h-.345l.334-1.602h.354c.454 0
 .542.373.444.845zm.472-2.753c-.108.511-.452.669-.708.669h-.295l.285-1.347h.266c.403
 0 .55.225.452.678zm6.83
 2.901c.295-1.416-.55-1.613-.944-1.652l.01-.02c.462-.098 1.219-.481
 1.453-1.583.248-1.16-.362-1.74-1.591-1.74h-2.831l-1.495
 7.02h2.94c1.21 0 2.153-.619
 2.458-2.025zm-1.996-.148c-.098.462-.354.757-.787.757h-.344l.335-1.602h.354c.452
 0
 .54.373.442.845zm.472-2.753c-.108.511-.453.669-.708.669h-.294l.285-1.347h.266c.402
 0 .55.225.45.678zm4.97-2.094h-2.951c.75.615.51 1.669.51
 1.669H19.2l2.338 1.857-2.167 1.834h-2.72c-.117.568-.712 1.424-1.125
 1.676h4.148L24 12.01z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://presse.notebooksbilliger.de/presskits'''

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
