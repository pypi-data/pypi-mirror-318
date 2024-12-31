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


class AirplayAudioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "airplayaudio"

    @property
    def original_file_name(self) -> "str":
        return "airplayaudio.svg"

    @property
    def title(self) -> "str":
        return "AirPlay Audio"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AirPlay Audio</title>
     <path d="M11.908.183a12.012 12.012 0 00-8.044 3.172c-4.882
 4.475-5.166 12.08-.692 16.962.204.244.448.447.692.692a.315.315 0
 00.408-.04l.53-.61a.32.32 0 000-.448C.53 15.965.243 9.253 4.23 4.982
 8.217.711 14.889.427 19.16 4.414c4.271 3.986 4.555 10.655.568
 14.927-.203.203-.365.407-.568.57a.32.32 0 000 .447l.53.611a.37.37 0
 00.446.04c4.882-4.516 5.166-12.081.692-16.962a11.98 11.98 0
 00-8.92-3.864zm.387 3.518A8.607 8.607 0 006.143 6c-3.458 3.213-3.66
 8.623-.447 12.08.122.123.243.285.406.407a.319.319 0 00.447
 0l.53-.61a.32.32 0 000-.446A7.263 7.263 0 014.8 12.183c0-3.946
 3.212-7.16 7.158-7.16s7.16 3.253 7.16 7.199a7.207 7.207 0 01-2.238
 5.209.319.319 0 000 .447l.529.61c.122.121.325.162.447.04a8.599 8.599
 0 00.408-12.122 8.494 8.494 0 00-5.97-2.705zm-.266 3.316A5.198 5.198
 0 008.34 8.48c-2.075 1.993-2.115 5.247-.122 7.322l.121.123a.319.319 0
 00.447 0l.53-.611a.32.32 0 000-.448 3.814 3.814 0 01-1.098-2.683
 3.732 3.732 0 013.742-3.742 3.732 3.732 0 013.742 3.742c0 1.017-.406
 1.951-1.139 2.683a.32.32 0 000 .448l.53.61a.32.32 0 00.447
 0c2.034-1.992 2.116-5.246.123-7.321a5.128 5.128 0
 00-3.633-1.586zm.006 7.744a.599.599 0 00-.402.146l-.04.041-7.159
 8.055a.506.506 0 00.041.69.437.437 0 00.283.124h14.36a.495.495 0
 00.489-.488.463.463 0 00-.121-.326l-7.08-8.055a.5.5 0 00-.37-.187z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.apple.com/legal/intellectual-prop'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://developer.apple.com/design/human-inte'''

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
