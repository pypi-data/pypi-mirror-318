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


class FishShellIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fishshell"

    @property
    def original_file_name(self) -> "str":
        return "fishshell.svg"

    @property
    def title(self) -> "str":
        return "fish shell"

    @property
    def primary_color(self) -> "str":
        return "#34C534"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>fish shell</title>
     <path d="m19.164 9.228-3.016 2.688v.527l3.016
 2.688v-1.228l-1.936-1.723 1.936-1.724V9.228m-6.658.046v1.208l1.905
 1.696-1.905 1.695v1.209l2.968-2.645v-.518l-2.968-2.645M9.781
 7.847a6.519 6.519 0 0 0-2.038-.335c-.672 0-1.349.112-2.03.335a9.23
 9.23 0 0 0-2.088 1.017v.723c.69-.4 1.377-.7 2.06-.897a7.388 7.388 0 0
 1 2.058-.296c.684 0 1.368.098 2.052.296a9.452 9.452 0 0 1
 2.075.897v-.723a9.229 9.229 0 0 0-2.09-1.017m.014 7.78a7.371 7.371 0
 0 1-2.052.296 7.388 7.388 0 0 1-2.057-.296 9.18 9.18 0 0
 1-2.061-.897v.723a9.228 9.228 0 0 0 2.088 1.017 6.492 6.492 0 0 0
 2.03.335c.678 0 1.357-.112 2.038-.335a9.227 9.227 0 0 0
 2.089-1.017v-.723c-.7.4-1.391.7-2.075.897m.602-11.23h-.51L7.28
 6.92h1.19l1.672-1.62 1.671 1.62h1.191l-2.607-2.525m-2.965
 13.68v-.824H6.427v.825l.786 1.527h.614l-.395-1.527M4.127
 10.95v1.216H5.13V10.95H4.127m-1.16-1.695L0 11.901v.518l2.967
 2.645v-1.208L1.063 12.16l1.904-1.695V9.256m20.68
 3.28c-.235-.3-.574-.509-1.017-.626.395-.103.696-.278.902-.525.206-.247.31-.556.31-.926
 0-.546-.197-.984-.59-1.314-.393-.33-.919-.495-1.575-.495-.22
 0-.473.025-.758.073-.284.048-.61.12-.974.217v.84c.314-.12.613-.21.9-.27a4.05
 4.05 0 0 1 .832-.091c.403 0 .714.093.933.278.218.185.328.451.328.798
 0
 .328-.118.584-.353.768-.235.184-.562.276-.98.276h-.697v.75h.696c.458
 0 .821.116 1.09.346.268.23.402.542.402.934 0
 .425-.134.75-.402.976-.269.226-.653.339-1.153.339a3.55 3.55 0 0
 1-.89-.117 4.395 4.395 0 0 1-.91-.358v.909a6.1 6.1 0 0 0
 .95.249c.323.057.639.085.95.085.738 0 1.315-.177
 1.733-.53.417-.355.626-.842.626-1.463 0-.449-.118-.823-.353-1.123" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/fish-shell/fish-site/blob/'''

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
