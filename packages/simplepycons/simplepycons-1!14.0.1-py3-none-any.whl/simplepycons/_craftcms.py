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


class CraftCmsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "craftcms"

    @property
    def original_file_name(self) -> "str":
        return "craftcms.svg"

    @property
    def title(self) -> "str":
        return "Craft CMS"

    @property
    def primary_color(self) -> "str":
        return "#E5422B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Craft CMS</title>
     <path d="M21.474 0H2.526A2.516 2.516 0 0 0 0 2.526v18.948A2.516
 2.516 0 0 0 2.526 24h18.948A2.534 2.534 0 0 0 24 21.474V2.526A2.516
 2.516 0 0 0 21.474 0m-9.516 14.625c.786 0 1.628-.31 2.442-1.039l1.123
 1.291c-1.18.955-2.527 1.488-3.874 1.488-2.667
 0-4.35-1.769-3.958-4.267.393-2.498 2.667-4.266 5.334-4.266 1.29 0
 2.498.505 3.34 1.431l-1.572 1.291c-.45-.59-1.207-.982-2.05-.982-1.6
 0-2.834 1.039-3.087 2.526-.224 1.488.674 2.527 2.302 2.527" />
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
