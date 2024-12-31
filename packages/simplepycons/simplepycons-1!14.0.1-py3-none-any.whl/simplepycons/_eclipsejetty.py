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


class EclipseJettyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "eclipsejetty"

    @property
    def original_file_name(self) -> "str":
        return "eclipsejetty.svg"

    @property
    def title(self) -> "str":
        return "Eclipse Jetty"

    @property
    def primary_color(self) -> "str":
        return "#FC390E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Eclipse Jetty</title>
     <path d="M4.9847 2.7514a.842.842 0 00-.8203.6525l-.617
 2.673a.842.842 0 00.023.4591.842.842 0 00-.222.403L.986
 17.1715c-.0428.0033-.0642.0065-.1198.0087a.842.842 0
 00-.8086.821l-.0575 2.3853a.842.842 0 00.8446.8622c1.3542-.0049
 2.7158-.0093 4.0669-.0156.543-.0142 1.0992-.2356
 1.5074-.6331.4083-.3976.6578-.921.842-1.548a.8442.8442 0
 00.0127-.048l.093-.4032a.842.842 0 00.8083.6073h2.5182a.842.842 0
 00.763-.486l6.8882-14.773c.26-.558-.1472-1.1974-.7628-1.1976h-2.5181a.842.842
 0 00-.763.4862L12.8664 6.313a.842.842 0
 00-.209-.0265h-2.4478l.578-2.5039c.1216-.5275-.279-1.031-.8203-1.0312zm15.6543
 0a.842.842 0 00-.763.4862l-6.8883 14.7728c-.26.5581.1473 1.1974.763
 1.1976h2.518a.842.842 0
 00.763-.486l6.8884-14.773c.26-.5581-.1473-1.1974-.763-1.1976zm-15.6543.842h4.9827l-.617
 2.6729H4.3679zm10.0789 0h2.518l-6.8883
 14.7728H8.1751l.3446-.739h1.9084a.842.842 0
 00.8202-.6524l.856-3.7076c.1216-.5275-.279-1.031-.8202-1.0312h-.2506l.2603-.5581h.5077a.842.842
 0 00.8202-.6526l.856-3.7075a.842.842 0 00.008-.3403zm5.5754
 0h2.5182l-6.8885 14.7728h-2.518zM4.1685 7.1284h2.6244l-.8122
 3.5182c-.1217.5275.2788 1.0311.8202
 1.0313H8.101l-.129.558H6.2835a.842.842 0 00-.8203.6525l-.856
 3.7076c-.1215.5275.279 1.031.8202 1.0312h1.3003l-.2741 1.1874c-.321
 1.0921-.8075 1.5347-1.5882
 1.5778l-4.0236.0144.0575-2.3855c.4885-.0192.7073.0034.851-.4182zm3.4882
 0h5.0008l-.8559 3.7077H6.801zm1.3083
 4.5495h1.4l-.2604.558H8.8361zm-2.6816 1.3999h5.0008l-.856
 3.7076H5.4272Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/eclipse/jetty.project/blob'''

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
