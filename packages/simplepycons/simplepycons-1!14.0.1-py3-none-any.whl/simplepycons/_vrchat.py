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


class VrchatIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vrchat"

    @property
    def original_file_name(self) -> "str":
        return "vrchat.svg"

    @property
    def title(self) -> "str":
        return "VRChat"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>VRChat</title>
     <path d="M22.732 6.767H1.268A1.27 1.27 0 0 0 0 8.035v5.296c0
 .7.57 1.268 1.268 1.268h18.594l1.725 2.22c.215.275.443.415.68.415.153
 0 .296-.06.403-.167.128-.129.193-.308.193-.536l-.002-1.939A1.27 1.27
 0 0 0 24 13.331V8.035c0-.7-.569-1.269-1.268-1.269Zm.8 6.564a.8.8 0 0
 1-.8.801h-.34v.031l.004 2.371c0
 .155-.05.233-.129.233s-.19-.079-.31-.235l-1.866-2.4H1.268a.8.8 0 0
 1-.8-.8V8.064a.8.8 0 0 1 .8-.8h21.464a.8.8 0 0 1 .8.8v5.266ZM4.444
 8.573c-.127 0-.225.041-.254.15l-.877
 3.129-.883-3.128c-.03-.11-.127-.15-.254-.15-.202 0-.473.126-.473.311
 0 .012.005.035.011.058l1.114
 3.63c.058.173.265.254.485.254s.433-.08.484-.254l1.109-3.63c.005-.023.011-.04.011-.058
 0-.179-.27-.312-.473-.312Zm2.925 2.36c.433-.132.757-.49.757-1.153
 0-.918-.612-1.207-1.368-1.207H5.614a.234.234 0 0 0-.242.231v3.752c0
 .156.184.237.374.237s.376-.081.376-.237V11.05h.484l.82
 1.593c.058.115.156.179.26.179.219 0 .467-.203.467-.393a.155.155 0 0
 0-.028-.092l-.756-1.403Zm-.61-.473h-.636V9.231h.635c.375 0
 .618.162.618.618s-.242.612-.618.612Zm10.056.826h1.004l-.502-1.772-.502
 1.772Zm4.684-3.095H9.366a.8.8 0 0 0-.8.8v3.383a.8.8 0 0 0
 .8.8h12.132a.8.8 0 0 0 .8-.8V8.992a.8.8 0 0 0-.8-.801Zm-10.946
 3.977c.525 0 .571-.374.589-.617.011-.179.173-.236.369-.236.26 0
 .38.075.38.369 0 .698-.57 1.142-1.379 1.142-.727
 0-1.327-.357-1.327-1.322v-1.61c0-.963.606-1.322 1.333-1.322.802 0
 1.374.427 1.374 1.097 0 .3-.121.37-.375.37-.214
 0-.37-.064-.375-.238-.012-.178-.052-.57-.6-.57-.387
 0-.606.213-.606.663v1.61c0 .45.219.664.617.664Zm4.703.388c0
 .156-.19.237-.375.237s-.375-.081-.375-.237V10.9h-1.299v1.656c0
 .156-.19.237-.375.237s-.375-.081-.375-.237V8.804c0-.161.185-.23.375-.23s.375.069.375.23v1.507h1.299V8.804c0-.161.185-.23.375-.23s.375.069.375.23v3.752Zm3.198.236c-.127
 0-.225-.04-.254-.15l-.22-.768h-1.322l-.219.768c-.029.11-.127.15-.254.15-.202
 0-.473-.127-.473-.311
 0-.012.006-.035.012-.058l1.114-3.63c.051-.173.265-.254.478-.254s.433.08.485.254l1.114
 3.63c.006.023.012.04.012.058 0
 .179-.272.311-.473.311Zm2.989-3.543h-.843v3.306c0
 .156-.19.237-.375.237s-.375-.081-.375-.237V9.25h-.848c-.15
 0-.237-.157-.237-.34 0-.162.075-.336.237-.336h2.44c.162 0
 .238.173.238.335 0 .18-.087.34-.237.34Z" />
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
