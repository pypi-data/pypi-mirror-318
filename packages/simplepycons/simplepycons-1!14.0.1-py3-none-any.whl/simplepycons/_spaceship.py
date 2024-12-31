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


class SpaceshipIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "spaceship"

    @property
    def original_file_name(self) -> "str":
        return "spaceship.svg"

    @property
    def title(self) -> "str":
        return "Spaceship"

    @property
    def primary_color(self) -> "str":
        return "#394EFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Spaceship</title>
     <path d="M11.9997 1.2529c1.0445 0 1.956.5689 2.441 1.4125l4.5883
 7.9314 4.45
 7.6915c.0466.074.2105.3585.27.4938.2216.4677.2505.9472.251 1.1595 0
 1.5496-1.2587 2.8056-2.8116 2.8056-.2949
 0-.579-.045-.8457-.129l-7.9011-2.6061a1.406 1.406 0 0 0-.4413-.0705
 1.413 1.413 0 0 0-.442.0705L3.658 22.6183l-.1623.0456a2.8398 2.8398 0
 0 1-.6838.0831c-1.5531
 0-2.8119-1.256-2.8119-2.8056.002-.243.0234-.5533.168-.9578.0294-.0911.0743-.176.1115-.264.0712-.1487.1607-.2875.2411-.4313l4.4493-7.6916
 4.5883-7.9313c.485-.8437 1.3971-1.4126 2.4416-1.4126z" />
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
