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


class MahindraIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mahindra"

    @property
    def original_file_name(self) -> "str":
        return "mahindra.svg"

    @property
    def title(self) -> "str":
        return "Mahindra"

    @property
    def primary_color(self) -> "str":
        return "#DD052B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mahindra</title>
     <path d="M5.145 11.311H6.78a.67.67 0 0 1
 .674.66v1.509H5.009a.408.408 0 0 1-.41-.404v-.524a.38.38 0 0 1
 .383-.375h1.354l-.144.306h-.998c-.043 0-.092.034-.092.081v.412c0
 .047.049.082.092.082h1.73v-.99c0-.191-.169-.338-.357-.338H4.945l.2-.419zm13.427-.787v2.959h-2.383a.408.408
 0 0 1-.41-.403v-1.11a.67.67 0 0 1 .675-.659h1.357l-.2.422h-.948c-.188
 0-.357.147-.357.337v.91c0 .046.049.08.092.08h1.644v-2.536h.53zM10.2
 13.483h.527v-1.51a.67.67 0 0 0-.674-.659H8.932l-.2.422h1.111c.188 0
 .357.147.357.337v1.41zm-2.195-2.96v2.96h.527v-2.96h-.527zm-4.4
 2.96h.527v-1.51a.67.67 0 0
 0-.674-.659H0v2.169h.526v-1.669c0-.047.05-.081.093-.081h1.09c.043 0
 .092.034.092.081v1.669h.527v-1.669c0-.047.049-.081.092-.081h.828c.188
 0 .357.147.357.337v1.413zm17.72-2.172H20a.67.67 0 0
 0-.674.66v1.509h.527v-1.41c0-.19.169-.337.357-.337h.914l.2-.422zm-6.753
 0a.67.67 0 0 1
 .675.66v1.509h-.527v-1.41c0-.19-.17-.337-.357-.337h-1.268v1.75h-.527v-2.169c.665
 0 1.333-.003
 2.004-.003zm-3.19.137.527-.306v2.338h-.526v-2.032zm.53-.609v-.322h-.526v.625l.526-.303zm9.782.472h1.632a.67.67
 0 0 1 .674.66v1.509h-2.445a.408.408 0 0 1-.41-.404v-.524a.38.38 0 0 1
 .383-.375h1.354l-.144.306h-.998c-.043 0-.092.034-.092.081v.412c0
 .047.049.082.092.082h1.73v-.99c0-.191-.169-.338-.357-.338h-1.622l.203-.419z"
 />
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
