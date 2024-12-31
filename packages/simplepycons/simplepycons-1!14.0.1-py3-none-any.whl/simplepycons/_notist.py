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


class NotistIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "notist"

    @property
    def original_file_name(self) -> "str":
        return "notist.svg"

    @property
    def title(self) -> "str":
        return "Notist"

    @property
    def primary_color(self) -> "str":
        return "#333333"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Notist</title>
     <path d="M5.9327
 3.8008c-1.099.11-2.288.4-3.038.74-1.069.499-1.259.869-.909 1.868.36
 1.0401.19 2.3081-1.0001 7.5053-.878 3.876-1.027 4.686-.977
 5.406.04.47.09.63.29.7901.22.179.33.189 1.688.129 3.408-.17
 4.0571-.22 4.2671-.34.24-.13.25-.2.44-1.758.32-2.8681 1.788-7.1552
 3.027-8.8942 1.0601-1.479 2.3591-2.128 3.0982-1.549.78.62.76
 1.559-.13 4.147-.68 1.999-.79 2.428-.909 3.617-.15 1.4601.13
 2.4891.96 3.4082.849.94 2.118 1.409 3.846 1.409 1.64 0 2.9681-.41
 4.3771-1.339 1.29-.86 2.8281-2.608
 3.0081-3.4281.1-.41-.07-.859-.35-.969-.41-.15-.65-.04-1.389.63-.859.78-1.249.949-2.008.889-1.0101-.08-1.4501-.66-1.4501-1.919
 0-.899.09-1.349.65-3.3171.79-2.728.93-3.9671.58-5.0271-.57-1.768-2.978-2.538-5.6461-1.798-1.449.41-3.238
 1.449-4.5971 2.688-.38.34-.68.59-.68.56
 0-.02.07-.35.16-.72.34-1.499.2-2.248-.479-2.598-.39-.2-1.599-.26-2.8281-.13z"
 />
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
