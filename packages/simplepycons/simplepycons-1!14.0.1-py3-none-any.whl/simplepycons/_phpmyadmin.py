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


class PhpmyadminIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "phpmyadmin"

    @property
    def original_file_name(self) -> "str":
        return "phpmyadmin.svg"

    @property
    def title(self) -> "str":
        return "phpMyAdmin"

    @property
    def primary_color(self) -> "str":
        return "#6C78AF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>phpMyAdmin</title>
     <path d="M5.463 3.476C6.69 5.225 7.497 7.399 7.68 9.798a12.9 12.9
 0 0 1-.672 5.254 4.29 4.29 0 0 1
 2.969-1.523c.05-.004.099-.006.148-.008.08-.491.47-3.45-.977-6.68-1.068-2.386-3-3.16-3.685-3.365Zm1.777.037s2.406
 1.066 3.326 5.547c.607 2.955.049 4.836-.402 5.773a7.347 7.347 0 0 1
 4.506-1.994c.86-.065 1.695.02
 2.482.233-.1-.741-.593-3.414-2.732-5.92-3.263-3.823-7.18-3.64-7.18-3.64Zm14.817
 9.701-17.92 3.049a2.284 2.284 0 0 1 1.535 2.254 2.31 2.31 0 0
 1-.106.61c.055-.027 2.689-1.275 6.342-2.034 3.238-.673 5.723-.36
 6.285-.273a6.46 6.46 0 0 1 3.864-3.606zm-6.213 4.078c-2.318
 0-4.641.495-6.614 1.166-2.868.976-2.951 1.348-5.55 1.043C1.844 19.286
 0 18.386 0 18.386s2.406 1.97 4.914 2.127c1.986.125 3.505-.822
 5.315-1.414 2.661-.871 4.511-.97 6.253-.975C19.361 18.116 24 19.353
 24 19.353s-2.11-1.044-5.033-1.72a13.885 13.885 0 0 0-3.123-.34Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/phpmyadmin/data/blob/b7d3b'''

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
