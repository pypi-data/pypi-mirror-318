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


class DeltaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "delta"

    @property
    def original_file_name(self) -> "str":
        return "delta.svg"

    @property
    def title(self) -> "str":
        return "Delta"

    @property
    def primary_color(self) -> "str":
        return "#003366"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Delta</title>
     <path d="M24
 13.455h-.689l-.288-.739h-1.2l-.289.739h-.644l1.233-2.96h.666zm-1.16-1.233l-.411-1.044-.411
 1.044zm-4.315 1.233h.66v-2.438h.995v-.51h-2.644v.51h.989zm-3.826
 0h1.927v-.511H15.36v-2.438h-.661zm-3.282-2.438h1.416v-.51h-2.077v2.948h2.121v-.511h-1.46v-.766h1.25v-.511h-1.25zm-4.981
 2.438h1.038c1.072 0 1.71-.555 1.71-1.472
 0-.916-.638-1.471-1.71-1.471H6.436zm.655-2.438h.383c.694 0 1.044.344
 1.044.96 0 .617-.344.961-1.044.961h-.383zm-2.277 2.155a.15.15 0 0 1
 .15.15.15.15 0 0 1-.15.15.15.15 0 0 1-.15-.15.15.15 0 0 1 .15-.15m0
 .277a.13.13 0 0 0 .134-.127c0-.073-.056-.128-.134-.128a.126.126 0 0
 0-.127.128c0 .072.055.127.127.127m-.033-.039H4.76v-.177h.067c.038 0
 .055.016.055.05 0
 .033-.022.044-.044.05l.055.077h-.028l-.05-.077h-.033zm0-.1h.028c.022
 0 .05 0 .05-.027 0-.022-.022-.028-.039-.028h-.039zM0
 13.85h4.626l-2.31-.978zm.172-.395l2.144-1.033 2.143
 1.033-2.143-3.304Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://news.delta.com/delta-air-lines-logos-'''

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
