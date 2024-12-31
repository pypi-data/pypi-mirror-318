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


class PlaystationVitaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "playstationvita"

    @property
    def original_file_name(self) -> "str":
        return "playstationvita.svg"

    @property
    def title(self) -> "str":
        return "PlayStation Vita"

    @property
    def primary_color(self) -> "str":
        return "#003791"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PlayStation Vita</title>
     <path d="M3.176 12.216H1.274c-.26
 0-.453.198-.453.538v1.235H0v-1.19c0-.668.42-1.119
 1.014-1.119h1.924c.471-.018.584-.252.584-.592
 0-.26-.13-.616-.584-.58H0v-.49h3.176c.832 0 1.16.481 1.16 1.07 0
 .669-.328 1.128-1.16 1.128zm3.488-1.122v1.813c0 .663-.299 1.076-1.126
 1.076H3.761v-.49h1.55c.318 0
 .507-.258.507-.586v-1.813c0-.578.28-1.077
 1.102-1.077h1.765v.49H7.158c-.412-.017-.494.32-.494.587zm4.84
 2.904c-.331-.018-.47-.27-.532-.377-.063-.107-1.92-3.609-1.92-3.609h.924l1.538
 2.855c.08.16.262.2.36.012l1.53-2.867h.577s-1.798 3.404-1.87
 3.52c-.071.117-.276.484-.607.466zm3.005-3.972h.84v3.96h-.84zm3.77.46l.003
 3.477h-.826V10.49l-1.57-.002v-.483L19.859
 10l-.002.489zm3.235-.481c-.314.005-.51.354-.579.467-.071.116-1.873
 3.527-1.873
 3.527h.578l.44-.84h2.541l.454.84H24s-1.86-3.508-1.923-3.616c-.062-.107-.201-.36-.533-.378h-.03zm-.18.996c.078-.005.155.047.2.138l.825
 1.525h-2.004l.818-1.538c.043-.082.102-.12.162-.125Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:PlayS'''

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
