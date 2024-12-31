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


class RedashIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "redash"

    @property
    def original_file_name(self) -> "str":
        return "redash.svg"

    @property
    def title(self) -> "str":
        return "Redash"

    @property
    def primary_color(self) -> "str":
        return "#FF7964"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Redash</title>
     <path d="M12 0C6.775 0 2.546 4.238 2.546 9.455c0 4.971 3.842 9.05
 8.727 9.423V24c3.405-3.49 5.837-6.072 7.307-7.756a9.5 9.5 0 0 0
 1.532-1.93l.005-.006q.003-.007.007-.014a9.4 9.4 0 0 0
 1.33-4.84C21.455 4.238 17.226 0 12 0m3.821
 5.818h1.385c.337.001.611.25.612.558v6.157c-.001.308-.275.557-.612.558H15.82c-.337-.001-.611-.25-.612-.558V6.376c0-.307.275-.557.612-.558M9.297
 7.921h1.386c.338 0
 .611.25.613.558v4.054c-.002.308-.275.557-.613.558H9.297c-.337-.001-.61-.25-.61-.558V8.479c0-.308.273-.558.61-.558m3.222
 1.534h1.396c.337 0 .61.25.61.558v2.52c0
 .308-.273.557-.61.558h-1.396c-.338-.001-.612-.25-.613-.558v-2.52c.001-.308.275-.558.613-.558M6.067
 10.71h1.396c.337.001.61.25.61.559v1.264c0
 .308-.273.557-.61.558H6.067c-.338-.001-.611-.25-.612-.558v-1.264c0-.308.274-.558.612-.559"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/getredash/website/blob/c45
4b523fdaa60218845313904c5498cda7e7b7a/static/assets/images/elements/re'''

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
