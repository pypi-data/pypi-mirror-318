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


class SallaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "salla"

    @property
    def original_file_name(self) -> "str":
        return "salla.svg"

    @property
    def title(self) -> "str":
        return "Salla"

    @property
    def primary_color(self) -> "str":
        return "#BAF3E6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Salla</title>
     <path d="M18.862 13.439a1.27 1.27 0 0 0-.81-.555 1.27 1.27 0 0
 0-.964.18c-3.422 2.231-6.75 2.231-10.178 0a1.27 1.27 0 0 0-.964-.18
 1.283 1.283 0 0 0-.434 2.327c2.142 1.394 4.326 2.1 6.49 2.1 2.166 0
 4.348-.706 6.488-2.102a1.27 1.27 0 0 0 .555-.81 1.27 1.27 0 0
 0-.18-.964zm5.103 2.82-1.171-9.764a5.24 5.24 0 0
 0-5.2-4.614H6.406a5.236 5.236 0 0 0-5.198 4.612l-1.17 9.766a5.235
 5.235 0 0 0 5.198 5.86h13.529a5.238 5.238 0 0 0 5.198-5.86zm-3.21
 2.4c-.532.6-1.265.929-2.066.929H5.311c-.801
 0-1.536-.33-2.066-.929a2.73 2.73 0 0 1-.676-2.16l1.157-9.657A2.764
 2.764 0 0 1 6.468 4.41h11.064a2.765 2.765 0 0 1 2.742 2.432l1.157
 9.656a2.72 2.72 0 0 1-.676 2.161" />
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
