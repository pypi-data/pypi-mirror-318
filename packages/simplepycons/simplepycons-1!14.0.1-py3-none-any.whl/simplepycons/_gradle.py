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


class GradleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gradle"

    @property
    def original_file_name(self) -> "str":
        return "gradle.svg"

    @property
    def title(self) -> "str":
        return "Gradle"

    @property
    def primary_color(self) -> "str":
        return "#02303A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gradle</title>
     <path d="M22.695 4.297a3.807 3.807 0 0 0-5.29-.09.368.368 0 0 0 0
 .533l.46.47a.363.363 0 0 0 .474.032 2.182 2.182 0 0 1 2.86
 3.291c-3.023 3.02-7.056-5.447-16.211-1.083a1.24 1.24 0 0 0-.534
 1.745l1.571 2.713a1.238 1.238 0 0 0
 1.681.461l.037-.02-.029.02.688-.384a16.083 16.083 0 0 0
 2.193-1.635.384.384 0 0 1 .499-.016.357.357 0 0 1 .016.534 16.435
 16.435 0 0 1-2.316 1.741H8.77l-.696.39a1.958 1.958 0 0 1-.963.25
 1.987 1.987 0 0 1-1.726-.989L3.9 9.696C1.06 11.72-.686 15.603.26
 20.522a.363.363 0 0 0 .354.296h1.675a.363.363 0 0 0 .37-.331 2.478
 2.478 0 0 1 4.915 0 .36.36 0 0 0 .357.317h1.638a.363.363 0 0 0
 .357-.317 2.478 2.478 0 0 1 4.914 0 .363.363 0 0 0
 .358.317h1.627a.363.363 0 0 0 .363-.357c.037-2.294.656-4.93 2.42-6.25
 6.108-4.57 4.502-8.486 3.088-9.9zm-6.229 6.901l-1.165-.584a.73.73 0 1
 1 1.165.587z" />
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
