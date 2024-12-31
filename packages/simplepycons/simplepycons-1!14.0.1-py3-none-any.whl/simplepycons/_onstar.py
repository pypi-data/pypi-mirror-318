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


class OnstarIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "onstar"

    @property
    def original_file_name(self) -> "str":
        return "onstar.svg"

    @property
    def title(self) -> "str":
        return "OnStar"

    @property
    def primary_color(self) -> "str":
        return "#003D7D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OnStar</title>
     <path d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372
 12-12S18.628 0 12 0zm-.049.763c6.233 0 11.304 5.066 11.304 11.294 0
 6.229-5.07 11.295-11.304 11.295-6.233
 0-11.304-5.066-11.304-11.295C.647 5.83 5.718.763 11.951.763zm0
 .287C5.877 1.05.936 5.988.936 12.057c0 6.07 4.941 11.008 11.015
 11.008 6.074 0 11.016-4.938 11.016-11.008
 0-6.069-4.942-11.007-11.016-11.007zm4.73 3.25l.582 1.7 1.8.064-1.44
 1.078.495 1.729-1.472-1.034-1.494 1.004.53-1.717-1.418-1.108
 1.8-.028zM7.99 7.11c2.892 0 4.967 2.155 4.967 4.82v.027c0 2.664-2.102
 4.847-4.994 4.847s-4.967-2.156-4.967-4.82v-.027c0-2.665 2.102-4.848
 4.994-4.848zm-.027 1.9c-1.66 0-2.812 1.313-2.812 2.92v.027c0 1.606
 1.179 2.945 2.839 2.945s2.812-1.312
 2.812-2.918v-.027c0-1.607-1.178-2.946-2.839-2.946zm9.976.322c1.54 0
 2.437 1.018 2.437
 2.665v4.646h-2.035V12.64c0-.964-.455-1.46-1.232-1.46-.776
 0-1.272.496-1.272 1.46v4.003h-2.035V9.466h2.035v1.018c.469-.603
 1.071-1.152 2.102-1.152Z" />
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
