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


class ArloIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "arlo"

    @property
    def original_file_name(self) -> "str":
        return "arlo.svg"

    @property
    def title(self) -> "str":
        return "Arlo"

    @property
    def primary_color(self) -> "str":
        return "#49B48A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Arlo</title>
     <path d="m16.21 11.172 4.963-5.792c.943-1.293 1.494-1.828
 1.07-3.94l-7.367 8.6a7.907 7.907 0 0 0-1.896 5.487L9.763 11.87a5.775
 5.775 0 0 0-.947-.829A9.979 9.979 0 0 0 7
 10.051c.213-.076.43-.14.649-.194.385-.094.78-.144 1.176-.147.444 0
 .881.07 1.3.237.416.168.82.432 1.212.858l.216.252
 1.336-1.129c-.01-.011-.241-.283-.251-.292a5.09 5.09 0 0 0-1.86-1.308
 5.233 5.233 0 0 0-1.953-.364c-.151 0-.299.007-.446.017-1.461.24-2.364
 1.104-3.714 1.244.001.006-4.58 0-4.581.002-.101 0-.115.144-.017.163
 1.202.24 3.341.699 4.844 1.214 1.142.529 2.24 1.205 3.106
 2.022.17.135.317.271.439.405l4.283 4.87c.61.501 1.395.755
 3.066.767a6.197 6.197 0 0 1-.695-1.337 6.173 6.173 0 0 1-.014-4.256
 6.139 6.139 0 0 1 1.114-1.903zM24
 22.56c-1.734-.022-2.489-.317-3.11-.888l-.962-1.093c-.065-.079-.13-.157-.197-.234l.011.023-1.704-1.937a4.794
 4.794 0 0 1-.905-4.806 4.755 4.755 0 0 1 .871-1.482l4.208-4.892c.43
 2.179-.192 2.666-1.21 4.09l-1.668 1.937a3.038 3.038 0 0 0-.739
 1.989c.001.741.272 1.458.761 2.014L24 22.56z" />
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
