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


class JetIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jet"

    @property
    def original_file_name(self) -> "str":
        return "jet.svg"

    @property
    def title(self) -> "str":
        return "JET"

    @property
    def primary_color(self) -> "str":
        return "#FBBA00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>JET</title>
     <path d="M15.778 19.044c3.048-.498 4.755-.73 8.219-2.395L24
 13.81c-3.228 3.225-9.249 5.146-15.07
 5.098-.75-.01-1.948.017-2.246-.024 3.1.49 6.18.556 9.094.159M3.836
 15.764c.75.003 1.805-.014 2.403-.394.535-.467.93-1.106
 1.247-1.828l1.545-4.697-2.157.013-1.199 3.664c-.225 1.161-.943
 1.566-1.483 1.483l-1.354-.097-.515 1.676
 1.513.18m13.29-.104l1.672-5.074h2.44l.543-1.665-5.907-.01-.556
 1.662H16.6l-1.73 5.077
 2.257.01m-3.859-.024l.564-1.718h-3.204l.297-.909h2.668l.543-1.641h-2.661l.262-.81h3.08l.57-1.713-5.267.027-2.205
 6.757 5.353.007m1.245-9.809c1.883-.072 3.743.083
 5.969.277-2.192-.809-5.7-1.407-8.344-1.407-4.344 0-8.644 1.054-12.117
 2.675L0 11.07c3.321-3.387 9.114-5.298 14.513-5.243" />
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
