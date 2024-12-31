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


class MicrostationIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "microstation"

    @property
    def original_file_name(self) -> "str":
        return "microstation.svg"

    @property
    def title(self) -> "str":
        return "Microstation"

    @property
    def primary_color(self) -> "str":
        return "#62BB47"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Microstation</title>
     <path d="M24 .357c-.938.217-3.086.22-3.631 1.15l-.55.922c-1.376
 2.348-4.833 11.069-8.183 11.181-3.35.113 1.762-10.712
 2.27-11.797-2.08.489-4.078.193-4.826 2.326-.775 2.212-1.54
 4.425-2.363 6.62-1.71 4.532-3.795 8.89-6.634
 12.767.064-.086.127-.171-.083.117 2.111-.422 4.03-.352 5.295-2.253
 1.17-1.759 1.92-3.73 2.712-5.68l.377-.927.303.286c3.017 2.844 5.334 0
 7.697-2.219l.349-.327 1.322 4.977 2.932-3.144a33.47 33.47 0 0
 1-.713-1.342l-.037-.08C18.302 8.742 21.6 3.935 23.861.566Z" />
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
