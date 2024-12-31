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


class HoneygainIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "honeygain"

    @property
    def original_file_name(self) -> "str":
        return "honeygain.svg"

    @property
    def title(self) -> "str":
        return "Honeygain"

    @property
    def primary_color(self) -> "str":
        return "#F9C900"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Honeygain</title>
     <path d="M18.721 3.048a1.352 1.352 0 0 0-1.38 1.56 6.38 6.38 0 0
 0-1.864 3.2l-.77-.001c-.63 0-1.35.003-2.12.016l-7.965-.028A4.394
 4.394 0 0 0 3.4 16.463l.002.002-2.096 3.543 4.343-1.48c2.612 1.705
 6.279 2.425 10.278 2.425a6.572 6.572 0 0 0 3.058-12.39 4.972 4.972 0
 0 1 2.552-1.16 1.352 1.352 0 1 0-.096-1.377c-1.47.188-2.787.861-3.881
 1.987-.22-.056-.443-.1-.67-.134a4.937 4.937 0 0 1 1.331-2.208 1.352
 1.352 0 1 0 .5-2.623ZM4.391 9.167c.053 0 .106 0
 .16.004l.033.001h.033l7.936.028-6.08 5.168-.021.018-.02.018a3.002
 3.002 0 0 1-2.195.793 3.02 3.02 0 0 1-2.856-3.17 3.014 3.014 0 0 1
 3.01-2.86Zm10.553.017h.455l.528.001a5.201 5.201 0 0 1 5.196 5.196 5.2
 5.2 0 0 1-5.196 5.195c-.354
 0-.701-.007-1.043-.018-1.779-1.578-2.676-3.269-2.665-5.026.021-3.025
 2.698-5.325 2.725-5.348zm-3.628 2.875a7.142 7.142 0 0 0-.474
 2.463c-.011 1.722.65 3.36 1.963 4.889a20.2 20.2 0 0
 1-2.575-.45c-1.076-1.835-1.427-3.545-1.045-5.091Zm-3.659 3.11c.008
 1.037.254 2.112.736 3.218-1.252-.488-2.297-1.124-3.118-1.898a4.393
 4.393 0 0 0 2.089-1.071Zm9.237-4.08a1.7 1.7 0 1 0 0 3.4 1.7 1.7 0 0 0
 0-3.4zm-.431.723a.545.545 0 0 1 .521.708.535.535 0 0
 1-.309.341.538.538 0 0 1-.322.032.535.535 0 0 1-.311-.188.552.552 0 0
 1-.122-.403.563.563 0 0 1 .09-.25.549.549 0 0 1 .453-.24z" />
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
