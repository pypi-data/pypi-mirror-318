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


class AltiumDesignerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "altiumdesigner"

    @property
    def original_file_name(self) -> "str":
        return "altiumdesigner.svg"

    @property
    def title(self) -> "str":
        return "Altium Designer"

    @property
    def primary_color(self) -> "str":
        return "#A5915F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Altium Designer</title>
     <path d="M19.14 5.876a1.012 1.012 0
 00-.442-.442L9.744.171c-.329-.226-.843-.226-1.203-.01L5.148
 2.145c-.051.041-.102.082-.144.123a1.086 1.086 0 00-.288.72l.01
 6.569-.02.215.062.123a.478.478 0 00.195.206.516.516 0 00.555.01L8.859
 8.2a.573.573 0 00.175-.175l.082-.165V4.643l2.251 1.326 3.536
 2.077a.413.413 0 01.164.185.442.442 0 01.062.226v7.052a.52.52 0
 01-.072.257c-.041.072-.082.123-.154.154l-4.225
 2.488-1.573.925v-3.228l1.953-1.172
 1.049-.627.185-.175.021-.051a.542.542 0 00.062-.247V9.999a.51.51 0
 00-.092-.288l-.062-.123-.144-.072c-.093-.041-.175-.041-.247-.041l-.175.01-6.363
 3.865a1.129 1.129 0 00-.442.463 1.281 1.281 0 00-.144.607v6.559c0
 .257.103.514.329.75.082.062.154.113.236.164l3.341
 1.943c.186.113.381.164.597.164.216 0
 .422-.051.596-.164l8.882-5.212c.195-.103.36-.267.442-.432.113-.185.164-.401.164-.617V6.483a1.236
 1.236 0 00-.153-.607zM8.387 7.624L5.447
 9.32V2.988c0-.072.031-.154.092-.216l.216-.123 2.632
 1.563v3.412zm-2.951 6.795c0-.093.021-.185.062-.278a.409.409 0
 01.175-.175l5.973-3.629v3.392l-.956.576-2.313 1.388-2.94
 1.778v-3.052zm0 6.559v-2.663l2.94-1.768v3.218l-2.632
 1.552-.103-.062c-.051-.031-.093-.051-.103-.062-.061-.071-.102-.143-.102-.215zm13.128-3.403a.518.518
 0 01-.072.257.342.342 0 01-.165.154l-8.892 5.222a.405.405 0 01-.452
 0l-2.508-1.47 4.575-2.693v-.01l4.215-2.478a.998.998 0 00.432-.442
 1.13 1.13 0 00.175-.606V8.457c0-.216-.062-.421-.165-.596a1.189 1.189
 0
 00-.432-.442l-3.536-2.077-3.352-1.974-1.923-1.141L8.911.788a.446.446
 0 01.452 0l8.985 5.294a.319.319 0 01.154.154.517.517 0
 01.062.247v11.092z" />
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
