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


class CssWizardryIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "csswizardry"

    @property
    def original_file_name(self) -> "str":
        return "csswizardry.svg"

    @property
    def title(self) -> "str":
        return "CSS Wizardry"

    @property
    def primary_color(self) -> "str":
        return "#F43059"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CSS Wizardry</title>
     <path d="M0 16.5V1.127C0 .502.506 0 1.127 0h21.748C23.498 0 24
 .505 24 1.126V15.95c-.676-.413-1.467-.62-2.372-.62-1.258
 0-2.212.296-2.862.886-.65.591-.974 1.333-.974 2.226 0 .979.336 1.698
 1.008 2.158.397.276 1.114.53 2.151.765l1.056.237c.618.135 1.07.29
 1.36.466.288.18.432.436.432.765 0 .564-.29.95-.872
 1.157l-.024.008H20.68a1.528 1.528 0 0
 1-.688-.462c-.185-.225-.31-.565-.372-1.021h-1.99c0 .56.109 1.053.325
 1.483h-1.681c.196-.396.294-.837.294-1.32
 0-.889-.297-1.568-.892-2.037-.384-.302-.952-.543-1.705-.724l-1.719-.412c-.663-.158-1.096-.296-1.299-.413a.858.858
 0 0 1-.473-.799c0-.387.16-.69.48-.906.32-.217.75-.325 1.286-.325.482
 0 .886.084 1.21.25.488.253.75.68.785
 1.28h2.003c-.036-1.06-.425-1.869-1.167-2.426-.742-.557-1.639-.836-2.69-.836-1.258
 0-2.212.296-2.861.886-.65.591-.975 1.333-.975 2.226 0 .979.336 1.698
 1.008 2.158.397.276 1.114.53 2.152.765l1.055.237c.618.135 1.071.29
 1.36.466.288.18.433.436.433.765 0 .564-.291.95-.873
 1.157l-.025.008h-2.223a1.528 1.528 0 0
 1-.688-.462c-.185-.225-.31-.565-.372-1.021h-1.99c0 .56.108 1.053.324
 1.483H6.611a4.75 4.75 0 0 0 .667-1.801H5.215c-.14.514-.316.9-.528
 1.157-.261.326-.603.54-1.026.644H2.42c-.45-.115-.839-.37-1.165-.762C.792
 22.68.56 21.842.56 20.724c0-1.119.218-1.984.656-2.595.437-.611
 1.035-.917 1.793-.917.744 0 1.305.217 1.684.65.212.243.386.604.52
 1.082H7.3c-.032-.622-.262-1.242-.69-1.86-.776-1.1-2.003-1.65-3.68-1.65-1.168
 0-2.145.355-2.929 1.067zm24
 3.654v-1.562h-.518c-.036-.6-.298-1.026-.785-1.279-.325-.166-.728-.25-1.21-.25-.537
 0-.966.108-1.286.325-.32.216-.48.518-.48.906 0
 .357.157.623.473.799.203.117.636.255
 1.299.413l1.718.412c.29.07.554.149.789.236z" />
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
