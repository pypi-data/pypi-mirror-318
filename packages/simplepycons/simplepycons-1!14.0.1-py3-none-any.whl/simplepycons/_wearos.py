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


class WearOsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wearos"

    @property
    def original_file_name(self) -> "str":
        return "wearos.svg"

    @property
    def title(self) -> "str":
        return "Wear OS"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wear OS</title>
     <path d="M8.416 21.1346c-.9687 0-1.8938-.56-2.3135-1.5015L.2193
 6.4198C-.3488 5.1432.2248 3.6472 1.5014 3.079c1.2767-.5681
 2.7727.0055 3.3408 1.2821l5.8832 13.2133c.5681 1.2767-.0055
 2.7727-1.2821 3.3408a2.5254 2.5254 0
 01-1.0273.2194zm7.1952.0368c-.891 0-1.7412-.515-2.1268-1.3816L7.39
 6.1024C6.867 4.9279 7.3955 3.5532 8.5686 3.03c1.173-.5218 2.5492.0054
 3.0724 1.1785l6.0943 13.6888c.5232 1.1745-.0054 2.5492-1.1785
 3.0724a2.3111 2.3111 0 01-.9456.2017zM24 5.195a2.3271 2.3271 0
 01-2.3271 2.327 2.3271 2.3271 0 01-2.3271-2.327 2.3271 2.3271 0
 012.327-2.3271A2.3271 2.3271 0 0124 5.1949zm-2.6119 5.116a2.4892
 2.4892 0 01-2.4892 2.4893 2.4892 2.4892 0 01-2.4893-2.4892 2.4892
 2.4892 0 012.4893-2.4893 2.4892 2.4892 0 012.4892 2.4893Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://partnermarketinghub.withgoogle.com/#/'''

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
