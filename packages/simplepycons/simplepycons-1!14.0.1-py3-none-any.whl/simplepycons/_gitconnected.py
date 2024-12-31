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


class GitconnectedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gitconnected"

    @property
    def original_file_name(self) -> "str":
        return "gitconnected.svg"

    @property
    def title(self) -> "str":
        return "Gitconnected"

    @property
    def primary_color(self) -> "str":
        return "#2E69AE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gitconnected</title>
     <path d="M6.734 5.42C2.865 5.42 0 8.405 0 12.035c0 3.607 2.842
 6.545 6.688 6.545 3.859 0 6.708-2.936 6.755-6.58l.002-.08c.03-2.19
 1.504-3.967 3.797-3.967 2.268 0 3.87 1.838 3.87 4.082 0 2.222-1.483
 4.037-3.823 4.037-1.334 0-2.43-.657-3.107-1.656a7.557 7.557 0 0
 1-1.41 2.53c1.163 1.013 2.71 1.634 4.47 1.634 3.893 0 6.758-2.986
 6.758-6.592 0-3.63-2.841-6.568-6.71-6.568-3.828 0-6.672 2.922-6.733
 6.5-.015.04 0 .101 0 .115 0 2.222-1.482 4.037-3.823 4.037-2.244
 0-3.845-1.84-3.845-4.084 0-2.221 1.482-4.035 3.799-4.035 1.232 0
 2.254.554 2.943 1.41l1.385-2.449A6.75 6.75 0 0 0 6.734 5.42Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://gitconnected.com/richard-hendricks-de'''

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
