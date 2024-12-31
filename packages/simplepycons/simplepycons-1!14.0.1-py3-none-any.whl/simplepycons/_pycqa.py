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


class PycqaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pycqa"

    @property
    def original_file_name(self) -> "str":
        return "pycqa.svg"

    @property
    def title(self) -> "str":
        return "PyCQA"

    @property
    def primary_color(self) -> "str":
        return "#201B44"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PyCQA</title>
     <path d="M3.256 6.935c-.176 1.188-.244 1.694.88
 1.694l-.008.068H0l.008-.068c1.008 0 1.096-.55
 1.283-1.694l.518-3.331c.187-1.187.275-1.693-.745-1.693l.008-.068H4.57c1.893
 0 2.901.47 2.901 1.618 0 1.9-2.127 2.383-3.761
 2.383h-.176l.008-.08h.148c1.371 0 1.733-1.47 1.733-2.654
 0-.825-.335-1.195-1.108-1.195h-.274zm7.905-1.251-.04-.008c-.657
 2.511-1.303 3.096-2.343 3.096-1.35
 0-1.315-1.008-1.203-1.685l.478-2.929c.028-.195-.127-.343-.402-.255l-.028-.028c.342-.167
 1.028-.382 1.498-.382.558 0 .753.207.646.872l-.51
 3.136c-.08.462.007.745.314.745.598 0 1.08-1.127
 1.439-2.586.167-.677.442-1.94.107-2.108l.028-.028c1.331-.099
 1.981-.079 1.734 1.511l-.53 3.359c-.275 1.725-2.566 3.419-3.734
 3.419-1.961 0-2.578-1.734-3.977-1.734-.597 0-.825.283-.825.558 0
 .243.168.462.518.462.235 0 .53-.235.423-.518 1.343-.135 1.371
 1.881-.08 1.881-.753 0-1.155-.538-1.155-1.175 0-.961.88-2.156
 2.163-2.156 2.264 0 3.144 2.331 3.706 2.331.733 0 .988-1.833
 1.096-2.363zM5.034 22.261c-2.094-.397-3.679-2.239-3.679-4.447 0-2.499
 2.028-4.527 4.526-4.527 2.499 0 4.527 2.028 4.527 4.527a4.51 4.51 0 0
 1-.549 2.162l-1.754-3.034zm3.071-4.32 2.534
 4.383H5.575zm7.604-8.397c-.957-.821-1.563-2.039-1.563-3.398 0-2.469
 2.005-4.474 4.475-4.474 2.469 0 4.474 2.005 4.474 4.474 0 1.23-.497
 2.344-1.3 3.154l.009.034c-.518.522-1.175.921-1.932
 1.136-1.511.43-3.06.031-4.163-.926m5.925-.807c.599-.696.961-1.601.961-2.591
 0-1.777-1.168-3.283-2.778-3.791zm.481 10.831 1.594
 2.76H13.397l5.156-8.929 2.371
 4.106H17.89v1.893l4.055-.001c.052.062.109.119.17.171m-3.725-1.563h3.831c.162-.292.473-.49.831-.49.523
 0 .948.425.948.948 0 .524-.425.949-.948.949a.951.951 0 0
 1-.844-.514H18.39z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/PyCQA/meta/blob/ac828d8d7e'''

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
