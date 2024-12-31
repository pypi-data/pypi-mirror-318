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


class CommitlintIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "commitlint"

    @property
    def original_file_name(self) -> "str":
        return "commitlint.svg"

    @property
    def title(self) -> "str":
        return "commitlint"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>commitlint</title>
     <path d="M7.988 4.822v.901h1.845v6.337c0 .809.187 1.433.563
 1.875.379.438.913.657 1.6.657h1.458v-.97H12.11c-.37
 0-.652-.13-.844-.393-.187-.263-.281-.652-.281-1.17V4.823ZM3.459
 7.418c-1.084 0-1.933.325-2.546.976C.304 9.044 0 9.944 0 11.096c0
 1.15.304 2.051.913 2.702.613.65 1.462.976 2.546.976a3.67 3.67 0 0 0
 1-.137c.33-.088.65-.221.958-.4V13.04c-.271.259-.565.45-.882.576a3 3 0
 0 1-1.076.18c-.717
 0-1.272-.232-1.664-.7-.387-.47-.582-1.138-.582-2.001
 0-.868.195-1.535.582-2.002.388-.467.943-.7 1.664-.7.388 0 .734.06
 1.038.181a3.1 3.1 0 0 1 .92.588V7.956a4.255 4.255 0 0 0-.97-.406 3.74
 3.74 0 0 0-.988-.132Zm12.855 6.123v1.128H24V13.54zm3.156 2.255-2.302
 3.382h1.3l1.694-2.204 1.684 2.204h1.3l-2.301-3.382z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/conventional-changelog/com
mitlint/blob/0b177635472214faac5a5800ced970bf4d2e6012/docs/assets/icon'''

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
