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


class ClouderaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cloudera"

    @property
    def original_file_name(self) -> "str":
        return "cloudera.svg"

    @property
    def title(self) -> "str":
        return "Cloudera"

    @property
    def primary_color(self) -> "str":
        return "#F96702"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cloudera</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0zm.344 20.251a8.25 8.25 0 1 1 0-16.502 8.21 8.21 0
 0 1 5.633 2.234L15.519 8.53a4.686 4.686 0 0 0-3.175-1.239 4.709 4.709
 0 1 0 3.284 8.081l2.657 2.346a8.224 8.224 0 0 1-5.941 2.533z" />
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
