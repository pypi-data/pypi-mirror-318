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


class SpacyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "spacy"

    @property
    def original_file_name(self) -> "str":
        return "spacy.svg"

    @property
    def title(self) -> "str":
        return "spaCy"

    @property
    def primary_color(self) -> "str":
        return "#09A3D5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>spaCy</title>
     <path d="M3.001 11.213c-.55-.065-.591-.803-1.297-.738-.342
 0-.66.143-.66.457 0 .473.73.517 1.17.636.75.228 1.476.383 1.476 1.199
 0 1.035-.811 1.394-1.884 1.394-.897 0-1.806-.318-1.806-1.142
 0-.228.22-.407.432-.407.269 0 .363.114.457.301.208.367.44.563
 1.019.563.367 0 .742-.139.742-.457 0-.452-.46-.55-.937-.66C.869
 12.122.143 12 .057 11.062c-.09-1.598 3.242-1.659
 3.433-.257-.004.253-.24.408-.489.408ZM6.964 9.81c1.171 0 1.835.979
 1.835 2.186 0 1.211-.644 2.185-1.835 2.185-.66
 0-1.072-.281-1.37-.713v1.598c0 .481-.155.714-.505.714-.428
 0-.506-.273-.506-.714v-4.648c0-.379.159-.612.506-.612.326 0
 .505.257.505.612v.13c.331-.416.71-.738 1.37-.738Zm-.277 3.54c.685 0
 .991-.632.991-1.37 0-.722-.31-1.37-.991-1.37-.714 0-1.044.587-1.044
 1.37 0 .762.335 1.37 1.044 1.37Zm2.907-2.398c0-.84.967-1.142
 1.904-1.142 1.317 0 1.86.384 1.86 1.656v1.223c0 .29.179.869.179 1.044
 0 .265-.244.432-.505.432-.29
 0-.506-.342-.661-.587-.428.342-.881.587-1.574.587-.766
 0-1.37-.453-1.37-1.199 0-.66.473-1.039 1.044-1.17 0 .004 1.835-.432
 1.835-.436 0-.563-.2-.812-.791-.812-.522
 0-.787.143-.991.457-.163.237-.143.379-.457.379-.253-.004-.473-.175-.473-.432Zm1.566
 2.524c.803 0 1.142-.424
 1.142-1.268v-.18c-.216.074-1.089.29-1.325.327-.253.049-.506.236-.506.534.008.326.342.587.689.587Zm5.9-5.26c1.134
 0 2.361.677 2.361 1.753a.49.49 0 0 1-.481.506c-.371
 0-.424-.2-.587-.481-.273-.502-.596-.836-1.297-.836-1.085-.008-1.57.921-1.57
 2.079 0 1.167.404 2.007 1.525 2.007.746 0 1.158-.433
 1.37-.991.086-.257.241-.506.563-.506.253 0 .506.257.506.534 0
 1.142-1.167 1.933-2.365 1.933-1.313 0-2.055-.555-2.463-1.476a3.48
 3.48 0 0 1-.326-1.525c-.009-1.77 1.023-2.997 2.764-2.997Zm6.483
 1.594c.29 0 .457.188.457.481 0 .119-.094.355-.13.482l-1.395
 3.665c-.31.795-.542 1.346-1.598 1.346-.502 0-.938-.045-.938-.481
 0-.253.191-.38.457-.38.048 0 .13.025.179.025.077 0 .13.024.179.024.53
 0 .604-.542.791-.917L20.2 10.724c-.078-.18-.131-.302-.131-.408
 0-.294.229-.506.534-.506.343 0 .478.269.563.563l.889
 2.642.889-2.442c.134-.379.147-.763.599-.763Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/explosion/spaCy/blob/c1798'''

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
