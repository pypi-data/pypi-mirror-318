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


class NixosIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nixos"

    @property
    def original_file_name(self) -> "str":
        return "nixos.svg"

    @property
    def title(self) -> "str":
        return "NixOS"

    @property
    def primary_color(self) -> "str":
        return "#5277C3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NixOS</title>
     <path d="M7.352 1.592l-1.364.002L5.32 2.75l1.557
 2.713-3.137-.008-1.32
 2.34H14.11l-1.353-2.332-3.192-.006-2.214-3.865zm6.175 0l-2.687.025
 5.846 10.127 1.341-2.34-1.59-2.765 2.24-3.85-.683-1.182h-1.336l-1.57
 2.705-1.56-2.72zm6.887 4.195l-5.846 10.125 2.696-.008 1.601-2.76
 4.453.016.682-1.183-.666-1.157-3.13-.008L21.778
 8.1l-1.365-2.313zM9.432 8.086l-2.696.008-1.601 2.76-4.453-.016L0
 12.02l.666 1.157 3.13.008-1.575 2.71 1.365 2.315L9.432 8.086zM7.33
 12.25l-.006.01-.002-.004-1.342 2.34 1.59 2.765-2.24 3.85.684
 1.182H7.35l.004-.006h.001l1.567-2.698 1.558 2.72
 2.688-.026-.004-.006h.01L7.33 12.25zm2.55 3.93l1.354 2.332 3.192.006
 2.215 3.865 1.363-.002.668-1.156-1.557-2.713 3.137.008
 1.32-2.34H9.881Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/NixOS/nixos-homepage/tree/'''

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
