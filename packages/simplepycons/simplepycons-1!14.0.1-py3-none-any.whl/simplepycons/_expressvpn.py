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


class ExpressvpnIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "expressvpn"

    @property
    def original_file_name(self) -> "str":
        return "expressvpn.svg"

    @property
    def title(self) -> "str":
        return "ExpressVPN"

    @property
    def primary_color(self) -> "str":
        return "#DA3940"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ExpressVPN</title>
     <path d="M11.705 2.349a4.874 4.874 0 00-4.39 2.797L6.033
 7.893h14.606c.41 0 .692.308.692.668 0 .359-.282.666-.692.666H2.592L0
 14.772h2.824c-.796 1.72-1.002 2.567-1.002 3.26 0 2.105 1.72 3.62
 4.416 3.62h8.239c1.771 0 3.337-1.412 3.337-3.03
 0-1.411-1.206-2.515-2.772-2.515H5.596c-.873
 0-1.284-.59-.924-1.335h11.859c4.004 0 7.469-3.029 7.469-6.802
 0-3.183-2.618-5.621-6.16-5.621z" />
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
