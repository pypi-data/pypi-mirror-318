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


class CoronaRendererIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "coronarenderer"

    @property
    def original_file_name(self) -> "str":
        return "coronarenderer.svg"

    @property
    def title(self) -> "str":
        return "Corona Renderer"

    @property
    def primary_color(self) -> "str":
        return "#E6502A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Corona Renderer</title>
     <path
 d="M19.734,11.603c0.078,0.376,0.116,0.76,0.116,1.144c0,1.44-0.562,2.846-1.556,3.889
 c-0.989,1.037-2.358,1.668-3.789,1.741c-1.445,0.074-2.885-0.418-3.979-1.365c-1.079-0.933-1.776-2.265-1.921-3.684
 c-0.148-1.445,0.273-2.914,1.17-4.057c0.877-1.118,2.168-1.879,3.574-2.095c1.439-0.222,2.934,0.127,4.123,0.97
 C18.627,8.965,19.448,10.214,19.734,11.603z
 M24,6v12c0,3.314-2.686,6-6,6H6c-3.314,0-6-2.686-6-6V6c0-3.314,2.686-6,6-6h12
 C21.314,0,24,2.686,24,6z
 M21.828,9.483c-0.465-1.398-1.274-2.674-2.334-3.697c-1.025-0.988-2.279-1.731-3.639-2.152
 c0.159,0.423,0.239,0.874,0.238,1.326c-1.109-1.455-2.809-2.4-4.632-2.564c-1.112-0.1-2.245,0.084-3.265,0.538
 c0.829,0.257,1.555,0.807,2.03,1.533C8.383,3.809,6.29,4.017,4.615,5.028C3.931,5.441,3.324,5.98,2.831,6.609
 c1.151-0.247,2.375,0.069,3.262,0.843c-0.74,0.709-1.754,1.087-2.778,1.039C3.469,8.742,3.652,8.973,3.859,9.18
 c-0.01,0.017-0.021,0.034-0.031,0.051c-0.696,0.314-1.288,0.842-1.68,1.496c-0.438,0.729-0.613,1.6-0.498,2.442
 c0.066,0.481,0.226,0.947,0.469,1.367c-0.108-0.934,0.684-1.758,1.622-1.686c0.921,0.071,1.576,0.983,1.351,1.88
 c-0.16,0.635-0.732,1.107-1.386,1.142c0.87,1.547,2.362,2.701,4.08,3.146c0.608,0.157,1.238,0.226,1.866,0.206
 c-0.471,0.358-1.029,0.608-1.637,0.711c1.493,1.016,3.275,1.567,5.08,1.578c1.455,0.009,2.905-0.33,4.202-0.991
 c1.249-0.636,2.345-1.562,3.184-2.684c0.851-1.139,1.43-2.475,1.676-3.876C22.417,12.472,22.305,10.919,21.828,9.483z"
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
