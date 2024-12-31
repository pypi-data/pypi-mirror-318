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


class ZensarIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zensar"

    @property
    def original_file_name(self) -> "str":
        return "zensar.svg"

    @property
    def title(self) -> "str":
        return "Zensar"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zensar</title>
     <path d="M12.929 13.776c.28.084 1.01.205 1.662.205 1.047 0
 1.64-.463 1.64-1.283
 0-.683-.464-1.01-1.412-1.29-.73-.213-1.04-.319-1.04-.653
 0-.38.334-.562.744-.554.561.008 1.062.425 1.336
 1.131h.129v-1.131a7.835 7.835 0 0 0-1.412-.167c-1.07 0-1.678.47-1.678
 1.23 0 .615.41.979 1.313 1.237.896.258 1.177.364 1.177.744 0
 .341-.364.57-.82.57-.721
 0-1.275-.54-1.518-1.284h-.121v1.245zm-1.911-3.72c-.4
 0-.847.207-1.253.651v-.597H8.023v.144c.418 0
 .6.213.6.524v3.127H9.78v-2.974c.243-.253.495-.343.66-.343.32 0
 .564.205.564.623v2.694h1.166v-2.694c0-.699-.378-1.154-1.152-1.154zm-5.606
 1.921v.228c0 .88.402 1.412 1.161 1.412.501 0 .88-.243
 1.154-.615l.137.083c-.334.585-.934.896-1.678.896-1.427
 0-2.11-.804-2.11-2.027 0-1.199.835-1.935 2.004-1.935 1.177 0
 1.807.698 1.807 1.73v.228H5.412zm.463-1.768a.986.986 0 0
 0-.463.107v1.464h1.192v-.767c0-.508-.243-.804-.729-.804zm14.5
 1.077v2.62H19.13v-.433a1.72 1.72 0 0 1-1.214.508c-.73
 0-1.185-.417-1.185-.964s.365-.804.767-.934l1.617-.53v-.57c0-.494-.25-.774-.706-.774-.15
 0-.271.018-.387.05v1.08a1.497 1.497 0 0 1-.516.084c-.38
 0-.623-.22-.623-.524 0-.561.79-.865 1.754-.865 1.01 0 1.738.342 1.738
 1.252zm-1.822 2.194a.767.767 0 0 0 .562-.213v-1.51l-1.1.367v.711c0
 .425.181.645.538.645zM3.681
 10.21v-.099H.121v1.48h.13c.106-.645.645-1.328 1.54-1.328v1.746L0
 13.807v.098h3.651V12.35h-.129c-.114.653-.698 1.404-1.624
 1.404v-1.745l1.783-1.8zM24 10.042v1.1h-.66c-.384
 0-.682.058-.866.403v2.36h-1.157v-3.127c0-.311-.182-.524-.6-.524v-.144h1.742v1.146c.37-.83.795-1.214
 1.366-1.214H24z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.zensar.com/about/our-story/our-br'''

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
