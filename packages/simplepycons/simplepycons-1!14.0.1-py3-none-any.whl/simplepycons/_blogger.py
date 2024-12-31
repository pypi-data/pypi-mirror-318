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


class BloggerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "blogger"

    @property
    def original_file_name(self) -> "str":
        return "blogger.svg"

    @property
    def title(self) -> "str":
        return "Blogger"

    @property
    def primary_color(self) -> "str":
        return "#FF5722"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Blogger</title>
     <path d="M21.976 24H2.026C.9 24 0 23.1 0 21.976V2.026C0 .9.9 0
 2.025 0H22.05C23.1 0 24 .9 24 2.025v19.95C24 23.1 23.1 24 21.976
 24zM12 3.975H9c-2.775 0-5.025 2.25-5.025 5.025v6c0 2.774 2.25 5.024
 5.025 5.024h6c2.774 0 5.024-2.25
 5.024-5.024v-3.975c0-.6-.45-1.05-1.05-1.05H18c-.524
 0-.976-.45-.976-.976 0-2.776-2.25-5.026-5.024-5.026zm3.074 12H9c-.525
 0-.975-.45-.975-.975s.45-.976.975-.976h6.074c.526 0
 .977.45.977.976s-.45.976-.975.976zm-2.55-7.95c.527 0
 .976.45.976.975s-.45.975-.975.975h-3.6c-.525
 0-.976-.45-.976-.975s.45-.975.975-.975h3.6z" />
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
