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


class MochaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mocha"

    @property
    def original_file_name(self) -> "str":
        return "mocha.svg"

    @property
    def title(self) -> "str":
        return "Mocha"

    @property
    def primary_color(self) -> "str":
        return "#8D6748"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mocha</title>
     <path d="M13.325 0c-.907 1.116-2.442 2.302-.768 4.814.558.628.838
 1.953.768 2.372 0 0
 2.512-1.464.977-4.116-.907-1.395-1.326-2.582-.977-3.07zm-2.79
 2.582c-.628.767-1.605 1.535-.489 3.279.35.349.489 1.256.489 1.535 0 0
 1.673-.978.627-2.792-.628-.907-.906-1.743-.627-2.022zm-5.094
 6a.699.699 0 0 0-.697.698c0 2.372.349 10.535 3.837
 14.512.14.139.28.208.489.208h5.86c.21 0 .35-.069.489-.208 3.488-3.908
 3.837-12.07 3.837-14.512a.7.7 0 0 0-.698-.699H12zm2.023
 2.163h9.21c.349 0 .697.278.697.697 0 1.953-.348 7.465-2.72
 10.326-.21.14-.35.208-.559.208H9.976a.633.633 0 0
 1-.488-.208c-2.372-2.79-2.652-8.373-2.722-10.326
 0-.35.28-.697.698-.697zm8.792 4.744s-.071.627-1.745
 1.255c-2.303.837-6.348.28-6.348.28.349 1.465.906 2.86 1.743
 3.907.07.14.28.209.419.209h3.489c.14 0 .279-.07.418-.209 1.186-1.395
 1.745-3.558 2.024-5.442z" />
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
