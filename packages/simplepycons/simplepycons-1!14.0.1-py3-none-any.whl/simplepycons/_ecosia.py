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


class EcosiaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ecosia"

    @property
    def original_file_name(self) -> "str":
        return "ecosia.svg"

    @property
    def title(self) -> "str":
        return "Ecosia"

    @property
    def primary_color(self) -> "str":
        return "#008009"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ecosia</title>
     <path d="M15.198
 6.818H8.786v10.48h6.412v-3.342h-3.98v-1.262H13.8V11.42h-2.584v-1.261h3.981zM11.972.06A12.003
 12.003 0 0 0 0 12.064a12.003 12.003 0 0 0 10.083
 11.848c.068-1.277.196-2.723.434-3.652v-.014c0-.005 0-.007-.01-.012
 0-.005-.01-.007-.012-.009 0-.002-.01-.002-.014-.002h-.356c-2.307
 0-5.943-.333-6.916-3.45-1.458-4.642 2.025-6.314 3.484-4.97 0
 .004.012.008.019.008.01 0 .014 0
 .02-.005.01-.005.013-.009.015-.016v-.021c-.322-.945-2.148-6.867
 2.64-8.496 4.08-1.369 8.07 1.491 7.461 5.265v.017c0
 .007.01.012.012.014 0 .002.012.005.016.005 0 0
 .012-.002.016-.005.298-.246 1.603-1.186 2.919-.148 1.247.982.844
 3.73-1.627 5.003-.01.002-.014.007-.02.014v.023c0
 .01.01.014.015.02.01.004.016.004.023.001 1.596-.239 4.316 1.193 2.11
 4.375-1.447 2.1-4.71 2.365-6.168 2.365h-1.071s-.01 0-.012.002c0
 .002-.01.005-.012.007 0 .002 0 .005-.01.009v.012c-.021.751.331
 2.304.693 3.688A12.003 12.003 0 0 0 24 12.063 12.003 12.003 0 0 0
 11.997.06a12.003 12.003 0 0 0-.03 0z" />
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
