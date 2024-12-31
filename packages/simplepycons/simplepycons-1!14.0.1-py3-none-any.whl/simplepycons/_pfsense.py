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


class PfsenseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pfsense"

    @property
    def original_file_name(self) -> "str":
        return "pfsense.svg"

    @property
    def title(self) -> "str":
        return "pfSense"

    @property
    def primary_color(self) -> "str":
        return "#212121"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>pfSense</title>
     <path d="M2.013 0C.898 0 0 .929 0 2.044v17.775L3.252
 8.27h3.282L6.1
 9.785h.063c.186-.217.433-.403.742-.62.31-.216.62-.402.96-.588.342-.186.713-.31
 1.116-.433.402-.124.805-.155 1.208-.155.867 0 1.579.154
 2.198.433.62.279 1.084.712 1.455 1.239.31.464.5 1.019.593
 1.669.006.06.027.135.027.189.062.712-.031 1.518-.28 2.385a8.571 8.571
 0 0 1-1.02 2.322 9.885 9.885 0 0 1-1.58 1.95 8.125 8.125 0 0 1-2.044
 1.364 5.536 5.536 0 0 1-2.354.495 5.655 5.655 0 0
 1-1.982-.34c-.588-.217-.99-.62-1.238-1.177h-.062L2.353
 24h19.603A2.042 2.042 0 0 0 24
 21.956V4.706c-.093-.03-.186-.06-.248-.092a2.771 2.771 0 0
 0-.557-.062c-.557 0-1.022.124-1.394.372-.34.248-.65.743-.867
 1.518l-.526 1.826h2.013l.495 1.58-1.3 1.27h-2.014l-2.446
 8.67h-3.53l2.446-8.67h-1.455l.805-2.85h1.425l.557-2.044c.185-.619.403-1.238.681-1.795a4.996
 4.996 0 0 1 1.053-1.487c.433-.434.99-.775 1.641-1.022.65-.248
 1.487-.372 2.447-.372.248 0 .464 0 .712.031A2.082 2.082 0 0 0 21.988
 0zm6.565 11.118c-.898 0-1.672.278-2.323.805-.65.526-1.083 1.239-1.331
 2.106-.248.867-.217 1.579.155 2.105.31.557.929.805 1.858.805.898 0
 1.672-.278 2.322-.805.65-.526 1.115-1.238
 1.363-2.105.247-.867.185-1.58-.155-2.106-.34-.527-.991-.805-1.89-.805Z"
 />
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
