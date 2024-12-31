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


class AwsOrganizationsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "awsorganizations"

    @property
    def original_file_name(self) -> "str":
        return "awsorganizations.svg"

    @property
    def title(self) -> "str":
        return "AWS Organizations"

    @property
    def primary_color(self) -> "str":
        return "#E7157B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AWS Organizations</title>
     <path d="M24 18.714v4.8c0 .288-.192.48-.48.48h-4.8c-.288
 0-.48-.192-.48-.48v-4.8c0-.288.192-.48.48-.48h1.92v-1.92h-8.16v1.92h1.92c.288
 0 .48.192.48.48v4.8c0 .288-.192.48-.48.48H9.6c-.288
 0-.48-.192-.48-.48v-4.8c0-.288.192-.48.48-.48h1.92v-1.92H3.36v1.92h1.92c.288
 0 .48.192.48.48v4.8c0 .288-.192.48-.48.48H.48c-.288
 0-.48-.192-.48-.48v-4.8c0-.288.192-.48.48-.48H2.4v-2.4c0-.288.192-.48.48-.48h8.64v-1.44h.96v1.44h8.64c.288
 0 .48.192.48.48v2.4h1.92c.288 0 .48.192.48.48zm-13.92
 4.32h3.84v-3.84h-3.84zm-9.12 0H4.8v-3.84H.96Zm18.24
 0h3.84v-3.84H19.2ZM6.24
 9.642V3.546c0-.192.096-.336.24-.432L11.76.042c.144-.048.336-.048.48
 0l5.28 3.072c.144.096.24.24.24.432v6.096c0
 .144-.096.288-.24.384l-5.28
 3.072q-.096.048-.24.048t-.24-.048l-5.28-3.072c-.144-.096-.24-.24-.24-.384Zm10.56-.288V4.362l-4.32
 2.496v4.992zm-9.6 0 4.32 2.496V6.858L7.2 4.362Zm.48-5.808L12
 5.994l4.32-2.448L12 1.05Z" />
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
