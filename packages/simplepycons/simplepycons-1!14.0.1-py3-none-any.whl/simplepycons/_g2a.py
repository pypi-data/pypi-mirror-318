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


class GTwoAIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "g2a"

    @property
    def original_file_name(self) -> "str":
        return "g2a.svg"

    @property
    def title(self) -> "str":
        return "G2A"

    @property
    def primary_color(self) -> "str":
        return "#F05F00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>G2A</title>
     <path d="M24 15.419s-1.8844-3.5895-3.1571-6.0153a1.6802 1.6802 0
 0 0-.4674-.5659 1.3021 1.3021 0 0 0-.7927-.2572 1.239 1.239 0 0
 0-.7715.2572 1.6802 1.6802 0 0 0-.4674.5659c-1.2726 2.4258-3.1783
 6.0153-3.1783 6.0153l1.7391.0004 2.6781-5.1339 1.2586
 2.4128h-1.9378l.6832 1.3053h1.9356l.7386 1.4154H24zM3.4872
 13.9588c-1.071 0-1.9392-.8682-1.9392-1.9392s.8682-1.9392
 1.9392-1.9392l3.9342-.0031V8.6212H3.3946C1.5174 8.6236-.0024 10.1473
 0 12.0244c.0024 1.8738 1.5208 3.3922 3.3946
 3.3946h4.0268v-4.1277H3.053v1.4571l2.8447-.0001v1.2141l-2.4105-.0036zm7.2305-1.2109
 3.0641-.0002c1.1395 0 2.0633-.9238
 2.0633-2.0633s-.9238-2.0633-2.0633-2.0633h-3.6463c-.804-.0002-1.4559.6515-1.4561
 1.4555v.0006l4.9963-.0001a.6157.6157 0 0 1 .6201.591.6064.6064 0 0
 1-.5894.6229l-.0159.0002h-3.185c-1.0725.0004-1.9417.8701-1.9413
 1.9426v2.185h5.4523l.7727-1.4566h-4.7014v-.5841a.63.63 0 0 1
 .6299-.6302z" />
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
