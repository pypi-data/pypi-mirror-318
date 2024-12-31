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


class PlaycanvasIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "playcanvas"

    @property
    def original_file_name(self) -> "str":
        return "playcanvas.svg"

    @property
    def title(self) -> "str":
        return "PlayCanvas"

    @property
    def primary_color(self) -> "str":
        return "#E05F2C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PlayCanvas</title>
     <path d="M6.115 0l-.002 3.414 5.823 3.41-5.82 3.414-.003 3.412
 11.774-6.826zm11.77 10.35L6.113 17.174 17.887
 24l-.002-3.414-5.82-3.412 5.822-3.412z" />
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
