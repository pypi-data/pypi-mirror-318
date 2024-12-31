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


class EuropeanUnionIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "europeanunion"

    @property
    def original_file_name(self) -> "str":
        return "europeanunion.svg"

    @property
    def title(self) -> "str":
        return "European Union"

    @property
    def primary_color(self) -> "str":
        return "#003399"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>European Union</title>
     <path d="M11.373 1.94 10.36 1.2h1.253L12 0l.387
 1.2h1.253l-1.013.74.386 1.207L12 2.4l-1.013.747Zm1.254 20.86.386
 1.2L12 23.26l-1.013.74.386-1.2-1.013-.74h1.253L12 20.853l.387
 1.207h1.253ZM1.64 12.8l-1.013.747.386-1.2L0 11.627h1.253l.387-1.2.387
 1.2h1.26l-1.02.746.386 1.2-1.013-.746Zm5.807-9.467.386 1.2L6.82
 3.8l-1.013.74.386-1.2L5.18 2.6h1.253l.387-1.2.387 1.2H8.46Zm-4.78
 3.08.386-1.2.394 1.2h1.22l-1.014.747.387 1.2-1.02-.747L2
 8.36l.387-1.2-1.014-.747ZM1.387 16.84h1.28l.386-1.2.394
 1.2h1.22l-1.014.747.387
 1.2-1.02-.74-1.02.74.387-1.2-1.014-.747Zm4.806
 4.56-1.013-.733h1.253l.387-1.2.387 1.2H8.46l-1.013.733.386
 1.2-1.013-.74-1.013.74Zm16.794-9.027.386
 1.2-1.013-.746-1.027.746.387-1.2-1.02-.746H22l.387-1.2.386
 1.2H24Zm-6.434-9.04L15.54 2.6h1.253l.387-1.2.387
 1.2h1.253l-1.013.733.386 1.2L17.18 3.8l-1.013.74.386-1.2Zm4
 3.074.394-1.2.386 1.2h1.254l-.987.753.387
 1.2-1.014-.747-1.02.747.387-1.2-1.007-.747Zm.78
 10.433h1.254l-.987.747.387
 1.2-1.014-.74-1.02.74.387-1.2-1.007-.747h1.254l.393-1.2.387
 1.2zm-2.513 3.827-1.013.733.386
 1.2-1.013-.74-1.013.74.386-1.2-1.013-.733h1.253l.387-1.2.387 1.2z" />
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
            "EU",
        ]
