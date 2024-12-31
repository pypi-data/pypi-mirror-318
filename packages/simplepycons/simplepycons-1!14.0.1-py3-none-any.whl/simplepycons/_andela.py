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


class AndelaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "andela"

    @property
    def original_file_name(self) -> "str":
        return "andela.svg"

    @property
    def title(self) -> "str":
        return "Andela"

    @property
    def primary_color(self) -> "str":
        return "#173B3F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Andela</title>
     <path d="M20.999 4.586 13.956.511A3.94 3.94 0 0 0 12 0c-.713
 0-1.378.183-1.946.511L2.982 4.586a4.013 4.013 0 0 0-1.917
 3.42v7.997a3.99 3.99 0 0 0 1.927 3.421l7.014 4.046c.587.337 1.262.53
 1.994.53.723 0 1.407-.193 1.994-.53l6.937-4.008a4.008 4.008 0 0 0
 2.004-3.468V7.997a4.003 4.003 0 0 0-1.936-3.411Zm.298
 7.534h-.038c-5.039.02-9.143 4.143-9.143 9.182a.117.117 0 0
 1-.116.116.118.118 0 0
 1-.116-.116v-.038c-.019-5.039-4.143-9.144-9.181-9.144a.116.116 0 0
 1-.116-.115c0-.068.058-.116.116-.116h.038c5.039-.019 9.143-4.143
 9.143-9.182 0-.067.058-.115.116-.115.067 0 .116.058.116.115 0 5.059
 4.114 9.182 9.181 9.182.068 0
 .116.058.116.116.01.067-.048.115-.116.115Z" />
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
