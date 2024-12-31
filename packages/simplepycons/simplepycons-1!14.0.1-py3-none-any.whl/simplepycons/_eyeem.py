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


class EyeemIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "eyeem"

    @property
    def original_file_name(self) -> "str":
        return "eyeem.svg"

    @property
    def title(self) -> "str":
        return "EyeEm"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>EyeEm</title>
     <path d="M3.673
 9.204v-1.04H0v5.722h3.68v-1.048H1.186V11.46h2.158v-1.017H1.186v-1.24zm2.162
 6.633l2.532-5.906h-1.24l-.902 2.357-.91-2.357H4.081l1.546 3.604-1.01
 2.303zm6.625-3.572v-.445c0-1.232-.75-1.966-1.89-1.966-1.179
 0-2.013.78-2.013 2.059 0 1.27.834 2.057 2.043 2.057.926 0 1.684-.536
 1.821-1.285l-1.124-.054c-.085.275-.337.436-.727.436-.505
 0-.804-.314-.827-.803zm-1.898-1.539c.505 0
 .75.314.773.796H9.743c.031-.505.345-.796.82-.796zm6.478-1.524v-1.04h-3.672v5.724h3.68v-1.048h-2.495V11.46h2.158v-1.018h-2.158v-1.24zm5.46.65c-.597
 0-.987.269-1.216.629-.26-.406-.697-.627-1.24-.627s-.864.206-1.04.482v-.407h-1.056v3.956h1.117V11.69c0-.474.268-.796.711-.796.406
 0 .643.283.643.788v2.205h1.117v-2.333c.046-.399.291-.659.689-.659.428
 0 .658.284.658.789v2.204H24V11.46c0-1.002-.597-1.606-1.5-1.606z" />
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
