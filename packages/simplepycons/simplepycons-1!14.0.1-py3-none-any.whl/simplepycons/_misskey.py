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


class MisskeyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "misskey"

    @property
    def original_file_name(self) -> "str":
        return "misskey.svg"

    @property
    def title(self) -> "str":
        return "Misskey"

    @property
    def primary_color(self) -> "str":
        return "#A1CA03"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Misskey</title>
     <path d="M8.91076
 16.8915c-1.03957.0038-1.93213-.6294-2.35267-1.366-.22516-.3217-.66989-.4364-.6761
 0v2.0148c0 .8094-.29152 1.5097-.87581
 2.1002-.56755.573-1.25977.8595-2.0779.8595-.80014
 0-1.49298-.2865-2.07727-.8601C.28408 19.05 0 18.3497 0
 17.5403V6.45968c0-.62378.17553-1.18863.52599-1.69455.36657-.52284.83426-.88582
 1.4018-1.08769a2.84574 2.84574 0 0 1 1.00049-.17742c.90125 0
 1.65239.35421 2.25281 1.06262l2.99713
 3.51572c.06699.05016.263.43696.73192.43696.47016 0
 .6916-.3868.75796-.43758l2.9717-3.5151c.6178-.70841 1.377-1.06262
 2.2782-1.06262.3337 0 .6675.05893 1.0012.17742.5669.20187
 1.0259.56422 1.377 1.08769.3665.50592.5501 1.07077.5501
 1.69455V17.5403c0 .8094-.2915 1.5097-.8758
 2.1002-.5675.573-1.2604.8595-2.0779.8595-.8008
 0-1.493-.2865-2.0779-.8601-.5669-.5899-.8504-1.2902-.8504-2.0996v-2.0148c-.0496-.5499-.5303-.2032-.7009
 0-.4503.8431-1.31369 1.3616-2.35264 1.366ZM21.447 8.60998c-.7009
 0-1.3015-.24449-1.8019-.73348-.4838-.50571-.7257-1.11277-.7257-1.82118s.2419-1.30711.7257-1.79611c.5004-.50571
 1.101-.75856 1.8019-.75856.7009 0 1.3017.25285
 1.8025.75856.5003.489.7505 1.0877.7505 1.79611 0 .70841-.2502
 1.31547-.7505
 1.82118-.5008.48899-1.1016.73348-1.8025.73348Zm.0248.50655c.7009 0
 1.2935.25285 1.7777.75856.5003.50571.7505 1.11301.7505
 1.82181v6.2484c0 .7084-.2502 1.3155-.7505
 1.8212-.4838.489-1.0764.7335-1.7777.7335-.7005
 0-1.3011-.2445-1.8019-.7335-.5003-.5057-.7505-1.1128-.7505-1.8212v-6.2484c0-.7084.2502-1.3157.7505-1.82181.5004-.50571
 1.101-.75856 1.8019-.75856Z" />
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
