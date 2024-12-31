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


class LeicaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "leica"

    @property
    def original_file_name(self) -> "str":
        return "leica.svg"

    @property
    def title(self) -> "str":
        return "Leica"

    @property
    def primary_color(self) -> "str":
        return "#E20612"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Leica</title>
     <path d="M9.42
 10.954c.198.011.35.146.343.29-.033.94-1.19.795-1.19.795s.17-1.126.846-1.085zm9.313
 2.064c.794 0 .952-1.605.952-1.64a.41.41 0 0 0-.423-.398c-.66 0-.9
 1.203-.9 1.508 0
 .116.007.53.37.53zm-9.949-5.08c.036-.318-.12-.662-.555-.662-1.06
 0-1.509 2.963-1.509 2.963s1.853-.438 2.064-2.301zm-6.244
 5.82c-.207.021-.423.114-.423.344 0 .139.235.382.608.37.49-.014
 1.085-.475 1.085-.475s-.506-.207-1.085-.239a1.026 1.026 0 0 0-.185
 0zM24 12.003C24 18.628 18.627 24 12 24 5.37 24 0 18.628 0 12.003 0
 5.374 5.371 0 12 0c6.627 0 12 5.374 12 12.003zM11.933 9.446c0
 .446.377.555.794.555.418 0 .82-.18.82-.635
 0-.456-.48-.555-.82-.555-.471 0-.794.193-.794.635zM9.366 10.53c-1.41
 0-2.407.866-2.407 1.904 0 .948.808 1.35 1.852 1.35 1.184 0 2.354-.714
 2.354-.714s.071.714 1.006.714c.964 0 1.72-.714 1.72-.714s.417.687
 1.376.687c.98 0 1.72-.793 1.72-.793s.272.74 1.243.74c.759 0
 1.164-.476 1.164-.476s.212.477.873.477c.808 0 1.402-.556
 1.402-.556l-.132-.476s-.307.238-.529.238c-.168 0-.265-.137-.265-.291
 0-.347.556-2.064.556-2.064l-1.35.026-.052.212s-.201-.37-.9-.37c-1.352
 0-2.085 1.166-2.116
 1.852-.007.149-.027.158-.027.158-.032.036-.497.583-1.085.583-.47
 0-.555-.384-.555-.635 0-.273.233-1.35.873-1.35.348 0
 .555.291.555.291l.186-.608s-.292-.236-.9-.238c-1.308-.001-2.19.967-2.222
 1.852-.007.132-.03.176-.027.185-.043.053-.35.423-.767.423-.286
 0-.291-.219-.291-.317 0-.135.555-2.064.555-2.064l-1.481.026-.503
 1.879s-.826.581-1.958.661c-.584.04-.794-.32-.794-.529v-.08c.001 0
 .246.027.424.027.14 0 1.878-.134 1.878-1.19
 0-.605-.613-.82-1.376-.82zm12.568 3.889-.132-.476s-3.096 1.078-9.022
 1.005c-4.089-.05-7.224-1.243-7.224-1.243s.119-.212.185-.344c.41-.835.9-2.514.9-2.514s2.805-.785
 2.805-3.016c0-.706-.674-1.162-1.323-1.19-2.264-.089-2.877 3.128-3.017
 3.677-.007.039-.026.053-.026.053-.698-.095-1.085-.238-1.085-.238l-.159.45c.471.223
 1.165.29 1.165.29-.136.865-.82 2.488-.82
 2.488s-.608-.186-1.376-.186c-1 0-1.35.47-1.376.768-.066.77.911 1.137
 1.587 1.137 1.32 0 2.011-.714 2.011-.714s3.695 1.402 7.567
 1.402c5.069 0 9.34-1.35 9.34-1.35z" />
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
