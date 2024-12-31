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


class ZebpayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zebpay"

    @property
    def original_file_name(self) -> "str":
        return "zebpay.svg"

    @property
    def title(self) -> "str":
        return "ZebPay"

    @property
    def primary_color(self) -> "str":
        return "#2072EF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ZebPay</title>
     <path d="M5.736 10.245S17.304 21.238 16.902
 20.83l.905-1.091L6.828 9.31c-.331.279-.698.592-1.092.935Zm-4.88
 4.38s-.828.823-.855 1.97c-.018.52.134 1.108.604 1.713 0 0
 .007.012.026.035a2.267 2.267 0 0 0
 .733.51c.038.016.08.035.126.05.11.042.237.077.373.108a4.28 4.28 0 0 0
 1.217.064l.222-.023c.076-.011.153-.02.232-.034.08-.012.161-.027.245-.042.007
 0 .011 0 .02-.004.007 0 .015 0 .022-.004.768-.151 1.706-.467
 2.836-1.022l-4.702-4.478c-.373.38-.743.767-1.1
 1.156Zm8.276-7.472s-.305.236-.801.636l-.294.236 10.907
 10.378.92-1.093L9.161 7.12c-.011.01-.019.022-.03.033Zm-5.91 5.07
 5.126 4.882a5.421 5.421 0 0 1 1.738-.32L4.27
 11.245c-.343.314-.693.64-1.047.978Zm5.529-8.885s-.414.14-.61.46L20.96
 16.011l.921-1.09L9.544
 3.158c-.276.04-.544.096-.793.18Zm5.959.443s-1.081-.353-2.434-.556l10.818
 10.253.906-1.07-.722-.682-8.18-7.79c-.128-.05-.256-.103-.388-.155Z"
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
