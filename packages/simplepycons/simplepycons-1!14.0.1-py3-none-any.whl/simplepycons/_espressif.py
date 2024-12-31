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


class EspressifIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "espressif"

    @property
    def original_file_name(self) -> "str":
        return "espressif.svg"

    @property
    def title(self) -> "str":
        return "Espressif"

    @property
    def primary_color(self) -> "str":
        return "#E7352C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Espressif</title>
     <path d="M12.926 19.324a7.6 7.6 0 00-2.983-6.754 7.44 7.44 0
 00-3.828-1.554.697.697 0 01-.606-.731.674.674 0 01.743-.617 8.97 8.97
 0 018 9.805 7.828 7.828 0 01-.298 1.542l1.989.56a11.039 11.039 0
 001.714-.651 12.159 12.159 0 00.217-2.343A12.57 12.57 0 007.212
 6.171a5.53 5.53 0 00-2 0 4.354 4.354 0 00-2.16 1.337 4.274 4.274 0
 001.909 6.856 9.896 9.896 0 001.074.195 4.011 4.011 0 013.337 3.954
 3.965 3.965 0 01-.64 2.16l1.371.88a10.182 10.182 0 002.057.342 7.52
 7.52 0 00.754-2.628m.16 4.73A13.073 13.073 0 01.001 10.983 12.982
 12.982 0 013.83 1.737l.743.697a12.067 12.067 0 000 17.141 12.067
 12.067 0 0017.141 0l.697.697a12.97 12.97 0 01-9.336 3.726M24
 10.993A10.993 10.993 0 0012.949 0c-.389 0-.766
 0-1.143.057l-.252.732a18.912 18.912 0 0111.588
 11.576l.731-.263c0-.366.069-.732.069-1.143m-1.269 5.165A17.53 17.53 0
 007.818 1.27a11.119 11.119 0 00-2.457 1.77v1.635A13.919 13.919 0
 0119.268 18.57h1.634a11.713 11.713 0 001.771-2.446M7.92 17.884a1.691
 1.691 0 11-1.69-1.691 1.691 1.691 0 011.69 1.691" />
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
