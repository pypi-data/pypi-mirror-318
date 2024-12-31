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


class ClojureIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "clojure"

    @property
    def original_file_name(self) -> "str":
        return "clojure.svg"

    @property
    def title(self) -> "str":
        return "Clojure"

    @property
    def primary_color(self) -> "str":
        return "#5881D8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Clojure</title>
     <path d="M11.503 12.216c-.119.259-.251.549-.387.858-.482
 1.092-1.016 2.42-1.21 3.271a4.91 4.91 0 0 0-.112 1.096c0
 .164.009.337.022.514.682.25 1.417.388 2.186.39a6.39 6.39 0 0 0
 2.001-.326 3.808 3.808 0 0
 1-.418-.441c-.854-1.089-1.329-2.682-2.082-5.362M8.355 6.813A6.347
 6.347 0 0 0 5.657 12a6.347 6.347 0 0 0 2.625 5.134c.39-1.622
 1.366-3.107
 2.83-6.084-.087-.239-.186-.5-.297-.775-.406-1.018-.991-2.198-1.513-2.733a4.272
 4.272 0 0 0-.947-.729M17.527
 19.277c-.84-.105-1.533-.232-2.141-.446A7.625 7.625 0 0 1 4.376 12a7.6
 7.6 0 0 1 2.6-5.73 5.582 5.582 0 0 0-1.324-.162c-2.236.02-4.597
 1.258-5.58 4.602-.092.486-.07.854-.07 1.29 0 6.627 5.373 12 12 12
 4.059 0 7.643-2.017 9.815-5.101-1.174.293-2.305.433-3.271.436-.362
 0-.702-.02-1.019-.058M15.273 16.952c.074.036.242.097.475.163a6.354
 6.354 0 0 0 2.6-5.115h-.002a6.354 6.354 0 0 0-6.345-6.345 6.338 6.338
 0 0 0-1.992.324c1.289 1.468 1.908 3.566 2.507
 5.862l.001.003c.001.002.192.637.518 1.48.326.842.789 1.885 1.293
 2.645.332.51.697.876.945.983M12.001 0a11.98 11.98 0 0 0-9.752
 5.013c1.134-.71 2.291-.967 3.301-.957 1.394.004 2.491.436
 3.017.732.127.073.248.152.366.233A7.625 7.625 0 0 1 19.625 12a7.605
 7.605 0 0 1-2.268 5.425c.344.038.709.063 1.084.061 1.328 0 2.766-.293
 3.842-1.198.703-.592 1.291-1.458 1.617-2.757.065-.502.1-1.012.1-1.531
 0-6.627-5.371-12-11.999-12" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Cloju'''

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
