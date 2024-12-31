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


class AntaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "anta"

    @property
    def original_file_name(self) -> "str":
        return "anta.svg"

    @property
    def title(self) -> "str":
        return "Anta"

    @property
    def primary_color(self) -> "str":
        return "#D70010"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Anta</title>
     <path d="M24 15.2372a20.744 20.744 0 0 0-9.86-7.5087 31.2657
 31.2657 0 0 1 6.9097 1.0135l-1.5536-1.3192A29.1614 29.1614 0 0 0
 9.0497 5.509a29.0797 29.0797 0 0 0-6.4051.7036L0 8.032c.335 0
 .8376-.021 1.1747-.021a25.1537 25.1537 0 0 1 20.4571 10.48ZM9.1963
 12.9758h3.3334l-.3329 1.183h-1.0532L9.9333
 18.491H8.7692l1.206-4.3322H8.8655zm-3.771 0H6.468l.4376
 2.9544.8229-2.9544h1.1977l-1.537 5.5152H6.221l-.4041-2.743-.7643
 2.743H3.8841ZM0 18.491l2.8225-5.5131h1.181L3.769
 18.491H2.5838l.0545-.7391H1.5264l-.3601.7391zm2.0206-1.8844h.6889l.2094-1.9474zm8.2122
 1.8844 2.8288-5.5131h1.1768l-.2346
 5.5131h-1.181l.0524-.7391h-1.1076l-.3644.7391zm2.0247-1.8844h.689l.2093-1.9474z"
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
