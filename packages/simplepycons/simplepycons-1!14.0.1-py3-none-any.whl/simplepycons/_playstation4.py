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


class PlaystationFourIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "playstation4"

    @property
    def original_file_name(self) -> "str":
        return "playstation4.svg"

    @property
    def title(self) -> "str":
        return "PlayStation 4"

    @property
    def primary_color(self) -> "str":
        return "#003791"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PlayStation 4</title>
     <path d="M12.302 13.18v-2.387c0-.486.227-.834.712-.834h2.99c.017
 0 .035-.018.035-.036v-.475c0-.004
 0-.008-.003-.012h-3.66c-.792.1-1.18.653-1.18 1.357v2.386c0
 .482-.233.831-.71.831H7.332c-.018 0-.036.012-.036.036v.475c0
 .02.01.035.023.04h3.584c.933-.025 1.393-.62 1.393-1.385zM.024
 14.564h1.05a.042.042 0
 00.025-.04v-1.52c0-.487.275-.823.676-.823h4.323c.974 0 1.445-.6
 1.445-1.384 0-.705-.386-1.257-1.18-1.357H.006c0
 .003-.006.005-.006.01v.475c0 .024.013.036.037.036h5.697c.484 0
 .712.35.712.833 0 .484-.227.836-.712.836H1.226c-.7 0-1.226.592-1.226
 1.373v1.519c0 .02.01.036.028.04zm15.998-.55h5.738c.017 0
 .03.012.03.024v.483c0 .024.017.036.035.036h1.035c.018 0
 .036-.01.036-.036v-.475c0-.018.02-.036.04-.036h1.028c.024 0
 .036-.018.036-.036v-.484c0-.018-.01-.036-.035-.036h-1.03c-.02
 0-.037-.017-.037-.035V9.96c0-.283-.104-.463-.28-.523h-.3a1.153 1.153
 0 00-.303.132l-6.18
 3.815c-.24.15-.323.318-.263.445.048.104.185.182.454.182zm.895-.637l4.79-2.961c.03-.024.09-.018.09.048v2.961c0
 .018-.016.036-.034.036h-4.817c-.04
 0-.06-.012-.065-.024-.006-.024.005-.042.036-.06z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:PlayS'''

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
