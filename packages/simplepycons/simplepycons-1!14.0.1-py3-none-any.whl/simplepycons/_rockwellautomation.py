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


class RockwellAutomationIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rockwellautomation"

    @property
    def original_file_name(self) -> "str":
        return "rockwellautomation.svg"

    @property
    def title(self) -> "str":
        return "Rockwell Automation"

    @property
    def primary_color(self) -> "str":
        return "#CD163F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rockwell Automation</title>
     <path d="m23.1252 6.157-4.6678-4.6678a.7667.7667 0 0
 0-.9801-.087l-8.983 6.0494c1.7005.1068 2.7313.7962 2.7313 2.3676 0
 1.372-.74 2.2257-1.9913 2.3746v.0239c.5814.1067.9676.3763
 1.254.74.0997.1264.1685.2752.2079.434l.7091 2.1498
 3.0528-7.6475a.7082.7082 0 0 1 .6572-.4452h2.6821l3.5668
 8.9325h-2.2075c-.448
 0-.8664-.2837-1.056-.7078-.113-.3264-.229-.6527-.344-.9787h-3.2396l-.629
 1.6865H9.0475c-.2584
 0-.4789-.191-.5238-.4522l-.8046-2.3409c-.1124-.4002-.5098-.4634-.9016-.4634h-.7835v3.2565H3.2789v-5.4148l-1.6486
 1.1093a.5568.5568 0 0 0-.2387.4564v3.4474c0
 .222.132.4213.3342.5098l15.5408 6.5045a.7678.7678 0 0 0
 .8468-.1601l5.0075-4.9865A2.983 2.983 0 0 0 24 15.7325v-7.465a2.9953
 2.9953 0 0 0-.8748-2.1106ZM8.3749
 10.2797c0-.806-.5504-.9226-1.1346-.9226H6.072v1.9h1.1262c.5954 0
 1.1767-.0773 1.1767-.9774zm6.8682 2.4223h1.8143l-.8889-2.5234ZM6.8303
 7.4348 16.431.3223c.1376-.1025.066-.3202-.1053-.3202H8.455a3.4405
 3.4405 0 0 0-2.4336 1.0083L1.0083 6.022A3.4405 3.4405 0 0 0 0
 8.4557v7.0886c0 .9128.3623 1.7876 1.0083 2.4336l5.0131 5.0117A3.4405
 3.4405 0 0 0 8.455 23.998h6.8176c.1896 0
 .2471-.257.0758-.3384l-13.5496-6.388a1.6147 1.6147 0 0
 1-.9268-1.4604v-3.3997c0-.3552.1685-.6894.4536-.9l1.952-1.4465V7.4348Z"
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
        return '''https://www.rockwellautomation.com/en-ie/comp'''

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
