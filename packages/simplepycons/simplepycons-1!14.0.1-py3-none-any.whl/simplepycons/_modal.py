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


class ModalIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "modal"

    @property
    def original_file_name(self) -> "str":
        return "modal.svg"

    @property
    def title(self) -> "str":
        return "Modal"

    @property
    def primary_color(self) -> "str":
        return "#7FEE64"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Modal</title>
     <path d="M4.89 5.57 0 14.002l2.521 4.4h5.05l4.396-7.718 4.512
 7.709 4.996.037L24 14.057l-4.857-8.452-5.073-.015-2.076 3.598L9.94
 5.57Zm.837.729h3.787l1.845 3.252H7.572Zm9.189.021 3.803.012 4.228
 7.355-3.736-.027zm-9.82.346L6.94 9.914l-4.209
 7.389-1.892-3.3Zm9.187.014 4.297 7.343-1.892 3.282-4.3-7.344zm-6.713
 3.6h3.79l-4.212 7.394H3.361Zm11.64 4.109 3.74.027-1.893
 3.281-3.74-.027z" />
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
