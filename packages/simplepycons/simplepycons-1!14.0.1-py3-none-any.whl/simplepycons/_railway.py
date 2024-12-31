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


class RailwayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "railway"

    @property
    def original_file_name(self) -> "str":
        return "railway.svg"

    @property
    def title(self) -> "str":
        return "Railway"

    @property
    def primary_color(self) -> "str":
        return "#0B0D0E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Railway</title>
     <path d="M.113 10.27A13.026 13.026 0 000
 11.48h18.23c-.064-.125-.15-.237-.235-.347-3.117-4.027-4.793-3.677-7.19-3.78-.8-.034-1.34-.048-4.524-.048-1.704
 0-3.555.005-5.358.01-.234.63-.459 1.24-.567
 1.737h9.342v1.216H.113v.002zm18.26
 2.426H.009c.02.326.05.645.094.961h16.955c.754 0 1.179-.429
 1.315-.96zm-17.318 4.28s2.81 6.902 10.93 7.024c4.855 0 9.027-2.883
 10.92-7.024H1.056zM11.988 0C7.5 0 3.593 2.466 1.531
 6.108l4.75-.005v-.002c3.71 0 3.849.016 4.573.047l.448.016c1.563.052
 3.485.22 4.996 1.364.82.621 2.007 1.99 2.712 2.965.654.902.842
 1.94.396 2.934-.408.914-1.289 1.458-2.353
 1.458H.391s.099.42.249.886h22.748A12.026 12.026 0 0024 12.005C24
 5.377 18.621 0 11.988 0z" />
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
