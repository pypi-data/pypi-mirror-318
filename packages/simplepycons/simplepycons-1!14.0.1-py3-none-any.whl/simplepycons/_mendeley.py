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


class MendeleyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mendeley"

    @property
    def original_file_name(self) -> "str":
        return "mendeley.svg"

    @property
    def title(self) -> "str":
        return "Mendeley"

    @property
    def primary_color(self) -> "str":
        return "#9D1620"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mendeley</title>
     <path d="M12.0037 9.1684h.019a2.355 2.355 0 011.5038 4.1655
 1.8076 1.8076 0 01-.8561.452 2.348 2.348 0 01-.6487.0923h-.019c-.2246
 0-.4421-.033-.6487-.0922a1.8126 1.8126 0 01-.8561-.4521 2.346 2.346 0
 01-.8511-1.8106 2.358 2.358 0 012.3569-2.355m-9.9731
 9.474c1.2652.1583 2.388-.762 2.5073-2.0573a2.4442 2.4442 0
 00-.2136-1.236c-1.7724-3.8889 6.9726-3.978
 5.4949-.3078l-.01.016c-.6988 1.1178-.3198 2.5695.841
 3.2402.4272.2486.9003.3508 1.3625.3308.4622.02.9354-.0822
 1.3624-.3308 1.161-.6717
 1.54-2.1224.8412-3.2402l-.01-.016c-1.4778-3.6703 7.2682-3.581
 5.4938.3077a2.4462 2.4462 0 00-.2126 1.2361c.1203 1.2953 1.2422
 2.2156 2.5083 2.0572a2.345 2.345 0
 001.4246-.7368s.5885-.4883.5795-1.7334c-.008-1.0156-.5795-1.578-.5795-1.578a2.2116
 2.2116 0
 00-1.8145-.6456c-1.6231-.036-1.8637-1.3073-1.4056-3.7033.1685-.4251.2416-.8802.2266-1.3354a3.4166
 3.4166 0 00-2.1304-3.2953c-.039-.017-.0782-.03-.1183-.0461a1.5138
 1.5138 0 00-.1343-.0461 3.4156 3.4156 0 00-4.004
 1.4526c-.8171.8973-1.187 1.4417-2.0272 1.4417-.799
 0-1.211-.5444-2.0271-1.4417a3.4126 3.4126 0
 00-4.1374-1.4075c-.0401.016-.0792.029-.1193.0461a3.4156 3.4156 0
 00-2.1294 3.2953c-.016.4552.0582.9103.2256 1.3354.4581 2.397.2175
 3.6672-1.4045
 3.7033-.795-.0852-1.3885.2426-1.988.8431-.6016.5995-.5514 2.2056 0
 2.9063.4.5103.9423.8632 1.598.9454" />
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
