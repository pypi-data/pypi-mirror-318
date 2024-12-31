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


class RelayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "relay"

    @property
    def original_file_name(self) -> "str":
        return "relay.svg"

    @property
    def title(self) -> "str":
        return "Relay"

    @property
    def primary_color(self) -> "str":
        return "#F26B00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Relay</title>
     <path d="M2.26428 4.93674C1.01354 4.93674 0 5.95018 0 7.20093c0
 1.25074 1.01363 2.26428 2.26437 2.26428 1.05365 0 1.9393-.71975
 2.1919-1.69462h10.3387c.98764 0 1.79128.80368 1.79128 1.79146 0
 .98779-.80359 1.79156-1.79128 1.79156h-5.7309c-1.67246 0-3.03319
 1.36067-3.03319 3.03318 0 1.67252 1.36063 3.03301 3.0332
 3.03301h10.49429c.26987.9487 1.14197 1.64346 2.17735 1.64346 1.25074
 0 2.26428-1.01344 2.26428-2.26419
 0-1.25074-1.01354-2.26428-2.26428-2.26428-1.0353
 0-1.9074.69469-2.17735 1.64328H9.06397c-.98777
 0-1.79145-.80359-1.79145-1.79128 0-.98797.80358-1.79164
 1.79146-1.79164h5.7309c1.67251 0 3.033-1.36063 3.033-3.0331
 0-1.67246-1.36044-3.03319-3.033-3.03319H4.42718c-.2863-.92243-1.1464-1.59212-2.1629-1.59212Z"
 />
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
