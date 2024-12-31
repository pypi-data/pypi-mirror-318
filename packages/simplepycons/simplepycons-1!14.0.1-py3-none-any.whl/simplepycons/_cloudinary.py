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


class CloudinaryIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cloudinary"

    @property
    def original_file_name(self) -> "str":
        return "cloudinary.svg"

    @property
    def title(self) -> "str":
        return "Cloudinary"

    @property
    def primary_color(self) -> "str":
        return "#3448C5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cloudinary</title>
     <path d="M24 14.8598c0 2.1729-1.3757 3.974-3.5903
 4.6996l-.0995.0318V17.989c1.3777-.5805 2.1869-1.7275
 2.1869-3.1291-.0072-2-1.6087-3.6288-3.6082-3.6699h-.5964l-.1432-.5686c-.7025-2.8996-3.2886-4.9489-6.2721-4.97a6.3915
 6.3915 0 0 0-5.811 3.664l-.1828.3757-.4175.0437a4.4311 4.4311 0 0
 0-3.3052 2.088c-1.2803 2.0856-.6274 4.8143 1.4583
 6.0947v1.6897h-.01l-.149-.0675a5.9402 5.9402 0 0
 1-3.3658-4.3494c-.5787-3.2291 1.57-6.3161 4.7991-6.8948a7.8766 7.8766
 0 0 1 6.9839-4.149c3.4724.025 6.535 2.28 7.5901 5.5883 2.5789.3366
 4.5138 2.5245 4.5327 5.1251zm-15.3176-1.322h.5647a.0656.0656 0 0 0
 .0457-.1113L7.084 11.2158l-.0007-.0007a.0656.0656 0 0
 0-.0927.0007L4.78 13.4265a.0656.0656 0 0 0
 .0477.1113h.5566a.0656.0656 0 0 1 .0657.0656v5.0574c0 .6588.534
 1.1928 1.1928 1.1928H9.247a.0656.0656 0 0 0
 .0457-.1113l-.33-.33a1.1928 1.1928 0 0 1-.348-.839v-4.97a.0676.0676 0
 0 1 .0676-.0655zm9.769 2.5466h.5667a.0655.0655 0 0 0
 .0457-.1133l-2.2107-2.2087-.0015-.0015a.0636.0636 0 0
 0-.0899.0015L14.551 15.971a.0657.0657 0 0 0
 .0457.1133h.5567a.0656.0656 0 0 1 .0656.0656v2.5108c0 .6588.534
 1.1928 1.1928 1.1928h2.6063a.0655.0655 0 0 0
 .0457-.1113l-.33-.33a1.1928 1.1928 0 0 1-.348-.839V16.15a.0656.0656 0
 0 1 .0657-.0656zm-4.8844-1.2743h.5646a.0656.0656 0 0 0
 .0477-.1114l-2.2107-2.2027-.0006-.0006a.0656.0656 0 0
 0-.0928.0006l-2.2087 2.2068a.0656.0656 0 0 0
 .0457.1113h.5626a.0676.0676 0 0 1 .0657.0676v3.7791c0 .6588.534
 1.1928 1.1928 1.1928h2.5983a.0656.0656 0 0 0
 .0477-.1113l-.332-.33a1.193 1.193 0 0
 1-.346-.839v-3.6956c0-.0366.0291-.0665.0657-.0676z" />
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
