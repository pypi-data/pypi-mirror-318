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


class FiverrIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fiverr"

    @property
    def original_file_name(self) -> "str":
        return "fiverr.svg"

    @property
    def title(self) -> "str":
        return "Fiverr"

    @property
    def primary_color(self) -> "str":
        return "#1DBF73"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fiverr</title>
     <path d="M23.004 15.588a.995.995 0 1 0 .002-1.99.995.995 0 0
 0-.002 1.99zm-.996-3.705h-.85c-.546 0-.84.41-.84
 1.092v2.466h-1.61v-3.558h-.684c-.547 0-.84.41-.84
 1.092v2.466h-1.61v-4.874h1.61v.74c.264-.574.626-.74
 1.163-.74h1.972v.74c.264-.574.625-.74 1.162-.74h.527v1.316zm-6.786
 1.501h-3.359c.088.546.43.858 1.006.858.43 0
 .732-.175.83-.487l1.425.4c-.351.848-1.22 1.364-2.255 1.364-1.748
 0-2.549-1.355-2.549-2.515 0-1.14.703-2.505 2.45-2.505 1.856 0 2.471
 1.384 2.471 2.408 0
 .224-.01.37-.02.477zm-1.562-.945c-.04-.42-.342-.81-.889-.81-.508
 0-.81.225-.908.81h1.797zM7.508 15.44h1.416l1.767-4.874h-1.62l-.86
 2.837-.878-2.837H5.72l1.787 4.874zm-6.6
 0H2.51v-3.558h1.524v3.558h1.591v-4.874H2.51v-.302c0-.332.235-.536.606-.536h.918V8.412H2.85c-1.162
 0-1.943.712-1.943 1.755v.4H0v1.316h.908v3.558z" />
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
