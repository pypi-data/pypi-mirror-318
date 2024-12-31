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


class CalendlyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "calendly"

    @property
    def original_file_name(self) -> "str":
        return "calendly.svg"

    @property
    def title(self) -> "str":
        return "Calendly"

    @property
    def primary_color(self) -> "str":
        return "#006BFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Calendly</title>
     <path d="M19.655 14.262c.281 0 .557.023.828.064 0
 .005-.005.01-.005.014-.105.267-.234.534-.381.786l-1.219 2.106c-1.112
 1.936-3.177 3.127-5.411 3.127h-2.432c-2.23
 0-4.294-1.191-5.412-3.127l-1.218-2.106a6.251 6.251 0 0 1
 0-6.252l1.218-2.106C6.736 4.832 8.8 3.641 11.035 3.641h2.432c2.23 0
 4.294 1.191 5.411 3.127l1.219 2.106c.147.252.271.519.381.786 0
 .004.005.009.005.014-.267.041-.543.064-.828.064-1.816
 0-2.501-.607-3.291-1.306-.764-.676-1.711-1.517-3.44-1.517h-1.029c-1.251
 0-2.387.455-3.2 1.278-.796.805-1.233 1.904-1.233 3.099v1.411c0
 1.196.437 2.295 1.233 3.099.813.823 1.949 1.278 3.2 1.278h1.034c1.729
 0 2.676-.841 3.439-1.517.791-.703 1.471-1.306
 3.287-1.301Zm.005-3.237c.399 0 .794-.036
 1.179-.11-.002-.004-.002-.01-.002-.014-.073-.414-.193-.823-.349-1.218.731-.12
 1.407-.396 1.986-.819
 0-.004-.005-.013-.005-.018-.331-1.085-.832-2.101-1.489-3.03-.649-.915-1.435-1.719-2.331-2.395-1.867-1.398-4.088-2.138-6.428-2.138-1.448
 0-2.855.28-4.175.841-1.273.543-2.423 1.315-3.407 2.299S2.878 6.552
 2.341 7.83c-.557 1.324-.842 2.726-.842 4.175 0 1.448.281 2.855.842
 4.174.542 1.274 1.314 2.423 2.298 3.407s2.129 1.761 3.407
 2.299c1.324.556 2.727.841 4.175.841 2.34 0 4.561-.74
 6.428-2.137a10.815 10.815 0 0 0 2.331-2.396c.652-.929 1.158-1.949
 1.489-3.03
 0-.004.005-.014.005-.018-.579-.423-1.255-.699-1.986-.819.161-.395.276-.804.349-1.218.005-.009.005-.014.005-.023.869.166
 1.692.506 2.404 1.035.685.505.552 1.075.446 1.416C22.184 20.437
 17.619 24 12.221 24c-6.625 0-12-5.375-12-12s5.37-12 12-12c5.398 0
 9.963 3.563 11.471 8.464.106.341.239.915-.446
 1.421-.717.529-1.535.873-2.404 1.034.128.716.128 1.45 0
 2.166-.387-.074-.782-.11-1.182-.11-4.184 0-3.968 2.823-6.736
 2.823h-1.029c-1.899 0-3.15-1.357-3.15-3.095v-1.411c0-1.738
 1.251-3.094 3.15-3.094h1.034c2.768 0 2.552 2.823 6.731 2.827Z" />
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
