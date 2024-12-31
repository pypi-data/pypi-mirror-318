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


class SololearnIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sololearn"

    @property
    def original_file_name(self) -> "str":
        return "sololearn.svg"

    @property
    def title(self) -> "str":
        return "Sololearn"

    @property
    def primary_color(self) -> "str":
        return "#149EF2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sololearn</title>
     <path d="M18.621 16.084a8.483 8.483 0 0 1-2.922
 6.427c-.603.53-.19 1.522.613 1.442a9.039 9.039 0 0 0 1.587-.3 8.32
 8.32 0 0 0 5.787-5.887 8.555 8.555 0 0 0-8.258-10.832 9.012 9.012 0 0
 0-1.045.06c-.794.1-.995 1.161-.29 1.542 2.701 1.452 4.53 4.285 4.53
 7.548zM7.906 18.597a8.538 8.538 0 0
 1-6.45-2.913c-.532-.6-1.527-.19-1.446.61a8.943 8.943 0 0 0 .3
 1.582c.794 2.823 3.064 5.026 5.907 5.766 5.727 1.492 10.87-2.773
 10.87-8.229 0-.35-.02-.7-.06-1.04-.1-.792-1.165-.992-1.547-.29a8.597
 8.597 0 0 1-7.574 4.514zM5.382 7.916a8.483 8.483 0 0 1
 2.924-6.427c.603-.531.19-1.522-.613-1.442a9.93 9.93 0 0
 0-1.598.29A8.339 8.339 0 0 0 .31 6.224a8.555 8.555 0 0 0 8.258
 10.832c.352 0 .704-.02 1.045-.06.794-.1.995-1.162.29-1.542a8.54 8.541
 0 0 1-4.52-7.538zm10.72-2.513a8.538 8.538 0 0 1 6.45 2.913c.53.6
 1.526.19 1.445-.61a8.945 8.945 0 0 0-.3-1.583C22.902 3.3 20.632 1.098
 17.788.357 12.071-1.145 6.928 3.12 6.928 8.576c0 .35.02.7.06
 1.041.1.791 1.168.991 1.549.29A8.58 8.58 0 0 1 16.1 5.404z" />
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
        yield from [
            "SoloLearn",
        ]
