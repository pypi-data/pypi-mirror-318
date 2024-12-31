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


class ShowtimeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "showtime"

    @property
    def original_file_name(self) -> "str":
        return "showtime.svg"

    @property
    def title(self) -> "str":
        return "Showtime"

    @property
    def primary_color(self) -> "str":
        return "#B10000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Showtime</title>
     <path d="M16.99 12.167c0-4.808 1.779-7.84 3.903-8.16C18.769 1.397
 15.221 0 11.999 0 8.451 0 5.265 1.54 3.07 3.985c2.094.416 2.806 2.174
 2.806 4.892H3.314c0-1.605-.334-2.436-1.284-2.436-.427
 0-.758.217-.954.587-.027.06-.057.122-.084.184a2.115 2.115 0 0
 0-.114.71c0 3.324 5.46 3.159 5.46 8.27 0 1.995-1.53 3.855-3.252
 3.855C5.35 22.52 8.441 24 12 24c3.46 0 6.577-1.464
 8.766-3.808-2.018-.509-3.776-3.413-3.776-8.025zm-1.142
 7.921h-2.746V13.26h-2.967v6.83H7.384V4.327h2.746v6.348h2.972V4.327h2.746v15.761zM2.372
 17.58c-1.32 0-2.399-2.32-2.372-5.8 1.905 1.72 3.681 2.11 3.681 4.145
 0 .981-.543 1.655-1.309 1.655zM24 12.002c0 2.844-.896 5.409-2.1
 5.409-1.445 0-2.181-2.703-2.181-5.498 0-2.654.771-5.308 2.181-5.308
 1.676 0 2.1 4.102 2.1 5.397z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Showt'''

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
