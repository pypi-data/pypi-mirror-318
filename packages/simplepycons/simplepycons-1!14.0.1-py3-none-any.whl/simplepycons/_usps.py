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


class UspsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "usps"

    @property
    def original_file_name(self) -> "str":
        return "usps.svg"

    @property
    def title(self) -> "str":
        return "USPS"

    @property
    def primary_color(self) -> "str":
        return "#333366"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>USPS</title>
     <path d="M3.145 4.577L0 19.423h20.855L24 4.577H3.145zm-.157
 3.806h9.436c.157 0 5.064 0 5.159.975H9.09l1.321 4.026c1.51-.723
 5.222-2.233 7.455-2.328.944-.031 1.321.126
 1.132.252-.126.063-1.038.189-1.761.377-1.258.315-1.321.315-2.642.755-1.478.503-2.705
 1.069-4.53 1.919L.723 18.983l2.265-10.6zm16.483
 1.698c-.535-.094-2.768.063-3.334.063-.126 0-.472.031-.472-.063
 0-.063.126-.063.377-.094s1.006-.157
 1.258-.283c.063-.063.22-.157.315-.252.031-.063.063-.094.157-.094h1.164c.755
 0 1.195.094 1.132.723-.031.315-.472 1.132-.629
 1.384-.063.094-.189.189-.157 0 .126-.503.597-1.321.189-1.384zm.88
 8.902H2.076s17.363-6.794 17.552-6.92c0 0
 1.541-2.076.629-2.925-.283-.283-.692-.283-2.265-.283 0
 0-.063-.598-2.485-1.164-.283-.063-11.858-2.517-11.858-2.517h19.628l-2.926
 13.809zm2.925-.695c0-.195-.114-.293-.358-.293h-.406v1.008h.146v-.439h.179l.276.455h.179L23
 18.564c.162-.016.276-.097.276-.276zm-.455.146h-.163v-.341h.211c.114 0
 .228.016.228.163 0 .162-.13.178-.276.178zm.016-.829a.868.868 0 0
 0-.894.878c0 .504.406.894.894.894s.894-.39.894-.894a.878.878 0 0
 0-.894-.878zm0 1.642c-.423 0-.731-.325-.731-.764
 0-.423.325-.748.731-.748.406 0 .731.325.731.748 0
 .439-.325.764-.731.764z" />
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
