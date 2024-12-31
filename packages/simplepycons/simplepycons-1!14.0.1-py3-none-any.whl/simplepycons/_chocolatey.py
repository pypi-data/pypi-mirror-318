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


class ChocolateyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "chocolatey"

    @property
    def original_file_name(self) -> "str":
        return "chocolatey.svg"

    @property
    def title(self) -> "str":
        return "Chocolatey"

    @property
    def primary_color(self) -> "str":
        return "#80B5E3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Chocolatey</title>
     <path d="M0 1.249l1.439 3.18L0 6.926l1.439 2.5L0 11.923l1.439
 2.424L0 16.845l1.439 2.5L0 22.75l2.8-.91c6.3.01 12.696.006 18.096
 0l3.104.91-2.044-3.635
 1.136-1.892-2.196-2.272-.004-.017V2.005c-6.551-.001-12.243 0-18.091
 0zm19.688
 1.968v7.03l-.23-.898-1.438-4.39-3.56.605-1.89-2.343zm-11.695.004h4.563L9.539
 4.428zm2.86 3.68a3.903 3.903 0 0 1 1.64.254c1.968.757 1.286 2.8.15
 4.012-.378.378-1.21.227-.605-.908.228-.454.454-1.363-.227-1.59-1.515-.53-3.255.682-3.634
 2.271-.378 1.363.606 2.801 2.347 2.423 1.439-.303 2.802-1.288
 3.332-1.742.53-.455.907.38.301 1.288-.68.908-1.74 1.968-2.65
 2.574-3.558 2.423-6.662-.758-5.375-4.392.677-1.845 2.454-4.041
 4.72-4.19zm6.527 2.031a.66.66 0 0 1 .454.182c.324.326.204.972-.268
 1.445-.473.474-1.121.593-1.446.268-.325-.326-.205-.972.267-1.445.292-.292.666-.461.993-.45zm-.42
 3.233a.66.66 0 0 1 .454.182c.325.325.206.973-.268
 1.446-.473.473-1.12.592-1.445.268-.324-.326-.205-.972.268-1.445.291-.292.664-.462.99-.451Z"
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
