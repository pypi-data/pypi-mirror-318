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


class SongkickIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "songkick"

    @property
    def original_file_name(self) -> "str":
        return "songkick.svg"

    @property
    def title(self) -> "str":
        return "Songkick"

    @property
    def primary_color(self) -> "str":
        return "#F80046"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Songkick</title>
     <path d="M6.55 18.779c-1.855
 0-3.372-.339-4.598-1.602l1.92-1.908c.63.631 1.74.853 2.715.853 1.186
 0 1.739-.391 1.739-1.089
 0-.291-.06-.529-.239-.717-.15-.154-.404-.273-.795-.324l-1.455-.205c-1.064-.152-1.891-.51-2.43-1.072-.555-.578-.84-1.395-.84-2.434C2.536
 8.066 4.2 6.45 6.96 6.45c1.74 0 3.048.407 4.086 1.448L9.171
 9.77c-.765-.766-1.77-.715-2.295-.715-1.039 0-1.465.597-1.465 1.125 0
 .152.051.375.24.561.15.153.404.307.832.359l1.467.203c1.09.153
 1.875.495 2.385 1.005.645.63.9 1.53.9 2.655 0 2.47-2.127 3.819-4.68
 3.819l-.005-.003zM20.813 2.651C19.178 1.432 17.37.612
 15.089.237v10.875l3.261-4.539h3.565l-4.095 5.72s.944 1.51 1.515
 2.405c.586.899 1.139 1.14 1.965 1.14h.57v2.806h-.872c-1.812
 0-2.9-.33-3.72-1.575-.504-.811-2.175-3.436-2.175-3.436v4.995H12.12V-.001H12c-3.852
 0-6.509.931-8.811 2.652C-.132 5.137.001 8.451.001 11.997c0 3.547-.133
 6.867 3.188 9.352C5.491 23.074 8.148 24 12 24s6.51-.927
 8.812-2.651C24.131 18.865 24 15.544 24
 11.997c0-3.546.132-6.859-3.188-9.346h.001z" />
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
