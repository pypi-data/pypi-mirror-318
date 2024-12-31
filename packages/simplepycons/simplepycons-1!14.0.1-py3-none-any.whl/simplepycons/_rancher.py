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


class RancherIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rancher"

    @property
    def original_file_name(self) -> "str":
        return "rancher.svg"

    @property
    def title(self) -> "str":
        return "Rancher"

    @property
    def primary_color(self) -> "str":
        return "#0075A8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rancher</title>
     <path d="M22.727 9.007a.713.713 0
 01-.726.855h-1.542V8.798h.468a.883.883 0
 00.875-.875v-.388c0-.477.12-.875.269-.875.139 0 .328.388.407.865l.249
 1.482zm-3.49-1.253c.486 0 .874.388.894.885v4.555a.883.883 0
 01-.875.875h-2.357a.883.883 0 01-.875-.875v-1.79a.871.871 0
 00-.348.696v1.502c0 .477.397.875.875.875h1.531v2.327a.535.535 0
 01-.537.538h-2.884a.535.535 0 01-.537-.538v-2.168a.535.535 0
 00-.537-.537h-7.2a.535.535 0 00-.538.537v2.168a.535.535 0
 01-.537.538H2.428a.535.535 0 01-.537-.538V10.58L.588
 11.603c-.06.04-.14.04-.189-.02l-.368-.438a.135.135 0
 01-.01-.159l1.91-2.914a.536.536 0 01.487-.318h10.165a.54.54 0
 01.527.627l-.21 1.243a.54.54 0 00.528.626h2.039a.535.535 0
 00.527-.437c-.13.04-.269.06-.418.06h-1.452c-.487
 0-.815-.388-.736-.866l.249-1.482c.08-.477.258-.865.407-.865.15 0
 .269.398.269.875v.229c.02-.01.05-.01.08-.01h4.843zm3.65-.537c0-.388.288-.557.556-.557.269
 0 .557.17.557.557 0 .378-.288.547-.557.547-.268
 0-.557-.17-.557-.547zm.984 0c0-.308-.2-.438-.418-.438-.219
 0-.428.13-.428.438 0
 .298.21.438.428.438.219-.01.418-.14.418-.438zm-.607-.279h.199c.1 0
 .199.03.199.17 0
 .08-.06.129-.13.149l.13.228h-.12l-.119-.218h-.05v.218h-.109v-.547zm.199.25c.05
 0 .09-.03.09-.08 0-.06-.05-.07-.09-.07h-.1v.15h.1z" />
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
