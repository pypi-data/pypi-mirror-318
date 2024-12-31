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


class SmrtIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "smrt"

    @property
    def original_file_name(self) -> "str":
        return "smrt.svg"

    @property
    def title(self) -> "str":
        return "SMRT"

    @property
    def primary_color(self) -> "str":
        return "#EE2E24"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SMRT</title>
     <path d="M2.6535 13.753c.8096 4.4368 4.677 7.8105 9.3392 7.8105
 4.677 0 8.6171-4.0882 9.3967-8.5422h-2.5631c-.7499 3.0597-3.5506
 6.0385-6.8334 6.0385-2.3686 0-4.4526-1.1984-5.727-2.999h5.292c.435 0
 .8542-.2304
 1.214-.7029l1.2895-1.8584c.121-.2305.3448-.3601.6145-.3601h7.54L24
 10.8318H13.6117c-.2535 0-.48.144-.6148.3284l-1.7089
 2.2932c-.1037.1728-.2852.288-.4946.288zm18.6783-3.5063c-.8096-4.4396-4.6468-7.8102-9.3242-7.8102-4.677
 0-8.4993 3.9755-9.2786 8.4299h2.5634c.7496-3.0598 3.4322-5.9265
 6.7302-5.9265 2.3686 0 4.452 1.1985 5.7263 2.9964h-5.3065c-.4348
 0-.8545.2305-1.2143.7058l-1.2892
 1.8581c-.121.2305-.3448.3604-.6148.3604h-7.54L0 13.1365h10.3883c.2535
 0
 .48-.144.6148-.3284l1.7089-2.3107c.1037-.1729.2852-.2881.4946-.2881z"
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
        return '''https://commons.wikimedia.org/wiki/File:SMRT_'''

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
