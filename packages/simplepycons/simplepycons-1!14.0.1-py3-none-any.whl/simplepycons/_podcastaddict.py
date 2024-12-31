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


class PodcastAddictIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "podcastaddict"

    @property
    def original_file_name(self) -> "str":
        return "podcastaddict.svg"

    @property
    def title(self) -> "str":
        return "Podcast Addict"

    @property
    def primary_color(self) -> "str":
        return "#F4842D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Podcast Addict</title>
     <path d="M5.36.037C2.41.037 0 2.447 0 5.397v13.207c0 2.95 2.41
 5.36 5.36 5.36h13.28c2.945 0 5.36-2.41
 5.36-5.36V5.396c0-2.95-2.415-5.36-5.36-5.36zm6.585 4.285a7.72 7.72 0
 017.717 7.544l.005 7.896h-3.39v-1.326a7.68 7.68 0 01-4.327 1.326
 7.777 7.777 0 01-2.384-.378v-4.63a3.647 3.647 0 002.416.91 3.666
 3.666 0 003.599-2.97h-1.284a2.416 2.416 0
 01-4.73-.66v-.031c0-1.095.728-2.023 1.728-2.316V8.403a3.67 3.67 0
 00-2.975 3.6v6.852a7.72 7.72 0 013.625-14.533zm.031
 1.87V7.43h.006a4.575 4.575 0 014.573 4.574v.01h1.237v-.01a5.81 5.81 0
 00-5.81-5.81zm0 2.149v1.246h.006a2.413 2.413 0 012.415
 2.416v.01h1.247v-.01a3.662 3.662 0 00-3.662-3.662zm0 2.252c-.78
 0-1.409.629-1.409 1.41 0 .78.629 1.409 1.41 1.409.78 0 1.409-.629
 1.409-1.41 0-.78-.629-1.409-1.41-1.409z" />
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
