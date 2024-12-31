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


class AeroflotIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "aeroflot"

    @property
    def original_file_name(self) -> "str":
        return "aeroflot.svg"

    @property
    def title(self) -> "str":
        return "Aeroflot"

    @property
    def primary_color(self) -> "str":
        return "#02458D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Aeroflot</title>
     <path d="M9.066 12.725c-.056-.135-.097-.272-.143-.406l-6.675.406
 1.35.693zm.909 1.247c-.057-.042-.115-.1-.17-.15a1.822 1.822 0 0
 1-.287-.318l-3.333.67
 1.419.509zm2.64-.286c.16-.025.4-.122.588-.268l-.968-2.032
 1.005-.51-.848-.782c-.602.292-1.206.58-1.809.868l.43
 1.025.694-.33zm1.65-4.241c.387.5.655 1.081.782 1.7h-.61a3.884 3.884 0
 0
 0-.172-.57c-.41-1.142-1.25-1.956-2.216-2.633-.127-.078-.241-.164-.37-.238.129.044.243.086.37.136.88.372
 1.662.885 2.216 1.605m.185
 6.517c-.225.114-.455.22-.682.33l-.565-1.193c-.37.139-.76.215-1.154.226-.424.02-.847-.04-1.249-.176l-.483
 1.143c-.157.014-.374 0-.512-.106a.378.378 0 0
 1-.169-.224c.204-.356.389-.723.579-1.087-.127-.088-.24-.152-.355-.27l.344-.437c.582.38
 1.22.585 1.845.585.627.022 1.25-.192
 1.832-.628.19.055.385.119.541.18-.058.046-.1.087-.157.136-.114.12-.213.242-.398.346.188.395.387.784.583
 1.175zm7.785-3.431L24 11.343h-9.55c0 .422-.06.784-.185 1.1-.369
 1.005-1.291 1.487-2.216 1.469-.908-.027-1.834-.524-2.244-1.441a2.745
 2.745 0 0 1-.229-1.128H0l1.75 1.188 7.316-.404c.138.553.397 1.037.74
 1.395a3.065 3.065 0 0 0 2.243 1.01 2.79 2.79 0 0 0
 2.216-.992c.312-.362.554-.826.694-1.385zm-.48.194l-1.352.663L15
 12.725a9.5 9.5 0 0 0 .129-.406zm-3.907 1.462l-1.48.52a357.77 357.77 0
 0
 1-2.286-.735c.069-.06.125-.117.183-.196.085-.074.157-.176.242-.254zm.711-.09l1.177-.575-4.86-.614c-.043.164-.171.298-.256.432zm-13.116
 0l-1.179-.542 4.885-.635c.09.152.171.286.27.42Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.aeroflot.ru/ru-en/information/onb'''

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
