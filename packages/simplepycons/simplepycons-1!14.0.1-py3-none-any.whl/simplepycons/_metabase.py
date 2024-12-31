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


class MetabaseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "metabase"

    @property
    def original_file_name(self) -> "str":
        return "metabase.svg"

    @property
    def title(self) -> "str":
        return "Metabase"

    @property
    def primary_color(self) -> "str":
        return "#509EE3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Metabase</title>
     <path d="M5.385 6.136c0 .807-.644 1.461-1.438
 1.461s-1.438-.654-1.438-1.461.644-1.461 1.438-1.461 1.438.654 1.438
 1.461zm-1.438 2.63c-.794 0-1.438.654-1.438 1.461s.644 1.461 1.438
 1.461 1.438-.654 1.438-1.461-.644-1.461-1.438-1.461zm5.465-2.63c0
 .807-.644 1.461-1.438 1.461s-1.438-.654-1.438-1.461.644-1.461
 1.438-1.461 1.438.654 1.438 1.461zm-.35
 0c0-.613-.488-1.111-1.088-1.111s-1.088.499-1.088 1.111.488 1.111
 1.088 1.111 1.088-.498 1.088-1.111zm-1.088 5.592c.794 0 1.438-.654
 1.438-1.461s-.644-1.461-1.438-1.461-1.438.654-1.438 1.461.643 1.461
 1.438 1.461zm5.464-5.592c0 .807-.644 1.461-1.438
 1.461s-1.438-.654-1.438-1.461.644-1.461 1.438-1.461 1.438.654 1.438
 1.461zm-.35 0c0-.613-.488-1.111-1.088-1.111s-1.088.498-1.088
 1.111S11.4 7.247 12 7.247s1.088-.498 1.088-1.111zm.35-4.675c0
 .807-.644 1.461-1.438 1.461s-1.438-.654-1.438-1.461S11.206 0 12
 0s1.438.654 1.438 1.461zm-.35 0C13.088.848 12.6.35 12
 .35s-1.088.498-1.088 1.111S11.4 2.572 12 2.572s1.088-.498
 1.088-1.111zm.35 8.806c0 .807-.644 1.461-1.438
 1.461s-1.438-.654-1.438-1.461.644-1.461 1.438-1.461 1.438.654 1.438
 1.461zm-.35 0c0-.613-.488-1.111-1.088-1.111s-1.088.498-1.088
 1.111.488 1.111 1.088 1.111 1.088-.499 1.088-1.111zm4.376-4.131c0
 .807-.644 1.461-1.438 1.461s-1.438-.654-1.438-1.461.644-1.461
 1.438-1.461 1.438.654 1.438 1.461zm-.35
 0c0-.613-.488-1.111-1.088-1.111s-1.088.498-1.088 1.111.488 1.111
 1.088 1.111 1.088-.498 1.088-1.111zm2.939 1.461c.794 0 1.438-.654
 1.438-1.461s-.644-1.461-1.438-1.461-1.438.654-1.438 1.461.644 1.461
 1.438 1.461zm-4.027 1.209c-.794 0-1.438.654-1.438 1.461s.644 1.461
 1.438 1.461 1.438-.654 1.438-1.461-.643-1.461-1.438-1.461zm4.027
 0c-.794 0-1.438.654-1.438 1.461s.644 1.461 1.438 1.461 1.438-.654
 1.438-1.461-.644-1.461-1.438-1.461zM3.947 12.857a1.45 1.45 0 0
 0-1.438 1.461c0 .807.644 1.461 1.438 1.461s1.438-.654
 1.438-1.461a1.45 1.45 0 0 0-1.438-1.461zm5.465 1.5c0 .807-.644
 1.461-1.438 1.461s-1.438-.654-1.438-1.461.644-1.461 1.438-1.461
 1.438.655 1.438 1.461zm-.35
 0c0-.613-.488-1.111-1.088-1.111s-1.088.498-1.088 1.111.488 1.111
 1.088 1.111 1.088-.498 1.088-1.111zM12 12.896c-.794 0-1.438.654-1.438
 1.461s.644 1.461 1.438 1.461 1.438-.654
 1.438-1.461-.644-1.461-1.438-1.461zm5.464 1.461c0 .807-.644
 1.461-1.438 1.461s-1.438-.654-1.438-1.461.644-1.461 1.438-1.461
 1.438.655 1.438 1.461zm-.35
 0c0-.613-.488-1.111-1.088-1.111s-1.088.498-1.088 1.111.488 1.111
 1.088 1.111 1.088-.498 1.088-1.111zm2.939-1.461c-.794
 0-1.438.654-1.438 1.461s.644 1.461 1.438 1.461 1.438-.654
 1.438-1.461-.644-1.461-1.438-1.461zM3.947 16.948c-.794
 0-1.438.654-1.438 1.461s.644 1.461 1.438 1.461 1.438-.654
 1.438-1.461-.644-1.461-1.438-1.461zm5.465 1.5c0 .807-.644 1.461-1.438
 1.461s-1.438-.654-1.438-1.461.644-1.461 1.438-1.461 1.438.654 1.438
 1.461zm-.35 0c0-.613-.488-1.111-1.088-1.111s-1.088.498-1.088
 1.111.488 1.111 1.088 1.111 1.088-.498 1.088-1.111zm4.376 0c0
 .807-.644 1.461-1.438 1.461s-1.438-.654-1.438-1.461.644-1.461
 1.438-1.461 1.438.654 1.438 1.461zm-.35
 0c0-.613-.488-1.111-1.088-1.111s-1.088.498-1.088 1.111.488 1.111
 1.088 1.111 1.088-.498 1.088-1.111zm.35 4.091c0 .807-.644 1.461-1.438
 1.461s-1.438-.654-1.438-1.461.644-1.461 1.438-1.461 1.438.654 1.438
 1.461zm-.35 0c0-.613-.488-1.111-1.088-1.111s-1.088.498-1.088
 1.111S11.4 23.65 12 23.65s1.088-.498 1.088-1.111zm4.376-4.091c0
 .807-.644 1.461-1.438 1.461s-1.438-.654-1.438-1.461.644-1.461
 1.438-1.461 1.438.654 1.438 1.461zm-.35
 0c0-.613-.488-1.111-1.088-1.111s-1.088.498-1.088 1.111.488 1.111
 1.088 1.111 1.088-.498 1.088-1.111zm2.939-1.461c-.794
 0-1.438.654-1.438 1.461s.644 1.461 1.438 1.461 1.438-.654
 1.438-1.461-.644-1.461-1.438-1.461z" />
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
