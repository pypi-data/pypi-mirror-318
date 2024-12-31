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


class SphinxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sphinx"

    @property
    def original_file_name(self) -> "str":
        return "sphinx.svg"

    @property
    def title(self) -> "str":
        return "Sphinx"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sphinx</title>
     <path d="M16.284
 19.861c0-.654.177-1.834.393-2.623.499-1.822.774-4.079.497-4.079-.116
 0-.959.762-1.873 1.694-3.472 3.54-7.197 5.543-10.312 5.543-1.778
 0-2.987-.45-4.154-1.545C.128 18.186 0 17.858 0
 16.703c0-1.188.117-1.468.909-2.175.718-.642 1.171-.813
 2.157-.813.76.171 1.21.16 1.457.461.251.296.338 1.265.035
 1.832-.162.303-.585.491-1.105.491-.49
 0-.77-.116-.669-.278.315-.511-.135-.857-.713-.548-.699.374-.711
 1.698-.021 2.322.969.878 3.65 1.208 5.262.648 1.743-.605 4.022-2.061
 5.841-3.732l1.6-1.469-2.088-.013c-2.186-.012-3.608-.273-8.211-1.506-1.531-.41-3.003-.765-3.271-.789-.304-.026-.503-.274-.487-.656.027-.646.378-1.127.793-1.308.249-.109
 1.977-.274 3.809-.761 7.136-1.898 7.569-1.629 12.323-.426 1.553.393
 3.351.821 4.147.835 1.227.022 1.493.124
 1.74.666.16.351.291.686.291.745 0 .058-.695.424-1.545.813-3.12
 1.428-4.104 2.185-3.088 3.635.421.602.412.666-.14
 1.052-.323.227-.59.687-.593 1.022-.009.908-.583 2.856-1.417
 3.624l-.732.675v-1.189Zm1.594-8.328c1.242-.346 1.994-.738
 3.539-1.562-1.272-.372-4.462-.895-4.462-.895-2.354-.472-2.108-.448-2.214.071a3.475
 3.475 0 0 1-.45 1.105c-.541.848-2.521
 1.026-3.656.483-.356-.171-.714-.821-.709-1.283.007-.65-.362-.801-.598-.714-.191.07-.813.079-2.179.448-4.514
 1.217-5.132 1.078-2.189 1.495.353.05 2.223.572 3.136.815 2.239.597
 2.658.641 5.556.581 2.015-.042 2.858-.163 4.226-.544ZM.732
 6.258c.056-.577.088-.702 1.692-1.025.919-.185 3.185-.785 5.036-1.333
 4.254-1.26 5.462-1.263 9.873-.026 1.904.535 4.037.973 4.74.975
 1.097.002 1.668.487 1.668.487.505 1.16.412 1.24-1.558 1.24-1.374
 0-2.558-.232-4.385-.857-1.389-.476-3.369-.923-4.451-1.004-1.974-.149-1.971-.15-8.072
 1.529-1.072.295-2.553.624-3.29.732l-1.342.196.089-.914Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/sphinx-doc/sphinx/blob/ed8'''

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
