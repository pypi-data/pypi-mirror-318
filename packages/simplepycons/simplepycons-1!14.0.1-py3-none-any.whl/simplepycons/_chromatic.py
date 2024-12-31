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


class ChromaticIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "chromatic"

    @property
    def original_file_name(self) -> "str":
        return "chromatic.svg"

    @property
    def title(self) -> "str":
        return "Chromatic"

    @property
    def primary_color(self) -> "str":
        return "#FC521F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Chromatic</title>
     <path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0
 12-12A12 12 0 0 0 12 0zm-.006 3.43a3.372 3.372 0 0 1 3.37
 3.369v2.199L9.628 5.689a4.261 4.261 0 0 0-.688-.32 3.351 3.351 0 0 1
 3.053-1.94zm-4.498 2.6c.588 0 1.17.156 1.684.452l5.734 3.311-2.91
 1.678-3.6-2.076a.46.46 0 0 0-.459 0L5.35
 10.893c-.22.126-.428.27-.621.433a3.349 3.349 0 0 1-.155-3.61A3.385
 3.385 0 0 1 7.496 6.03zm8.723.015a3.383 3.383 0 0 1 3.205 1.672 3.37
 3.37 0 0 1-1.235 4.6l-5.736 3.308v-3.357l3.602-2.077a.459.459 0 0 0
 .228-.398V6.799c0-.253-.021-.506-.064-.754zm-8.504 4.543v6.617c0
 .254.021.505.066.754a3.4 3.4 0 0 1-.285.012 3.383 3.383 0 0
 1-2.92-1.684 3.343 3.343 0 0 1-.338-2.555 3.342 3.342 0 0 1
 1.57-2.044l1.907-1.1zm.908 0 2.912 1.68v4.152a.46.46 0 0 0
 .23.396l2.594 1.498h.002c.22.127.45.235.688.32a3.35 3.35 0 0 1-3.055
 1.938 3.373 3.373 0 0 1-3.371-3.367v-6.617zm10.647 2.088a3.347 3.347
 0 0 1 .154 3.611 3.372 3.372 0 0 1-4.604 1.233l-1.908-1.1
 5.738-3.309a4.31 4.31 0 0 0 .62-.435z" />
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
