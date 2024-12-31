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


class PremierLeagueIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "premierleague"

    @property
    def original_file_name(self) -> "str":
        return "premierleague.svg"

    @property
    def title(self) -> "str":
        return "Premier League"

    @property
    def primary_color(self) -> "str":
        return "#360D3A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Premier League</title>
     <path d="M11.176 0s-.681 1.938-.867 2.527C9.844 2.202 8.386 1.194
 7.78.775c.14.806.356 2.124.403
 2.403-.124-.093-.821-.698-1.875-1.194.589.682 1.008 1.736 1.271
 2.588a10.566 10.566 0 0 1 5.238-1.379c.977 0 1.94.14
 2.854.403.093-.884.279-1.968.682-2.758-.915.728-1.474 1.503-1.551
 1.596-.031-.186-.093-1.52-.17-2.434-.372.403-1.8 2.016-2.063
 2.264C12.384 1.938 11.176 0 11.176 0zm1.674 3.86c-1.674
 0-3.3.386-4.696 1.115.713.046 1.224.668 1.395
 1.164-.558-.45-1.442-.667-1.985-.078-.511.589-.464 1.688.047
 2.572-1.193-.605-1.194-2.185-.775-2.867A10.392 10.392 0 0 0 3.61
 9.594l1.07.172c-1.24 1.426-2.107 3.953-2.107 5.146l1.75-.543c-.31
 1.054-.401 4.602.653 6.385 0 0 1.38-.96 2.945-3.363.65 2.17.356 3.985
 0 5.767 2.82 1.581 6.09.696 8.012-.683l.357 1.35c2.248-1.489
 3.488-3.628
 3.72-6.124l.837.93c1.286-3.829.28-6.883-1.565-9.502l-.078.637-.79-.87s.17-.077.31-.263c.03-.078-.046-.495-.371-.774-.31.078-.56.264-.684.45a3.222
 3.222 0 0 0-.93-.543c.062.077.604.79.65 1.007.466.388 1.102.837 1.52
 1.395-.34-.403-1.984-.497-2.728-.078 0
 0-.744-.868-1.426-1.473-.14-.511.326-.96.326-.96s-.48-.03-.93.42c-.682-.512-1.55-.745-1.55-.745-.961.14-1.612.82-1.612.82.217.14.512.327.776.42.511.217
 1.006.139 1.332.139.263 0 .636.078.636.078s.635.495 1.565
 1.565c-1.426-.574-2.915.062-3.969-.45-1.24-.62-1.146-1.595-1.146-1.595s-.836-.11-.836-.141c0
 0 .618-.82 1.548-1.1l-.464-.402c.558-.465 1.534-1.085 3.115-1.24 0 0
 .683.262 2.11 1.285.232-.326.308-1.008.308-1.008.728.248 2.217 1.333
 2.806
 1.984-.325-.759-.559-1.223-.636-2.013-.357-.357-1.24-1.101-3.069-1.551.295.605.264
 1.115.264
 1.115-.34-.45-1.055-1.146-1.55-1.332-.295-.015-.605-.047-.93-.047zm3.271
 7.068a4.323 4.323 0 0 0 1.256.697v1.348c-.465.403-1.985 1.675-3.008
 1.566-.573-1.1-1.115-2.107-1.115-2.107s1.565-1.318
 2.867-1.504zm2.975.031c.465 1.131.59 2.48.078
 3.379-.28-.605-.636-.947-1.008-1.35v-1.347s.418-.264.93-.682zm-.977
 3.395c.465.511.559 1.068.559 1.068-.202 1.131-.836 1.846-1.301
 2.14.046-.821-.172-1.519-.172-1.519-.34.372-1.13.743-1.596.836l-.697-1.3c.822-.032
 2.201-1.194 2.201-1.194l1.006-.031z" />
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
