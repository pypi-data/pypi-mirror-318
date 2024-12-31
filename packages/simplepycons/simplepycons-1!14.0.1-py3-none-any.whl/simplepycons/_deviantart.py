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


class DeviantartIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "deviantart"

    @property
    def original_file_name(self) -> "str":
        return "deviantart.svg"

    @property
    def title(self) -> "str":
        return "DeviantArt"

    @property
    def primary_color(self) -> "str":
        return "#05CC47"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DeviantArt</title>
     <path d="M19.207 4.794l.23-.43V0H15.07l-.436.44-2.058
 3.925-.646.436H4.58v5.993h4.04l.36.436-4.175
 7.98-.24.43V24H8.93l.436-.44
 2.07-3.925.644-.436h7.35v-5.993h-4.05l-.36-.438 4.186-7.977z" />
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
