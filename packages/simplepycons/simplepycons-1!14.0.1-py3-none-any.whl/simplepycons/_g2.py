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


class GTwoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "g2"

    @property
    def original_file_name(self) -> "str":
        return "g2.svg"

    @property
    def title(self) -> "str":
        return "G2"

    @property
    def primary_color(self) -> "str":
        return "#FF492C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>G2</title>
     <path d="M12 0a12 12 0 1 0 0 24 12 12 0 0 0 0-24Zm.122 5.143c.45
 0 .9.044 1.342.132l-1.342 2.806C9.962 8.08 8.203 9.84 8.203 12s1.76
 3.92 3.92 3.92c.937 0 1.844-.338 2.553-.951l1.483 2.572A6.856 6.856 0
 0 1 5.266 12a6.856 6.856 0 0 1 6.856-6.856Zm3.498.49a1.262 1.262 0 0
 1 .026 0c.427 0 .792.113 1.101.34.31.229.466.546.466.946 0 .639-.36
 1.03-1.035
 1.376l-.377.191c-.403.204-.602.385-.657.706h2.05v.85h-3.101v-.144c0-.526.103-.96.314-1.306.211-.345.576-.65
 1.102-.917l.242-.117c.427-.216.538-.401.538-.625
 0-.266-.228-.458-.6-.458-.44
 0-.773.228-1.004.694l-.592-.595c.13-.279.338-.502.619-.675a1.7 1.7 0
 0 1 .908-.266Zm-2.094 5.388h3.394l1.697 2.937-1.697
 2.94-1.697-2.94H11.83l1.696-2.937Z" />
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
