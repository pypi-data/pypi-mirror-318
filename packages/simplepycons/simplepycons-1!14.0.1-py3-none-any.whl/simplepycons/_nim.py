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


class NimIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nim"

    @property
    def original_file_name(self) -> "str":
        return "nim.svg"

    @property
    def title(self) -> "str":
        return "Nim"

    @property
    def primary_color(self) -> "str":
        return "#FFE953"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nim</title>
     <path d="M12.095 3.2s-.92.778-1.857
 1.55c-.964-.032-2.856.199-3.88.598C5.412 4.708 4.582 4 4.582 4s-.709
 1.305-1.154 2.07c-.662.377-1.325.8-1.917 1.36C.824 7.14.026 6.782 0
 6.77c.911 1.967 1.524 3.936 3.19 5.12 2.654-4.483 14.983-4.07
 17.691-.025 1.75-.977 2.43-3.078
 3.119-5.018-.075.026-1.012.362-1.619.61-.363-.423-1.217-1.072-1.702-1.385a96.008
 96.008 0 00-1.131-2.122s-.794.632-1.715
 1.322c-1.243-.246-2.747-.544-4.012-.47A52.988 52.988 0 0112.095
 3.2zM.942 10.95l2.189 5.67c3.801 5.367 13.508 5.74 17.74.105
 1.001-2.415 2.352-5.808 2.352-5.808-1.086 1.72-2.852 2.909-3.94
 3.549-.774.453-2.558.727-2.558.727l-4.684-2.597-4.71
 2.545s-1.761-.303-2.558-.701c-1.608-.92-2.69-2.004-3.83-3.49z" />
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
