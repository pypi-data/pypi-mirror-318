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


class ZingatIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zingat"

    @property
    def original_file_name(self) -> "str":
        return "zingat.svg"

    @property
    def title(self) -> "str":
        return "Zingat"

    @property
    def primary_color(self) -> "str":
        return "#009CFB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zingat</title>
     <path d="M11.995 24c-.232-.287-.46-.57-.687-.856a82.547 82.547 0
 0 1-4.373-6.027 38.926 38.926 0 0
 1-2.498-4.335c-.44-.88-.792-1.801-1.052-2.749a6.21 6.21 0 0
 1-.159-2.168 8.381 8.381 0 0 1 1.85-4.557A8.71 8.71 0 0 1
 9.906.249a8.593 8.593 0 0 1 2.365-.243c1.955.07 3.715.693 5.251
 1.909a8.503 8.503 0 0 1 2.944 4.336c.25.831.364 1.696.337 2.562a6.695
 6.695 0 0 1-.376 1.856c-.385 1.179-.919 2.29-1.517
 3.374-.302.551-.624 1.088-.938 1.628a1.055 1.055 0 0
 1-.035.056.987.987 0 0 1-.904.604.985.985 0 0 1-.97-.83 1.25 1.25 0 0
 1-.016-.202v-4.832a.295.295 0 0
 0-.135-.275c-.526-.39-1.044-.792-1.564-1.189l-2.269-1.734a.103.103 0
 0 0-.143-.006l-.006.006-3.825 2.92a.981.981 0 0
 1-1.23-1.53l.025-.018c.184-.144.368-.288.562-.428a.168.168 0 0 0
 .076-.152V5.737a.986.986 0 0 1 .95-1.23c.534 0
 .976.437.981.971.022.086.034.174.035.263l-.001.915
 1.274-.972c.211-.162.421-.325.633-.486a.966.966 0 0 1
 1.168-.007c1.619 1.227 3.239 2.457 4.858
 3.688.143.104.275.222.394.352a.84.84 0 0 1
 .184.561v1.647c.157-.35.303-.704.437-1.065.124-.309.226-.626.304-.95.11-.486.093-.983.048-1.477a4.853
 4.853 0 0 0-.086-.678 6.854 6.854 0 0 0-.276-.884 6.776 6.776 0 0
 0-.926-1.71c-.954-1.237-2.208-2.045-3.694-2.494a4.382 4.382 0 0
 0-.944-.164c-.45-.028-.9-.038-1.35-.031-.873
 0-1.681.259-2.469.62a6.946 6.946 0 0 0-2.649 2.166c-.393.517-.656
 1.108-.901 1.713a5.154 5.154 0 0 0-.329 1.642c-.028.452-.037.904.069
 1.344.089.342.201.678.334 1.005.538 1.392 1.244 2.701 2.008
 3.98a64.18 64.18 0 0 0 4.378
 6.355c.187-.159.342-.352.488-.552.552-.751 1.101-1.502
 1.648-2.256.174-.241.368-.449.675-.527a.976.976 0 0 1 1.196.804 1 1 0
 0 1-.211.754c-.778 1.058-1.55 2.12-2.339 3.168-.441.586-.908
 1.152-1.364 1.725l-.066.073Zm.027-13.788h.81a1.03 1.03 0 0 1 1.018
 1.022v1.621c0 .56-.461 1.021-1.021 1.021h-1.607a1.03 1.03 0 0
 1-1.041-1.004v-1.614a1.027 1.027 0 0 1 .997-1.046h.844Zm.869
 1.837v-.778c0-.074-.026-.104-.101-.104h-1.54c-.082
 0-.105.032-.105.11v1.525c0 .08.027.109.107.109h1.528c.086 0
 .113-.033.112-.117-.009-.242 0-.492 0-.74l-.002-.005h.001Z" />
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
