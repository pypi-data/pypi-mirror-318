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


class BattledotnetIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "battledotnet"

    @property
    def original_file_name(self) -> "str":
        return "battledotnet.svg"

    @property
    def title(self) -> "str":
        return "Battle.net"

    @property
    def primary_color(self) -> "str":
        return "#4381C3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Battle.net</title>
     <path d="M18.94 8.296C15.9 6.892 11.534 6 7.426
 6.332c.206-1.36.714-2.308 1.548-2.508 1.148-.275 2.4.48 3.594
 1.854.782.102 1.71.28 2.355.429C12.747 2.013 9.828-.282
 7.607.565c-1.688.644-2.553 2.97-2.448 6.094-2.2.468-3.915 1.3-5.013
 2.495-.056.065-.181.227-.137.305.034.058.146-.008.194-.04 1.274-.89
 2.904-1.373 5.027-1.676.303 3.333 1.713 7.56 4.055
 10.952-1.28.502-2.356.536-2.946-.087-.812-.856-.784-2.318-.19-4.04a26.764
 26.764 0 0 1-.807-2.254c-2.459 3.934-2.986 7.61-1.143 9.11 1.402 1.14
 3.847.725 6.502-.926 1.505 1.672 3.083 2.74 4.667
 3.094.084.015.287.043.332-.034.034-.06-.08-.124-.131-.149-1.408-.657-2.64-1.828-3.964-3.515
 2.735-1.929 5.691-5.263 7.457-8.988 1.076.86 1.64 1.773 1.398
 2.595-.336 1.131-1.615 1.84-3.403 2.185a27.697 27.697 0 0 1-1.548
 1.826c4.634.16 8.08-1.22
 8.458-3.565.286-1.786-1.295-3.696-4.053-5.17.696-2.139.832-4.04.346-5.588-.029-.08-.106-.27-.196-.27-.068
 0-.067.13-.063.187.135 1.547-.263 3.2-1.062 5.19zm-8.533
 9.869c-1.96-3.145-3.09-6.849-3.082-10.594 3.702-.124 7.474.748 10.714
 2.627-1.743 3.269-4.385 6.1-7.633 7.966h.001z" />
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
