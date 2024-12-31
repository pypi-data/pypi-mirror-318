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


class ProcessingFoundationIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "processingfoundation"

    @property
    def original_file_name(self) -> "str":
        return "processingfoundation.svg"

    @property
    def title(self) -> "str":
        return "Processing Foundation"

    @property
    def primary_color(self) -> "str":
        return "#006699"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Processing Foundation</title>
     <path d="M11.999 0a12 12 0 100 24A12 12 0 0012 0zm1.183
 5.255h.048c3.273 0 5.247 1.48 5.247 4.103 0 2.727-1.974 4.536-5.295
 4.669v-1.742c1.837-.11 2.801-1.061 2.801-2.744
 0-1.498-.957-2.442-2.8-2.516zm-1.773.026l.005 11.896c.779.052
 1.583.18 2.26.337l-.269 1.324H6.788v-1.324a14.96 14.96 0
 012.26-.337V6.993a14.71 14.71 0 01-2.26-.337V5.33h2.26c.64 0
 1.469-.028 2.361-.05z" />
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
