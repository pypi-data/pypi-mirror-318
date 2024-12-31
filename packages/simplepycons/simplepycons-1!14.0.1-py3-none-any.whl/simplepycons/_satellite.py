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


class SatelliteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "satellite"

    @property
    def original_file_name(self) -> "str":
        return "satellite.svg"

    @property
    def title(self) -> "str":
        return "Satellite"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Satellite</title>
     <path d="M10.413 7.62c.042 0 .063.02.105.02.062 0
 .148-.02.21-.061l.736-.415c.21-.124.273-.372.148-.559l-.946-1.635a.374.374
 0 0
 0-.253-.187c-.105-.02-.23-.02-.315.042l-.735.414c-.211.125-.274.373-.148.56l.946
 1.635c.042.082.147.145.252.186zm3.699
 4.06-.735.413c-.21.125-.274.374-.148.56l.946 1.635a.373.373 0 0 0
 .253.187c.041 0 .062.02.104.02a.409.409 0 0 0
 .211-.062l.735-.414c.21-.125.274-.373.148-.56l-.946-1.635a.375.375 0
 0 0-.252-.187.558.558 0 0 0-.316.042ZM11.989 0C6.105 0 1.333 4.7
 1.333 10.499c0 .953.127 1.884.379 2.795.147.56.735.87
 1.282.725.567-.145.882-.725.736-1.263a8.098 8.098 0 0
 1-.316-2.237C3.436 5.86 7.28 2.071 11.99 2.071s8.555 3.79 8.555
 8.428c0 3.189-1.787 6.067-4.667 7.517a6.35 6.35 0 0
 1-.861.372c-.126.041-.252.104-.4.145a1.046 1.046 0 0 0-.735.994c0
 .498.084 1.056.274
 1.657l-2.46-1.305c-.987-.517-1.955-1.056-2.753-1.822-.904-.87-1.198-1.429-1.282-2.444-.084-.931.147-1.594.904-2.505.4-.497.924-.85
 1.344-1.097.4-.25.82-.477 1.262-.685a2.097 2.097 0 0 0 2.27.146 2.053
 2.053 0 0 0 .798-2.816c-.567-.995-1.849-1.347-2.858-.788a2.021 2.021
 0 0 0-1.051
 1.575c-.525.249-1.05.538-1.534.849-.547.331-1.262.828-1.87
 1.573-.758.932-1.514 2.133-1.367 3.976.126 1.532.631 2.527 1.892
 3.748 1.009.974 2.101 1.595 3.258 2.196l3.95
 2.05c.211.103.463.165.694.165.379 0 .736-.145 1.009-.394a1.41 1.41 0
 0 0 .315-1.656 7.646 7.646 0 0
 1-.588-1.677c.252-.104.505-.229.756-.332 3.595-1.801 5.823-5.384
 5.823-9.36C22.645 4.701 17.875 0 11.989 0Z" />
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
