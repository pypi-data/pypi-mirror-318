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


class KikIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kik"

    @property
    def original_file_name(self) -> "str":
        return "kik.svg"

    @property
    def title(self) -> "str":
        return "Kik"

    @property
    def primary_color(self) -> "str":
        return "#82BC23"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kik</title>
     <path d="M11.482 16.752c-.01.688-.56 1.242-1.238 1.242-.689
 0-1.23-.541-1.244-1.23h-.016v-6.243H9v-.029c0-.693.556-1.256
 1.237-1.256s1.236.563 1.236
 1.258v.045h.016v6.225h-.016l.009-.012zm11.137-4.889c.75 0 1.381.618
 1.381 1.377 0 .76-.631 1.375-1.381 1.375-.766
 0-1.395-.615-1.395-1.379 0-.766.615-1.381
 1.379-1.381l.016.008zm-2.084 4.186c.121.195.193.432.193.686 0
 .703-.553 1.26-1.244 1.26-.463
 0-.869-.256-1.08-.631l-2.053-2.746-.631.586v1.635h-.014c-.039.652-.57
 1.168-1.225 1.168-.674
 0-1.221-.553-1.221-1.238v-.025h-.016v-9.45h.027v-.047c0-.69.551-1.253
 1.23-1.253.674 0 1.225.562 1.225 1.253v.07h.016l.01 4.597
 2.311-2.261c.229-.255.559-.405.928-.405.689 0 1.248.57 1.248 1.26 0
 .346-.133.646-.344.871l.012.015-1.621 1.605 2.281
 3.061-.016.016-.016-.027zm-13.246 0c.12.195.195.432.195.686 0
 .703-.555 1.26-1.244 1.26-.466
 0-.871-.256-1.081-.631l-2.054-2.746-.63.586v1.631H2.46c-.036.654-.57
 1.17-1.221 1.17-.676
 0-1.225-.555-1.225-1.238v-.027H0V7.29h.031c-.004-.015-.004-.029-.004-.044
 0-.69.551-1.252 1.23-1.252.675 0 1.225.559 1.225 1.25v.07h.016l.01
 4.6 2.311-2.261c.23-.255.562-.405.931-.405.687 0 1.245.57 1.245 1.26
 0 .33-.131.646-.346.871l.016.015-1.627 1.605 2.271
 3.061-.016.016-.004-.027z" />
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
