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


class IkeaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ikea"

    @property
    def original_file_name(self) -> "str":
        return "ikea.svg"

    @property
    def title(self) -> "str":
        return "IKEA"

    @property
    def primary_color(self) -> "str":
        return "#0058A3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>IKEA</title>
     <path d="M0 7.2v9.6h24V7.2H0zm12.002 9.12C5.308 16.32.48 14.36.48
 12s4.831-4.32 11.522-4.32c6.69 0 11.518 1.96 11.518 4.32s-4.824
 4.32-11.518
 4.32zm-.225-6.062h4.176v.964c-.103-.047-.203-.047-.306-.047h-1.758v.46h1.689v.732h-1.689v.457h1.758c.103
 0 .203 0
 .306-.05v.967h-4.176c.052-.101.052-.198.052-.299V10.56c0-.101
 0-.198-.052-.302zm-7.076.302v2.881c0 .101 0
 .198.052.299H2.4c.052-.101.052-.198.052-.299V10.56c0-.101
 0-.198-.052-.299h2.353c-.052.101-.052.198-.052.299zm6.447
 2.881c.076.107.158.208.255.299H8.805c0-.101-.1-.306-.21-.467-.11-.161-.705-1.044-.705-1.044v1.212c0
 .101 0 .198.052.299H5.778c.052-.101.052-.198.052-.299V10.56c0-.101
 0-.198-.052-.299h2.164c-.052.101-.052.198-.052.299v1.259s.691-.88.85-1.085c.12-.154.268-.373.268-.473h2.257c-.155.101-.327.282-.468.45l-.826.984s1.039
 1.548 1.177 1.746zm10.546-3.005a.178.178 0 0
 0-.175-.178h-.21v.551h.083v-.195h.12l.11.195h.093l-.12-.212a.184.184
 0 0 0 .099-.161zm-.189.101h-.114v-.191h.124c.055 0 .093.047.093.101 0
 .053-.048.093-.103.09zm-.021-.457h-.031a.444.444 0 0 0-.437.457c0
 .007 0 .017-.003.023a.466.466 0 0 0 .482.447.464.464 0 0 0
 .458-.47v-.017a.454.454 0 0 0-.469-.44zm0 .823a.372.372 0 0
 1-.375-.366v-.027a.357.357 0 0 1 .375-.339c.206 0
 .375.165.375.366s-.168.366-.375.366zm-.877-.339c-.038-.101-.093-.198-.065-.299h-3.017c.014.101-.024.198-.062.299l-1.07
 2.881a.852.852 0 0
 1-.162.299h1.785c-.014-.101.024-.198.058-.299.034-.101.072-.198.072-.198l.021-.054h1.304l.021.05c.048.118.083.198.083.198.041.101.079.198.069.299h2.263a.837.837
 0 0 1-.169-.299 690.277 690.277 0 0 0-1.131-2.877zm-2.167
 1.893c.155-.42.289-.772.299-.806.028-.074.048-.151.062-.228.017.077.041.154.069.228l.316.806h-.746z"
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
