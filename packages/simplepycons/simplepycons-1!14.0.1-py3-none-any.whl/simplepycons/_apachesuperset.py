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


class ApacheSupersetIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "apachesuperset"

    @property
    def original_file_name(self) -> "str":
        return "apachesuperset.svg"

    @property
    def title(self) -> "str":
        return "Apache Superset"

    @property
    def primary_color(self) -> "str":
        return "#20A6C9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apache Superset</title>
     <path d="M6.168 6.045C2.603 6.045 0 8.579 0 12.014c0 3.434 2.603
 5.941 6.168 5.941 2.184 0 3.888-1.026 5.775-3.078 1.53 2.033 4.037
 3.136 5.89 3.078 3.566 0 6.167-2.503 6.167-5.941
 0-3.438-2.601-5.97-6.168-5.97-2.864 0-5.138 2.425-5.771
 3.173-.76-.9-1.674-1.665-2.682-2.274-1.019-.588-2.084-.898-3.211-.898Zm2.875
 1.303c1.156.595 1.952 1.42 2.639 2.304-.534.63-1.245 1.483-1.739
 2.07-.56-.658-1.58-1.907-2.609-2.308ZM6.186 9.703c1.018.027 1.81.458
 3.435 2.408-1.158 1.378-2.202 2.244-3.435 2.244-1.51
 0-2.41-.99-2.41-2.31s.906-2.382 2.41-2.342zm11.535 0c1.51 0 2.408
 1.026 2.408 2.342 0 1.315-.862 2.301-2.402
 2.31-.571-.037-1.529-.026-3.442-2.314l.074-.09.002.002c1.122-1.328
 2.097-2.25 3.36-2.25zm-3.762 2.738c.61.68 1.795 1.988 2.713
 2.24l-1.684
 2.016h-.002c-.753-.371-2.031-1.134-2.716-2.215l1.689-2.04z" />
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
