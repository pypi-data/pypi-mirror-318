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


class DblpIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dblp"

    @property
    def original_file_name(self) -> "str":
        return "dblp.svg"

    @property
    def title(self) -> "str":
        return "dblp"

    @property
    def primary_color(self) -> "str":
        return "#004F9F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>dblp</title>
     <path d="M3.075.002c-.096.013-.154.092-.094.31L4.97 7.73 3.1
 8.6s-.56.26-.4.85l2.45 9.159s.16.59.72.33l6.169-2.869
 1.3-.61s.52-.24.42-.79l-.01-.06-1.13-4.22-.658-2.45-.672-2.49v-.04s-.16-.59-.84-1L3.5.141s-.265-.16-.425-.139zM18.324
 5.03a.724.724 0 0 0-.193.06l-5.602 2.6.862 3.2 1.09
 4.08.01.06c.05.47-.411.79-.411.79l-1.88.87.5
 1.89.04.1c.07.17.28.6.81.91l6.95 4.269s.68.41.52-.17l-1.981-7.4
 1.861-.86s.56-.26.4-.85L18.85 5.42s-.116-.452-.526-.39z" />
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
