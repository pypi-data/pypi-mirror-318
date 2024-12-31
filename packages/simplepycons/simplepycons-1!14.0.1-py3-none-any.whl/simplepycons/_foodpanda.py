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


class FoodpandaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "foodpanda"

    @property
    def original_file_name(self) -> "str":
        return "foodpanda.svg"

    @property
    def title(self) -> "str":
        return "foodpanda"

    @property
    def primary_color(self) -> "str":
        return "#D70F64"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>foodpanda</title>
     <path d="M4.224 0a3.14 3.14 0 00-3.14 3.127 3.1 3.1 0 001.079
 2.36 11.811 11.811 0 00-2.037 6.639C.126 18.68 5.458 24 12 24c6.542 0
 11.874-5.32 11.874-11.874a11.69 11.69 0 00-2.025-6.614 3.136 3.136 0
 001.09-2.373A3.132 3.132 0 0019.8.012a3.118 3.118 0 00-2.636
 1.438A11.792 11.792 0 0012.012.264c-1.845 0-3.595.419-5.152
 1.174A3.133 3.133 0 004.224 0zM12 1.198c1.713 0 3.331.396 4.78
 1.102a10.995 10.995 0 014.29 3.715 10.89 10.89 0 011.882 6.135c.011
 6.039-4.901 10.951-10.94 10.951-6.04 0-10.951-4.912-10.951-10.951
 0-2.277.694-4.386 1.88-6.135A11.08 11.08 0 017.232 2.3 10.773 10.773
 0 0112 1.198zM7.367 6.345c-.853.012-1.743.292-2.28.653-1.031.682-2.29
 2.156-2.085 4.181.191 2.025 1.785 3.283 2.612 3.283.826 0 1.234-.42
 1.485-1.45.252-1.018 1.115-2.192
 2.217-3.45s-.024-2.469-.024-2.469c-.393-.513-1.052-.727-1.755-.747a3.952
 3.952 0 00-.17-.001zm9.233.007l-.17.001c-.702.02-1.358.233-1.746.752
 0 0-1.126 1.21-.024 2.469 1.114 1.258 1.965 2.432 2.217 3.45.251
 1.019.659 1.438 1.485 1.45.827 0 2.409-1.258
 2.612-3.283.204-2.025-1.054-3.51-2.084-4.182-.544-.36-1.437-.643-2.29-.657zm-8.962
 2c.348 0 .624.275.624.623-.012.335-.288.623-.624.623a.619.619 0
 01-.623-.623c0-.348.276-.624.623-.624zm8.891 0c.348 0
 .623.275.623.623-.012.335-.287.623-.623.623a.619.619 0
 01-.623-.623c0-.348.288-.624.623-.624zm-4.541 4.025c-.527
 0-2.06.096-2.06.587 0 .887 1.88 1.522 2.06 1.474.18.048 2.06-.587
 2.06-1.474 0-.49-1.52-.587-2.06-.587zM9.076 15.17c0 1.414 1.294 2.564
 2.912 2.564 1.618 0 2.924-1.15 2.924-2.564z" />
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
