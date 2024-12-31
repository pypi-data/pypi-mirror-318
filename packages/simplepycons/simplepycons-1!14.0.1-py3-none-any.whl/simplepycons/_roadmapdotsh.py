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


class RoadmapdotshIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "roadmapdotsh"

    @property
    def original_file_name(self) -> "str":
        return "roadmapdotsh.svg"

    @property
    def title(self) -> "str":
        return "roadmap.sh"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>roadmap.sh</title>
     <path d="M20.693 0H3.307A3.307 3.307 0 0 0 0 3.307v17.386A3.307
 3.307 0 0 0 3.307 24h17.386A3.307 3.307 0 0 0 24 20.693V3.307A3.307
 3.307 0 0 0 20.693 0zm-7.706
 9.18c-.349.031-.689.078-1.021.142-.333.063-.65.134-.95.214a3.64 3.64
 0 0 0-.736.237v8.097a5.522 5.522 0 0
 1-.76.143c-.333.047-.68.07-1.045.07a5.87 5.87 0 0 1-.95-.07 1.588
 1.588 0 0 1-.688-.285 1.476 1.476 0 0
 1-.452-.57c-.095-.253-.142-.578-.142-.974V9.061c0-.364.063-.673.19-.926.142-.27.34-.507.594-.713a3.93
 3.93 0 0 1 .926-.546 9.133 9.133 0 0 1 2.54-.736 8.093 8.093 0 0 1
 1.378-.119c.76 0 1.361.15 1.804.451.444.285.665.76.665 1.425 0
 .222-.032.443-.095.665a3.075 3.075 0 0 1-.237.57c-.341
 0-.682.016-1.021.047zm5.113
 8.453c-.412.443-.974.665-1.686.665s-1.274-.222-1.686-.665c-.412-.443-.617-.998-.617-1.662
 0-.665.205-1.22.617-1.663.412-.443.974-.664 1.686-.664s1.274.221
 1.686.664c.411.444.617.998.617 1.663 0 .664-.206 1.219-.617 1.662z"
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
