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


class ChartdotjsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "chartdotjs"

    @property
    def original_file_name(self) -> "str":
        return "chartdotjs.svg"

    @property
    def title(self) -> "str":
        return "Chart.js"

    @property
    def primary_color(self) -> "str":
        return "#FF6384"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Chart.js</title>
     <path d="M12 0L1.605 6v12L12 24l10.395-6V6zm0 1.41l9.172
 5.295v10.59L12 22.59l-9.172-5.295V6.705zM5.902 8.334c-1.306
 0-1.983.956-2.574 2.41v6.262L12
 22.014l8.672-5.008v-5.971c-.447-.264-.894-.412-1.336-.412-4.275
 0-3.97 4.885-6.717
 5.8-2.748.917-3.511-8.089-6.717-8.089zm12.364.457c-2.9 0-2.137
 4.732-5.342 4.732-1.63
 0-2.52-1.317-3.477-1.981.148.326.3.655.442.98.467 1.068.922 2.09
 1.379 2.734.228.322.455.541.644.644a.595.595 0 0 0
 .549.05c.558-.187.968-.571 1.36-1.112.39-.541.74-1.228
 1.154-1.916.413-.688.894-1.385 1.59-1.918.695-.534 1.607-.881
 2.77-.881.465 0 .908.136
 1.337.352v-.121c-.633-.849-1.348-1.563-2.406-1.563zm-6.68.152c-.868
 0-1.491.82-2.076 2.06.094.055.192.106.277.167 1.06.761 1.798 1.853
 3.137 1.853.678 0 1.067-.218
 1.418-.585-.722-1.546-1.432-3.492-2.756-3.495Z" />
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
