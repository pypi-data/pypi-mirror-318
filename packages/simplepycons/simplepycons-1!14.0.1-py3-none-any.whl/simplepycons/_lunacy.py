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


class LunacyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lunacy"

    @property
    def original_file_name(self) -> "str":
        return "lunacy.svg"

    @property
    def title(self) -> "str":
        return "Lunacy"

    @property
    def primary_color(self) -> "str":
        return "#179DE3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Lunacy</title>
     <path d="M12.031 6h-6v12h11.996v-6l-5.996 5.996Zm6.563
 2.309a4.013 4.013 0 0 1-2.371-2.375 4.03 4.03 0 0 1-2.375 2.375 4.04
 4.04 0 0 1 2.375 2.375 4.013 4.013 0 0 1 2.37-2.375ZM0 9.602c0-3.364
 0-5.043.652-6.325A6.044 6.044 0 0 1 3.277.652C4.56 0 6.238 0 9.602
 0h4.796c3.364 0 5.043 0 6.325.652a6.044 6.044 0 0 1 2.625 2.625C24
 4.56 24 6.238 24 9.602v4.796c0 3.364 0 5.043-.652 6.325a6.044 6.044 0
 0 1-2.625 2.625C19.44 24 17.762 24 14.398 24H9.602c-3.364 0-5.043
 0-6.325-.652a6.044 6.044 0 0 1-2.625-2.625C0 19.44 0 17.762 0
 14.398Z" />
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
