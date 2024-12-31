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


class WalletconnectIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "walletconnect"

    @property
    def original_file_name(self) -> "str":
        return "walletconnect.svg"

    @property
    def title(self) -> "str":
        return "WalletConnect"

    @property
    def primary_color(self) -> "str":
        return "#3B99FC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WalletConnect</title>
     <path d="M4.913 7.519c3.915-3.831 10.26-3.831 14.174
 0l.471.461a.483.483 0 0 1 0 .694l-1.611 1.577a.252.252 0 0 1-.354
 0l-.649-.634c-2.73-2.673-7.157-2.673-9.887 0l-.694.68a.255.255 0 0
 1-.355 0L4.397 8.719a.482.482 0 0 1 0-.693l.516-.507Zm17.506 3.263
 1.434 1.404a.483.483 0 0 1 0 .694l-6.466 6.331a.508.508 0 0 1-.709
 0l-4.588-4.493a.126.126 0 0 0-.178 0l-4.589 4.493a.508.508 0 0 1-.709
 0L.147 12.88a.483.483 0 0 1 0-.694l1.434-1.404a.508.508 0 0 1 .709
 0l4.589 4.493c.05.048.129.048.178 0l4.589-4.493a.508.508 0 0 1 .709
 0l4.589 4.493c.05.048.128.048.178 0l4.589-4.493a.507.507 0 0 1 .708
 0Z" />
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
