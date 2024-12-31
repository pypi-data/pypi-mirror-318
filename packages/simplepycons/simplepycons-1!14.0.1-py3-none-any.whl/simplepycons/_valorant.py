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


class ValorantIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "valorant"

    @property
    def original_file_name(self) -> "str":
        return "valorant.svg"

    @property
    def title(self) -> "str":
        return "Valorant"

    @property
    def primary_color(self) -> "str":
        return "#FA4454"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Valorant</title>
     <path d="M23.792 2.152a.252.252 0 0 0-.098.083c-3.384 4.23-6.769
 8.46-10.15 12.69-.107.093-.025.288.119.265 2.439.003 4.877 0
 7.316.001a.66.66 0 0 0 .552-.25c.774-.967 1.55-1.934
 2.324-2.903a.72.72 0 0 0 .144-.49c-.002-3.077
 0-6.153-.003-9.23.016-.11-.1-.206-.204-.167zM.077
 2.166c-.077.038-.074.132-.076.205.002 3.074.001 6.15.001
 9.225a.679.679 0 0 0 .158.463l7.64 9.55c.12.152.308.25.505.247 2.455
 0 4.91.003 7.365 0 .142.02.222-.174.116-.265C10.661 15.176 5.526
 8.766.4 2.35c-.08-.094-.174-.272-.322-.184z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Valor'''

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
