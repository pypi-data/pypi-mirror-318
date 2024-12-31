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


class SartoriusIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sartorius"

    @property
    def original_file_name(self) -> "str":
        return "sartorius.svg"

    @property
    def title(self) -> "str":
        return "Sartorius"

    @property
    def primary_color(self) -> "str":
        return "#FFED00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sartorius</title>
     <path d="M21.3766 12.4988c0 .6105-.2898 1.0715-.9317
 1.0715s-.9315-.4733-.9315-1.0715V9.988h-.588v2.51c0 .8212.5135 1.5959
 1.5195 1.5959.9829 0 1.5097-.7747 1.5097-1.5958v-.1646h-.578zm-3.8398
 1.5133h.588V9.988h-.588Zm-5.3263-4.0183h-.095v.5125h.095c.8374 0
 1.498.6697 1.498 1.5316 0 .8678-.6606 1.5375-1.498
 1.5375s-1.4991-.6697-1.4991-1.5375h-.5463c0 1.1473.905 2.05 2.0454
 2.05s2.0442-.9027
 2.0442-2.05c0-1.1415-.9038-2.044-2.0442-2.044m11.052
 1.7986c-.2856-.1283-.6287-.1934-.8787-.2983-.2737-.1168-.3738-.2753-.3738-.5377
 0-.315.2618-.5543.6604-.5543.5237 0
 .768.2568.7796.6302h.5294c.0178-.5835-.4045-1.1262-1.309-1.1262-.7437
 0-1.2386.4611-1.2386 1.0445 0
 .495.231.7768.5999.9751.2856.1517.5851.1868.8648.2917.4089.1513.5329.3598.5329.6551
 0 .4044-.278.6626-.7362.6626h-.058v.4782h.0348c.8139 0 1.33-.5083
 1.33-1.1435.0001-.4174-.2027-.8387-.7375-1.0774m-6.4054-.5346c0-.728-.5226-1.2695-1.277-1.2695h-1.194v.5302h1.1752c.38
 0 .7484.297.7484.739 0
 .4252-.3387.7455-.7662.7455h-.62v.53l.467-.0046.7814
 1.484h.6475l-.8442-1.552c.4416-.1346.8819-.5913.8819-1.2032ZM11.3194
 9.988H8.3478v.5293h.7138v3.495h.5819v-3.495h1.6759zm-7.312 0L2.469
 14.0123h.5705l1.2708-3.3314 1.3126 3.3314h.6118L4.6132 9.988ZM.553
 12.761v-.215H.0005v.2147c-.0178.652.4202 1.2525 1.412
 1.2525h.0355v-.4887h-.0356c-.5287
 0-.8594-.3379-.8594-.7632zm1.4118-.9614c-.2852-.128-.6474-.198-.897-.303-.2732-.1159-.3564-.2795-.3564-.5417
 0-.3146.2608-.5534.6594-.5534.5227 0
 .7662.2563.7781.6292h.5285c.0178-.5827-.4039-1.1245-1.3069-1.1245-.7426
 0-1.2415.4602-1.2416 1.0433 0
 .466.1903.7806.5822.9785.2852.145.594.1865.8733.2913.297.1107.41.204.4514.3671h.6c-.0829-.3437-.3146-.6229-.671-.7865zm6.1307-.5426c0-.728-.5226-1.2695-1.277-1.2695h-1.216v.53h1.1972c.38
 0 .7483.297.7483.739 0
 .4252-.3385.7454-.7661.7454h-.6415v.53l.4894-.0046.7812
 1.484h.6474l-.8437-1.552c.4405-.1334.8808-.59.8808-1.202z" />
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
