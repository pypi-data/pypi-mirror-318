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


class GrapheneosIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "grapheneos"

    @property
    def original_file_name(self) -> "str":
        return "grapheneos.svg"

    @property
    def title(self) -> "str":
        return "GrapheneOS"

    @property
    def primary_color(self) -> "str":
        return "#0053A3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GrapheneOS</title>
     <path d="m6.953 7.244 3.458-1.97a1.901 1.901 0 0
 1-.108-.608c0-.835.608-1.525 1.407-1.67V0h.58v2.995a1.704 1.704 0 0 1
 1.407 1.67c0 .219-.045.418-.118.609l3.468
 1.97c.127-.146.281-.273.454-.382a1.705 1.705 0 0 1
 2.151.382l2.596-1.498.29.508-2.595 1.498a1.69 1.69 0 0 1-1.244
 2.242v4.012a1.69 1.69 0 0 1 1.244 2.242l2.596
 1.498-.29.508-2.597-1.498a1.705 1.705 0 0 1-2.151.382 2.065 2.065 0 0
 1-.454-.382c-1.153.654-2.306 1.317-3.468 1.97.073.19.118.39.118.608 0
 .835-.608 1.525-1.407 1.67V24h-.58v-2.995a1.704 1.704 0 0
 1-1.407-1.67c0-.219.045-.418.108-.609l-3.458-1.97a2.065 2.065 0 0
 1-.454.382 1.705 1.705 0 0 1-2.151-.382l-2.596 1.498-.29-.508
 2.595-1.498a1.69 1.69 0 0 1 1.244-2.242V9.994a1.69 1.69 0 0
 1-1.244-2.242L1.461 6.254l.29-.508 2.597 1.498a1.705 1.705 0 0 1
 2.151-.382c.173.11.327.236.454.382Zm9.803 9.004a1.682 1.682 0 0 1
 .128-1.425 1.702 1.702 0 0 1 1.234-.835v-3.976a1.702 1.702 0 0
 1-1.234-.835 1.682 1.682 0 0 1-.128-1.425L13.29
 5.773c-.318.363-.772.59-1.289.59-.517 0-.971-.227-1.289-.59L7.244
 7.752c.163.454.136.98-.128 1.425a1.702 1.702 0 0
 1-1.234.835v3.976c.5.073.962.363 1.234.835.264.445.291.971.128
 1.425l3.467 1.979c.318-.363.772-.59 1.289-.59.517 0 .971.227
 1.289.59z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/GrapheneOS/branding-extra/'''

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
