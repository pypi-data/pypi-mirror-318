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


class FreshIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fresh"

    @property
    def original_file_name(self) -> "str":
        return "fresh.svg"

    @property
    def title(self) -> "str":
        return "Fresh"

    @property
    def primary_color(self) -> "str":
        return "#FFDB1E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fresh</title>
     <path d="M18.144
 1.913c-.818-.017-1.704.078-2.626.264-2.46.496-5.215 1.667-7.73
 3.319-2.877 1.89-5.037 4.094-6.346 6.056-.656.981-1.1 1.9-1.309
 2.708s-.192 1.536.187 2.067c.93 1.3 1.312 2.654 1.748
 3.747.218.547.449 1.034.809 1.409s.868.606 1.49.606c.368 0
 .685-.08.937-.247s.422-.407.537-.665a3.3 3.3 0 0 0 .178-.544c3.863
 1.74 7.955 1.54 10.295.732 1.096 1.247 3.982.724 3.258-1.81
 2.963-2.534 6.465-7.13 2.963-15.678a5 5 0 0
 0-.88-.74q-.062-.063-.13-.125h-.002c-.674-.587-1.56-.92-2.586-1.044q-.384-.047-.793-.055m-.031.732q.374.01.72.05c.92.112
 1.68.398 2.216.863.404.352.572.715.596 1.136s-.112.916-.407
 1.463c-.59 1.091-1.797 2.349-3.265 3.559-2.937 2.42-6.922 4.68-9.034
 5.52-2.462.98-3.108 2.701-3.389 4.043-.078.383-.14.73-.204
 1.027v.003a5 5 0 0 1-.07.291q-.044.16-.097.282a1 1 0 0 1-.125.215.7.7
 0 0 1-.15.14c-.112.076-.27.128-.537.128q-.173 0-.312-.024a1.04 1.04 0
 0 1-.467-.192 1.5 1.5 0 0
 1-.189-.167c-.244-.253-.452-.66-.659-1.176-.105-.268-.213-.566-.33-.881a28
 28 0 0 0-.292-.756c-.034-.082-.065-.163-.102-.247A10.4 10.4 0 0 0 .91
 15.905a1 1 0 0 1-.07-.12 1 1 0 0 1-.064-.184l-.011-.05a1.5 1.5 0 0
 1-.032-.231 2 2 0 0 1 .002-.26l.004-.073a3 3 0 0 1
 .044-.311v-.002q.022-.112.053-.232c.18-.695.586-1.556
 1.207-2.488C3.287 10.09 5.388 7.94 8.187 6.101c2.443-1.604 5.13-2.743
 7.474-3.216a11.2 11.2 0 0 1 2.452-.24m-2.007.923c-1.601.254-5.374
 1.608-8.391 3.636-.679.456-.681.559-.291 1.118-.583
 0-1.008-.102-1.653.469-3.576 3.162-4.71 6.603-2.183 6.603 1.167 0
 3.236-.562 4.224-.932.17-.064.676-1.383.676-1.685 0-.906.906.85
 1.171.725.954-.45 3.035-1.548 5.737-3.498 2.851-2.057 6.479-5.276
 3.115-6.181-.295-.08-1.516.1-1.813.2 0-.202-.327-.444-.592-.455m-5.45
 3.507c.235.337 1.2.44 1.776.507-.517.327-.764.617-1.05
 1.525-1.06-.442-2.294-.22-3.18.304.714-.541 1.19-.732
 1.521-1.829.41.087.608-.057.933-.507" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/denoland/fresh/blob/7e4a22'''

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
