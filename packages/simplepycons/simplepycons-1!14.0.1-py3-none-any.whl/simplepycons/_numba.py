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


class NumbaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "numba"

    @property
    def original_file_name(self) -> "str":
        return "numba.svg"

    @property
    def title(self) -> "str":
        return "Numba"

    @property
    def primary_color(self) -> "str":
        return "#00A3E0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Numba</title>
     <path d="M16.419 15.204s7.235-5.335
 4.305-8.786c-3.398-4.003-12.921 4.486-13.962 2.76-1.04-1.725
 8.452-5.86
 9.481-6.55.112-.075.144-.218.112-.383l1.099-.127-.685-.345.175-.685-.796.621C15.85
 1.173 15.34.595 15.049.393c-1.035-.685-2.93-.52-5.685.86-2.756
 1.38-9.147 5.685-5.877 10.51 2.93 4.306 11.35-3.094 12.756-1.9 1.205
 1.035-8.095 7.411-8.095 7.411h3.965C11.43 18.999 8.148 24 8.148
 24l11.934-8.621c-1.253-.186-3.663-.175-3.663-.175zM13.175.908a.776.776
 0 01.823.716.776.776 0 01-.717.823.776.776 0 01-.823-.716.768.768 0
 01.717-.823z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/numba/numba/blob/0db8a2bcd'''

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
