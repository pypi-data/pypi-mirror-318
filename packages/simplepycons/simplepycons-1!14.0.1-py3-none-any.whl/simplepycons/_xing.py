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


class XingIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "xing"

    @property
    def original_file_name(self) -> "str":
        return "xing.svg"

    @property
    def title(self) -> "str":
        return "Xing"

    @property
    def primary_color(self) -> "str":
        return "#006567"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Xing</title>
     <path d="M18.188 0c-.517 0-.741.325-.927.66 0 0-7.455
 13.224-7.702 13.657.015.024 4.919 9.023 4.919
 9.023.17.308.436.66.967.66h3.454c.211 0
 .375-.078.463-.22.089-.151.089-.346-.009-.536l-4.879-8.916c-.004-.006-.004-.016
 0-.022L22.139.756c.095-.191.097-.387.006-.535C22.056.078 21.894 0
 21.686 0h-3.498zM3.648 4.74c-.211
 0-.385.074-.473.216-.09.149-.078.339.02.531l2.34 4.05c.004.01.004.016
 0 .021L1.86 16.051c-.099.188-.093.381 0
 .529.085.142.239.234.45.234h3.461c.518 0
 .766-.348.945-.667l3.734-6.609-2.378-4.155c-.172-.315-.434-.659-.962-.659H3.648v.016z"
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
