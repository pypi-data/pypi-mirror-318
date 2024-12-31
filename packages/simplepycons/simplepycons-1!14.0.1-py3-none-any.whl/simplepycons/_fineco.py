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


class FinecoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fineco"

    @property
    def original_file_name(self) -> "str":
        return "fineco.svg"

    @property
    def title(self) -> "str":
        return "Fineco"

    @property
    def primary_color(self) -> "str":
        return "#00549F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fineco</title>
     <path d="M1.712 8.72a1.702 1.702 0 0 0-1.21.488A1.678 1.678 0 0 0
 0 10.404v3.176a1.677 1.677 0 0 0 .496 1.207 1.702 1.702 0 0 0
 1.216.493h20.576v-.016a1.702 1.702 0 0 0 1.21-.487A1.678 1.678 0 0 0
 24 13.58v-3.176a1.677 1.677 0 0 0-.502-1.196 1.703 1.703 0 0
 0-1.21-.488Zm18.256 1.462c1.136 0 2.048.81 2.048 1.795 0 .984-.912
 1.794-2.048 1.794-1.136 0-2.048-.683-2.048-1.794 0-1.112.912-1.795
 2.048-1.795zm-3.344.016a3.238 3.238 0 0 1 .96.143l-.16.524a2.416
 2.416 0 0 0-.8-.127c-.992 0-1.792.397-1.792 1.254 0 .858.8 1.255
 1.792 1.255a2.432 2.432 0 0 0 .784-.127l.16.524a3.238 3.238 0 0
 1-.944.143c-1.52 0-2.464-.683-2.464-1.795 0-1.111 1.104-1.794
 2.464-1.794zm-14.336.063h2.576v.508h-1.92v.97h1.824v.508H2.944v1.477h-.656Zm3.312
 0h.656v3.469H5.6Zm1.504 0h.816l1.088 1.477a9.027 9.027 0 0 1 .72
 1.16h.016a12.977 12.977 0 0 1-.064-1.446v-1.191h.656v3.462H9.6L8.496
 12.2a11.58 11.58 0 0 1-.752-1.207h-.016c.032.444.032.905.032
 1.477v1.238l-.656.016zm4
 0h2.576v.524h-1.92v.953h1.824v.524H11.76v.953l1.92-.016v.524h-2.576zm8.864.445c-.768
 0-1.392.397-1.392 1.27 0 .874.624 1.271 1.392 1.271.768 0 1.392-.572
 1.392-1.27 0-.7-.624-1.271-1.392-1.271z" />
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
