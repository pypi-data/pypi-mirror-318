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


class TrimbleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "trimble"

    @property
    def original_file_name(self) -> "str":
        return "trimble.svg"

    @property
    def title(self) -> "str":
        return "Trimble"

    @property
    def primary_color(self) -> "str":
        return "#0063A3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Trimble</title>
     <path d="M2.598 18.338a9.1 9.1 0 0 0 4.799 2.82L2.598
 24zm4.764-15.52a9.14 9.14 0 0 0-4.764 2.81V0zM22.854 12l-4.811
 2.851a9.65 9.65 0 0 0 .014-5.693zM5.758 4.301a9.4 9.4 0 0 1
 5.297-.615 4.3 4.3 0 0
 0-2.425.828c-.756-.213-2.185-.369-2.872-.213M14.9 14.602c-2.367
 1.828-6.156 1.322-8.459-.605a23 23 0 0 1 2.673-3.483c1.359 1.208
 3.398 1.7 5.035.936.38 1.014.633 2.073.751 3.152m-9.72-.42a15.4 15.4
 0 0 0-1.621 3.751 8.5 8.5 0 0 1-2.406-5.603 8.54 8.54 0 0 1
 1.939-5.79c-.651 2.393.058 5.506 2.088
 7.642m8.6-3.636c-1.137.532-2.746.326-3.976-.723a19 19 0 0 1
 2.339-1.865 11.4 11.4 0 0 1 1.637 2.588m-1.527-3.893a8.7 8.7 0 0
 0-2.519-1.735c.909-.593 3-.629 4.301.72a8.4 8.4 0 0 0-1.782
 1.015M5.922 14.88c2.399 1.937 6.253 2.59 9.051.881a7.4 7.4 0 0 1-.468
 2.719 8.06 8.06 0 0 1-5.014 1.893 8.05 8.05 0 0
 1-5.085-1.684c.136-.689.505-2.016 1.516-3.809m8.653-4.932a12.7 12.7 0
 0 0-1.632-2.544 7 7 0 0 1 1.667-1.003c.681.945.861 2.587-.035
 3.547m1.544-2.064c.837 1.87.874 4.207-.354 5.844a14 14 0 0
 0-.778-2.822c.419-.367.743-.835.941-1.363a3.5 3.5 0 0 0
 .191-1.659M9.14 9.096c-.758-1.049-.992-2.402-.229-3.451a7.7 7.7 0 0 1
 2.53 1.581 19.5 19.5 0 0 0-2.301 1.87m6.773 5.95a6.5 6.5 0 0 0
 1.609-3.749 8.65 8.65 0 0 1-1.71 5.88q.144-1.061.101-2.131M7.956
 5.347c-.846 1.347-.467 3.226.487 4.443a24 24 0 0 0-2.725
 3.499c-1.876-2.141-2.624-5.575-1.013-7.92a6.5 6.5 0 0 1 3.251-.022"
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
