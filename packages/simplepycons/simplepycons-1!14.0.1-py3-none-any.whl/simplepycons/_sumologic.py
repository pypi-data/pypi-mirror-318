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


class SumoLogicIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sumologic"

    @property
    def original_file_name(self) -> "str":
        return "sumologic.svg"

    @property
    def title(self) -> "str":
        return "Sumo Logic"

    @property
    def primary_color(self) -> "str":
        return "#000099"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sumo Logic</title>
     <path d="M4.922
 10.756v2.513h-.586v-.266c-.134.216-.379.341-.737.341-.595
 0-.89-.308-.89-.799v-1.79h.64v1.62c0 .262.142.416.417.416.32 0
 .516-.184.516-.52v-1.515zm4.161.757v1.756h-.64v-1.564c0-.3-.121-.483-.4-.483s-.441.208-.441.5v1.547h-.64v-1.564c0-.32-.134-.483-.4-.483-.283
 0-.441.208-.441.5v1.547H5.48v-2.513h.595v.279c.146-.242.387-.362.716-.362.32
 0 .561.133.699.37.17-.245.424-.37.753-.37.536 0 .84.32.84.84zm5.143
 1.756h-.64V9.774h.64zm6.949
 0h-.641v-2.513h.64zm-.654-2.892h.662v-.611h-.662zm3.055
 2.035c-.263.279-.441.387-.683.387-.287
 0-.49-.167-.582-.425v-.732c.095-.262.3-.428.59-.428.213 0
 .383.074.654.328l.4-.395c-.321-.35-.633-.478-1.053-.478-.587
 0-1.04.307-1.22.823v1.032c.175.516.62.82 1.203.82.453 0 .765-.15
 1.115-.583zm-22.257-.69c-.175-.038-.3-.072-.37-.088-.088-.025-.154-.058-.188-.104v-.192c.059-.091.2-.15.396-.15.27
 0 .457.063.753.296l.345-.416c-.35-.291-.649-.395-1.082-.395-.499
 0-.844.204-.982.495v.632c.109.212.358.333.858.441.178.042.3.071.37.084.091.029.175.066.22.133v.22c-.062.1-.212.154-.407.154a.977.977
 0 01-.408-.079 1.854 1.854 0 01-.454-.295L0 12.87c.4.353.736.474
 1.215.474.512 0 .874-.196
 1.011-.508V12.2c-.116-.237-.395-.362-.907-.479zm9.445-1.053c-.578
 0-1.032.312-1.215.81v1.058c.183.5.641.811 1.215.811.574 0 1.028-.312
 1.211-.807v-1.065c-.187-.495-.64-.807-1.21-.807zm.591
 1.71c-.1.266-.312.424-.595.424s-.495-.158-.6-.424v-.741c.1-.266.313-.429.6-.429s.491.163.59.429zm4.585-1.71c-.578
 0-1.032.312-1.219.81v1.058c.187.5.641.811 1.22.811.578 0 1.027-.312
 1.21-.807v-1.065c-.183-.495-.636-.807-1.21-.807zm.591
 1.71c-.1.266-.312.424-.59.424a.62.62 0
 01-.6-.424v-.741c.1-.266.312-.429.6-.429.286 0
 .49.163.59.429zm2.85-1.623v.279c-.162-.242-.416-.362-.765-.362-.475
 0-.857.29-1.024.753v1.036c.163.462.545.749 1.024.749.32 0
 .562-.108.732-.32v.2c0 .415-.241.61-.616.61-.278
 0-.507-.082-.873-.299l-.313.462c.354.237.77.366 1.195.37.707 0
 1.227-.378 1.227-1.086v-2.392zm-.079
 1.527c-.095.237-.295.387-.545.387a.574.574 0
 01-.545-.387v-.687a.572.572 0 01.545-.382c.254 0 .45.145.545.382z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://sites.google.com/sumologic.com/sumo-l'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://sites.google.com/sumologic.com/sumo-l'''

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
