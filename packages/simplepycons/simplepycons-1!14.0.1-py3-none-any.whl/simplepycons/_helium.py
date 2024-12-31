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


class HeliumIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "helium"

    @property
    def original_file_name(self) -> "str":
        return "helium.svg"

    @property
    def title(self) -> "str":
        return "Helium"

    @property
    def primary_color(self) -> "str":
        return "#0ACF83"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Helium</title>
     <path d="M12 0c6.6274 0 12 5.3726 12 12s-5.3726 12-12 12S0
 18.6274 0 12 5.3726 0 12 0Zm2.5535 5.6062a2.7033 2.7033 0 0 0-.7421
 1.3856c-1.923-.7238-4.1285-.264-5.5968 1.2045-1.4696 1.4696-1.929
 3.6777-1.2024 5.6018a2.7037 2.7037 0 0 0-1.3947.7441c-1.0604
 1.0604-1.0604 2.7799 0 3.8403 1.0605 1.0604 2.7798 1.0604 3.8403
 0a2.7035 2.7035 0 0 0 .746-1.4034 5.255 5.255 0 0 0 1.8373.332c1.3756
 0 2.7344-.5344 3.7442-1.5442 1.463-1.463 1.9253-3.6579
 1.2127-5.576a2.703 2.703 0 0 0 1.3957-.7444c1.0605-1.0604
 1.0605-2.7798 0-3.8403-1.0604-1.0604-2.7798-1.0604-3.8402 0zm3.1724
 3.1725c-.4029.403-.9577.5877-1.5231.5072a.3058.3058 0 0
 0-.0793.0001.9214.9214 0 0 0-.9875.6035.9208.9208 0 0 0
 .0307.7007c.602 1.3006.3253 2.8556-.6886 3.8695-1.014 1.0138-2.569
 1.291-3.87.6884a.9211.9211 0 0 0-.7098-.0276.9212.9212 0 0
 0-.5172.4781.9195.9195 0 0 0-.0831.4539.308.308 0 0 0 0 .0915 1.7992
 1.7992 0 0 1-.5009 1.5636c-.6991.699-1.8368.699-2.5362 0a1.7821
 1.7821 0 0
 1-.5252-1.2681c0-.4791.1865-.9295.5252-1.2682.4028-.4029.9579-.5873
 1.5516-.506a.921.921 0 0 0 .1824.0205c.13 0
 .262-.0277.3877-.0858a.9213.9213 0 0 0 .4753-.5104.921.921 0 0
 0-.0247-.7167c-.602-1.3006-.3253-2.8555.6886-3.8694 1.014-1.014
 2.5692-1.2909 3.87-.6885a.9212.9212 0 0 0 .7074.0287.9218.9218 0 0 0
 .5197-.4792c.083-.1793.103-.3715.07-.5583a1.7988 1.7988 0 0 1
 .5009-1.5637c.6991-.6993 1.8369-.6993 2.536 0 .6993.6993.6993 1.837 0
 2.5362zm-7.1177 1.8111c-.7758.7759-.7758 2.0337 0 2.8095.7759.776
 2.0338.776 2.8096 0 .7758-.7758.7758-2.0336
 0-2.8095-.7758-.7757-2.0337-.7757-2.8096 0z" />
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
