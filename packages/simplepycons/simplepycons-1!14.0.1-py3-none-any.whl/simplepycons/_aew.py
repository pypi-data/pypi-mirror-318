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


class AewIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "aew"

    @property
    def original_file_name(self) -> "str":
        return "aew.svg"

    @property
    def title(self) -> "str":
        return "AEW"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AEW</title>
     <path d="M0 6.925v10.086h3.674v-.51H.53V7.435h4.526v-.51zm18.944
 0v.511h4.526V16.5h-3.144v.511H24V6.925zm-7.727-.891v1.453h1.537v-.383H11.71V6.91h.86v-.336h-.86v-.157h1.044v-.383H11.71zm1.765
 0v1.453h1.39V7.06h-.897V6.034zm1.551 0v1.453h.493V6.034zm.648
 0v.427h.557v1.026h.493V6.461h.558v-.427h-1.051zm1.765
 0v1.453h1.537v-.383H17.44V6.91h.86v-.336h-.86v-.157h1.044v-.383H17.44zM11.45
 8.225l-3.785.006.015 3.466 1.57
 4.01h5.144l-.707-1.77H9.84V10h2.32zm-1.288
 2.862v1.77h3.107l-.712-1.77zM6.265 6.034l-.748
 1.453h.538l.122-.278h.699l.135.278h.536l-.753-1.453zm1.363
 0v1.453h1.39V7.06h-.897V6.034zm1.55
 0v1.453h1.39V7.06h-.896V6.034zm-2.65.444l.187.391h-.377zm16.29
 1.73l-2.148.003-1.368 3.47-.938-3.467-2.142.003-.92
 3.443-1.355-3.44-2.177.004 2.966 7.483h1.633l.938-3.462.934
 3.462h1.653zm-16.844.025l-1.845.003-2.946
 7.472H3.37l.342-.9h2.333l-.686-1.747h-.955l.635-1.673 1.706
 4.32h2.17zm13.091 8.195c-.398.002-.663.14-.805.316a.76.76 0
 00.005.91c.603.625 1.574.134
 1.632.008v-.622h-.892v.344h.405v.086c-.114.152-.598.143-.722-.053-.124-.225-.038-.374.008-.444.277-.3.753-.062.784.004l.365-.293a1.332
 1.332 0 00-.78-.256zm-7.877.01a2.177 2.177 0
 00-.269.02c-.293.06-.476.207-.517.346-.128.491.571.567.571.567.623.03.571.098.572.123-.065.136-.42.087-.529.07-.221-.042-.43-.186-.43-.186l-.271.3c.76.482
 1.38.226
 1.48.17.3-.171.29-.484.192-.621-.076-.093-.307-.207-.535-.232-.204-.048-.604-.011-.558-.141.06-.12.682-.04.845.095l.24-.295c-.233-.168-.517-.22-.791-.216zm-7.085.047l.504
 1.397h.505l.278-.854.266.854h.506l.502-1.397h-.497l-.258.866-.297-.866h-.444l-.294.874-.265-.874zm2.693
 0v1.397h.502v-.392h.31l.324.392h.591l-.384-.448c.6-.234.334-.927-.234-.95h-.06zm1.89
 0v1.397h1.537v-.328H9.18v-.195h.86v-.335h-.86v-.158h1.044v-.381zm3.427
 0v.413h.557v.984h.494v-.984h.557v-.413zm1.758
 0v1.397h1.39V17.5h-.897v-1.016zm1.562 0v1.397h.493V16.485zm.766
 0v1.397h.493v-.804l.772.804h.466v-1.396h-.493v.761l-.716-.761zm-8.904.372h.531c.19-.003.189.286
 0 .292h-.53z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:AEW_L'''

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
        yield from [
            "All Elite Wrestling",
        ]
