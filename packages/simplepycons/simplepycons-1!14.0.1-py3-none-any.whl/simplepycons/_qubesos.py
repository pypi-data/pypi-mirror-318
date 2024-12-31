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


class QubesOsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qubesos"

    @property
    def original_file_name(self) -> "str":
        return "qubesos.svg"

    @property
    def title(self) -> "str":
        return "Qubes OS"

    @property
    def primary_color(self) -> "str":
        return "#3874D8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Qubes OS</title>
     <path d="M21.893 20.79l-2.289-1.332 1.547-.895a2.402 2.402 0 0 0
 1.2-2.08V7.098l-.003-.059a2.402 2.402 0 0
 0-1.198-2.027l-3.899-2.255-4.21-2.436a2.473 2.473 0 0
 0-.237-.118L12.77.187l-.093-.036-.052-.019c-.028-.01-.057-.018-.085-.027l-.062-.019-.079-.02-.072-.017-.073-.013-.079-.013-.068-.008-.087-.008-.063-.004A10.324
 10.324 0 0 0 11.9
 0h-.03l-.082.001-.076.002-.093.007-.064.006c-.037.004-.073.01-.11.016-.014.004-.029.006-.044.009a3.266
 3.266 0 0 0-.154.034 2.39 2.39 0 0 0-.602.245L5.536 3.277l-3
 1.736a2.407 2.407 0 0 0-1.201 2.083v9.385a2.405 2.405 0 0 0 1.2
 2.08l8.108 4.693a2.395 2.395 0 0 0 2.4.002l1.804-1.044 2.302
 1.339c1.03.599 2.687.599 3.716 0l1.03-.6c1.027-.597
 1.027-1.562-.002-2.161zm-10.71-2.695l-4.46-2.583a1.324 1.324 0 0
 1-.66-1.143V9.206c0-.236.063-.464.177-.662l.002.001c.116-.2.282-.368.482-.485l4.459-2.58c.092-.053.189-.093.289-.122l.034-.01c.035-.01.07-.015.105-.022.023-.004.045-.01.068-.013.031-.004.062-.004.093-.006.028
 0 .055-.004.083-.004.036 0
 .073.004.11.007.02.002.038.002.058.005.037.005.074.014.11.022.018.004.037.007.055.012.04.011.077.025.115.04l.045.015c.052.022.104.047.154.076l4.46
 2.58c.198.116.364.283.48.483l.002.003-.003.002c.116.201.177.43.177.661v5.161c0
 .15-.028.295-.076.433a1.32 1.32 0 0 1-.583.71l-4.46 2.582a1.312 1.312
 0 0 1-1.316 0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/QubesOS/qubes-attachment/b'''

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
