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


class OTwoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "o2"

    @property
    def original_file_name(self) -> "str":
        return "o2.svg"

    @property
    def title(self) -> "str":
        return "O2"

    @property
    def primary_color(self) -> "str":
        return "#0050FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>O2</title>
     <path d="M9.473.191C3.827.191 0 4.271 0 9.917c0 5.317 3.86 9.726
 9.472 9.726 5.61 0 9.433-4.409 9.433-9.726C18.905 4.27 15.116.19
 9.473.19zm-.002 2.77c3.677 0 5.79 3.422 5.79 6.956 0 3.314-1.785
 6.956-5.79 6.956-4.007 0-5.827-3.642-5.827-6.956 0-3.534 2.148-6.956
 5.827-6.956zm11.69 12.48a5.47 5.47 0 0 0-2.44.588l.13 1.367c.543-.353
 1.204-.66 1.9-.66.695 0 1.34.355 1.34 1.11 0 1.509-2.791 3.84-3.558
 4.584v1.38H24v-1.298h-3.36c1.344-1.32 3.1-2.924 3.1-4.668
 0-1.614-1.013-2.403-2.58-2.403z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.telefonica.de/presse/fotos/logos.'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.telefonica.de/presse/fotos/logos.'''

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
