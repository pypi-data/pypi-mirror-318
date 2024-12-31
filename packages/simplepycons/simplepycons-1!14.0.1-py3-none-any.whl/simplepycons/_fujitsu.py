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


class FujitsuIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fujitsu"

    @property
    def original_file_name(self) -> "str":
        return "fujitsu.svg"

    @property
    def title(self) -> "str":
        return "Fujitsu"

    @property
    def primary_color(self) -> "str":
        return "#FF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fujitsu</title>
     <path d="M16.56 3C14.15 3 12.04 4.24 10.68 5.97L10.68 9.76C12.5
 4.71 16.56 5.08 16.56 5.08C19.5 5.08 21.84 7.38 21.84 10.2C21.84
 13.04 19.5 15.33 16.56 15.33A5.32 5.32 0 0 1 12.84 13.83L10.28
 11.03A6.06 6.06 0 0 0 6.03 9.32C2.7 9.32 0 11.93 0 15.16C0 18.4 2.7
 21 6.03 21C7.9 21 9.58 20.19 10.68 18.89L10.68 15.86C8.88 19.29 6.03
 18.92 6.03 18.92C3.9 18.92 2.17 17.24 2.17 15.16C2.17 13.1 3.9 11.42
 6.03 11.42C7.09 11.42 8.05 11.84 8.75 12.5L11.31 15.31A7.5 7.5 0 0 0
 16.56 17.43C20.67 17.43 24 14.19 24 10.2C24 6.21 20.67 3 16.56 3Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.fujitsu.com/global/about/brandman'''

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
