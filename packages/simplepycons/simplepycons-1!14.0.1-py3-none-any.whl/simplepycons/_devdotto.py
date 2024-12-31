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


class DevdottoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "devdotto"

    @property
    def original_file_name(self) -> "str":
        return "devdotto.svg"

    @property
    def title(self) -> "str":
        return "dev.to"

    @property
    def primary_color(self) -> "str":
        return "#0A0A0A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>dev.to</title>
     <path d="M7.42 10.05c-.18-.16-.46-.23-.84-.23H6l.02 2.44.04
 2.45.56-.02c.41 0 .63-.07.83-.26.24-.24.26-.36.26-2.2
 0-1.91-.02-1.96-.29-2.18zM0 4.94v14.12h24V4.94H0zM8.56
 15.3c-.44.58-1.06.77-2.53.77H4.71V8.53h1.4c1.67 0 2.16.18
 2.6.9.27.43.29.6.32 2.57.05 2.23-.02 2.73-.47
 3.3zm5.09-5.47h-2.47v1.77h1.52v1.28l-.72.04-.75.03v1.77l1.22.03
 1.2.04v1.28h-1.6c-1.53
 0-1.6-.01-1.87-.3l-.3-.28v-3.16c0-3.02.01-3.18.25-3.48.23-.31.25-.31
 1.88-.31h1.64v1.3zm4.68 5.45c-.17.43-.64.79-1 .79-.18
 0-.45-.15-.67-.39-.32-.32-.45-.63-.82-2.08l-.9-3.39-.45-1.67h.76c.4 0
 .75.02.75.05 0 .06 1.16 4.54 1.26
 4.83.04.15.32-.7.73-2.3l.66-2.52.74-.04c.4-.02.73 0 .73.04 0 .14-1.67
 6.38-1.8 6.68z" />
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
