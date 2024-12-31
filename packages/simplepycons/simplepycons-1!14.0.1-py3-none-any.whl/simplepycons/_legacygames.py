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


class LegacyGamesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "legacygames"

    @property
    def original_file_name(self) -> "str":
        return "legacygames.svg"

    @property
    def title(self) -> "str":
        return "Legacy Games"

    @property
    def primary_color(self) -> "str":
        return "#144B9E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Legacy Games</title>
     <path d="M1.62 5.985v12.033L11.992 24l10.37-5.987L22.38 6 11.988
 0Zm19.146.955.002 10.123-8.793 5.045-8.758-5.023L3.216
 6.94l8.77-5.06Zm-8.781-3.176a2.03 2.03 0 0 1 .87
 3.863v2.936l3.863-2.256c.203-.118.427-.196.66-.227l1.602-.218a.104.104
 0 0 1 .098.165l-.963 1.308a1.78 1.78 0 0 1-.54.485L13.6 12.13l2.393
 1.403c.564-.41 1.393-.46 2.144-.082l.16.088c1.041.618 1.488 1.86.999
 2.771-.49.913-1.731
 1.15-2.772.532-.748-.444-1.19-1.21-1.198-1.944l-2.472-1.451v3.042a2.03
 2.03 0 0 1 1.154 1.673l.006.16a2.03 2.03 0 1
 1-2.899-1.833v-2.915l-4.236 2.46a.595.595 0 0
 1-.242.079l-1.746.166a.104.104 0 0 1-.093-.165l1.043-1.399a.594.594 0
 0 1
 .177-.157l4.374-2.555-2.418-1.418c-.564.409-1.391.458-2.142.08l-.16-.087c-1.04-.619-1.488-1.86-.998-2.772.49-.912
 1.73-1.15 2.772-.531.75.445 1.19 1.212 1.197 1.947l2.471
 1.449.001-3.043a2.03 2.03 0 0 1-1.153-1.674l-.006-.16c0-1.12.908-2.03
 2.029-2.03z" />
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
