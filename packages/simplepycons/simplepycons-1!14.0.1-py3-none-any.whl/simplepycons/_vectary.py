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


class VectaryIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vectary"

    @property
    def original_file_name(self) -> "str":
        return "vectary.svg"

    @property
    def title(self) -> "str":
        return "Vectary"

    @property
    def primary_color(self) -> "str":
        return "#6100FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vectary</title>
     <path d="M2.1797 2.3184a6.6198 6.6198 0 0
 0-.2734.0117c-.628.017-1.2937.412-1.6094.955-.3423.5267-.395
 1.3011-.127 1.8692l4.2715 9.668c.2394.5807.845 1.0623 1.4649
 1.164.614.1323 1.3555-.0942 1.791-.5468 1.0385-1.0052 1.8471-2.4642
 2.1425-4.0215.2956-1.5574.0788-3.2117-.5195-4.5274-.5696-1.3282-1.6479-2.603-2.998-3.4336-1.2658-.7785-2.7708-1.1679-4.1426-1.1386zm18.8574
 0c-.9528.0168-1.9351.2075-2.834.5898-1.7978.7646-3.267 2.3-3.914
 3.8613L8.1719
 20.6211c-.0507.1103-.0512.2522-.002.3633.0459.1124.149.21.2637.25
 1.5734.617 3.6982.622 5.496-.1426 1.7978-.7646 3.269-2.3
 3.9161-3.8613l6.1152-13.8516c.0508-.1103.0512-.2523.002-.3633-.0458-.1124-.147-.21-.2617-.25-.7867-.3085-1.7113-.464-2.664-.4472z"
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
