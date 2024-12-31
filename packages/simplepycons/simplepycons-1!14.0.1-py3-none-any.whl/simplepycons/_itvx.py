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


class ItvxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "itvx"

    @property
    def original_file_name(self) -> "str":
        return "itvx.svg"

    @property
    def title(self) -> "str":
        return "ITVx"

    @property
    def primary_color(self) -> "str":
        return "#DEEB52"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ITVx</title>
     <path d="M15.91 11.018a59.87 59.87 0 0 0-.98-.27c-.1
 0-.16.05-.2.17-.35 1.2-.9 2.53-1.38
 3.36-.16-.3-.45-.83-.73-1.3l-1.04-1.83c-.22-.34-.36-.43-.64-.43-.57
 0-1.42.51-1.42 1 0 .16.04.28.21.57.2.32.3.6.3.92 0 .82-.62 1.56-1.8
 1.56-.55
 0-.99-.16-1.27-.45-.27-.28-.4-.65-.4-1.27v-1.03c.2.08.44.12.73.12h.93c.13
 0
 .17-.05.17-.16v-1c0-.11-.04-.17-.17-.17H6.56v-1.63c0-.2-.05-.33-.16-.43-.16-.15-.5-.22-.89-.22-.4
 0-.72.07-.89.22-.1.1-.16.24-.16.43v4c0 .66-.1 1.02-.34
 1.27-.2.22-.53.34-.88.34s-.66-.12-.84-.31c-.2-.2-.29-.48-.29-.9v-2.6c0-.11-.04-.16-.16-.16H.18c-.12
 0-.17.05-.17.16v2.35c0 .94.25 1.47.67 1.9.55.54 1.48.79 2.38.79.88 0
 1.81-.32 2.36-.82a4 4 0 0 0 2.6.82c1.42 0 2.47-.6
 3.08-1.6.27.43.47.74.67 1.02.28.42.54.58 1.12.58.54 0 .87-.13
 1.17-.59.78-1.18 1.44-2.59 1.92-3.88.05-.16.1-.28.1-.35
 0-.08-.05-.14-.17-.18zm-14.85-.92c.66 0 1.07-.46 1.07-1.05
 0-.6-.4-1.06-1.07-1.06-.65-.01-1.06.46-1.06 1.05 0 .59.4 1.05 1.06
 1.05zm22.84 5.1-2.28-3.13c-.05-.07-.05-.14
 0-.2l2.1-3.07c.07-.09.11-.15.11-.28 0-.12-.07-.25-.19-.37a.51.51 0 0
 0-.39-.17.4.4 0 0 0-.24.1l-2.9 2.22c-.06.05-.13.05-.2
 0l-2.89-2.22a.4.4 0 0 0-.25-.1.51.51 0 0 0-.38.17c-.12.12-.2.25-.2.37
 0 .13.05.2.11.28l2.11 3.07c.05.06.05.13 0 .2l-2.28 3.13a.42.42 0 0
 0-.1.26c0 .14.06.26.18.38.11.11.24.18.38.18.1 0
 .17-.04.26-.1l3.06-2.23a.17.17 0 0 1 .2 0l3.07
 2.23c.09.06.16.1.26.1.14 0 .27-.07.38-.18.12-.12.18-.24.18-.38
 0-.1-.04-.17-.1-.26z" />
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
