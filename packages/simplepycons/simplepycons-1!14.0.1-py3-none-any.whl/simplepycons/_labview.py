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


class LabviewIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "labview"

    @property
    def original_file_name(self) -> "str":
        return "labview.svg"

    @property
    def title(self) -> "str":
        return "LabVIEW"

    @property
    def primary_color(self) -> "str":
        return "#FFDB00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LabVIEW</title>
     <path d="M9.176 4.469a.817.817 0 00-.768.816v7.055a.816.816 0
 001.182.73l7.058-3.527a.818.818 0 000-1.463L9.59 4.553a.808.808 0
 00-.414-.084zm1.918
 3.107h.638v.916h.916v.639h-.916v.918h-.638V9.13h-.918v-.639h.918v-.916zm-4.752
 7.51v.367h.262c.086 0 .136.05.136.137v3.869h.41v-.273a2.6 2.6 0
 00-.011-.256h.011s.281.603 1.028.603c.82 0 1.41-.646 1.41-1.635
 0-.97-.522-1.642-1.361-1.642-.802
 0-1.065.598-1.065.598H7.15s.012-.113.012-.256v-1.131c0-.267-.112-.381-.379-.381h-.441zm2.855
 0v.387h.063c.118 0 .18.018.224.136l1.436
 3.85h.467l1.437-3.85c.044-.118.105-.136.223-.136h.834v3.601h-.41v.385h1.25v-.385h-.418v-3.601h.418v-.387h-1.805c-.31
 0-.404.056-.516.361l-1.076
 2.942c-.08.223-.168.566-.168.566h-.011s-.088-.343-.168-.566L9.9
 15.447c-.105-.298-.199-.361-.51-.361h-.193zm5.922 0v.387h.404v3.607c0
 .268.112.379.38.379h1.89c.268 0 .379-.111.379-.379v-.435h-.404v.29c0
 .094-.05.14-.137.14h-1.535c-.087
 0-.137-.046-.137-.14v-1.484h1.64v-.387h-1.64v-1.591h1.492c.087 0
 .137.043.137.136v.293h.41v-.435c0-.268-.112-.381-.379-.381h-2.5zM0
 15.088v.385h.268c.086 0 .136.043.136.136v3.471c0
 .268.112.379.38.379h1.81c.267 0 .379-.111.379-.379v-.435h-.41v.29c0
 .094-.05.137-.137.137H.976c-.086
 0-.136-.043-.136-.136v-3.47c0-.267-.112-.378-.38-.378H0zm18.334
 0v.385h.076c.118 0 .197.018.229.136l1.002
 3.85h.515l.897-3.047c.08-.28.156-.64.156-.64h.012s.067.366.142.646l.815
 3.041h.515l1.008-3.85c.031-.118.106-.136.23-.136H24v-.385h-.193c-.311
 0-.453.055-.528.36l-.76
 3.015c-.055.224-.1.467-.1.467h-.01s-.039-.243-.1-.467l-.877-3.358h-.43l-.963
 3.358c-.062.224-.12.467-.12.467h-.01s-.039-.243-.095-.467l-.757-3.016c-.075-.304-.219-.36-.53-.36h-.193zM4.637
 16.256c-.274
 0-1.02.094-1.02.53v.298h.404v-.2c0-.23.454-.273.61-.273.572 0
 .808.23.808.883v.037h-.173c-.542 0-1.916.038-1.916 1.076 0
 .622.54.926 1.062.926.784 0 1.046-.678
 1.04-.678h.01s-.005.094-.005.23c0
 .256.106.374.373.374h.43v-.367h-.262c-.087
 0-.137-.044-.137-.137v-1.498c0-.672-.236-1.201-1.224-1.201zm3.527.387c.578
 0 .988.49.988 1.255 0 .796-.452 1.262-1.006 1.262-.671
 0-.996-.628-.996-1.256 0-.889.492-1.261 1.014-1.261zm-2.906
 1.224h.181v.143c0 .54-.362 1.162-.959 1.162-.466 0-.695-.298-.695-.59
 0-.703.982-.715 1.473-.715Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://forums.ni.com/t5/NI-Partner-Network/N'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://forums.ni.com/t5/NI-Partner-Network/N'''

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
