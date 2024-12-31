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


class SymantecIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "symantec"

    @property
    def original_file_name(self) -> "str":
        return "symantec.svg"

    @property
    def title(self) -> "str":
        return "Symantec"

    @property
    def primary_color(self) -> "str":
        return "#FDB511"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Symantec</title>
     <path d="M22.877 0v.738h.738V0h-.738zm0
 .738h-.738v.739h.738V.738zm0 .739v.738h.738v-.738h-.738zm-.738
 0h-1.477v.738h-.738V3.69h-.738v.74h-1.479v.725A10.572 10.572 0 0011
 2.77C5.136 2.77.385 7.52.385 13.385.385 19.248 5.136 24 11
 24s10.615-4.752
 10.615-10.615c0-2.56-.904-4.906-2.412-6.739h.72v-.738h.74V4.43h.737V3.69h.739v-.738H21.4v-.738h.739v-.738zM19.186
 3.69v-.738h-.74v.738h.74zM11 6.154a7.193 7.193 0 014.033
 1.23h-.28v.739h-.737c-1.927 2.409-2.414 3.466-3.182
 5.414-.871-1.763-1.911-2.978-3.711-3.783l-.02-.006c-.327-.083-.493-.125-.718.19-.23.322-.092.613.183.955a35.212
 35.212 0 00.586.703c.547.646 1.095 1.289 1.508 2.035.408.738.877
 1.772 1.242 2.574.223.49.406.894.51
 1.088.22.406.752.584.955.584.985-.117 1.08-.582
 1.242-1.379l.057-.264c.336-1.574.771-3.203
 2.824-5.158v-.736h.738V9.6h.74v-.295a7.193 7.193 0 011.26 4.08c0
 3.99-3.24 7.23-7.23 7.23s-7.2-3.24-7.2-7.23 3.21-7.23 7.2-7.23z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Syman'''

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
