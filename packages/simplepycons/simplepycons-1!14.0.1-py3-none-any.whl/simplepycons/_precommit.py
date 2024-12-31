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


class PrecommitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "precommit"

    @property
    def original_file_name(self) -> "str":
        return "precommit.svg"

    @property
    def title(self) -> "str":
        return "pre-commit"

    @property
    def primary_color(self) -> "str":
        return "#FAB040"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>pre-commit</title>
     <path d="M12 0c-.563 0-1.127.215-1.557.645L.645
 10.443c-.86.86-.86 2.254 0 3.114l9.798 9.798c.86.86 2.254.86 3.114
 0l9.798-9.798c.86-.86.86-2.254 0-3.114L13.557.645A2.195 2.195 0 0012
 0zm0 1.74c.493 0 .987.186 1.361.56L21.7 10.64c.75.75.75 1.973 0
 2.722L13.361 21.7c-.374.375-.868.56-1.361.56s-.987-.185-1.361-.56L2.3
 13.361a1.93 1.93 0 010-2.722L10.639 2.3c.374-.375.868-.56
 1.361-.56zm0 .62c-.333 0-.664.127-.92.382L2.742 11.08a1.295 1.295 0
 000 1.84l8.338 8.338a1.296 1.296 0 001.84 0l8.338-8.338a1.295 1.295 0
 000-1.84L12.92 2.742A1.296 1.296 0 0012 2.36zM9.207 7.624h3.959c.55 0
 1.015.079 1.4.238.385.16.7.371.942.633.241.262.417.561.527.897a3.34
 3.34 0 010 2.084c-.11.34-.286.64-.527.902a2.628 2.628 0
 01-.942.633c-.385.16-.85.238-1.4.238h-2.043v3.156H9.207zm1.916
 1.484v2.657h1.514c.222 0
 .434-.016.64-.05.207-.032.39-.097.547-.193.158-.095.284-.23.38-.404.094-.174.142-.401.142-.682
 0-.28-.048-.507-.143-.681a1.053 1.053 0 00-.379-.404 1.513 1.513 0
 00-.547-.194 4.056 4.056 0 00-.64-.049z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/pre-commit/pre-commit.com/'''

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
