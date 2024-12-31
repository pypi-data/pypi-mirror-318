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


class ToyotaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "toyota"

    @property
    def original_file_name(self) -> "str":
        return "toyota.svg"

    @property
    def title(self) -> "str":
        return "Toyota"

    @property
    def primary_color(self) -> "str":
        return "#EB0A1E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Toyota</title>
     <path d="M12 3.848C5.223 3.848 0 7.298 0 12c0 4.702 5.224 8.152
 12 8.152S24 16.702 24 12c0-4.702-5.223-8.152-12-8.152zm7.334 3.839c0
 1.08-1.725 1.913-4.488 2.246-.26-2.58-1.005-4.279-1.963-4.913
 2.948.184 6.45 1.227 6.45 2.667zM12 16.401c-.96
 0-1.746-1.5-1.808-4.389.577.047 1.18.072 1.808.072.628 0 1.23-.025
 1.807-.072-.061 2.89-.847 4.389-1.807 4.389zm0-6.308c-.59
 0-1.155-.019-1.69-.054.261-1.728.92-3.15 1.69-3.15.77 0 1.428 1.422
 1.689 3.15-.535.034-1.099.054-1.689.054zm-.882-5.075c-.956.633-1.706
 2.333-1.964 4.915C6.391 9.6 4.665 8.767 4.665 7.687c0-1.44 3.504-2.49
 6.453-2.669zM2.037 11.68a5.265 5.265 0 011.048-3.164c.27 1.547 2.522
 2.881 5.972 3.37V12c0 3.772.879 6.203 2.087
 6.97-5.107-.321-9.107-3.48-9.107-7.29zm10.823 7.29c1.207-.767
 2.087-3.198 2.087-6.97v-.115c3.447-.488 5.704-1.826 5.972-3.37a5.26
 5.26 0 011.049 3.165c-.004 3.81-4.008 6.969-9.109 7.29z" />
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
