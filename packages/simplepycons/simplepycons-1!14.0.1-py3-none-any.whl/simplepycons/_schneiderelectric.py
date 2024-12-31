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


class SchneiderElectricIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "schneiderelectric"

    @property
    def original_file_name(self) -> "str":
        return "schneiderelectric.svg"

    @property
    def title(self) -> "str":
        return "Schneider Electric"

    @property
    def primary_color(self) -> "str":
        return "#3DCD58"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Schneider Electric</title>
     <path d="M16.73.313c-3.56-.049-7.797 1.68-11.288
 5.02-.87.83-1.607 1.725-2.28 2.642h3.042L5.497
 9.99H1.864c-.346.636-.672 1.266-.922 1.906h4.307l-.687
 2.016H.327c-.724 3.079-.262 5.953 1.559 7.777 3.54 3.538 11.01 2.292
 16.591-3.048.977-.93 1.783-1.931
 2.511-2.96h-3.906l.596-2.013h4.568c.334-.64.643-1.274.883-1.914h-4.992l.554-2.01h5.051c.623-2.917.132-5.62-1.638-7.39C20.76
 1.01 18.867.34 16.73.312Zm-1.044 4.714h4.968l-.634 2.938h-3.002c-.323
 0-.46.054-.592.201-.05.058-.07.115-.09.23l-1.639 6.22c-.385
 2.179-3.065 4.359-6.555 4.359H3.288l.842-3.198h3.119a.984.984 0 0 0
 .775-.347c.076-.09.177-.232.19-.377L9.509 9.62c.381-2.182 2.686-4.592
 6.177-4.592Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.se.com/us/en/assets/739/media/202'''

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
