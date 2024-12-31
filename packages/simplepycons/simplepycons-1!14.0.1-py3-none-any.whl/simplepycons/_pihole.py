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


class PiholeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pihole"

    @property
    def original_file_name(self) -> "str":
        return "pihole.svg"

    @property
    def title(self) -> "str":
        return "Pi-hole"

    @property
    def primary_color(self) -> "str":
        return "#96060C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pi-hole</title>
     <path d="M4.344 0c.238 4.792 3.256 7.056 6.252
 7.376.165-1.692-4.319-5.6-4.319-5.6-.008-.011.009-.025.019-.014 0 0
 4.648 4.01 5.423 5.645 2.762-.15 5.196-1.947 5-4.912 0 0-4.12-.613-5
 4.618C11.48 2.753 8.993 0 4.344 0zM12 7.682v.002a3.68 3.68 0 0
 0-2.591 1.077L4.94 13.227a3.683 3.683 0 0 0-.86 1.356 3.31 3.31 0 0
 0-.237 1.255A3.681 3.681 0 0 0 4.92 18.45l4.464 4.466a3.69 3.69 0 0 0
 2.251
 1.06l.002.001c.093.01.187.015.28.017l-.1-.008c.06.003.117.009.177.009l-.077-.001L12
 24l-.004-.005a3.68 3.68 0 0 0 2.61-1.077l4.469-4.465a3.683 3.683 0 0
 0 1.006-1.888l.012-.063a3.682 3.682 0 0 0
 .057-.541l.003-.061c0-.017.003-.05.004-.06h-.002a3.683 3.683 0 0
 0-1.077-2.607l-4.466-4.468a3.694 3.694 0 0 0-1.564-.927l-.07-.02a3.43
 3.43 0 0 0-.946-.133L12 7.682zm3.165 3.357c.023 1.748-1.33 3.078-1.33
 4.806.164 2.227 1.733 3.207 3.266
 3.146-.035.003-.068.007-.104.009-1.847.135-3.209-1.326-5.002-1.326-2.23.164-3.21
 1.736-3.147 3.27l-.008-.104c-.133-1.847 1.328-3.21
 1.328-5.002-.173-2.32-1.867-3.284-3.46-3.132.1-.011.203-.021.31-.027
 1.847-.133 3.209 1.328 5.002 1.328 2.082-.155 3.074-1.536
 3.145-2.968zM4.344 0c.238 4.792 3.256 7.056 6.252
 7.376.165-1.692-4.319-5.6-4.319-5.6-.008-.011.009-.025.019-.014 0 0
 4.648 4.01 5.423 5.645 2.762-.15 5.196-1.947 5-4.912 0 0-4.12-.613-5
 4.618C11.48 2.753 8.993 0 4.344 0zM12 7.682v.002a3.68 3.68 0 0
 0-2.591 1.077L4.94 13.227a3.683 3.683 0 0 0-.86 1.356 3.31 3.31 0 0
 0-.237 1.255A3.681 3.681 0 0 0 4.92 18.45l4.464 4.466a3.69 3.69 0 0 0
 2.251
 1.06l.002.001c.093.01.187.015.28.017l-.1-.008c.06.003.117.009.177.009l-.077-.001L12
 24l-.004-.005a3.68 3.68 0 0 0 2.61-1.077l4.469-4.465a3.683 3.683 0 0
 0 1.006-1.888l.012-.063a3.682 3.682 0 0 0
 .057-.541l.003-.061c0-.017.003-.05.004-.06h-.002a3.683 3.683 0 0
 0-1.077-2.607l-4.466-4.468a3.694 3.694 0 0 0-1.564-.927l-.07-.02a3.43
 3.43 0 0 0-.946-.133L12 7.682zm3.165 3.357c.023 1.748-1.33 3.078-1.33
 4.806.164 2.227 1.733 3.207 3.266
 3.146-.035.003-.068.007-.104.009-1.847.135-3.209-1.326-5.002-1.326-2.23.164-3.21
 1.736-3.147 3.27l-.008-.104c-.133-1.847 1.328-3.21
 1.328-5.002-.173-2.32-1.867-3.284-3.46-3.132.1-.011.203-.021.31-.027
 1.847-.133 3.209 1.328 5.002 1.328 2.082-.155 3.074-1.536
 3.145-2.968z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://pi-hole.net/trademark-rules-and-brand'''
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
