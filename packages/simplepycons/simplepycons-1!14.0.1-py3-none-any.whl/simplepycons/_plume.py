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


class PlumeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "plume"

    @property
    def original_file_name(self) -> "str":
        return "plume.svg"

    @property
    def title(self) -> "str":
        return "Plume"

    @property
    def primary_color(self) -> "str":
        return "#7C5CDF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Plume</title>
     <path d="M4.528
 9.532c0-.368.095-.735.284-1.063v-.001l2.94-5.093a3.776 3.776 0 0 1
 3.27-1.887l6.644.002c.294 0
 .526.262.476.565-.038.238-.261.402-.502.402l-6.618-.002c-1.004
 0-1.93.535-2.433 1.404L5.65 8.95h.001a1.17 1.17 0 0 0-.002
 1.16l-.001-.002 2.75 4.764a.087.087 0 0 1-.074.13h-.767a.348.348 0 0
 1-.301-.173L4.81 10.592v-.001a2.127 2.127 0 0 1-.282-1.059Zm.819
 6.926v.001a2.133 2.133 0 0 0 1.837 1.064h4.894c.124 0
 .24-.065.301-.173l.384-.664a.087.087 0 0 0-.076-.13H7.186h.001a1.163
 1.163 0 0 1-1.003-.583v.002l-2.94-5.092a2.809 2.809 0 0 1
 0-2.81l3.312-5.73c.12-.208.089-.483-.098-.636a.483.483 0 0
 0-.727.13L2.407 7.59a3.776 3.776 0 0 0 0 3.776Zm14.126-1.99c0
 .368-.096.735-.284 1.063v.001l-2.941 5.093a3.776 3.776 0 0 1-3.27
 1.887l-6.643-.002a.484.484 0 0
 1-.477-.565c.038-.238.262-.402.502-.402l6.618.002a2.81 2.81 0 0 0
 2.433-1.404l2.94-5.092a1.171 1.171 0 0 0
 .001-1.16l-2.75-4.763a.087.087 0 0 1 .076-.13h.766c.124 0
 .24.066.302.174l2.444 4.237.001.002c.188.328.282.694.282
 1.059zm-6.937 5.525H6.655a3.776 3.776 0 0 1-3.27-1.888L.065
 12.35a.483.483 0 0 1 .222-.683c.23-.104.503.005.63.224l3.306
 5.73a2.809 2.809 0 0 0 2.432 1.405h5.88-.002a1.171 1.171 0 0 0
 1.006-.578v.001l2.75-4.764a.087.087 0 0 1 .151 0l.383.663a.349.349 0
 0 1 0 .349l-2.447 4.236v.001a2.128 2.128 0 0 1-1.84
 1.06zm11.399-8.341-3.32-5.755a3.776 3.776 0 0
 0-3.27-1.888h-5.88a2.134 2.134 0 0 0-1.84 1.059l-.001.002-2.447
 4.236a.348.348 0 0 0 0 .348l.383.663a.087.087 0 0 0 .15
 0l2.751-4.764v.001a1.163 1.163 0 0 1 1.005-.578h5.88c1.003 0 1.93.535
 2.431 1.405l3.306 5.73c.127.22.4.328.63.224a.483.483 0 0 0
 .222-.683zM18.653 7.54l2.94 5.093a3.775 3.775 0 0 1 0 3.775l-3.324
 5.753a.484.484 0 0
 1-.727.13c-.187-.152-.218-.427-.097-.636l3.31-5.73a2.81 2.81 0 0 0
 .001-2.809l-2.94-5.09a1.173 1.173 0 0 0-1.003-.583h-5.5a.087.087 0 0
 1-.076-.13l.384-.664a.348.348 0 0 1 .301-.174l4.892.001h.002a2.128
 2.128 0 0 1 1.837 1.064z" />
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
