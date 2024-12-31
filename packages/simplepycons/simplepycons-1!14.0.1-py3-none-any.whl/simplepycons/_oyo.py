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


class OyoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "oyo"

    @property
    def original_file_name(self) -> "str":
        return "oyo.svg"

    @property
    def title(self) -> "str":
        return "OYO"

    @property
    def primary_color(self) -> "str":
        return "#EE2E24"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OYO</title>
     <path d="M19.843 16.185C22.135 16.185 24 14.307 24
 12c0-2.309-1.865-4.185-4.157-4.185-2.293 0-4.158 1.876-4.158 4.185 0
 2.307 1.865 4.185 4.158 4.185zm0-5.677c.817 0 1.482.67 1.482
 1.492s-.666 1.49-1.483 1.49A1.488 1.488 0 0 1 18.36
 12c0-.824.665-1.493 1.482-1.493zM4.157 16.185c2.293 0 4.158-1.878
 4.158-4.185 0-2.309-1.865-4.185-4.158-4.185C1.866 7.815 0 9.691 0
 12c0 2.307 1.866 4.185 4.157 4.185zm0-5.677c.818 0 1.483.67 1.483
 1.492s-.665 1.49-1.483 1.49A1.488 1.488 0 0 1 2.677
 12c0-.824.664-1.493 1.48-1.493zm7.84-.094L10.722 7.87H7.733l2.791
 5.564v2.62h2.948v-2.62l2.791-5.564h-2.99l-1.275 2.544Z" />
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
