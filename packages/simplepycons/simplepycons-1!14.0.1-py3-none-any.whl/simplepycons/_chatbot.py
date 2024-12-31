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


class ChatbotIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "chatbot"

    @property
    def original_file_name(self) -> "str":
        return "chatbot.svg"

    @property
    def title(self) -> "str":
        return "ChatBot"

    @property
    def primary_color(self) -> "str":
        return "#0066FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ChatBot</title>
     <path d="M11.999 0c-2.25 0-4.5.06-6.6.21a5.57 5.57 0 00-5.19
 5.1c-.24 3.21-.27 6.39-.06 9.6a5.644 5.644 0 005.7
 5.19h3.15v-3.9h-3.15c-.93.03-1.74-.63-1.83-1.56-.18-3-.15-6 .06-9
 .06-.84.72-1.47 1.56-1.53 2.04-.15 4.2-.21 6.36-.21s4.32.09
 6.36.18c.81.06 1.5.69 1.56 1.53.24 3 .24 6 .06 9-.12.93-.9 1.62-1.83
 1.59h-3.15l-6 3.9V24l6-3.9h3.15c2.97.03 5.46-2.25
 5.7-5.19.21-3.18.18-6.39-.03-9.57a5.57 5.57 0
 00-5.19-5.1c-2.13-.18-4.38-.24-6.63-.24zm-5.04 8.76c-.36
 0-.66.3-.66.66v2.34c0 .33.18.63.48.78 1.62.78 3.42 1.2 5.22 1.26
 1.8-.06 3.6-.48
 5.22-1.26.3-.15.48-.45.48-.78V9.42c0-.09-.03-.15-.09-.21a.648.648 0
 00-.87-.36c-1.5.66-3.12 1.02-4.77
 1.05-1.65-.03-3.27-.42-4.77-1.08a.566.566 0 00-.24-.06z" />
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
