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


class ApacheOpenofficeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "apacheopenoffice"

    @property
    def original_file_name(self) -> "str":
        return "apacheopenoffice.svg"

    @property
    def title(self) -> "str":
        return "Apache OpenOffice"

    @property
    def primary_color(self) -> "str":
        return "#0E85CD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apache OpenOffice</title>
     <path d="M12 0C5.372 0 0 5.371 0 12c0 .843.088 1.667.254
 2.462a12.594 12.594 0 013.309-.44c1.836 0 3.579.392 5.152
 1.099a12.536 12.536 0 017.303-2.332c1.704 0 3.33.339
 4.811.953l.023.01a.186.186 0 01-.083.353l-.267-.02a12.525 12.525 0
 00-.895-.032c-4.208 0-7.988 1.546-10.281 4.681l-.11.151a.183.183 0
 01-.28.008C6.76 16.847 3.894 16.037.677 15.981 2.32 20.65 6.768 24
 11.998 24 18.628 24 24 18.627 24 12c0-6.628-5.373-12-12.001-12zm9.395
 7.181c-.042-.004-.114-.016-.16-.022a6.703 6.703 0
 00-.405-.051c-2.447-.23-4.725.449-6.21
 2.171-.063.064-.118.067-.179.003-1.181-1.34-2.864-1.935-4.795-2.118a7.24
 7.24 0 00-2.01.09l-.01.001-.02.002a.125.125 0
 01-.075-.223l.035-.02a7.23 7.23 0 014.05-.795c1.054.1 2.035.42
 2.9.91a7.279 7.279 0 016.797-.255c.045.025.093.047.14.073a.116.116 0
 01.067.11c0 .069-.044.134-.125.124z" />
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
