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


class BudibaseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "budibase"

    @property
    def original_file_name(self) -> "str":
        return "budibase.svg"

    @property
    def title(self) -> "str":
        return "Budibase"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Budibase</title>
     <path d="M2 0a2 2 0 0 0-2 2v20a2 2 0 0 0 2 2h20a2 2 0 0 0 2-2V2a2
 2 0 0 0-2-2Zm2 6h2.5v5.22c.59-.634 1.326-.95 2.21-.95a3.372 3.372 0 0
 1 2.565 1.13c.178.199.327.422.46.66V6h2.505v5.22c.59-.634 1.324-.95
 2.21-.95a3.372 3.372 0 0 1 2.566 1.13c.31.345.55.75.724
 1.22.175.47.26.965.26 1.495 0 .54-.09 1.045-.27 1.52a3.73 3.73 0 0
 1-.755 1.234c-.32.35-.7.625-1.14.83-.434.2-.905.301-1.415.301-.92
 0-1.65-.345-2.186-1.035v.81h-2.5v-1.601a3.595 3.595 0 0 1-1.638
 1.525c-.435.2-.905.301-1.41.301-.92
 0-1.651-.345-2.186-1.035v.81H4Zm4.035 6.484a1.566 1.566 0 0
 0-1.125.487 1.733 1.733 0 0 0-.474 1.174 1.623 1.623 0 0 0 .468
 1.16c.145.145.322.265.522.355.2.09.409.135.629.135a1.566 1.566 0 0 0
 1.125-.484c.145-.15.26-.326.345-.526.08-.205.125-.41.125-.63a1.675
 1.675 0 0 0-.47-1.175c-.15-.15-.32-.27-.51-.36a1.491 1.491 0 0
 0-.635-.136Zm7.74 0a1.566 1.566 0 0 0-1.125.487 1.733 1.733 0 0
 0-.474 1.174 1.623 1.623 0 0 0 .469
 1.16c.145.145.32.265.52.355.2.09.41.135.63.135a1.566 1.566 0 0 0
 1.125-.484c.145-.15.26-.326.346-.526.08-.205.125-.41.125-.63a1.675
 1.675 0 0 0-.471-1.175c-.15-.15-.32-.27-.51-.36a1.491 1.491 0 0
 0-.635-.136Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Budibase/budibase/blob/613
7ffd9a278ecb3e4dbb42af804c9652741699e/packages/builder/assets/bb-emble'''

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
