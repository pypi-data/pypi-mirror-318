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


class UmbracoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "umbraco"

    @property
    def original_file_name(self) -> "str":
        return "umbraco.svg"

    @property
    def title(self) -> "str":
        return "Umbraco"

    @property
    def primary_color(self) -> "str":
        return "#3544B1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Umbraco</title>
     <path d="M0 11.982A12 12 0 1 1 12 24 12 12 0 0 1 0 11.982zm11.756
 4.11a11.856 11.856 0 0 1-2.773-.25 2.12 2.12 0 0
 1-1.514-1.218q-.41-.943-.396-2.895a18.419 18.419 0 0 1
 .127-2.04q.118-.988.236-1.629l.082-.425a.201.201 0 0 0 0-.038.244.244
 0 0 0-.201-.236l-1.544-.246H5.74a.243.243 0 0 0-.235.189 6.517 6.517
 0 0 0-.089.409c-.088.455-.17.9-.26 1.548a19.99 19.99 0 0 0-.176 2.12
 11.165 11.165 0 0 0 0 1.486q.05 1.977.675 3.155.626 1.179 2.106 1.695
 1.482.517 4.135.506h.22q2.655.01 4.134-.506 1.478-.518
 2.1-1.695.623-1.178.678-3.147a11.165 11.165 0 0 0 0-1.485 19.99 19.99
 0 0 0-.176-2.121 30.014 30.014 0 0 0-.26-1.548 6.724 6.724 0 0
 0-.088-.41.243.243 0 0 0-.236-.188h-.04l-1.548.242a.236.236 0 0
 0-.203.236.201.201 0 0 0 0 .037l.081.426q.118.643.236 1.63a18.709
 18.709 0 0 1 .126 2.039q.019 1.95-.396 2.892a2.12 2.12 0 0 1-1.502
 1.22 11.82 11.82 0 0 1-2.769.247Z" />
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
