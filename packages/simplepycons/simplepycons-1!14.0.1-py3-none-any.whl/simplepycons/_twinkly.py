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


class TwinklyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "twinkly"

    @property
    def original_file_name(self) -> "str":
        return "twinkly.svg"

    @property
    def title(self) -> "str":
        return "Twinkly"

    @property
    def primary_color(self) -> "str":
        return "#FCC15E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Twinkly</title>
     <path d="M20.0413 0H4.0304C1.8333 0 0 1.7968 0 3.9939v16.0116C0
 22.2019 1.8333 24 4.0304 24h16.0109C22.2384 24 24 22.2019 24
 20.0055V3.9939C24 1.7968 22.2384 0 20.0413 0zm.4101
 10.3762c-.0781.343-.2058.6212-.3418.8641-.2763.4865-.5909.861-.9182
 1.221-.265.2895-1.0359 1.0642-1.2763 1.3002a.1197.1197 0 0
 0-.0277.1296c.1347.3355.6124 1.3934.6262 2.8007.012 1.2795-.1567
 2.1631-.1932 2.3312-.1473.6879-.8541
 1.0611-1.5155.9736-.0409-.0051-1.0353-.0957-3.0939-1.2871-.7093-.4103-1.4022-1.107-1.4022-1.107l-.0164.0138c-1.5898
 1.6502-3.8202 2.7333-3.8202
 2.7333-.854.4242-1.89.0761-2.3148-.7772-.083-.1674-.4934-1.535-.2196-3.8416.0642-.5425.4179-1.8182.4487-1.9133-.1208-.1063-1.2147-1.2449-1.5929-1.732-1.3499-1.7352-1.2952-2.469-1.2952-2.469.0629-.9465.9201-1.3694
 1.0938-1.4638.3398-.1756.6683-.2946 1.0013-.389.6627-.19 1.3405-.2473
 1.9994-.1989.6577.0459 1.2977.1888 1.8812.4355.5847.2404 1.1209.5551
 1.5891.9346.472.3688.8779.7987 1.2373
 1.2493.0529.0661.0566.163.0019.2272a.175.175 0 0
 1-.2196.0403l-.0031-.0019c-.9786-.5457-1.9913-.9459-2.9844-1.0479-.4966-.0446-.9787-.044-1.4394.0428-.3575.0648-.6942.18-1.0108.3185a.0566.0566
 0 0 0-.0189.09c.2127.2316.9069.9881 2.4854 1.9516.7961.4852 1.2405
 1.0076.9805 1.8 0 0-.7294 2.0743-.5683 2.1228.1611.0484 2.0876-1.5042
 2.0876-1.5042.6665-.4525 1.4564-.3292 2.0335.3732 1.0894 1.3254
 2.2651 2.2846 2.3664
 2.2191.1007-.0655-.1353-1.6867-.5564-3.1166-.146-.4966.0661-.8603.4003-1.1077.3096-.2284
 2.087-1.6212
 2.6037-2.3475.2379-.3342.2064-.4638-.1888-.5998-1.6445-.5652-3.3797.0277-3.3797.0277a.6343.6343
 0 0 1-.8201-.3663.642.642 0 0
 1-.0396-.1976c-.0403-.8635-.2158-1.7383-.5368-2.552-.2656-.6722-.6325-1.3009-1.1165-1.8233a.062.062
 0 0 0-.0925.0019c-.3229.3757-.6231.7691-.8628 1.2096-.4651.8553-.5709
 1.5218-.6741
 1.8566-.0132.0447-.0573.0686-.1064.0812-.0919.0239-.1769-.0554-.1693-.1498.1372-1.7559
 1.2745-3.323
 1.715-3.8712.1252-.1548.1441-.197.304-.0818l.0365.0209c.827.601
 1.4551 1.4305 1.9107 2.3198.3147.618.552 1.2707.7187 1.946a.0687.0687
 0 0 0 .0875.0491c.6564-.1995 1.3424-.2807
 2.0064-.2706.4897.0107.9252.0466
 1.4387.1473.2757.0598.5463.1466.8434.3109.2876.163.6199.4374.81.8597.1951.4197.1843.8767.1082
 1.214z" />
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
