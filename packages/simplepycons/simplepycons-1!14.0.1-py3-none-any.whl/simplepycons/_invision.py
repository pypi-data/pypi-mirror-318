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


class InvisionIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "invision"

    @property
    def original_file_name(self) -> "str":
        return "invision.svg"

    @property
    def title(self) -> "str":
        return "InVision"

    @property
    def primary_color(self) -> "str":
        return "#FF3366"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>InVision</title>
     <path d="M5.265 15.108a4.715 4.715 0 0 0-.124 1.036c0 1.215.658
 2.021 2.058 2.021 1.16 0 2.102-.69 2.78-1.803l-.415
 1.661h2.304l1.319-5.28c.329-1.338.966-2.032 1.934-2.032.761 0
 1.235.473 1.235 1.255a2.46 2.46 0 0 1-.103.742l-.679 2.427a3.63 3.63
 0 0 0-.144 1.03c0 1.151.679 1.996 2.099 1.996 1.214 0 2.182-.781
 2.716-2.654l-.905-.35c-.453 1.255-.844 1.482-1.152 1.482-.308
 0-.474-.206-.474-.618a2.737 2.737 0 0 1 .103-.638l.66-2.366a5.23 5.23
 0 0 0 .226-1.5c0-1.771-1.07-2.695-2.368-2.695-1.214 0-2.449
 1.096-3.066 2.249L13.721 9h-3.518l-.495 1.824h1.648l-1.014
 4.055c-.797 1.77-2.26 1.799-2.443
 1.758-.302-.068-.494-.183-.494-.576a3.847 3.847 0 0 1
 .144-.942l1.544-6.124H5.184l-.493 1.824h1.625zm2.902-7.385a1.38 1.38
 0 1 0-1.4-1.38 1.384 1.384 0 0 0 1.4 1.38zM0 0h24v24H0Z" />
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
