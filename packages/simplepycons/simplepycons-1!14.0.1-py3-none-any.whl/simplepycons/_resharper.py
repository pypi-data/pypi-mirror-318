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


class ResharperIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "resharper"

    @property
    def original_file_name(self) -> "str":
        return "resharper.svg"

    @property
    def title(self) -> "str":
        return "ReSharper"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ReSharper</title>
     <path d="M24 0H0v24h24V0ZM3.006
 19.476h9v1.5h-9v-1.5Zm9.824-9.392h-.98V8.432h1.264l.324-1.908h-1.136V4.872h1.416l.324-1.864h1.704l-.332
 1.864h1.88l.324-1.864h1.7l-.304 1.864h.98v1.652h-1.28l-.324
 1.908h1.136v1.652h-1.42l-.336 1.936h-1.7l.332-1.936h-1.868l-.32
 1.936h-1.72l.336-1.936ZM3.014 3.008H7.15c1.144 0 2.021.304
 2.632.912.529.553.808 1.3.772 2.064v.028a2.802 2.802 0 0 1-.536 1.784
 3.065 3.065 0 0 1-1.404.992l2.204 3.224h-2.32L6.63
 9.24H5.014v2.772h-2V3.008Zm13.672 5.424.328-1.908h-1.876l-.32
 1.908h1.868ZM7.014 7.408c.415.014.821-.129 1.136-.4a1.2 1.2 0 0 0
 .4-.928v-.028a1.156 1.156 0 0 0-.4-.968 1.836 1.836 0 0
 0-1.148-.32H5.014v2.592l2 .052Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.jetbrains.com/company/brand/logos'''

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
