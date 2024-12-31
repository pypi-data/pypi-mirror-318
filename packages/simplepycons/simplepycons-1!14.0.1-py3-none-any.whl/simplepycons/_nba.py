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


class NbaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nba"

    @property
    def original_file_name(self) -> "str":
        return "nba.svg"

    @property
    def title(self) -> "str":
        return "NBA"

    @property
    def primary_color(self) -> "str":
        return "#253B73"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NBA</title>
     <path d="M9.19 0a2.486 2.486 0 0 0-2.485 2.484v19.029A2.488 2.488
 0 0 0 9.19 24h5.615a2.493 2.493 0 0 0 2.49-2.487V2.484A2.488 2.488 0
 0 0 14.81 0zm0 .584h3.21c-.62.237-.707.508-.73
 1.366-.105.01-.325-.087-.25.434 0 0
 .043.346.18.286-.133.918.023.99-.93
 1.031l-.047.067c-.95.093-1.25-.027-2.05 1.603 0
 0-.207.505-.268.714-.197.415-.674 1.328-.819
 1.919-.046.2-.14.264-.01.553.185.417-.124.527.95.496V9.3s-.286.247-.346.398c-.061.147-.226.89-.22
 1.237.019.917.767 1.683.992 2.597l.492.07c.282.634 1.495 2.355 1.743
 2.582.057.159.365.355.545.551.149.141 1.025 1.1 2.054
 1.692-.007-.001.164.344.249.618-.342.275.32.777.52
 1.609.012.107-.19.222.114.495-.022 1.256-.402 1.918.241
 2.266H9.191a1.9 1.9 0 0 1-1.9-1.901V2.486a1.9 1.9 0 0 1
 1.9-1.902zm3.804.002h1.815a1.9 1.9 0 0 1 1.897 1.898v9.193a1.653
 1.653 0 0
 0-.22-.397c0-.255-.272-.249-.346-.344-.07-.081.067-.128-.407-.235-.09-.05-.158-.747-.158-.747-.07-.447-.229-.754-.467-1.227-.12-.243-.177-1.001-.305-1.386.071-1.767-.493-2.28-.95-2.569-.174-.11-.262-.191-.433-.29l-.005-.082c-.133-.126-.402-.264-.623-.362-.068-.07-.037-.22.01-.276.15-.02.348-.356.513-.703.129.009.174-.118.214-.19.138-.222.288-.413.096-.542.435-.777.154-1.301-.08-1.321-.095-.195-.26-.316-.551-.42zm.551
 6.338c.06.319.34 1.929.456 2.187.123.259.535 1.05.73 1.54a1.69 1.69 0
 0 0-1.294 1.646 1.692 1.692 0 0 0 1.693 1.691 1.692 1.692 0 0 0
 1.576-1.066v8.59a1.887 1.887 0 0 1-1.598
 1.877h-.017c.833-.502.319-1.46.16-2.022-.012-.033.014-.074.026-.1.045-.08-.045-.257-.045-.257-.098-.09-.127-.561-.182-.772-.089-.358.157-.971.157-1.18
 0-.206-.156-.491-.445-.858-.069-.078-.276-1.86-.462-2.313-.258-.623-.339-.526-.64-1.266-.24-.525-.055-1.295-.59-3.085.005.006.12-.113.12-.113s-.422-1.55-.561-1.975c-.14-.426-.385-.456-.385-.456s.002-.172.012-.216c.02-.07.516-1.367.558-1.407.001-.03.717-.514.731-.445Z"
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
