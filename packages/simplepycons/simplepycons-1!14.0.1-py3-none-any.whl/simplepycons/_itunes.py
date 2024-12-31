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


class ItunesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "itunes"

    @property
    def original_file_name(self) -> "str":
        return "itunes.svg"

    @property
    def title(self) -> "str":
        return "iTunes"

    @property
    def primary_color(self) -> "str":
        return "#FB5BC5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>iTunes</title>
     <path d="M11.977 23.999c-2.483 0-4.898-.777-6.954-2.262a11.928
 11.928 0 01-4.814-7.806A11.954 11.954 0 012.3 4.994 11.85 11.85 0
 0110.08.159a11.831 11.831 0 018.896 2.104 11.933 11.933 0 014.815
 7.807 11.958 11.958 0 01-2.091 8.937 11.855 11.855 0 01-7.78 4.835
 12.17 12.17 0 01-1.943.157zm-6.474-2.926a11.022 11.022 0 008.284 1.96
 11.044 11.044 0 007.246-4.504c3.583-5.003
 2.445-12.003-2.538-15.603a11.022 11.022 0 00-8.284-1.96A11.046 11.046
 0 002.966 5.47C-.618 10.474.521 17.473 5.503
 21.073zm10.606-3.552a2.08 2.08 0
 001.458-1.468l.062-.216.008-5.786c.006-4.334
 0-5.814-.024-5.895a.535.535 0 00-.118-.214.514.514 0
 00-.276-.073c-.073 0-.325.035-.56.078-1.041.19-7.176 1.411-7.281
 1.45a.786.786 0 00-.399.354l-.065.128s-.031 9.07-.078 9.172a.7.7 0
 01-.376.35 9.425 9.425 0
 01-.609.137c-1.231.245-1.688.421-2.075.801-.22.216-.382.51-.453.82-.067.294-.045.736.051
 1.005.1.281.262.521.473.71.192.148.419.258.674.324.563.144 1.618-.016
 2.158-.328a2.36 2.36 0
 00.667-.629c.06-.089.15-.268.2-.399.176-.456.181-8.581.204-8.683a.44.44
 0 01.32-.344c.147-.04 6.055-1.207
 6.222-1.23.146-.02.284.027.36.12a.29.29 0
 01.109.096c.048.07.051.213.058 2.785.008 2.96.012 2.892-.149
 3.079-.117.136-.263.189-.864.31-.914.188-1.226.276-1.576.447-.437.213-.679.446-.867.835a1.58
 1.58 0 00-.182.754c.001.49.169.871.55
 1.245.035.034.069.066.104.097.192.148.387.238.633.294.37.082
 1.124.025 1.641-.126z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:ITune'''

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
