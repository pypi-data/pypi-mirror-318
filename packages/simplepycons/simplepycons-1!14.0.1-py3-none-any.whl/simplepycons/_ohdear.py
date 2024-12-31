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


class OhDearIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ohdear"

    @property
    def original_file_name(self) -> "str":
        return "ohdear.svg"

    @property
    def title(self) -> "str":
        return "Oh Dear"

    @property
    def primary_color(self) -> "str":
        return "#FF3900"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Oh Dear</title>
     <path d="m10.811 9.3333c2.5345 0 4.5966 1.9939 4.5966 4.4444 0
 2.4506-2.0621 4.4444-4.5966 4.4444-2.2139
 0-4.0673-1.5215-4.5007-3.5397h-6.3101v-1.7972h6.3072c0.42873-2.0242
 2.285-3.5519 4.5036-3.5519zm7.3308-3.5556v3.8766c0.60102-0.38439
 1.3334-0.586 2.1395-0.586 1.7157 0 3.7189 1.1521 3.7189
 4.3993v4.4583h-1.8453v-4.4583c0-1.0234-0.25022-1.7562-0.74385-2.1787-0.38875-0.33283-0.84479-0.40252-1.1591-0.40252-0.96256
 0-2.1102 0.44768-2.1102 2.5812v4.4583h-1.8453v-12.148zm-7.3308
 5.3741c-1.4978 0-2.7159 1.178-2.7159 2.6259s1.218 2.6259 2.7159
 2.6259c1.4975 0 2.7155-1.178
 2.7155-2.6259s-1.218-2.6259-2.7155-2.6259z" />
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
