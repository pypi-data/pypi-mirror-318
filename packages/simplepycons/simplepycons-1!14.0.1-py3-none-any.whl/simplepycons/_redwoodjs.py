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


class RedwoodjsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "redwoodjs"

    @property
    def original_file_name(self) -> "str":
        return "redwoodjs.svg"

    @property
    def title(self) -> "str":
        return "RedwoodJS"

    @property
    def primary_color(self) -> "str":
        return "#BF4722"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>RedwoodJS</title>
     <path d="M6.989 3.47l4.66 3.181c.105.07.228.108.354.111a.634.634
 0 0 0 .354-.111l4.664-3.192a.637.637 0 0
 0-.089-1.087L12.272.065a.64.64 0 0 0-.56 0L7.067 2.372a.636.636 0 0
 0-.078 1.098zm6.597 4.179c0 .211.104.408.276.528l3.736 2.553a.628.628
 0 0 0 .776-.05l3.134-2.803a.637.637 0 0
 0-.028-.973l-2.992-2.393a.635.635 0 0 0-.751-.029l-3.874
 2.65a.644.644 0 0 0-.277.517zm-9.291 3.474a.64.64 0 0 1
 .209.538.625.625 0 0 1-.315.485l-2.231 1.337a.63.63 0 0
 1-.718-.049.64.64 0 0 1-.21-.693l.825-2.596a.63.63 0 0 1
 1.023-.281l1.417 1.259zm12.1.271l-4.033-2.76a.634.634 0 0 0-.708
 0l-4.033 2.76a.646.646 0 0 0-.276.485.664.664 0 0 0 .212.521l4.03
 3.605a.635.635 0 0 0 .842 0l4.03-3.605a.647.647 0 0
 0-.064-1.006zm-10.758-.713l-3.13-2.803a.648.648 0 0
 1-.213-.503.626.626 0 0 1 .237-.481l2.992-2.407a.641.641 0 0 1
 .754-.029l3.87 2.65a.639.639 0 0 1 0 1.07l-3.732 2.553a.633.633 0 0
 1-.778-.05zm16.073 4.026l-3.187-1.908a.627.627 0 0 0-.744.071l-3.895
 3.477a.644.644 0 0 0-.204.587.636.636 0 0 0 .388.483l5.404
 2.19a.634.634 0 0 0 .815-.332l1.675-3.752a.64.64 0 0
 0-.252-.816zm.442-4.561l.825 2.596h-.007a.635.635 0 0
 1-.927.742l-2.234-1.337a.623.623 0 0 1-.305-.485.631.631 0 0 1
 .209-.538l1.416-1.262a.63.63 0 0 1 1.023.284zm-11.82 6.786a.637.637 0
 0 0-.202-.585L6.235 12.87a.627.627 0 0 0-.744-.071l-3.187
 1.908a.648.648 0 0 0-.255.813l1.678 3.752a.632.632 0 0 0
 .814.332l5.4-2.19a.637.637 0 0 0 .391-.482zm1.912 1.07l4.334
 1.755c.212.091.358.29.382.521a.635.635 0 0 1-.269.596l-4.338
 3.013A.625.625 0 0 1 12 24a.64.64 0 0
 1-.354-.114l-4.334-3.013a.635.635 0 0 1
 .124-1.117l4.334-1.755a.642.642 0 0 1 .474.001z" />
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
