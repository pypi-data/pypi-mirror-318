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


class FortinetIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fortinet"

    @property
    def original_file_name(self) -> "str":
        return "fortinet.svg"

    @property
    def title(self) -> "str":
        return "Fortinet"

    @property
    def primary_color(self) -> "str":
        return "#EE3124"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fortinet</title>
     <path d="M0 9.785h6.788v4.454H0zm8.666-6.33h6.668v4.453H8.666zm0
 12.637h6.668v4.454H8.666zm8.522-6.307H24v4.454h-6.812zM2.792
 3.455C1.372 3.814.265 5.404 0 7.425v.506h6.788V3.454zM0
 16.091v.554c.24 1.926 1.276 3.466 2.624
 3.9h4.188v-4.454zm24-8.184v-.506c-.265-1.998-1.372-3.587-2.792-3.972h-4.02v4.454H24zM21.376
 20.57c1.324-.458 2.36-1.974 2.624-3.9v-.554h-6.812v4.454Z" />
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
