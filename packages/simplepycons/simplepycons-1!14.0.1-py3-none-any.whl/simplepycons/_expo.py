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


class ExpoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "expo"

    @property
    def original_file_name(self) -> "str":
        return "expo.svg"

    @property
    def title(self) -> "str":
        return "Expo"

    @property
    def primary_color(self) -> "str":
        return "#000020"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Expo</title>
     <path d="M0 20.084c.043.53.23 1.063.718 1.778.58.849 1.576 1.315
 2.303.567.49-.505 5.794-9.776 8.35-13.29a.761.761 0 011.248 0c2.556
 3.514 7.86 12.785 8.35 13.29.727.748 1.723.282
 2.303-.567.57-.835.728-1.42.728-2.046
 0-.426-8.26-15.798-9.092-17.078-.8-1.23-1.044-1.498-2.397-1.542h-1.032c-1.353.044-1.597.311-2.398
 1.542C8.267 3.991.33 18.758 0 19.77Z" />
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
