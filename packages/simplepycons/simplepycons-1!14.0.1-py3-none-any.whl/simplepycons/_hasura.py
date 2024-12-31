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


class HasuraIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hasura"

    @property
    def original_file_name(self) -> "str":
        return "hasura.svg"

    @property
    def title(self) -> "str":
        return "Hasura"

    @property
    def primary_color(self) -> "str":
        return "#1EB4D4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hasura</title>
     <path d="M23.558 8.172c.707-2.152.282-6.447-1.09-8.032a.419.419 0
 0 0-.664.051l-1.69 2.59a1.322 1.322 0 0 1-1.737.276C16.544 1.885
 14.354 1.204 12 1.204s-4.544.68-6.378 1.853a1.326 1.326 0 0
 1-1.736-.276L2.196.191A.42.42 0 0 0 1.532.14C.16 1.728-.265 6.023.442
 8.172c.236.716.3 1.472.16 2.207-.137.73-.276 1.61-.276 2.223C.326
 18.898 5.553 24 11.997 24c6.447 0 11.671-5.105 11.671-11.398
 0-.613-.138-1.494-.276-2.223a4.468 4.468 0 0 1 .166-2.207zm-11.56
 13.284c-4.984 0-9.036-3.96-9.036-8.827
 0-.16.005-.316.014-.473.18-3.316 2.243-6.15 5.16-7.5 1.17-.546
 2.481-.848 3.864-.848s2.69.302 3.864.85c2.917 1.351 4.98 4.187 5.16
 7.501.008.157.014.316.014.473-.003 4.864-4.057 8.824-9.04
 8.824zm3.915-5.43-2.31-3.91-1.98-3.26a.26.26 0 0
 0-.223-.125H9.508a.26.26 0 0 0-.227.13.246.246 0 0 0 .003.254l1.895
 3.109-2.542 3.787a.25.25 0 0 0-.011.259.26.26 0 0 0
 .23.132h1.905a.259.259 0 0 0 .218-.116l1.375-2.096 1.233
 2.088a.263.263 0 0 0 .224.127h1.878c.094 0 .18-.049.224-.127a.241.241
 0 0 0 0-.251z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/hasura/graphql-engine/blob'''

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
