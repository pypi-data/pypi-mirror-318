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


class VenmoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "venmo"

    @property
    def original_file_name(self) -> "str":
        return "venmo.svg"

    @property
    def title(self) -> "str":
        return "Venmo"

    @property
    def primary_color(self) -> "str":
        return "#008CFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Venmo</title>
     <path d="M21.772 13.119c-.267 0-.381-.251-.38-.655
 0-.533.121-1.575.712-1.575.267 0 .357.243.357.598 0 .533-.13
 1.632-.689 1.632Zm.502-3.377c-1.677 0-2.405 1.285-2.405 2.658 0
 1.042.421 1.874 1.693 1.874 1.717 0 2.438-1.406 2.438-2.763
 0-1.025-.462-1.769-1.726-1.769Zm-3.833 0c-.558
 0-.964.17-1.393.477-.154-.275-.462-.477-.932-.477-.542
 0-.947.219-1.247.437l-.04-.364H13.54l-.688
 4.354h1.506l.479-3.053c.129-.065.323-.154.518-.154.145 0
 .267.049.267.267 0 .056-.016.145-.024.218l-.429
 2.722h1.498l.478-3.053c.138-.073.324-.154.51-.154.146 0
 .268.049.268.267 0 .056-.017.145-.025.218l-.429
 2.722h1.499l.461-2.908c.025-.153.049-.388.049-.549
 0-.582-.267-.97-1.037-.97Zm-6.871 0c-.575
 0-.98.219-1.287.421l-.017-.348H8.962l-.689
 4.354H9.78l.478-3.053c.13-.065.324-.154.518-.154.147 0
 .268.049.268.242 0 .081-.024.227-.032.299l-.422
 2.666h1.499l.462-2.908c.024-.153.049-.388.049-.549
 0-.582-.268-.97-1.03-.97Zm-5.631
 1.834c.041-.485.413-.824.697-.824.162 0 .299.097.299.291 0
 .404-.713.533-.996.533Zm.843-1.834c-1.604 0-2.382 1.39-2.382 2.698 0
 1.01.478 1.817 1.814 1.817.527 0 1.07-.113
 1.418-.282l.186-1.26c-.494.25-.874.347-1.271.347-.365
 0-.64-.194-.64-.687.826-.008 2.252-.347 2.252-1.453
 0-.687-.494-1.18-1.377-1.18Zm-4.239.267c.089.186.146.412.146.743 0
 .606-.429 1.494-.777 2.06l-.373-2.989L0 9.969l.705 4.2h1.757c.77-1.01
 1.718-2.448 1.718-3.554 0-.347-.073-.622-.235-.889l-1.402.283Z" />
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
