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


class JioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jio"

    @property
    def original_file_name(self) -> "str":
        return "jio.svg"

    @property
    def title(self) -> "str":
        return "Jio"

    @property
    def primary_color(self) -> "str":
        return "#0A2885"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Jio</title>
     <path d="M12 0A12 12 0 1 1 0 12 12 12 0 0 1 12 0m5.587
 14.559c-.883 0-1.49-.648-1.49-1.574 0-.912.62-1.56
 1.49-1.56s1.491.648 1.491 1.573c0 .897-.634 1.56-1.49
 1.56zm.03-5.152c-2.265 0-3.772 1.437-3.772 3.576 0 2.195 1.451 3.604
 3.729 3.604 2.264 0 3.755-1.409 3.755-3.59
 0-2.153-1.475-3.59-3.713-3.59zM11.78 6.272c-.856 0-1.395.483-1.395
 1.243 0 .774.552 1.257 1.435 1.257.857 0 1.395-.483
 1.395-1.257s-.552-1.243-1.435-1.243m.152 3.204h-.277c-.675
 0-1.187.317-1.187 1.285v4.42c0 .98.496 1.284 1.216 1.284h.275c.677 0
 1.16-.33 1.16-1.285v-4.419c0-.995-.47-1.285-1.187-1.285M8.316
 7.392h-.4c-.76 0-1.174.43-1.174 1.285v4.13c0 1.063-.36 1.436-1.2
 1.436-.662 0-1.201-.29-1.63-.816C3.87 13.373 3 13.786 3 14.81c0 1.104
 1.035 1.781 2.955 1.781 2.334 0 3.563-1.173
 3.563-3.742V8.675c0-.856-.413-1.283-1.202-1.283" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Relia'''

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
