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


class PrometheusIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "prometheus"

    @property
    def original_file_name(self) -> "str":
        return "prometheus.svg"

    @property
    def title(self) -> "str":
        return "Prometheus"

    @property
    def primary_color(self) -> "str":
        return "#E6522C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Prometheus</title>
     <path d="M12 0C5.373 0 0 5.372 0 12c0 6.627 5.373 12 12
 12s12-5.373 12-12c0-6.628-5.373-12-12-12zm0 22.46c-1.885
 0-3.414-1.26-3.414-2.814h6.828c0 1.553-1.528 2.813-3.414
 2.813zm5.64-3.745H6.36v-2.046h11.28v2.046zm-.04-3.098H6.391c-.037-.043-.075-.086-.111-.13-1.155-1.401-1.427-2.133-1.69-2.879-.005-.025
 1.4.287 2.395.511 0 0 .513.119
 1.262.255-.72-.843-1.147-1.915-1.147-3.01 0-2.406 1.845-4.508
 1.18-6.207.648.053 1.34 1.367 1.387 3.422.689-.951.977-2.69.977-3.755
 0-1.103.727-2.385 1.454-2.429-.648 1.069.168 1.984.894
 4.256.272.854.237 2.29.447 3.201.07-1.892.395-4.652 1.595-5.605-.529
 1.2.079 2.702.494 3.424.671 1.164 1.078 2.047 1.078 3.716a4.642 4.642
 0 01-1.11 2.996c.792-.149 1.34-.283 1.34-.283l2.573-.502s-.374
 1.538-1.81 3.019z" />
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
