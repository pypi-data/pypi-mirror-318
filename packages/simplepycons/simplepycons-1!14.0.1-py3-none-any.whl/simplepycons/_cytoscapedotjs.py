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


class CytoscapedotjsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cytoscapedotjs"

    @property
    def original_file_name(self) -> "str":
        return "cytoscapedotjs.svg"

    @property
    def title(self) -> "str":
        return "Cytoscape.js"

    @property
    def primary_color(self) -> "str":
        return "#F7DF1E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cytoscape.js</title>
     <path d="M24 0v24H0V0h24zm-4.8416 7.2596c-.939
 0-1.7199.6988-1.8416 1.61l-2.7097.6834a1.8574 1.8574 0
 00-1.5505-.834c-1.026 0-1.858.832-1.858 1.858 0 1.0259.832 1.8579
 1.858 1.8579.2554 0 .5063-.052.7388-.1528l1.792 1.8298a2.0325 2.0325
 0
 00-.0493.0932l-2.3452-.316c-.1616-.868-.9238-1.5154-1.8264-1.5154-1.0259
 0-1.858.832-1.858 1.858 0 1.0258.8321 1.858 1.858 1.858a1.859 1.859 0
 001.6365-.9776l2.3456.316c.0214.1408.0573.2788.1074.412l-.984.8666a1.136
 1.136 0 00-.3179-.0454c-.626 0-1.1337.5077-1.1337 1.1338 0 .6258.5078
 1.1336 1.1337 1.1336.626 0 1.1336-.5078 1.1336-1.1336
 0-.0496-.0031-.0988-.0096-.1476l.9446-.832c.34.2325.7417.3572
 1.1578.3572.082 0 .1638-.0048.245-.0145l.8342 1.665a1.8536 1.8536 0
 00-.5009 1.269c0 1.0258.8322 1.858 1.8581 1.858 1.026 0 1.858-.8322
 1.858-1.858 0-1.026-.832-1.8581-1.858-1.8581-.0873
 0-.1743.006-.2604.0182l-.8039-1.6046a2.0519 2.0519 0 00.6834-1.5305
 2.0553 2.0553 0 00-.9357-1.724l.7343-2.4191c.9905-.04 1.7818-.856
 1.7818-1.8565 0-1.0259-.8321-1.858-1.858-1.858zm-1.582
 2.8326c.1244.2014.2862.3776.4762.5185l-.7442 2.4523a2.046 2.046 0
 00-.8189.2015l-1.787-1.8249a1.8483 1.8483 0 00.2025-.6736z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/cytoscape/cytoscape.js/blo
b/97c27700feefe2f7b79fca248763049e9a0b38c6/documentation/img/cytoscape'''

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
