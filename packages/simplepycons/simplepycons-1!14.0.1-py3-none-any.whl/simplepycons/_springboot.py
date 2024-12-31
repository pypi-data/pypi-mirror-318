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


class SpringBootIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "springboot"

    @property
    def original_file_name(self) -> "str":
        return "springboot.svg"

    @property
    def title(self) -> "str":
        return "Spring Boot"

    @property
    def primary_color(self) -> "str":
        return "#6DB33F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Spring Boot</title>
     <path d="m23.693
 10.7058-4.73-8.1844c-.4094-.7106-1.4166-1.2942-2.2402-1.2942H7.2725c-.819
 0-1.8308.5836-2.2402 1.2942L.307 10.7058c-.4095.7106-.4095 1.873 0
 2.5837l4.7252 8.189c.4094.7107 1.4166 1.2943 2.2402 1.2943h9.455c.819
 0 1.826-.5836 2.2402-1.2942l4.7252-8.189c.4095-.7107.4095-1.8732
 0-2.5838zM10.9763
 5.7547c0-.5365.4377-.9742.9742-.9742s.9742.4377.9742.9742v5.8217c0
 .5366-.4377.9742-.9742.9742s-.9742-.4376-.9742-.9742zm.9742
 12.4294c-3.6427 0-6.6077-2.965-6.6077-6.6077.0047-2.0896.993-4.0521
 2.6685-5.304a.8657.8657 0 0 1 1.2142.1788.8657.8657 0 0 1-.1788
 1.2143c-2.1602 1.6048-2.612 4.6592-1.0072 6.8194 1.6049 2.1603 4.6593
 2.612 6.8195 1.0072 1.2378-.9177 1.9673-2.372 1.9673-3.9157a4.8972
 4.8972 0 0
 0-1.9861-3.925c-.386-.2824-.466-.8284-.1836-1.2143.2824-.386.8283-.466
 1.2143-.1835 1.6895 1.2471 2.6826 3.2238 2.6873 5.3228 0 3.6474-2.965
 6.6077-6.6077 6.6077z" />
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
