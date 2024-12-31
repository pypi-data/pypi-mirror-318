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


class WhenIWorkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wheniwork"

    @property
    def original_file_name(self) -> "str":
        return "wheniwork.svg"

    @property
    def title(self) -> "str":
        return "When I Work"

    @property
    def primary_color(self) -> "str":
        return "#51A33D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>When I Work</title>
     <path d="M12 24C5.342 24 0 18.582 0 12 0 5.342 5.342 0 12 0s12
 5.342 12 12c0 6.582-5.342 12-12 12zm0-21.986c-5.497 0-9.987
 4.489-9.987 9.986 0 5.498 4.49 9.988 9.987 9.988 5.498 0 9.987-4.49
 9.987-9.988 0-5.497-4.489-9.986-9.987-9.986zm5.885 11.148H9.213c-.384
 0-.695-.309-.698-.691v-1.012c0-.387.311-.697.698-.697h8.748c.387 0
 .697.311.697.697v1.006c-.077.387-.387.697-.773.697zm-2.246-3.871H6.891c-.383.002-.697-.307-.698-.691V7.59c0-.311.31-.621.697-.621h8.748c.31
 0 .62.311.62.619v1.006c.001.386-.31.697-.619.697zm-8.748
 5.418h8.748c.388 0
 .696.311.696.697v1.006c.002.383-.309.695-.691.697H6.891c-.388-.076-.697-.387-.697-.773V15.33c-.001-.31.309-.621.697-.621z"
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
