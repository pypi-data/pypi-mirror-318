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


class ZettlrIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zettlr"

    @property
    def original_file_name(self) -> "str":
        return "zettlr.svg"

    @property
    def title(self) -> "str":
        return "Zettlr"

    @property
    def primary_color(self) -> "str":
        return "#1CB27E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zettlr</title>
     <path d="M2.46.188C.335.57.023 2.534.022 4.295L.02 17.325c0
 1.545-.224 3.96.723 5.28 1.201 1.673 3.567 1.355 5.365
 1.351l8.31.03c1.61-.003 5.626.104 7.2-.23 2.115-.448 2.326-2.31
 2.328-4.082l.01-13.634c.001-1.532.311-3.425-.68-4.71C22.021-.296
 19.557.025 17.744.026L13.24.043c-1.614 0-9.195-.14-10.782.145m14.249
 3.665c0 .528.185 1.466-.037
 1.947-.11.239-.49.384-.703.518-.496.315-.961.676-1.418 1.044-1.477
 1.185-3.034 2.818-3.428 4.74-.182.895-.164 1.988.59 2.626 1.21 1.023
 3.035-.024 4.317.987 1.337 1.053 1.14 3.071.37
 4.39-.184.316-.417.797-.75.982-.23.13-.598.064-.853.064h-1.85c.057-.37.35-.58.575-.862.374-.47.673-.984.668-1.6-.01-1.157-1.127-1.17-1.983-1.17-1.518
 0-3.296-.216-4.073-1.724-1.337-2.595.33-5.731 2.105-7.633.695-.746
 1.684-1.333 2.276-2.154h-4.07V3.853z" />
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
