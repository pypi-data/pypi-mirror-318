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


class NfcIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nfc"

    @property
    def original_file_name(self) -> "str":
        return "nfc.svg"

    @property
    def title(self) -> "str":
        return "NFC"

    @property
    def primary_color(self) -> "str":
        return "#002E5F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NFC</title>
     <path d="M23.958 1.98C23.895 1 23.143.256
 22.145.197c-1.102-.066-4.668-.12-5.693-.12 1.832 1.264 2.082 3.644
 2.255 8.066.101 2.62.01 11.799.002 12.188l-.049
 2.504-9.628-9.63v-3.014l7.656 7.658c.02-1.516.04-3.492.04-5.299
 0-1.76-.026-3.354-.076-4.193-.288-4.819-.737-7.077-3.253-7.962-.77-.27-1.487-.335-2.683-.351C9.728.032
 2.848.037 1.854.091.8.147.09.914.042 1.9c-.048.977-.064 19.174 0
 20.165.062.98.815 1.724 1.812 1.782 1.102.067 4.668.075
 5.694.075-1.832-1.264-2.083-3.643-2.255-8.066-.1-2.62-.009-11.8
 0-12.188l.047-2.504 9.629 9.63v3.013L7.312 6.152c-.02 1.514-.04
 3.49-.04 5.298 0 1.76.026 3.354.077 4.192.288 4.82.736 7.077 3.252
 7.962.77.271 1.487.337 2.683.352.987.012 7.868.006 8.861-.047
 1.056-.056 1.765-.822 1.813-1.811.048-.976.064-19.127 0-20.118" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://nfc-forum.org/our-work/nfc-branding/n'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://nfc-forum.org/our-work/nfc-branding/n'''

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
