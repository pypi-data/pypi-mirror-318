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


class ClarifaiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "clarifai"

    @property
    def original_file_name(self) -> "str":
        return "clarifai.svg"

    @property
    def title(self) -> "str":
        return "Clarifai"

    @property
    def primary_color(self) -> "str":
        return "#1955FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Clarifai</title>
     <path d="M2.78 14.772A2.768 2.768 0 0 1 0 12.008a2.781 2.781 0 0
 1 2.78-2.78 2.765 2.765 0 0 1 2.764 2.764c0 1.52-1.23 2.78-2.764
 2.78zM17.119 1.83c-2.05 0-2.142 1.732-5.27 1.732-3.16
 0-3.419-1.732-5.287-1.732a2.765 2.765 0 0 0-2.765 2.765 2.775 2.775 0
 0 0 2.765 2.764c2.066 0 2.157-1.731 5.286-1.731 3.16 0 3.418 1.731
 5.286 1.731A2.765 2.765 0 0 0 19.9 4.595a2.778 2.778 0 0
 0-2.78-2.765zm0 14.81c-2.066 0-2.157 1.732-5.286 1.732-3.16
 0-3.418-1.731-5.286-1.731a2.765 2.765 0 0 0-2.765 2.764 2.775 2.775 0
 0 0 2.765 2.765c2.066 0 2.157-1.732 5.286-1.732 3.16 0 3.418 1.732
 5.286 1.732a2.765 2.765 0 0 0 0-5.53zm4.101-7.397c-2.08 0-2.005
 1.823-4.617 1.823-2.416-.015-2.446-1.823-4.755-1.823-1.443 0-2.628
 1.322-2.628 2.765s1.2 2.764 2.765 2.764c2.08 0 2.005-1.823
 4.618-1.823 2.415 0 2.445 1.808 4.77 1.808 1.442 0 2.627-1.322
 2.627-2.765 0-1.427-1.2-2.749-2.78-2.749Z" />
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
