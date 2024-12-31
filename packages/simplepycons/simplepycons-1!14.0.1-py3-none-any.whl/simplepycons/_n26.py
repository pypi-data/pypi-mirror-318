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


class NTwentySixIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "n26"

    @property
    def original_file_name(self) -> "str":
        return "n26.svg"

    @property
    def title(self) -> "str":
        return "N26"

    @property
    def primary_color(self) -> "str":
        return "#48AC98"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>N26</title>
     <path d="M0 3.803v1.195h7.436V3.803H0zM12.69 7.29c-2.034 0-3.038
 1.252-3.038 2.684 0 .234.027.468.092.728l1.393.135a3.697 3.697 0 0
 1-.09-.793c0-1.072.71-1.586 1.598-1.586.866 0 1.507.485 1.507 1.652 0
 1.186-.58 1.995-1.464 2.88-.925.923-2.4 2.027-3.112
 2.534v1.092h6.135v-1.195h-4.168c.695-.48 1.69-1.279
 2.133-1.72.502-.503 1.931-1.794 1.931-3.636
 0-1.903-1.24-2.775-2.918-2.775zm8.34 0c-1.976 0-3.454 1.517-3.454
 4.916 0 3.017 1.233 4.508 3.356 4.508 1.754 0 3.068-1.198 3.068-3.172
 0-1.542-.823-3.066-2.793-3.066-1.1 0-1.884.51-2.281 1.263
 0-1.78.62-3.33 2.094-3.33.937 0 1.309.538 1.507
 1.422l1.366-.271c-.321-1.527-1.292-2.27-2.864-2.27zM.075
 7.389v9.228h1.33v-6.312c0-.56-.013-.898-.039-1.223h.026c.136.372.298.699.539
 1.123l3.732 6.412h1.69V7.39H6.04v6.31c0 .56.013.898.04
 1.223h-.028a7.252 7.252 0 0 0-.537-1.123L1.783 7.389H.076zm20.817
 4.185c1.114 0 1.744.822 1.744 1.992 0 1.256-.717 2.034-1.701
 2.034-1.09 0-1.843-1.001-1.973-2.329.33-1.133 1.063-1.697
 1.93-1.697zM0 19.008v1.19h7.436v-1.19H0z" />
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
