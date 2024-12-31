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


class AutodeskRevitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "autodeskrevit"

    @property
    def original_file_name(self) -> "str":
        return "autodeskrevit.svg"

    @property
    def title(self) -> "str":
        return "Autodesk Revit"

    @property
    def primary_color(self) -> "str":
        return "#186BFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Autodesk Revit</title>
     <path d="M24 22.665H2.994c-.519
 0-.838-.293-.835-.723.001.042.002-.148.003-.463.142-.083.283-.165.427-.247l.078-.045.07-.058.015-.013.127-.078
 1.294-.804h1.134c3.35 0 11.817 0 16.548.007.159 0 .631 0
 1.002-.371.371-.372.37-.853.37-1.011-.008-2.057-.001-4.109.005-6.16.008-2.39.016-4.86
 0-7.298v-.063l.61-.007c.169-.003.143.197.143.296.014 5.68-.02
 11.36.015 17.038zM14.326
 8.982c.006-.281.006-.56.006-.859-.009-.5-.395-1.055-.916-1.055-.435
 0-.919.006-1.432.006v3.01h1.432c.52 0 .9-.584.91-1.102zM3.887 19.234
 3.853 1.363l.007-.025.026-.003h17.313c.51.232.943.56 1.033 1.16.023
 1.052 0 1.896 0 2.854.001.023-.002.036 0 .059.03 4.489-.022
 8.963-.005 13.453 0
 .285-.072.38-.37.38-5.99-.008-17.97-.007-17.97-.007zm5.624-3.971h2.395l.057-.051v-3.5c.316.001.57-.005.787-.005.075
 0 .348.075.449.286.36.757.692 1.531 1.125 2.25.583.967 1.704 1.204
 2.469 1.204.528 0 .528-.024.528-.245
 0-.423-.006-.935-.006-1.374-.403-.039-.734-.163-.929-.541-.362-.705-.74-1.401-1.119-2.114.248-.072.218-.057.302-.092.859-.357
 1.139-.951
 1.213-1.71.05-.503.059-1.144.025-1.395-.112-.833-.378-1.454-1.036-1.932-.773-.562-1.678-.657-2.582-.687a62.395
 62.395 0 0 0-3.678.012v9.894zm-5.658-13.9C1.631 2.64.98 3.087.223
 3.513.025 3.622 0 3.895 0 4.1l.02 17.45c.575-.357 3.293-1.96
 3.867-2.316L3.853 1.363z" />
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
