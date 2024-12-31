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


class ApostropheIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "apostrophe"

    @property
    def original_file_name(self) -> "str":
        return "apostrophe.svg"

    @property
    def title(self) -> "str":
        return "Apostrophe"

    @property
    def primary_color(self) -> "str":
        return "#6236FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apostrophe</title>
     <path d="M15.674
 0c-.795.001-1.794.095-3.167.313l-4.6.729c-3.138.497-4.224 1.003-5.274
 1.798a6.485 6.485 0 00-2.24 3.082c-.43 1.245-.577 2.434-.08
 5.571l.729 4.6c.497 3.138 1.003 4.22 1.798 5.273a6.485 6.485 0
 003.082 2.24c1.245.431 2.434.578 5.571.081l4.6-.729c3.138-.497
 4.22-1.003 5.273-1.799a6.477 6.477 0
 002.24-3.081c.431-1.245.578-2.434.082-5.571l-.73-4.6c-.497-3.138-1.003-4.224-1.799-5.274a6.477
 6.477 0 00-3.081-2.24C17.378.152 16.695 0 15.674 0zm-5.319
 4.566a.52.52 0 01.003 0 .52.52 0 01.52.444l.77 4.865a.52.52 0
 01-.435.6l-4.859.77a.52.52 0 01-.602-.436l-.77-4.866a.52.52 0
 01.435-.6l4.86-.77a.52.52 0 01.078-.007zM9.92 5.692l-3.823.605.612
 3.83 3.813-.605zm6.504 2.91a3.274 3.274 0 01.497 6.513 3.258 3.258 0
 01-3.713-2.726 3.274 3.274 0 013.216-3.787zm-.054 1.058a2.226 2.226 0
 10.388 4.42 2.208 2.208 0 001.818-2.541 2.226 2.226 0
 00-2.206-1.879zm-6.45 3a.52.52 0 01.424.208l3.824 4.964a.52.52 0
 01-.333.839l-5.932.937a.52.52 0 01-.576-.695l2.108-5.901a.52.52 0
 01.486-.352zm.18 1.611L8.61 18.438l4.186-.664z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/apostrophecms/apostrophe/b'''

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
