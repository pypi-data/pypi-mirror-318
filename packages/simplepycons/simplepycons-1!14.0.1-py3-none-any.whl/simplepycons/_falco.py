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


class FalcoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "falco"

    @property
    def original_file_name(self) -> "str":
        return "falco.svg"

    @property
    def title(self) -> "str":
        return "Falco"

    @property
    def primary_color(self) -> "str":
        return "#00AEC7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Falco</title>
     <path d="M2.812
 0c-.23.012-.416.112-.503.329-.155.382.043.66.298.916l10.186
 10.17c.16.16.336.31.523.37l.742-.742c-.06-.187-.212-.363-.373-.523C10.291
 7.129 6.897 3.739 3.5.35 3.31.16 3.107-.01 2.812 0Zm.95
 4.485a.543.543 0 0
 0-.434.178c-.265.262-.246.573-.037.867.094.128.198.248.312.36 2.439
 2.436 4.88 4.87 7.323
 7.302.165.164.363.333.578.404l.738-.738c-.094-.268-.316-.447-.51-.641a4831.46
 4831.315 0 0 0-6.246-6.24c-.431-.43-.861-.865-1.306-1.281a.711.711 0
 0 0-.418-.211ZM19.33 8.262a.301.301 0 0 0-.213.078c-1.708 1.699-3.417
 3.395-5.127 5.092l-8.027 8.014-.02-.02a56.5 56.498 0 0 0-1.36
 1.401c-.233.25-.32.57-.05.86.282.303.623.284.934.054.233-.172.434-.388.64-.594l.543-.54
 1.506-1.503c3.656-3.647 7.307-7.298
 10.953-10.955l2.637-.46c-.377-.38-1.794-1.44-2.416-1.427Zm-14.78.803a.582.582
 0 0
 0-.345.193c-.208.228-.206.492-.045.733.15.217.32.42.508.605a773.152
 773.129 0 0 0 3.486 3.484c.394.393.787.787 1.195
 1.164.09.087.2.15.32.184l.774-.774c-.05-.198-.184-.356-.332-.503a3008.15
 3008.06 0 0 0-4.724-4.715 1.443 1.443 0 0 0-.452-.315.725.725 0 0
 0-.384-.056Zm15.137 2.56c-.27.018-.485.208-.687.41l-9.86
 9.844-.726.724c-.174.175-.352.367-.408.575-.045.164-.013.34.156.521.423.455.82.13
 1.154-.205 3.568-3.559 7.134-7.117
 10.7-10.68.169-.168.339-.34.357-.6a.562.562 0 0 0-.395-.542.71.71 0 0
 0-.29-.046zm.057 3.58c-.226.012-.438.178-.625.364-1.357 1.346-2.706
 2.702-4.063 4.05-.474.47-.452.91.018 1.37.796.782 1.59 1.565 2.363
 2.37.433.45.907.732 1.518.613.14.01.249.03.353.02.446-.042 1.01-.012
 1.024-.626.014-.633-.535-.636-.995-.619-.466.017-.809-.174-1.119-.5-.476-.5-.952-1.004-1.466-1.463-.456-.406-.391-.703.023-1.1
 1.091-1.05 2.152-2.132
 3.217-3.207.314-.318.593-.697.17-1.096-.143-.134-.283-.183-.418-.176z"
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
