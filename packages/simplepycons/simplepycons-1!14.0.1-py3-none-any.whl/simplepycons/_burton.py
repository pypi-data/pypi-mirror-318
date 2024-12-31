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


class BurtonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "burton"

    @property
    def original_file_name(self) -> "str":
        return "burton.svg"

    @property
    def title(self) -> "str":
        return "Burton"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Burton</title>
     <path d="M11.9852 1.5427a.2544.2544 0 00-.2098.1167l-.9744
 1.5088a.624.624 0 01-.3532.2618l-.5747.1643a.7493.7493 0
 00-.4524.362L6.9551 8.4735a.7424.7424 0
 01-.48.3695c-.1543.036-.3882.0866-.6213.132a.5525.5525 0
 00-.4013.3226c-.2956.6863-.8678 2.0149-1.1562 2.6826a1.0018 1.0018 0
 01-.5097.5162l-.4244.1906a1.0061 1.0061 0 00-.5425.6013s-.6473
 1.6657-1.1468 3.1669c-.4515 1.3568-1.6317 5.445-1.6317
 5.445a.4273.4273 0 00.0904.4915.32.32 0 00.466-.1066s1.5767-3.3727
 2.1518-4.473a.3106.3106 0
 01.4612-.093c.2536.165.3786.6073.6632.8644a.2578.2578 0
 00.4215-.1034c.206-.5042.6888-2.0741.8511-2.7236.1356-.5411.5956-.5898.858-.1938l.1896.2345a2.2525
 2.2525 0 00.7133.592l.3496.1853a.5006.5006 0
 01.2283.2446l.3828.8973a.7493.7493 0 00.6609.455l.119.0046a.7503.7503
 0 01.633.3978c.176.3314.4613.9323.7038 1.326a.2593.2593 0
 00.4735-.0595 15.4276 15.4276 0
 00.5997-2.0607c.1408-.7166.5788-.625.7299-.431.0551.07.245.3576.2966.4163a.252.252
 0 00.4586-.0972 12.312 12.312 0
 00.4033-1.9043c.0386-.2912.358-.3281.5106-.0793.1629.2657.4287.741.5734
 1.0232a2.5873 2.5873 0 01.2358.6163l.211.9516a2.1773 2.1773 0 00.6662
 1.1276 3.3829 3.3829 0 00.4768.4219.2676.2676 0
 00.4091-.1054c.111-.2548.2517-.6868.335-.9354a.2534.2534 0
 01.1925-.1675c.1073-.0211.1794-.0303.333-.0712a.8444.8444 0
 00.564-.4918l.207-.4995a.257.257 0
 01.4663-.012c.0751.1353.2088.4168.2716.572a1.975 1.975 0
 01.089.2462l.1647.6362a2.248 2.248 0 00.2894.659l.0752.1167a2.1315
 2.1315 0 00.7848.7217.2476.2476 0
 00.3496-.1217c.2348-.5461.3253-1.3597.4332-1.8837a.285.285 0
 01.5162-.0924c.6114 1.0018 2.3264 3.921 2.3264 3.921a.3122.3122 0
 00.5409-.3096c-.0432-.0988-1.5061-3.7875-2.912-7.0531-1.2846-2.9848-2.5247-5.5752-2.5247-5.5752a.4576.4576
 0 00-.5568-.2469c-.3762.1119-.7863.357-1.071.4557a.5375.5375 0
 01-.6466-.2528c-.3467-.6362-1.1121-2.2981-1.8152-3.6137-.7611-1.4239-1.7256-3.3197-2.2431-4.069a.2544.2544
 0 00-.2134-.1096z" />
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
