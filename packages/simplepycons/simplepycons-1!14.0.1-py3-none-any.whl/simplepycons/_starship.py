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


class StarshipIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "starship"

    @property
    def original_file_name(self) -> "str":
        return "starship.svg"

    @property
    def title(self) -> "str":
        return "Starship"

    @property
    def primary_color(self) -> "str":
        return "#DD0B78"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Starship</title>
     <path d="M15.521 9.62a1.057 1.057 0 11-2.115 0 1.057 1.057 0
 012.115 0zM24 12c0 6.627-5.373 12-12 12-.35 0-.697-.015-1.04-.044
 2.019-1.89 2.548-5.061 2.548-5.061l-3.226-1.053s-1.499 3.23-5.599
 3.67A11.98 11.98 0 010 12C0 5.373 5.373 0 12 0s12 5.373 12 12zM8.628
 6.606c-1.23-.13-1.885-.83-2.03-2.031-.142 1.159-.77 1.88-2.032 2.031
 1.168.227 1.83.918 2.031 2.032-.02-1.154.666-1.825 2.031-2.032zm7.786
 5.207c1.11-2.483.392-4.252-1.233-6.246-2.043 1.5-3.759 3.023-3.636
 5.149-1.375.675-2.261 1.206-3.147 2.289l2.779 1.103-.368 1.267 3.637
 1.062.443-1.181 2.825.651c.014-1.496-.38-3.097-1.3-4.094z" />
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
