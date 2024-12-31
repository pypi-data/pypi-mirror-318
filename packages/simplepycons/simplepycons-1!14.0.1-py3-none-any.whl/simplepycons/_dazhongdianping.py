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


class DazhongDianpingIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dazhongdianping"

    @property
    def original_file_name(self) -> "str":
        return "dazhongdianping.svg"

    @property
    def title(self) -> "str":
        return "Dazhong Dianping"

    @property
    def primary_color(self) -> "str":
        return "#FF6633"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dazhong Dianping</title>
     <path d="M6.922 0c-2.407 0-3.28.25-4.16.72A4.905 4.905 0 0 0 .72
 2.763C.25 3.642 0 4.515 0 6.922v10.156c0 2.407.25 3.28.72 4.16.471.88
 1.162 1.57 2.042 2.041.88.47 1.753.721 4.16.721h10.156c2.407 0
 3.28-.25 4.16-.72a4.907 4.907 0 0 0
 2.041-2.042c.471-.88.721-1.753.721-4.16V6.922c0-2.407-.25-3.28-.72-4.16A4.905
 4.905 0 0 0 21.237.72C20.358.25 19.485 0 17.078 0H6.922zm3.139
 2.703a3.07 3.07 0 0 1 3.07 3.07 3.07 3.07 0 0 1-3.07 3.07 3.07 3.07 0
 0 1-3.07-3.07 3.07 3.07 0 0 1 3.07-3.07zm6.994 1.617c.145.66.195
 1.35.13 2.057-.17 1.88-1.105 3.52-2.48 4.656 3.177.427 5.685 2.65
 6.514
 5.5.08.22.148.486.217.723l-2.688.685c-.06-.222-.127-.452-.19-.67-.751-2.622-3.55-4.172-6.273-3.466-2.718.704-4.338
 3.391-3.642
 6.021l.199.729-2.688.687c-.07-.247-.132-.512-.195-.754a7.38 7.38 0 0
 1-.215-2.554c.199-2.2 1.345-4.1
 3.014-5.36-2.634-.47-4.716-2.312-5.506-4.678l2.62-.677c.566 1.534
 2.012 2.689 3.8 2.84 2.446.207 4.604-1.544
 4.818-3.91.036-.394.013-.78-.056-1.151l2.62-.678z" />
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
