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


class UbiquitiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ubiquiti"

    @property
    def original_file_name(self) -> "str":
        return "ubiquiti.svg"

    @property
    def title(self) -> "str":
        return "Ubiquiti"

    @property
    def primary_color(self) -> "str":
        return "#0559C9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ubiquiti</title>
     <path d="M23.1627 0h-1.4882v1.4882h1.4882zm-5.2072
 10.4226V7.4409l.0007.001h2.9755v2.9762h2.9756v.9433c0 1.0906-.0927
 2.3827-.306 3.3973-.1194.5672-.3004 1.1308-.5127
 1.672-.2175.5537-.468 1.0841-.7408 1.5595a11.6795 11.6795 0 0
 1-1.2456
 1.7762l-.0253.0294-.0417.0488c-.1148.1347-.2283.2679-.3531.398a11.7612
 11.7612 0 0 1-.4494.4492c-1.9046 1.8343-4.3861 2.98-6.9808
 3.243-.3122.032-.939.0652-1.2519.0652-.3139-.001-.9397-.0331-1.252-.0651-2.5946-.263-5.0761-1.4097-6.9806-3.243a11.75
 11.75 0 0
 1-.4495-.4494c-.131-.1356-.249-.2748-.3683-.4154l-.0006-.0004-.0512-.0603a11.6576
 11.6576 0 0
 1-1.2456-1.7762c-.2727-.4763-.5233-1.0058-.7408-1.5595-.2123-.5414-.3933-1.1048-.5128-1.6718C.1854
 13.743.0927 12.452.0927 11.3616V.1864h5.9518v10.2362s0 .7847.0099
 1.0415l.0022.0599v.0004c.0127.332.0247.6575.0594.9812.098.919.3014
 1.7913.7203 2.5288.1213.213.2443.42.3915.616.8953 1.1939 2.2577
 2.0901 3.9573 2.3398.2022.0294.6108.0552.8149.0552.204 0
 .6125-.0258.8149-.0552 1.6996-.2497 3.062-1.146
 3.9573-2.3398.148-.196.2701-.403.3914-.616.419-.7375.6224-1.6095.7204-2.5288.0346-.3243.047-.6503.0594-.9831l.0022-.0584c.0099-.2568.0099-1.0415.0099-1.0415zm.7427-8.19h2.2326v2.2319h2.9764v2.9764h-2.9764V4.4654h-2.2326V2.2328Z"
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
