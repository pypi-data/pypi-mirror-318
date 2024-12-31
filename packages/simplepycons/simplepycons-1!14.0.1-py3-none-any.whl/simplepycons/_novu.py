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


class NovuIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "novu"

    @property
    def original_file_name(self) -> "str":
        return "novu.svg"

    @property
    def title(self) -> "str":
        return "Novu"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Novu</title>
     <path d="M18.48 9.6193c0
 .6452-.7834.9647-1.2347.5035L8.0067.6804C9.256.2398 10.6 0 12 0c2.387
 0 4.611.6969 6.48 1.8983zm3.36-4.4895v4.4895c0 3.6564-4.4392
 5.4669-6.9962 2.8534L4.9087 2.3185C1.9323 4.5022 0 8.0255 0 12c0
 2.5553.7987 4.924 2.16 6.8701v-4.4654c0-3.6564 4.4392-5.4669
 6.9963-2.8534l9.9214 10.1403C22.0617 19.5086 24 15.9806 24
 12c0-2.5553-.7987-4.924-2.16-6.8702ZM6.7546 13.9012l9.2212
 9.4245C14.7316 23.7625 13.3934 24 12 24c-2.3869
 0-4.611-.6968-6.48-1.8983v-7.697c0-.6453.7834-.9647 1.2346-.5035z" />
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
