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


class ZebraTechnologiesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zebratechnologies"

    @property
    def original_file_name(self) -> "str":
        return "zebratechnologies.svg"

    @property
    def title(self) -> "str":
        return "Zebra Technologies"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zebra Technologies</title>
     <path d="M5.145
 13.109H4.6v-1.545l.545.546v.999zm-2.183-.095.546.546v.771L2.417
 13.24v-3.092L1.003 8.739a2.73 2.73 0 0 1 .465-.306l1.494
 1.489V8.126a.899.899 0 0 1 .084
 1.793h.7l.002.003.543.543H2.962v2.549zm.546-2.545-.003
 2.636h.546l.002-2.088-.545-.548zm1.873
 1.095-.546-.546h-.781l.545.546h.782zm-3.51 1.162v-2.348L.616
 9.125c-.118.143-.221.299-.308.464l1.016 1.016v.771L.093
 10.144c-.059.217-.09.445-.093.68l1.87 1.902zM.01 11.604v.772l3.498
 3.499v-.772L.01 11.605zm6.227.815h-.546v.69h-.546a.899.899 0 1 0
 1.798 0l-.706-.69zm2.977.701 1.658-3.186h-2.55l-.41.78h1.469l-1.659
 3.185h2.551l.41-.779H9.213zm2.95-2.407h1.307v-.779h-2.27V13.9h2.27v-.778h-1.308v-.82h1.308v-.78h-1.308v-.808zm1.78-.779V13.9h1.622c.404
 0 .642-.053.838-.184.256-.173.404-.5.404-.868
 0-.291-.089-.523-.267-.69-.125-.119-.232-.172-.476-.226.214-.059.303-.112.416-.231a.937.937
 0 0 0
 .268-.69c0-.38-.167-.72-.44-.886-.214-.136-.505-.19-1.01-.19h-1.356zm.962.72h.226c.452
 0 .636.136.636.457 0 .327-.184.464-.624.464h-.238v-.921zm0
 1.622h.22c.291 0 .387.012.493.072.143.077.214.214.214.404 0
 .32-.172.458-.576.458h-.35v-.934zm3.239.09.868
 1.533h1.153l-.874-1.456c.511-.202.767-.6.767-1.207
 0-.434-.155-.79-.428-1.005-.262-.202-.642-.297-1.165-.297h-1.284V13.9h.963v-1.533zm0-.541v-1.1h.368c.34
 0 .571.226.571.553 0 .344-.238.547-.63.547h-.309zm4.566
 1.294h-1.285l-.245.78h-1.015l1.308-3.964h1.224L24
 13.899h-1.045l-.244-.78zm-.244-.78-.398-1.269-.398 1.27h.796z" />
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
