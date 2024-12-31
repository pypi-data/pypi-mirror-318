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


class DeeplIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "deepl"

    @property
    def original_file_name(self) -> "str":
        return "deepl.svg"

    @property
    def title(self) -> "str":
        return "DeepL"

    @property
    def primary_color(self) -> "str":
        return "#0F2B46"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DeepL</title>
     <path d="M20.907 4.93953 12.68543.18573a1.3577 1.3577 0 0
 0-1.3709 0L3.09298 4.9565a1.3766 1.3766 0 0 0-.68639
 1.18233v9.52646a1.3766 1.3766 0 0 0 .68639 1.19363l8.22157
 4.75946.06223.03583 4.04856
 2.3458-.01131-2.06106.0075-1.1446.0038.01885v-.38467c0-.23006.1188-.43371.29605-.56005l.264-.15086.12633-.06977h-.0075l4.80283-2.7795a1.3803
 1.3803 0 0 0 .68639-1.19551V6.13505a1.3803 1.3803 0 0
 0-.68642-1.19552m-9.85269 9.68863a1.4275 1.4275 0 0 1-.39976 1.3841
 1.4086 1.4086 0 0 1-1.97054 0 1.4199 1.4199 0 0 1 0-2.06294 1.4086
 1.4086 0 0 1
 2.0422.07543l3.32822-1.91585.6864.38656zm5.77019-2.41367a1.4086
 1.4086 0 0 1-1.97054 0 1.4256 1.4256 0 0
 1-.3696-1.47837l-.0132.0075-3.7525-2.1723-.05657.05656a1.4086 1.4086
 0 0 1-1.97053 0 1.4199 1.4199 0 0 1 0-2.06293 1.4086 1.4086 0 0 1
 1.97242 0c.3941.37713.52422.91832.39033 1.40672l3.7808
 2.20059.01886-.01886a1.4086 1.4086 0 0 1 1.97242 0 1.42746 1.42746 0
 0 1 0 2.06105z" />
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
