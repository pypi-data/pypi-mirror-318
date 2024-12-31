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


class BmwIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bmw"

    @property
    def original_file_name(self) -> "str":
        return "bmw.svg"

    @property
    def title(self) -> "str":
        return "BMW"

    @property
    def primary_color(self) -> "str":
        return "#0066B1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>BMW</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0zm0 .78C18.196.78 23.219 5.803 23.219 12c0
 6.196-5.022 11.219-11.219 11.219C5.803 23.219.781 18.196.781
 12S5.804.78 12 .78zm-.678.63c-.33.014-.66.042-.992.078l-.107
 2.944a9.95 9.95 0 0 1 .71-.094l.07-1.988-.013-.137.043.13.664
 1.489h.606l.664-1.488.04-.131-.01.137.07
 1.988c.232.022.473.054.71.094l-.109-2.944a14.746 14.746 0 0
 0-.992-.078l-.653 1.625-.023.12-.023-.12-.655-1.625zm6.696
 1.824l-1.543
 2.428c.195.15.452.371.617.522l1.453-.754.092-.069-.069.094-.752
 1.453c.163.175.398.458.53.63l2.43-1.544a16.135 16.135 0 0
 0-.46-.568L18.777
 6.44l-.105.092.078-.115.68-1.356-.48-.48-1.356.68-.115.078.091-.106
 1.018-1.539c-.18-.152-.351-.291-.57-.46zM5.5
 3.785c-.36.037-.638.283-1.393 1.125a18.97 18.97 0 0 0-.757.914l2.074
 1.967c.687-.76.966-1.042
 1.508-1.613.383-.405.6-.87.216-1.317-.208-.242-.558-.295-.85-.175l-.028.01.01-.026a.7.7
 0 0 0-.243-.734.724.724 0 0
 0-.537-.15zm.006.615c.136-.037.277.06.308.2.032.14-.056.272-.154.382-.22.25-1.031
 1.098-1.031 1.098l-.402-.383c.417-.51.861-.974 1.062-1.158a.55.55 0 0
 1 .217-.139zM12 4.883a7.114 7.114 0 0 0-7.08 6.388v.002a7.122 7.122 0
 0 0 8.516 7.697 7.112 7.112 0 0 0 5.68-6.97A7.122 7.122 0 0 0 12
 4.885v-.002zm-5.537.242c.047 0
 .096.013.14.043.088.059.128.16.106.26-.026.119-.125.231-.205.318l-1.045
 1.12-.42-.4s.787-.832 1.045-1.099c.102-.106.168-.17.238-.205a.331.331
 0 0 1 .14-.037zM12 5.818A6.175 6.175 0 0 1 18.182 12H12v6.182A6.175
 6.175 0 0 1 5.818 12H12V5.818Z" />
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
