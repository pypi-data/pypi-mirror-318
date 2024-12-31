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


class IntelIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "intel"

    @property
    def original_file_name(self) -> "str":
        return "intel.svg"

    @property
    def title(self) -> "str":
        return "Intel"

    @property
    def primary_color(self) -> "str":
        return "#0071C5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Intel</title>
     <path d="M20.42 7.345v9.18h1.651v-9.18zM0
 7.475v1.737h1.737V7.474zm9.78.352v6.053c0 .513.044.945.13
 1.292.087.34.235.618.44.828.203.21.475.359.803.451.334.093.754.136
 1.255.136h.216v-1.533c-.24 0-.445-.012-.593-.037a.672.672 0 0
 1-.39-.173.693.693 0 0 1-.173-.377 4.002 4.002 0 0
 1-.037-.606v-2.182h1.193v-1.416h-1.193V7.827zm-3.505 2.312c-.396
 0-.76.08-1.082.241-.327.161-.6.384-.822.668l-.087.117v-.902H2.658v6.256h1.639v-3.214c.018-.588.16-1.02.433-1.299.29-.297.642-.445
 1.044-.445.476 0 .841.149 1.082.433.235.284.359.686.359
 1.2v3.324h1.663V12.97c.006-.89-.229-1.595-.686-2.09-.458-.495-1.1-.742-1.917-.742zm10.065.006a3.252
 3.252 0 0 0-2.306.946c-.29.29-.525.637-.692 1.033a3.145 3.145 0 0
 0-.254 1.273c0 .452.08.878.241 1.274.161.395.39.742.674
 1.032.284.29.637.526 1.045.693.408.173.86.26 1.342.26 1.397 0
 2.262-.637 2.782-1.23l-1.187-.904c-.248.297-.841.699-1.583.699-.464
 0-.847-.105-1.138-.321a1.588 1.588 0 0
 1-.593-.872l-.019-.056h4.915v-.587c0-.451-.08-.872-.235-1.267a3.393
 3.393 0 0 0-.661-1.033 3.013 3.013 0 0 0-1.02-.692 3.345 3.345 0 0
 0-1.311-.248zm-16.297.118v6.256h1.651v-6.256zm16.278 1.286c1.132 0
 1.664.797 1.664 1.255l-3.32.006c0-.458.525-1.255 1.656-1.261zm7.073
 3.814a.606.606 0 0 0-.606.606.606.606 0 0 0 .606.606.606.606 0 0 0
 .606-.606.606.606 0 0 0-.606-.606zm-.008.105a.5.5 0 0 1 .002 0 .5.5 0
 0 1 .5.501.5.5 0 0 1-.5.5.5.5 0 0 1-.5-.5.5.5 0 0 1
 .498-.5zm-.233.155v.699h.13v-.285h.093l.173.285h.136l-.18-.297a.191.191
 0 0 0 .118-.056c.03-.03.05-.074.05-.136
 0-.068-.02-.117-.063-.154-.037-.038-.105-.056-.185-.056zm.13.099h.154c.019
 0 .037.006.056.012a.064.064 0 0 1
 .037.031c.013.013.012.031.012.056a.124.124 0 0 1-.012.055.164.164 0 0
 1-.037.031c-.019.006-.037.013-.056.013h-.154Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.intel.com/content/www/us/en/newsr'''

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
