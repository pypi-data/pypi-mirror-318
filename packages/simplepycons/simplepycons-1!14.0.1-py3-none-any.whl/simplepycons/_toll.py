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


class TollIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "toll"

    @property
    def original_file_name(self) -> "str":
        return "toll.svg"

    @property
    def title(self) -> "str":
        return "Toll"

    @property
    def primary_color(self) -> "str":
        return "#007A68"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Toll</title>
     <path d="M21.852 13.351H24l-.645 1.455h-3.346c-.689
 0-1.158-.584-.898-1.15l1.978-4.463h2.356l-1.75
 3.954c-.037.088-.008.202.157.204ZM6.147 10.647l-1.843
 4.159H3.303c-.601
 0-1.061-.556-.852-1.045l1.379-3.114H0l.112-.252h7.375c.375 0
 .955-.058 1.534-.338.155-.074.845-.473
 1.503-.864h1.474c-.411.194-2.381 1.141-2.617
 1.227-.618.225-1.017.227-1.526.227H6.147Zm.538-.471H.209c.195-.442.632-.983
 1.933-.983h6.18c-.351.44-.704.983-1.637.983Zm10.001
 2.971c-.037.088-.007.202.157.204h2.149l-.644 1.455h-3.347c-.689
 0-1.157-.584-.898-1.15l1.978-4.463h2.356l-1.75
 3.954h-.001Zm-1.831-3.439c.283.402.128 1-.107 1.506l-.91 2.055c-.686
 1.655-3.056 1.536-3.056
 1.536H8.085s-2.332.122-1.315-2.167l.785-1.774h.655c.531 0 1.182-.165
 1.48-.282l3.509-1.389h.616c.497 0 .871.24 1.037.515h.003Zm-2.4
 1.376c.119-.291-.054-.437-.294-.437h-1.7c-.343-.002-.512.168-.563.279-.036.074-.854
 1.925-.854
 1.925-.233.518.261.501.261.501h1.617s.52.002.756-.512l.777-1.757v.001Z"
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
