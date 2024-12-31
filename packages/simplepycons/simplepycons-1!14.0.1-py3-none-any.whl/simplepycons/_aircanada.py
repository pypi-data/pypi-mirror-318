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


class AirCanadaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "aircanada"

    @property
    def original_file_name(self) -> "str":
        return "aircanada.svg"

    @property
    def title(self) -> "str":
        return "Air Canada"

    @property
    def primary_color(self) -> "str":
        return "#F01428"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Air Canada</title>
     <path d="M12.394 16.958c0-.789.338-.902 1.127-.451a54.235 54.235
 0 0 0 2.704 1.465c0-.45.451-.789 1.24-.564.789.226 1.577.338
 1.577.338s-.45-1.014-.676-1.464c-.338-.789 0-1.24.338-1.352 0
 0-.45-.338-.789-.564-.676-.45-.563-1.014.113-1.24.902-.45 2.141-.9
 2.141-.9-.338-.226-.789-.79-.338-1.578.45-.676 1.24-1.69
 1.24-1.69H18.93c-.79 0-1.015-.676-1.015-1.127 0 0-1.239.901-2.14
 1.465-.79.563-1.465 0-1.352-.902a37 37 0 0 0
 .338-2.93c-.451.451-1.24.339-1.69-.337-.564-1.127-1.127-2.48-1.127-2.48S11.38
 4 10.817 5.128c-.338.676-1.127.788-1.578.45a37 37 0 0 0 .338
 2.93c.113.789-.563 1.352-1.352.789-.901-.564-2.253-1.465-2.253-1.465
 0 .45-.226 1.014-1.014 1.127H2.817s.789 1.014 1.24 1.69c.45.676 0
 1.352-.339 1.577 0 0 1.127.564 2.141.902.676.338.902.788.113
 1.24-.226.225-.789.563-.789.563.45.112.789.563.45 1.352-.225.45-.675
 1.464-.675 1.464s.788-.225 1.577-.338c.789-.225 1.127.226 1.24.564 0
 0 1.352-.789 2.704-1.465.676-.45 1.127-.225 1.127.45v1.916c0
 1.127-.226 2.254-.564 2.93-5.07-.564-9.352-4.62-9.352-10.028 0-5.521
 4.62-10.029 10.366-10.029 5.747 0 10.367 4.508 10.367 10.029 0
 5.183-4.057 9.464-9.24 10.028v1.352C19.268 22.592 24 17.746 24 11.775
 24 5.352 18.592.282 11.944.282 5.408.282 0 5.352 0 11.662c0 5.521
 4.169 10.14 9.69 11.155.902.225 1.465.338
 2.028.901.564-1.126.676-3.38.676-4.62Z" />
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
