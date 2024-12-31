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


class OpenfaasIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "openfaas"

    @property
    def original_file_name(self) -> "str":
        return "openfaas.svg"

    @property
    def title(self) -> "str":
        return "OpenFaaS"

    @property
    def primary_color(self) -> "str":
        return "#3B5EE9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OpenFaaS</title>
     <path d="M4.304 0A4.31 4.31 0 0 0 0 4.304v15.391A4.31 4.31 0 0 0
 4.304 24h15.392A4.31 4.31 0 0 0 24 19.695V4.305A4.31 4.31 0 0 0
 19.695 0zm-.006.776h15.398a3.532 3.532 0 0 1 3.528 3.528v15.391c0
 .205-.019.409-.054.61-1.234-.015-1.858-.412-2.514-.834-.708-.454-1.51-.97-3.04-.97s-2.33.516-3.038.97c-.17.11-.338.217-.514.317a43.042
 43.042 0 0 1-.775-1.907.806.806 0 0 1 .01-.739c.3-.489 1.23-.691
 1.572-.729.361-.027 5.97-.555 6.306-7.153a.42.42 0 0
 0-.72-.317c-.457.464-1.886 1.634-3 1.47a11.06 11.06 0 0
 1-.693-.127c-1.425-.293-3.339-.685-4.972
 1.72-1.633-2.406-3.548-2.012-4.972-1.72-.248.05-.48.098-.697.128-1.108.162-2.538-1.007-2.997-1.471a.42.42
 0 0 0-.72.316c.336 6.58 5.914 7.124 6.304 7.153.086.012 1.1.16
 1.48.717.15.237.184.529.092.793a19.35 19.35 0 0 1-.552
 1.747c-.107-.065-.214-.13-.32-.198-.708-.454-1.51-.97-3.039-.97-1.53
 0-2.332.516-3.04.97-.654.42-1.277.816-2.5.834a3.532 3.532 0 0
 1-.055-.61V4.305A3.532 3.532 0 0 1 4.298.775zm4.474 2.108l-4.74 1.429
 1.293 4.288 3.165-.955-.19 1.229
 4.894.757.684-4.426-4.62-.715zm10.494.813l-4.938.348.315 4.466
 4.938-.347Z" />
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
