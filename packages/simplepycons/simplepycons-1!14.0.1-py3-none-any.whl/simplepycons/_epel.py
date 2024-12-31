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


class EpelIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "epel"

    @property
    def original_file_name(self) -> "str":
        return "epel.svg"

    @property
    def title(self) -> "str":
        return "EPEL"

    @property
    def primary_color(self) -> "str":
        return "#FC0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>EPEL</title>
     <path d="M.702 2.361c-1.188.11-.88.154 1.98.286 5.677.242 9.043
 1.144 11.353 2.993 1.232 1.012 2.187 3.146 2.187
 3.146s-3.639.836-7.797 1.65c-4.159.814-7.46 1.54-7.327 1.584.352.11
 5.214-.484 10.319-1.276l4.87-.734c.078-.012.036.394.036.514 0
 1.1-1.122 2.948-2.794 4.599-2.75 2.684-6.623 4.686-11.573
 5.962-1.364.352-2.2.638-1.892.638 1.188.044 5.742-1.298 7.81-2.266
 2.685-1.276 4.401-2.508 6.491-4.664 1.48-1.842 2.994-2.796
 3.056-5.017l3.06-.506c1.629-.264 3.103-.55
 3.28-.616.241-.088.285-.352.197-1.012-.154-1.21-1.1-2.156-3.014-3.037-2.904-1.342-5.88-1.603-7.442-.68-.173.101-.376.417-.534.486a1079.7
 1079.7 0 00-2.365-.862C7.567 2.515 3.848 2.075.702 2.361zm19.032
 2.773c1.628.484 4.18 2.014 3.792
 2.09l-3.066.601-3.386.772c-.644-1.435-1.491-2.232-2.628-3.305l.133-.327c.322-.796
 2.536-.602 5.155.169z" />
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
