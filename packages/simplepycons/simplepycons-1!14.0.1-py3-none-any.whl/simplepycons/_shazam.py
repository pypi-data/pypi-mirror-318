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


class ShazamIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "shazam"

    @property
    def original_file_name(self) -> "str":
        return "shazam.svg"

    @property
    def title(self) -> "str":
        return "Shazam"

    @property
    def primary_color(self) -> "str":
        return "#0088FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Shazam</title>
     <path d="M12 0C5.373 0-.001 5.371-.001 12c0 6.625 5.374 12 12.001
 12s12-5.375 12-12c0-6.629-5.373-12-12-12M9.872 16.736c-1.287
 0-2.573-.426-3.561-1.281-1.214-1.049-1.934-2.479-2.029-4.024-.09-1.499.42-2.944
 1.436-4.067C6.86 6.101 8.907 4.139 8.993 4.055c.555-.532 1.435-.511
 1.966.045.53.557.512 1.439-.044 1.971-.021.02-2.061 1.976-3.137
 3.164-.508.564-.764 1.283-.719 2.027.049.789.428 1.529 1.07
 2.086.844.73 2.51.891 3.553-.043.619-.559 1.372-1.377
 1.38-1.386.52-.567 1.4-.603 1.965-.081.565.52.603 1.402.083
 1.969-.035.035-.852.924-1.572 1.572-1.005.902-2.336 1.357-3.666
 1.357m8.41-.099c-1.143 1.262-3.189 3.225-3.276
 3.309-.27.256-.615.385-.96.385-.368
 0-.732-.145-1.006-.43-.531-.559-.512-1.439.044-1.971.021-.02
 2.063-1.977
 3.137-3.166.508-.563.764-1.283.719-2.027-.048-.789-.428-1.529-1.07-2.084-.844-.73-2.51-.893-3.552.044-.621.556-1.373
 1.376-1.38
 1.384-.521.566-1.399.604-1.966.084-.564-.521-.604-1.404-.082-1.971.034-.037.85-.926
 1.571-1.573 1.979-1.778 5.221-1.813 7.227-.077 1.214 1.051 1.935 2.48
 2.028 4.025.092 1.497-.419 2.945-1.434 4.068" />
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
