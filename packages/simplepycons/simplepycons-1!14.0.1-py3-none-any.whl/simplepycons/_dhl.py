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


class DhlIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dhl"

    @property
    def original_file_name(self) -> "str":
        return "dhl.svg"

    @property
    def title(self) -> "str":
        return "DHL"

    @property
    def primary_color(self) -> "str":
        return "#FFCC00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DHL</title>
     <path d="M4.22 10.303l-.767 1.043h4.18c.21 0
 .208.078.105.218-.105.142-.28.39-.386.534-.054.073-.154.207.171.207h1.71l.505-.69c.314-.426.028-1.312-1.095-1.312H4.22zm7.204
 0l-1.475 2.002h5.39l1.473-2.002H14.61l-.843
 1.146h-.985l.846-1.146h-2.203zm6.105 0l-1.474
 2.002h2.334l1.472-2.002H17.53zm-12.845 1.3l-1.54 2.094h3.754c1.24 0
 1.932-.844 2.145-1.136h-2.56c-.326
 0-.226-.133-.172-.207.107-.143.283-.388.388-.53.104-.14.107-.22-.105-.22h-1.91zM0
 12.562v.242h3.398l.176-.242H0zm9.762 0l-.836
 1.136h2.203l.836-1.136H9.762zm3.185 0l-.836
 1.136h2.203l.836-1.136h-2.203zm2.918
 0s-.159.22-.238.326c-.276.374-.033.81.87.81h3.538l.834-1.136h-5.004zm5.408
 0l-.177.242H24v-.242h-2.727zM0 13.01v.24h3.068l.178-.24H0zm20.943
 0l-.175.24H24v-.24h-3.057zM0 13.457v.24h2.74l.176-.24H0zm20.615
 0l-.177.24H24v-.24h-3.385z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.dpdhl-brands.com/dhl/en/guides/de'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.dpdhl-brands.com/dhl/en/guides/de'''

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
