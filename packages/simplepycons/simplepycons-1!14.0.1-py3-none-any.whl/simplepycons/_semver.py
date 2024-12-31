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


class SemverIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "semver"

    @property
    def original_file_name(self) -> "str":
        return "semver.svg"

    @property
    def title(self) -> "str":
        return "SemVer"

    @property
    def primary_color(self) -> "str":
        return "#3F4551"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SemVer</title>
     <path d="M.357 9.024A12.07 12.07 0 002.97 19.867a12.051 12.051 0
 0010.38 4.063c7.768-.703 13.086-9.799
 9.517-16.8-.416-1.19-2.07-.368-1.903.596.287.7.526 1.421.713
 2.155a9.983 9.983 0 01-3.926 10.25 9.965 9.965 0
 01-14.807-3.809A9.984 9.984 0 014.44 5.448a9.968 9.968 0 014.85-3.044
 9.868 9.868 0 017.02.631.333.333 0 01.155.429l-3.962
 10.62c-.107.81-.69.786-.797 0l-2.38-7.37a1.572 1.572 0
 00-.773-.988c-1.19-.56-3.093.667-2.379 2.155l3.914 10.441c.524 1.393
 1.023 1.834 2.058 1.834s1.535-.44 2.058-1.834L20 3.94a1.036 1.036 0
 00-.369-1.19C13.1-2.907 2.32.641.357 9.023z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/semver/semver.org/blob/b69'''

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
