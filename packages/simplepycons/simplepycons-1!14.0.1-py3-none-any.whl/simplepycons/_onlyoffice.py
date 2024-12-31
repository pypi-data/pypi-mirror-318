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


class OnlyofficeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "onlyoffice"

    @property
    def original_file_name(self) -> "str":
        return "onlyoffice.svg"

    @property
    def title(self) -> "str":
        return "ONLYOFFICE"

    @property
    def primary_color(self) -> "str":
        return "#444444"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ONLYOFFICE</title>
     <path d="M10.501 11.724.631 7.16c-.841-.399-.841-1.014
 0-1.376l9.87-4.563c.841-.399 2.194-.399 2.998 0l9.87
 4.563c.841.398.841 1.014 0 1.376l-9.87
 4.563c-.841.362-2.194.362-2.998 0zm0
 5.468-9.87-4.563c-.841-.399-.841-1.014 0-1.376l3.363-1.558 6.507
 3.006c.841.398 2.194.398 2.998 0l6.507-3.006 3.363 1.558c.841.398.841
 1.014 0 1.376l-9.87 4.563c-.841.398-2.194.398-2.998 0zm0
 0.0001-9.87-4.563c-.841-.399-.841-1.014 0-1.376l3.363-1.558 6.507
 3.006c.841.398 2.194.398 2.998 0l6.507-3.006 3.363 1.558c.841.398.841
 1.014 0 1.376l-9.87 4.563c-.841.398-2.194.398-2.998 0zm0
 5.613-9.87-4.563c-.841-.398-.841-1.014 0-1.376l3.436-1.593 6.398
 2.97c.84.398 2.193.398 2.997 0l6.398-2.97 3.436 1.593c.841.399.841
 1.014 0 1.376l-9.87 4.563c-.768.362-2.12.362-2.925 0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.onlyoffice.com/en/press-downloads'''

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
