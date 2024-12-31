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


class SncfIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sncf"

    @property
    def original_file_name(self) -> "str":
        return "sncf.svg"

    @property
    def title(self) -> "str":
        return "SNCF"

    @property
    def primary_color(self) -> "str":
        return "#CA0939"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SNCF</title>
     <path d="M2.093 5.76c4.628 0 14.881.633 21.698
 4.934.21.135.25.27.173.519-.039.115-2.151 6.74-2.151
 6.74-.096.287-.25.287-.423.287H.384c-.25
 0-.384-.172-.384-.384V6.182c0-.25.173-.384.46-.384.423 0 .96-.038
 1.633-.038zm.288 6.355c-.384.941.71 1.517 1.67 1.959.788.345 1.345.71
 1.133 1.113-.134.346-.71.5-1.478.5-.672
 0-1.517-.212-2.19-.519l-.383.845c.5.211 1.478.519 2.342.557 1.594.038
 2.65-.346
 3.073-1.229.426-.976-.575-1.51-1.518-1.963l-.092-.045-.138-.066c-.787-.345-1.305-.557-1.17-.94.133-.461.92-.634
 1.631-.596.346 0
 .595.039.922.135l.25-.807c-.346-.077-.634-.096-1.057-.096-1.42-.038-2.688.346-2.995
 1.152Zm13.595-1.21c-1.344 0-2.554.461-3.284 1.268 0
 .038-.038.038-.077.038-.038 0-.038
 0-.038-.038l.384-1.19h-1.133l-1.267
 3.82c-.384-1.113-1.21-2.63-2.19-3.82H7.163l-.883
 2.803c.442.345.576.595.73.921 0 0 0 .039.038.039 0 0 .038 0 .038-.039
 0-.038.788-2.419.788-2.419a14.506 14.506 0 0 1 2.016
 4.167h1.267l.634-1.997s0-.039.038-.039c0 0 .039 0 .039.039.172 1.229
 1.44 2.074 3.225 2.074 1.133 0 2.19-.308
 2.439-.423l.672-2.112h2.573l.25-.807h-2.612l.461-1.363h3.072l.288-.845h-4.34l-1.44
 4.551c-.326.077-.71.096-1.094.096-.845 0-1.555-.211-1.94-.672a1.467
 1.467 0 0 1-.326-1.267c.173-1.152 1.306-1.901 2.823-1.901.326 0 .634
 0 .96.077l.327-.884c-.346-.076-.807-.076-1.23-.076z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.sncf.com/fr/groupe/marques/sncf/i'''
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
