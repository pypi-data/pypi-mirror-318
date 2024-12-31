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


class SnapchatIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "snapchat"

    @property
    def original_file_name(self) -> "str":
        return "snapchat.svg"

    @property
    def title(self) -> "str":
        return "Snapchat"

    @property
    def primary_color(self) -> "str":
        return "#FFFC00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Snapchat</title>
     <path d="M12.206.793c.99 0 4.347.276 5.93 3.821.529 1.193.403
 3.219.299
 4.847l-.003.06c-.012.18-.022.345-.03.51.075.045.203.09.401.09.3-.016.659-.12
 1.033-.301.165-.088.344-.104.464-.104.182 0
 .359.029.509.09.45.149.734.479.734.838.015.449-.39.839-1.213
 1.168-.089.029-.209.075-.344.119-.45.135-1.139.36-1.333.81-.09.224-.061.524.12.868l.015.015c.06.136
 1.526 3.475 4.791 4.014.255.044.435.27.42.509 0
 .075-.015.149-.045.225-.24.569-1.273.988-3.146
 1.271-.059.091-.12.375-.164.57-.029.179-.074.36-.134.553-.076.271-.27.405-.555.405h-.03c-.135
 0-.313-.031-.538-.074-.36-.075-.765-.135-1.273-.135-.3
 0-.599.015-.913.074-.6.104-1.123.464-1.723.884-.853.599-1.826
 1.288-3.294 1.288-.06 0-.119-.015-.18-.015h-.149c-1.468
 0-2.427-.675-3.279-1.288-.599-.42-1.107-.779-1.707-.884-.314-.045-.629-.074-.928-.074-.54
 0-.958.089-1.272.149-.211.043-.391.074-.54.074-.374
 0-.523-.224-.583-.42-.061-.192-.09-.389-.135-.567-.046-.181-.105-.494-.166-.57-1.918-.222-2.95-.642-3.189-1.226-.031-.063-.052-.15-.055-.225-.015-.243.165-.465.42-.509
 3.264-.54 4.73-3.879
 4.791-4.02l.016-.029c.18-.345.224-.645.119-.869-.195-.434-.884-.658-1.332-.809-.121-.029-.24-.074-.346-.119-1.107-.435-1.257-.93-1.197-1.273.09-.479.674-.793
 1.168-.793.146 0 .27.029.383.074.42.194.789.3 1.104.3.234 0
 .384-.06.465-.105l-.046-.569c-.098-1.626-.225-3.651.307-4.837C7.392
 1.077 10.739.807 11.727.807l.419-.015h.06z" />
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
