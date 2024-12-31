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


class PocketIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pocket"

    @property
    def original_file_name(self) -> "str":
        return "pocket.svg"

    @property
    def title(self) -> "str":
        return "Pocket"

    @property
    def primary_color(self) -> "str":
        return "#EF3F56"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pocket</title>
     <path d="M18.813 10.259l-5.646
 5.419c-.32.305-.73.458-1.141.458-.41
 0-.821-.153-1.141-.458l-5.646-5.419c-.657-.628-.677-1.671-.049-2.326.63-.657
 1.671-.679 2.325-.05l4.511 4.322 4.517-4.322c.66-.631 1.697-.607
 2.326.049.631.645.615 1.695-.045
 2.326l-.011.001zm5.083-7.546c-.299-.858-1.125-1.436-2.041-1.436H2.179c-.9
 0-1.717.564-2.037 1.405-.094.25-.142.511-.142.774v7.245l.084
 1.441c.348 3.277 2.047 6.142 4.682
 8.139.045.036.094.07.143.105l.03.023c1.411 1.03 2.989 1.728 4.694
 2.072.786.158 1.591.24 2.389.24.739 0 1.481-.067
 2.209-.204.088-.029.176-.045.264-.06.023 0 .049-.015.074-.029
 1.633-.36 3.148-1.036 4.508-2.025l.029-.031.135-.105c2.627-1.995
 4.324-4.862 4.686-8.148L24
 10.678V3.445c0-.251-.031-.5-.121-.742l.017.01z" />
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
