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


class TalosIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "talos"

    @property
    def original_file_name(self) -> "str":
        return "talos.svg"

    @property
    def title(self) -> "str":
        return "Talos"

    @property
    def primary_color(self) -> "str":
        return "#FF7300"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Talos</title>
     <path d="M9.678 11.98c0-2.664-1.13-6.896-2.867-10.804a12 12 0 0
 0-1.585.917c1.608 3.668 2.647 7.553 2.647 9.886 0 2.254-1.08
 6.145-2.735 9.865a12 12 0 0 0 1.576.93c1.79-3.976 2.964-8.229
 2.964-10.795m6.442 0c0-2.336 1.042-6.22 2.646-9.89a12 12 0 0
 0-1.608-.922c-1.756 3.957-2.843 8.166-2.843 10.816 0 2.564 1.177
 6.819 2.965 10.797a12 12 0 0 0
 1.575-.931c-1.655-3.723-2.735-7.616-2.735-9.87m5.45 6.525.31.307a12
 12 0 0 0 .936-1.612c-1.866-1.893-3.457-3.938-3.47-5.233-.012-1.264
 1.57-3.308 3.446-5.222a12 12 0 0 0-.945-1.603l-.259.258c-2.739
 2.766-4.063 4.92-4.047 6.583.016 1.662 1.332 3.81 4.028 6.522M2.411
 5.405l-.26-.259a12 12 0 0 0-.946 1.608c3.123 3.173 3.452 4.704 3.448
 5.217-.012 1.3-1.603 3.34-3.47 5.229a12 12 0 0 0 .939
 1.608c.106-.106.207-.204.31-.308 2.694-2.711 4.01-4.842
 4.026-6.516s-1.308-3.809-4.047-6.58M12.002 24c.303 0
 .602-.016.898-.037V.037A12 12 0 0 0 12 0c-.304
 0-.605.015-.905.037v23.925q.448.035.903.038z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/siderolabs/talos/blob/e3fd'''

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
