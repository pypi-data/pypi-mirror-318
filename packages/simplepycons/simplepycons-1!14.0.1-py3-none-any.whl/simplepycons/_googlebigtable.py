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


class GoogleBigtableIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlebigtable"

    @property
    def original_file_name(self) -> "str":
        return "googlebigtable.svg"

    @property
    def title(self) -> "str":
        return "Google Bigtable"

    @property
    def primary_color(self) -> "str":
        return "#669DF6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Bigtable</title>
     <path d="M10.511.278s0-.4.456-.24c.267.094 3.728 2.243 5.88
 3.533l.006.003.364.217c.004.003.007.009.011.011.322.2.656.42
 1.006.673.27.165.43.463.42.78l-.06 7.566a.42.42 0 0
 1-.192.396l-1.2.815V5.436c-.042-.034-.083-.07-.131-.098l-5.06-3.01c-.744-.466-1.5-1.642-1.5-2.05zm-2.89
 12.171 4.39 2.614 4.388-2.566v-1.079L12.25 13.84a.78.78 0 0
 1-.24.072.43.43 0 0 1-.24-.072l-4.149-2.47v1.08zm0 1.943c0
 .17.086.327.228.42l3.933
 2.398c.123.06.162.07.228.064.088-.003.173-.074.252-.112l3.933-2.398a.468.468
 0 0 0 .228-.42v-.791L12.25 16.07a.432.432 0 0 1-.48 0L7.621
 13.6v.79zm8.778-4.137v-.516a.467.467 0 0
 0-.228-.408l-3.933-2.398a.444.444 0 0 0-.456 0L7.85 9.331a.492.492 0
 0 0-.228.408v.516l4.39 2.614 4.388-2.614zm-4.473 11.332L6.95
 18.625c-.041-.025-.06-.07-.096-.1v-8.63l-1.2.708a.491.491 0 0
 0-.227.395v7.867a.9.9 0 0 0 .407.72l1.272.79c-.002
 0-.003-.003-.005-.004l6.024 3.59a.216.216 0 0 0 .336-.216 3.262 3.262
 0 0 0-1.535-2.158zM8.891 4.097a.845.845 0 0 1 .859.009L16.41
 8.06V6.645a.444.444 0 0 0-.24-.371l-6.38-3.778a.81.81 0 0
 0-.85-.012l-1.433.856C5.56 4.498 1.525 6.893 1.36 6.975a.276.276 0 0
 0 0 .48 3.154 3.154 0 0 0 2.495-.312L8.89 4.097zM22.635 16.49a3.154
 3.154 0 0 0-2.519.3l-5.036 2.986a.875.875 0 0 1-.887
 0l-.018-.006-6.554-3.867v1.39c.021.152.093.292.204.397l6.356
 3.765a.84.84 0 0 0 .887 0l1.415-.863h-.004l6.156-3.646a.252.252 0 0 0
 0-.456zM10.967 6.13l-1.2-.708a.407.407 0 0 0-.431 0L3.688
 8.756a.863.863 0 0 0-.456.767v8.862a.216.216 0 0 0 .36.156 3.297
 3.297 0 0 0 1.043-2.398v-5.996a.9.9 0 0 1 .098-.367l6.234-3.65zm2.11
 11.728 1.2.683a.42.42 0 0 0 .443
 0l5.684-3.418c.335-.207.442-.408.442-.706l.002-.001V12.665c0
 .006-.004.01-.004.017-.006-2.494-.013-6.831.004-7.104.024-.384-.372-.252-.372-.252a3.37
 3.37 0 0 0-1.007 2.399v5.995a.97.97 0 0 1-.191.413l-6.2 3.725z" />
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
