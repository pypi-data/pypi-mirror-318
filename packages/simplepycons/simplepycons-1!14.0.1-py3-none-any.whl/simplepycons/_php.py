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


class PhpIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "php"

    @property
    def original_file_name(self) -> "str":
        return "php.svg"

    @property
    def title(self) -> "str":
        return "PHP"

    @property
    def primary_color(self) -> "str":
        return "#777BB4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PHP</title>
     <path d="M7.01 10.207h-.944l-.515 2.648h.838c.556 0 .97-.105
 1.242-.314.272-.21.455-.559.55-1.049.092-.47.05-.802-.124-.995-.175-.193-.523-.29-1.047-.29zM12
 5.688C5.373 5.688 0 8.514 0 12s5.373 6.313 12 6.313S24 15.486 24
 12c0-3.486-5.373-6.312-12-6.312zm-3.26
 7.451c-.261.25-.575.438-.917.551-.336.108-.765.164-1.285.164H5.357l-.327
 1.681H3.652l1.23-6.326h2.65c.797 0 1.378.209 1.744.628.366.418.476
 1.002.33 1.752a2.836 2.836 0 0
 1-.305.847c-.143.255-.33.49-.561.703zm4.024.715l.543-2.799c.063-.318.039-.536-.068-.651-.107-.116-.336-.174-.687-.174H11.46l-.704
 3.625H9.388l1.23-6.327h1.367l-.327 1.682h1.218c.767 0 1.295.134
 1.586.401s.378.7.263 1.299l-.572 2.944h-1.389zm7.597-2.265a2.782
 2.782 0 0 1-.305.847c-.143.255-.33.49-.561.703a2.44 2.44 0 0
 1-.917.551c-.336.108-.765.164-1.286.164h-1.18l-.327
 1.682h-1.378l1.23-6.326h2.649c.797 0 1.378.209 1.744.628.366.417.477
 1.001.331 1.751zM17.766 10.207h-.943l-.516 2.648h.838c.557 0
 .971-.105
 1.242-.314.272-.21.455-.559.551-1.049.092-.47.049-.802-.125-.995s-.524-.29-1.047-.29z"
 />
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
