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


class DlibIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dlib"

    @property
    def original_file_name(self) -> "str":
        return "dlib.svg"

    @property
    def title(self) -> "str":
        return "Dlib"

    @property
    def primary_color(self) -> "str":
        return "#008000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dlib</title>
     <path
 d="M5.2188.0022c-.5082-.01-1.0158.015-1.5223.046v23.9085c.9724.068
 1.954.055 2.9238-.032.2836-.9399.5742-1.8784.8605-2.8177 1.488-.2455
 2.9172-.7078 4.192-1.361 1.04.5022 2.0797 1.0049 3.12 1.5067a14.2125
 14.2125 0 0 0
 2.0759-1.5805c-.6353-.8301-1.2734-1.6589-1.9098-2.4884.8294-1.02
 1.4426-2.1614 1.7261-3.3565 1.1902-.2287 2.3801-.4583
 3.5705-.6865a10.5282 10.5282 0 0
 0-.0302-2.2869c-1.1825-.2277-2.3653-.4548-3.5479-.6824-.2922-1.1939-.8713-2.3444-1.7235-3.3545.6384-.8293
 1.2757-1.6593
 1.9148-2.4884-.6128-.5881-1.297-1.117-2.0432-1.5984-1.0537.5102-2.1086
 1.019-3.1628 1.5285-1.2667-.6671-2.6973-1.1432-4.187-1.3868C7.1875
 1.9292 6.898.987 6.6103.0442c-.463-.028-.927-.049-1.3914-.042Zm2.33
 5.388c3.6866.8142 6.464 3.7461 6.2778 6.8008-.0934 2.8969-2.6816
 5.6581-6.2426
 6.3976-.1694-.2268-.0253-.7803-.0734-1.1335-.002-4.0243-.003-8.0486-.005-12.073l.0428.01z"
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
        return '''https://github.com/davisking/dlib/blob/8a2c74'''

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
