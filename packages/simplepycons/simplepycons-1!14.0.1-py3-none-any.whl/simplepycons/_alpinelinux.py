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


class AlpineLinuxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "alpinelinux"

    @property
    def original_file_name(self) -> "str":
        return "alpinelinux.svg"

    @property
    def title(self) -> "str":
        return "Alpine Linux"

    @property
    def primary_color(self) -> "str":
        return "#0D597F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Alpine Linux</title>
     <path d="M5.998 1.607L0 12l5.998 10.393h12.004L24 12 18.002
 1.607H5.998zM9.965 7.12L12.66 9.9l1.598 1.595.002-.002 2.41
 2.363c-.2.14-.386.252-.563.344a3.756 3.756 0 01-.496.217 2.702 2.702
 0 01-.425.111c-.131.023-.25.034-.358.034-.13
 0-.242-.014-.338-.034a1.317 1.317 0 01-.24-.072.95.95 0
 01-.2-.113l-1.062-1.092-3.039-3.041-1.1 1.053-3.07 3.072a.974.974 0
 01-.2.111 1.274 1.274 0 01-.237.073c-.096.02-.209.033-.338.033-.108
 0-.227-.009-.358-.031a2.7 2.7 0 01-.425-.114 3.748 3.748 0
 01-.496-.217 5.228 5.228 0 01-.563-.343l6.803-6.727zm4.72.785l4.579
 4.598 1.382 1.353a5.24 5.24 0 01-.564.344 3.73 3.73 0 01-.494.217
 2.697 2.697 0 01-.426.111c-.13.023-.251.034-.36.034-.129
 0-.241-.014-.337-.034a1.285 1.285 0
 01-.385-.146c-.033-.02-.05-.036-.053-.04l-1.232-1.218-2.111-2.111-.334.334L12.79
 9.8l1.896-1.897zm-5.966 4.12v2.529a2.128 2.128 0 01-.356-.035 2.765
 2.765 0 01-.422-.116 3.708 3.708 0 01-.488-.214 5.217 5.217 0
 01-.555-.34l1.82-1.825Z" />
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
