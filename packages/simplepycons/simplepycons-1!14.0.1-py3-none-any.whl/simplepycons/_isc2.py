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


class IscTwoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "isc2"

    @property
    def original_file_name(self) -> "str":
        return "isc2.svg"

    @property
    def title(self) -> "str":
        return "ISC2"

    @property
    def primary_color(self) -> "str":
        return "#468145"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ISC2</title>
     <path d="M14.153 8.677c.876 0 1.592.333
 2.196.839.014.012.063.051.077.064.059.049.071.052.142-.022l.068-.072.518-.566c.055-.065.046-.07.006-.112l-.071-.069c-.777-.69-1.776-1.183-2.936-1.183-2.454
 0-4.366 1.972-4.366 4.45s1.912 4.438 4.366 4.438c1.16 0 2.161-.523
 2.939-1.226.086-.074.118-.101.032-.187l-.528-.577c-.086-.087-.109-.066-.195.008-.604.505-1.372.861-2.248.861-1.763
 0-3.194-1.431-3.194-3.317 0-1.898 1.431-3.329 3.194-3.329ZM4.1
 9.824c0-.752.617-1.208 1.443-1.208.716 0 1.246.296
 1.814.826.086.086.114.134.2.035l.512-.553c.087-.099.04-.123-.046-.209a3.317
 3.317 0 0 0-2.492-1.159c-1.419 0-2.541.924-2.541 2.256 0 2.786 4.292
 2.207 4.292 4.142 0 .789-.69 1.406-1.714 1.406-.985
 0-1.504-.454-2.047-.971-.086-.087-.105-.107-.179-.033l-.585.553c-.087.074-.078.08-.017.179.561.756
 1.607 1.344 2.828 1.344 1.53 0 2.849-1.011 2.849-2.429
 0-2.934-4.317-2.28-4.317-4.179ZM1.147 7.639v7.616a.06.06 0 0
 1-.019.044L.044
 16.346c-.016.016-.044.004-.044-.019V7.639c0-.014.012-.026.026-.026h1.095c.014
 0 .026.012.026.026Zm20.056-.066c-1.11 0-1.99.49-2.533 1.168a1.213
 1.213 0 0
 0-.057.081c-.04.061-.029.066.027.128.14.156.576.649.576.649.018.019.035.02.051.006l.075-.071c.346-.358.936-.95
 1.849-.95 1.024 0 1.64.642 1.64 1.578 0 1.33-.762 1.962-2.459
 3.389-.494.415-1.405 1.215-1.633 1.414a.158.158 0 0
 0-.052.117v1.194c0 .053.063.082.103.047.468-.411 2.405-2.107
 3.034-2.641 1.629-1.384 2.068-2.324 2.068-3.532
 0-1.467-1.06-2.577-2.689-2.577Zm2.734 7.792H21.2a.064.064 0 0
 0-.064.064v.81c0 .035.029.063.064.063h2.737a.063.063 0 0 0
 .063-.063v-.81a.064.064 0 0 0-.063-.064Z" />
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
        yield from [
            "(ISC)²",
        ]
