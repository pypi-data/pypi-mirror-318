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


class CarrefourIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "carrefour"

    @property
    def original_file_name(self) -> "str":
        return "carrefour.svg"

    @property
    def title(self) -> "str":
        return "Carrefour"

    @property
    def primary_color(self) -> "str":
        return "#004E9F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Carrefour</title>
     <path d="M12.14 4.045c-2.569 0-3.572 3.64-3.572 7.979 0 4.34
 1.003 7.931 3.572 7.931 1.541 0 2.855-.903 2.86-1.645a.625.625 0 0
 0-.199-.453c-.73-.706-1.016-1.412-1.018-2.034-.005-1.189 1.026-2.074
 1.977-2.074 1.306 0 2.077 1.027 2.077 2.357 0 1.26-.537 2.31-1.121
 3.15a.193.193 0 0 0-.034.107c0 .065.04.12.098.12.035 0
 .076-.02.122-.065l6.561-6.344c.328-.28.537-.608.537-1.073
 0-.468-.21-.794-.537-1.073l-6.561-6.346c-.045-.045-.087-.064-.122-.064-.059
 0-.097.055-.098.12 0 .035.01.073.034.107.584.84 1.12 1.89 1.12 3.15 0
 1.329-.77 2.356-2.076 2.356-.95
 0-1.982-.884-1.977-2.073.002-.622.288-1.328 1.018-2.033A.624.624 0 0
 0 15 5.69c-.004-.743-1.319-1.646-2.86-1.646m-5.043.537L.537
 10.93C.209 11.207 0 11.534 0 12c0 .465.21.793.537 1.073l6.56
 6.345c.042.043.083.06.117.06.062 0 .105-.057.103-.123a.188.188 0 0
 0-.057-.123C5.72 17.32 4.6 15.126 4.6 12.024c0-3.104 1.12-5.341
 2.66-7.255a.185.185 0 0 0 .057-.123c.002-.068-.04-.123-.103-.123-.034
 0-.075.017-.117.06" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://en.wikipedia.org/wiki/File:Carrefour_'''

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
