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


class PumaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "puma"

    @property
    def original_file_name(self) -> "str":
        return "puma.svg"

    @property
    def title(self) -> "str":
        return "Puma"

    @property
    def primary_color(self) -> "str":
        return "#242B2F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Puma</title>
     <path d="M23.845 3.008c-.417-.533-1.146-.106-1.467.08-2.284
 1.346-2.621 3.716-3.417 5.077-.626 1.09-1.652 1.89-2.58
 1.952-.686.049-1.43-.084-2.168-.405-1.807-.781-2.78-1.792-3.017-1.97-.487-.37-4.23-4.015-7.28-4.164
 0
 0-.372-.75-.465-.763-.222-.025-.45.451-.616.501-.15.053-.413-.512-.565-.487-.153.02-.302.586-.6.877-.22.213-.486.2-.637.463-.052.096-.034.265-.093.42-.127.32-.551.354-.555.697
 0
 .381.357.454.669.72.248.212.265.362.554.461.258.088.632-.187.964-.088.277.081.543.14.602.423.054.256
 0 .658-.34.613-.112-.015-.598-.174-1.198-.11-.725.077-1.553.309-1.634
 1.11-.041.447.514.97 1.055.866.371-.071.196-.506.399-.716.267-.27
 1.772.944 3.172.944.593 0 1.031-.15
 1.467-.605.04-.029.093-.102.155-.11a.632.632 0 01.195.088c1.131.897
 1.984 2.7 6.13 2.721.582.007 1.25.279 1.796.777.48.433.764 1.125
 1.037 1.825.418 1.053 1.161 2.069 2.292 3.203.06.068.99.78
 1.06.833.012.01.084.167.053.255-.02.69-.123 2.67 1.365
 2.753.366.02.275-.231.275-.41-.005-.341-.065-.685.113-1.04.253-.478-.526-.709-.509-1.756.019-.784-.645-.651-.984-1.25-.19-.343-.368-.532-.35-.946.073-2.38-.517-3.948-.805-4.327-.227-.294-.423-.403-.207-.54
 1.24-.815 1.525-1.574 1.525-1.574.66-1.541 1.256-2.945
 2.075-3.57.166-.12.589-.44.852-.56.763-.362 1.173-.578
 1.388-.788.356-.337.635-1.053.294-1.48z" />
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
