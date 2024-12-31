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


class FloodIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "flood"

    @property
    def original_file_name(self) -> "str":
        return "flood.svg"

    @property
    def title(self) -> "str":
        return "Flood"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Flood</title>
     <path d="M19.683
 16.283c-1.233-.066-1.85-1.533-2.15-2.433-.266-.767-.666-2.117-.966-2.933-.35-.95-.45-1.017-.65-1.017-.417
 0-.734 1.183-1.05 2.067-.667 1.833-1.167 3.85-2.934 3.85-1.533
 0-2.216-1.184-2.7-1.884-.45-.666-.716-.816-1.133-.816-.533
 0-.783.466-1.267 1.283-.283.467-.6.95-.966
 1.267-.1.083-.934.733-1.717.633-.45-.067-.767-.333-.767-.783
 0-.617.684-.734 1.067-.884.333-.116.733-.716.933-1.05.534-.916
 1.217-2.116 2.75-2.116 1.35 0 2 .866 2.5 1.55.45.616.717 1.116 1.234
 1.133.433.017 1.033-1.617 1.383-2.75.533-1.733 1.233-3.333
 2.633-3.333 1.884 0 2.434 2.633 3.017 4.65.083.3.283.933.333
 1.016.267.567.484.934.717
 1.05.267.15.7.434.567.934-.084.383-.434.583-.834.566zm-15.366-1.6c.016
 0 .016 0 0 0 .016 0 .016 0 0 0zM12 0C5.367 0 0 5.367 0 12s5.367 12 12
 12 12-5.367 12-12S18.633 0 12 0zm0 22.017A10.015 10.015 0 011.983 12
 10.015 10.015 0 0112 1.983 10.015 10.015 0 0122.017 12 10.015 10.015
 0 0112 22.017Z" />
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
