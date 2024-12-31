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


class EdxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "edx"

    @property
    def original_file_name(self) -> "str":
        return "edx.svg"

    @property
    def title(self) -> "str":
        return "edX"

    @property
    def primary_color(self) -> "str":
        return "#02262B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>edX</title>
     <path d="M6.359 10.416c.053.162.079.334.079.516a3.154 3.154 0 0
 1-.011.231h-3c.065-.236.152-.451.262-.644.109-.193.239-.359.39-.497.15-.138.318-.246.503-.321.184-.075.383-.113.595-.113.209
 0
 .392.036.549.108.156.071.288.169.394.292.107.123.186.266.239.428zm5.444-.4a1.206
 1.206 0 0 0-.436-.305 1.48 1.48 0 0 0-.58-.108c-.284
 0-.547.063-.79.19a1.952 1.952 0 0 0-.631.528 2.61 2.61 0 0 0-.421.808
 3.305 3.305 0 0 0-.154 1.029c0
 .233.033.446.1.641s.16.362.28.5c.12.138.263.246.431.323.168.077.354.116.56.116.287
 0 .553-.067.798-.203.244-.135.458-.32.639-.554a2.71 2.71 0 0 0
 .426-.826c.102-.316.154-.658.154-1.024
 0-.236-.033-.448-.098-.636a1.405 1.405 0 0 0-.278-.479zM24
 7.468l-2.398 11.276H10.727l.625-2.852H0L2.227 5.256h13.577l-.462
 2.212H24zM7.362 11.045a2.51 2.51 0 0 0-.169-.954 2.069 2.069 0 0
 0-.457-.7 1.951 1.951 0 0 0-.669-.434 2.22 2.22 0 0 0-.809-.148 2.73
 2.73 0 0 0-1.162.246 2.628 2.628 0 0 0-.911.695c-.253.3-.451.659-.593
 1.077a4.346 4.346 0 0 0-.212 1.393c0 .373.059.703.177.99a2.01 2.01 0
 0 0 1.198 1.172c.273.101.564.151.872.151.321 0
 .616-.039.885-.115a2.55 2.55 0 0 0
 .708-.318c.204-.135.372-.295.505-.48a1.84 1.84 0 0 0
 .287-.595h-.938a1.279 1.279 0 0
 1-.508.513c-.222.126-.517.19-.883.19-.168 0-.333-.028-.497-.085a1.202
 1.202 0 0 1-.444-.274 1.41 1.41 0 0 1-.321-.49 1.913 1.913 0 0
 1-.123-.726c0-.048.001-.094.003-.138.002-.044.004-.09.008-.138h3.986c.01-.051.019-.114.026-.187l.02-.226a6.153
 6.153 0 0 0 .021-.419zm5.036 3.392L14.04 6.71h-.898l-.682
 3.217h-.082a1.406 1.406 0 0 0-.228-.454 1.56 1.56 0 0 0-.375-.354
 1.786 1.786 0 0 0-.487-.228 1.93 1.93 0 0 0-.567-.082 2.506 2.506 0 0
 0-1.45.456 2.892 2.892 0 0 0-.575.534c-.173.208-.32.442-.444.7a3.925
 3.925 0 0 0-.285.841c-.066.303-.1.62-.1.952 0
 .342.053.652.159.929.106.277.25.513.434.708.183.195.395.345.639.449.243.105.503.157.78.157.352
 0
 .681-.076.985-.228.304-.152.557-.36.759-.623h.082l-.159.754h.852zm6.116-1.39l3.578-4.125H20.09l-2.184
 2.704h-.108l-1.155-2.704h-2.025l1.736 3.928-3.748
 4.44h1.976l2.406-2.852h.162l1.3 2.852h1.988l-1.924-4.243z" />
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
