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


class RossmannIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rossmann"

    @property
    def original_file_name(self) -> "str":
        return "rossmann.svg"

    @property
    def title(self) -> "str":
        return "Rossmann"

    @property
    def primary_color(self) -> "str":
        return "#C3002D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rossmann</title>
     <path d="M12 0C5.391 0 0 5.391 0 12s5.391 12 12 12 12-5.391
 12-12S18.609 0 12 0m0 2.088a9.93 9.93 0 0 1 7.477
 3.39H16l.348-.607c.347-.783-.958-1.392-1.393-.61l-.607
 1.218H4.52C6.435 3.392 9.131 2.088 12 2.088m8.434 4.695A10.07 10.07 0
 0 1 21.912 12c0 4.087-2.522 7.653-6.174 9.13l-3.912-3.911q-.13-.131
 0-.262l1.39-2.783c.088-.087.174-.174.26-.174h2.436c.087 0
 .088.087.088.174l-.697 1.478s0
 .174.088.174l.869.61c.087.087.175-.001.261-.088l.956-2.26c.087-.087.174-.174.261-.174h.87s.087
 0 .087.174L18
 15.652s-.001.174.086.174l.957.61c.087.087.173-.001.26-.088 0-.087
 1.045-2.26 1.045-2.434.26-.609.172-1.652-1.045-1.652h-1.39a.19.19 0 0
 1-.175-.174v-4.61q0-.26.262-.26zm-16.782.088s9.13.434 9.217.434.26 0
 .26.174c.087.173.87 2.174.957 2.261s.087.348-.348.348H4.87a1.15 1.15
 0 0 0-1.13 1.13v3.305c0
 .261.086.522.173.696.261.26.696.433.783.433.087.087.174.001.174-.086v-4.261c0-.087.087-.174.174-.174H6s.173
 0 .086.088c-.348.435-.434.87-.434 1.652 0 1.217.87 1.999 1.217 2.26 0
 0 .087.087 0 .174S6 17.044 6 17.13q-.13.131 0 .262l4.348
 4.26c-4.696-.87-8.174-4.87-8.174-9.653 0-1.913.522-3.65
 1.478-5.129M9.912 14h.957s.173 0 .086.174-1.39 2.696-1.39
 2.783v.174l4.52
 4.435c-.52.174-1.042.173-1.564.26l-4.435-4.433c-.087-.087 0-.175
 0-.262s1.48-2.87 1.566-2.957c0-.087.086-.174.26-.174" />
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
