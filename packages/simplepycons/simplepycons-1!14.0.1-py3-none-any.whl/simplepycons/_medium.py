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


class MediumIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "medium"

    @property
    def original_file_name(self) -> "str":
        return "medium.svg"

    @property
    def title(self) -> "str":
        return "Medium"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Medium</title>
     <path d="M4.21 0A4.201 4.201 0 0 0 0 4.21v15.58A4.201 4.201 0 0 0
 4.21 24h15.58A4.201 4.201 0 0 0 24
 19.79v-1.093c-.137.013-.278.02-.422.02-2.577
 0-4.027-2.146-4.09-4.832a7.592 7.592 0 0 1
 .022-.708c.093-1.186.475-2.241 1.105-3.022a3.885 3.885 0 0 1
 1.395-1.1c.468-.237 1.127-.367 1.664-.367h.023c.101 0
 .202.004.303.01V4.211A4.201 4.201 0 0 0 19.79 0Zm.198
 5.583h4.165l3.588 8.435
 3.59-8.435h3.864v.146l-.019.004c-.705.16-1.063.397-1.063
 1.254h-.003l.003 10.274c.06.676.424.885 1.063
 1.03l.02.004v.145h-4.923v-.145l.019-.005c.639-.144.994-.353
 1.054-1.03V7.267l-4.745 11.15h-.261L6.15 7.569v9.445c0 .857.358 1.094
 1.063 1.253l.02.004v.147H4.405v-.147l.019-.004c.705-.16 1.065-.397
 1.065-1.253V6.987c0-.857-.358-1.094-1.064-1.254l-.018-.004zm19.25
 3.668c-1.086.023-1.733 1.323-1.813 3.124H24V9.298a1.378 1.378 0 0
 0-.342-.047Zm-1.862 3.632c-.1 1.756.86 3.239 2.204 3.634v-3.634z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://medium.design/logos-and-brand-guideli'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://medium.design/logos-and-brand-guideli'''

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
