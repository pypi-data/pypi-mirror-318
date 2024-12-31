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


class RedditIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "reddit"

    @property
    def original_file_name(self) -> "str":
        return "reddit.svg"

    @property
    def title(self) -> "str":
        return "Reddit"

    @property
    def primary_color(self) -> "str":
        return "#FF4500"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Reddit</title>
     <path d="M12 0C5.373 0 0 5.373 0 12c0 3.314 1.343 6.314 3.515
 8.485l-2.286 2.286C.775 23.225 1.097 24 1.738 24H12c6.627 0 12-5.373
 12-12S18.627 0 12 0Zm4.388 3.199c1.104 0 1.999.895 1.999 1.999 0
 1.105-.895 2-1.999 2-.946
 0-1.739-.657-1.947-1.539v.002c-1.147.162-2.032 1.15-2.032
 2.341v.007c1.776.067 3.4.567 4.686 1.363.473-.363 1.064-.58 1.707-.58
 1.547 0 2.802 1.254 2.802 2.802 0 1.117-.655 2.081-1.601 2.531-.088
 3.256-3.637 5.876-7.997 5.876-4.361
 0-7.905-2.617-7.998-5.87-.954-.447-1.614-1.415-1.614-2.538 0-1.548
 1.255-2.802 2.803-2.802.645 0 1.239.218 1.712.585 1.275-.79
 2.881-1.291 4.64-1.365v-.01c0-1.663 1.263-3.034
 2.88-3.207.188-.911.993-1.595 1.959-1.595Zm-8.085 8.376c-.784
 0-1.459.78-1.506 1.797-.047 1.016.64 1.429 1.426 1.429.786 0
 1.371-.369 1.418-1.385.047-1.017-.553-1.841-1.338-1.841Zm7.406
 0c-.786 0-1.385.824-1.338 1.841.047 1.017.634 1.385 1.418 1.385.785 0
 1.473-.413 1.426-1.429-.046-1.017-.721-1.797-1.506-1.797Zm-3.703
 4.013c-.974 0-1.907.048-2.77.135-.147.015-.241.168-.183.305.483 1.154
 1.622 1.964 2.953 1.964 1.33 0 2.47-.81
 2.953-1.964.057-.137-.037-.29-.184-.305-.863-.087-1.795-.135-2.769-.135Z"
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
