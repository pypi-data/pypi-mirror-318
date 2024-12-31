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


class QbittorrentIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qbittorrent"

    @property
    def original_file_name(self) -> "str":
        return "qbittorrent.svg"

    @property
    def title(self) -> "str":
        return "qbittorrent"

    @property
    def primary_color(self) -> "str":
        return "#2F67BA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>qbittorrent</title>
     <path d="M11.911 23.994c-1.31
 0-2.605-.232-3.831-.705-3.4-1.024-6.2-3.865-7.433-7.58-1.23-3.708-.685-7.654
 1.459-10.554C4.062 2.038 7.677.094 11.742.008c4.064-.079 7.758 1.703
 9.882 4.785a12.066 12.066 0 0 1 2.369 7.145c.138 3.733-1.75
 7.368-5.052 9.728-2.147 1.535-4.61 2.328-7.03 2.328zm.11-22.314c-.081
 0-.162 0-.244.002-3.5.074-6.599 1.725-8.29 4.415-1.856 2.516-2.31
 5.893-1.25 9.086 1.06 3.197 3.448 5.636 6.386 6.523 3.025 1.165
 6.496.633 9.345-1.402 2.847-2.035 4.473-5.144
 4.351-8.318v-.032c0-2.214-.73-4.41-2.055-6.185-1.78-2.58-4.84-4.09-8.243-4.09zM9.406
 20.246v-4.578a2.663 2.663 0 0 1-.952.863 2.573 2.573 0 0
 1-1.29.344c-1.016
 0-1.893-.444-2.63-1.33-.731-.887-1.097-2.102-1.097-3.646
 0-.939.148-1.781.444-2.527.301-.746.734-1.309 1.299-1.69A3.26 3.26 0
 0 1 7.052 7.1c1.058 0 1.891.487 2.5
 1.46v-1.25h1.306v12.935H9.406zm-4.477-8.285c0 1.203.232 2.108.694
 2.711.463.6 1.016.9 1.662.9.619 0 1.15-.286
 1.597-.855.446-.576.67-1.447.67-2.615
 0-1.245-.237-2.18-.71-2.81-.468-.627-1.02-.941-1.654-.941-.63
 0-1.164.293-1.605.88-.435.581-.654 1.491-.654 2.73m9.55
 4.702h-1.346V3.755h1.452v4.604c.613-.84 1.395-1.258 2.347-1.258.526 0
 1.024.117 1.492.351.464.222.864.558 1.161.978.307.416.546.922.718
 1.514.172.593.258 1.227.258 1.902 0 1.603-.363 2.841-1.088
 3.716-.727.874-1.598 1.312-2.614 1.312-1.011
 0-1.804-.46-2.379-1.382v1.17m-.016-4.746c0 1.122.14 1.932.42
 2.432.456.815 1.074 1.223 1.854 1.223.635 0 1.183-.3
 1.646-.898.462-.604.693-1.503.693-2.695
 0-1.22-.224-2.122-.67-2.703-.44-.58-.975-.872-1.605-.872-.634
 0-1.182.303-1.645.907-.463.6-.694 1.468-.694 2.607" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/qbittorrent/qBittorrent/bl
ob/73028f9930d9ab9d89edb60ed4aedb66d75669d9/src/icons/qbittorrent-tray'''

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
