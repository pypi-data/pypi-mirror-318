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


class BlueprintIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "blueprint"

    @property
    def original_file_name(self) -> "str":
        return "blueprint.svg"

    @property
    def title(self) -> "str":
        return "Blueprint"

    @property
    def primary_color(self) -> "str":
        return "#137CBD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Blueprint</title>
     <path d="M21.809 5.524L12.806.179l-.013-.007.078-.045h-.166a1.282
 1.282 0 0 0-1.196.043l-.699.403-8.604 4.954a1.285 1.285 0 0 0-.644
 1.113v10.718c0 .46.245.884.644 1.113l9.304 5.357c.402.232.898.228
 1.297-.009l9.002-5.345c.39-.231.629-.651.629-1.105V6.628c0-.453-.239-.873-.629-1.104zm-19.282.559L11.843.719a.642.642
 0 0 1 .636.012l9.002 5.345a.638.638 0 0 1 .207.203l-4.543
 2.555-4.498-2.7a.963.963 0 0 0-.968-.014L6.83 8.848 2.287
 6.329a.644.644 0 0 1 .24-.246zm14.13 8.293l-4.496-2.492V6.641a.32.32
 0 0 1 .155.045l4.341 2.605v5.085zm-4.763-1.906l4.692 2.601-4.431
 2.659-4.648-2.615a.317.317 0 0 1-.115-.112l4.502-2.533zm-.064
 10.802l-9.304-5.357a.643.643 0 0 1-.322-.557V7.018L6.7 9.51v5.324c0
 .348.188.669.491.84l4.811 2.706.157.088v4.887a.637.637 0 0
 1-.329-.083z" />
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
