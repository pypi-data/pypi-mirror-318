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


class UfcIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ufc"

    @property
    def original_file_name(self) -> "str":
        return "ufc.svg"

    @property
    def title(self) -> "str":
        return "UFC"

    @property
    def primary_color(self) -> "str":
        return "#D20A0A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>UFC</title>
     <path d="M6.308 7.843h2.797s-1.86 6.639-1.951 6.998c-.177.69-.353
 1.316-2.043 1.316-2.037 0-3.22-.007-3.777
 0-.698.007-1.521-.633-1.296-1.464l1.91-6.85H4.8S3.2 13.553 3.166
 13.7c-.029.148-.19.557.698.564.64.014.69-.155.803-.564.268-.922
 1.64-5.857 1.64-5.857zm10.272 0l-.507 1.824H9.986l.507-1.824zm-8.404
 8.314l1.459-5.244h6.086l-.507 1.823h-3.262l-.95
 3.421zm11.47-5.385c-.26.957-.493 1.774-.754
 2.738-.05.17-.162.416-.127.57.078.367 1.29.226
 1.726.226h1.945c-.155.612-.33 1.21-.5
 1.81h-4.63c-.676-.064-1.557-.353-1.472-1.226.028-.274.156-.584.24-.887a1189.7
 1189.7 0 001.24-4.463c.176-.648.317-1.197.83-1.457.333-.17.861-.218
 1.255-.24H24c-.162.606-.331 1.211-.5 1.81h-2.643c-.317
 0-.669-.036-.845.084-.19.141-.295.775-.366 1.035z" />
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
