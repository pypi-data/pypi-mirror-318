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


class FloatplaneIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "floatplane"

    @property
    def original_file_name(self) -> "str":
        return "floatplane.svg"

    @property
    def title(self) -> "str":
        return "Floatplane"

    @property
    def primary_color(self) -> "str":
        return "#00AEEF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Floatplane</title>
     <path
 d="M17.948,20.162c-1.81,1.527-4.078,2.366-6.466,2.366c-2.682,0-5.19-1.047-7.088-2.933c-1.897-1.897-2.933-4.416-2.933-7.088
 c0-2.399,0.84-4.667,2.366-6.466L2.911,4.874C1.101,6.902,0,9.585,0,12.518C0,18.864,5.136,24,11.482,24
 c2.933,0,5.616-1.101,7.644-2.911L17.948,20.162z
 M8.331,2.988c1.003-0.327,2.061-0.502,3.151-0.502c2.682,0,5.19,1.047,7.088,2.933
 c1.897,1.897,2.933,4.416,2.933,7.088c0,1.09-0.174,2.148-0.502,3.151l1.134,1.134c0.534-1.319,0.829-2.77,0.829-4.285
 c0-6.346-5.136-11.482-11.482-11.482c-1.516,0-2.966,0.294-4.285,0.829L8.331,2.988z
 M9.683,6.444L3.446,0l-0.97,1.516
 C2.388,1.657,2.399,1.843,2.508,1.974L7.916,8.92L9.683,6.444z
 M7.655,14.96l-2.508-1.886l-0.458,0.774
 c-0.055,0.087-0.044,0.196,0.033,0.273l2.115,2.29L7.655,14.96z
 M12.158,9.007l-0.578-0.6l0.153-0.611
 c0.065-0.273,0.087-0.491,0.065-0.622c-0.087-0.393-0.273-0.687-0.273-0.687l-5.474,5.866c0,0,0.371,0.36,0.905-0.055
 c0.24-0.185,1.189-0.96,2.203-1.799l0.927,1.189L12.158,9.007z
 M17.501,14.263l0.153-0.611c0.055-0.207,0.087-0.382,0.065-0.502
 c-0.065-0.393-0.218-0.687-0.218-0.687l-5.866,5.474c0,0,0.36,0.371,0.916,0c0.273-0.185,1.428-0.992,2.584-1.821l6.891,5.365
 c0.131,0.109,0.316,0.12,0.458,0.033L24,20.543L17.501,14.263z
 M9.061,16.389c0.883-0.676,2.115-1.625,3.217-2.475l1.243,0.97
 l2.039-2.475l-0.676-0.654l0.218-0.774c0.109-0.393,0.153-0.698,0.12-0.883c-0.109-0.567-0.36-0.981-0.36-0.981l-8.069,8.069
 c0,0,0.251,0.207,0.774,0l2.279,2.104c0.076,0.065,0.185,0.076,0.273,0.033l0.774-0.458L9.061,16.389z"
 />
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
