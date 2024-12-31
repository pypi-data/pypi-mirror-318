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


class RubyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ruby"

    @property
    def original_file_name(self) -> "str":
        return "ruby.svg"

    @property
    def title(self) -> "str":
        return "Ruby"

    @property
    def primary_color(self) -> "str":
        return "#CC342D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ruby</title>
     <path d="M20.156.083c3.033.525 3.893 2.598 3.829 4.77L24 4.822
 22.635 22.71 4.89 23.926h.016C3.433 23.864.15 23.729 0 19.139l1.645-3
 2.819 6.586.503 1.172 2.805-9.144-.03.007.016-.03 9.255
 2.956-1.396-5.431-.99-3.9 8.82-.569-.615-.51L16.5 2.114
 20.159.073l-.003.01zM0 19.089zM5.13 5.073c3.561-3.533 8.157-5.621
 9.922-3.84 1.762 1.777-.105 6.105-3.673 9.636-3.563 3.532-8.103
 5.734-9.864 3.957-1.766-1.777.045-6.217 3.612-9.75l.003-.003z" />
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
