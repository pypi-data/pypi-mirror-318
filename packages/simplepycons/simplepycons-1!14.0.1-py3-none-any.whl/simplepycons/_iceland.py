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


class IcelandIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "iceland"

    @property
    def original_file_name(self) -> "str":
        return "iceland.svg"

    @property
    def title(self) -> "str":
        return "Iceland"

    @property
    def primary_color(self) -> "str":
        return "#CC092F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Iceland</title>
     <path d="M7.7442 13.9186c-.9419 0-1.2558-.4186-1.3256-.7674L9
 12.593c0-1.8837-1.1512-2.2325-1.8837-2.2325-.9419
 0-1.9884.6976-1.9884 2.1976 0 1.3256.907 2.1628 2.407 2.1628.4535 0
 .9418-.1046
 1.221-.2093l-.1396-.6976c-.2442.0697-.593.1046-.8721.1046zm-.628-2.7558c.3838
 0
 .6629.279.6978.8372l-1.5.314c.0348-.7326.314-1.1512.8023-1.1512zm6.0698-.8023c-.6627
 0-1.2558.1744-1.6046.279 0
 .035.1395.6977.1744.7675.3837-.1396.907-.2442 1.2558-.2442.5582 0
 .8024.1744.8024.5581v.1744c-1.7442 0-2.4768.628-2.4768 1.4303 0
 .907.8023 1.3953 1.9535 1.3953.7674 0 1.3953-.1395
 1.6744-.2093v-2.7209c.0349-.9767-.5581-1.4302-1.779-1.4302zm.628
 3.5232c-.1047.0349-.314.0349-.4187.0349-.3837
 0-.8372-.1744-.8372-.628 0-.4534.3838-.6976
 1.221-.6627v1.2558zm9-4.6046v1.186c-.1396-.0349-.314-.0698-.593-.0698-1.0117
 0-2.093.6977-2.093 2.1977 0 1.3256.872 2.128 2.3022 2.128.593 0
 1.2907-.1047 1.5698-.1745V9.2791Zm0
 4.6395c-.1047.0349-.2442.0349-.314.0349-.7326
 0-1.1512-.5233-1.1512-1.3954 0-.6628.2791-1.3604 1.0814-1.3604.1047 0
 .314.0349.3838.0349zM0 9.2791h1.0814v5.2325H0Zm3.9767 5.4418c-1.2209
 0-2.0232-.8372-2.0232-2.0581 0-1.3256.872-2.2675 2.0581-2.2675.2791 0
 .628.0698.8372.1745l-.2093.7325c-.1395-.0349-.314-.1046-.4535-.1046-.6627
 0-1.1162.5581-1.1162 1.3953 0 .8372.4186 1.3256 1.0465 1.3256.1744 0
 .4186-.0349.6279-.1046l.1744.7325c-.2093.0698-.6279.1744-.9419.1744zM9.628
 9.2791h1.0814v5.2325H9.6279ZM19.5
 14.5116h-1.1512v-2.686c0-.5582-.279-.6977-.6976-.6977-.2093
 0-.4535.0349-.628.0698v3.314h-1.1511v-3.942c.279-.0697 1.1163-.2092
 1.814-.2092 1.2558 0 1.8139.4535 1.8139 1.3953z" />
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
