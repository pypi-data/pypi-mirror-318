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


class FirefoxBrowserIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "firefoxbrowser"

    @property
    def original_file_name(self) -> "str":
        return "firefoxbrowser.svg"

    @property
    def title(self) -> "str":
        return "Firefox Browser"

    @property
    def primary_color(self) -> "str":
        return "#FF7139"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Firefox Browser</title>
     <path d="M8.824 7.287c.008 0 .004 0 0 0zm-2.8-1.4c.006 0 .003 0 0
 0zm16.754 2.161c-.505-1.215-1.53-2.528-2.333-2.943.654 1.283 1.033
 2.57 1.177
 3.53l.002.02c-1.314-3.278-3.544-4.6-5.366-7.477-.091-.147-.184-.292-.273-.446a3.545
 3.545 0 01-.13-.24 2.118 2.118 0 01-.172-.46.03.03 0
 00-.027-.03.038.038 0 00-.021 0l-.006.001a.037.037 0
 00-.01.005L15.624 0c-2.585 1.515-3.657 4.168-3.932 5.856a6.197 6.197
 0 00-2.305.587.297.297 0 00-.147.37c.057.162.24.24.396.17a5.622 5.622
 0 012.008-.523l.067-.005a5.847 5.847 0 011.957.222l.095.03a5.816
 5.816 0 01.616.228c.08.036.16.073.238.112l.107.055a5.835 5.835 0
 01.368.211 5.953 5.953 0 012.034
 2.104c-.62-.437-1.733-.868-2.803-.681 4.183 2.09 3.06 9.292-2.737
 9.02a5.164 5.164 0 01-1.513-.292 4.42 4.42 0
 01-.538-.232c-1.42-.735-2.593-2.121-2.74-3.806 0 0 .537-2 3.845-2
 .357 0 1.38-.998
 1.398-1.287-.005-.095-2.029-.9-2.817-1.677-.422-.416-.622-.616-.8-.767a3.47
 3.47 0 00-.301-.227 5.388 5.388 0 01-.032-2.842c-1.195.544-2.124
 1.403-2.8
 2.163h-.006c-.46-.584-.428-2.51-.402-2.913-.006-.025-.343.176-.389.206-.406.29-.787.616-1.136.974-.397.403-.76.839-1.085
 1.303a9.816 9.816 0 00-1.562 3.52c-.003.013-.11.487-.19
 1.073-.013.09-.026.181-.037.272a7.8 7.8 0
 00-.069.667l-.002.034-.023.387-.001.06C.386 18.795 5.593 24 12.016
 24c5.752 0 10.527-4.176
 11.463-9.661.02-.149.035-.298.052-.448.232-1.994-.025-4.09-.753-5.844z"
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
