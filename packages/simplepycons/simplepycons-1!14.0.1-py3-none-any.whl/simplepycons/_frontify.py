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


class FrontifyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "frontify"

    @property
    def original_file_name(self) -> "str":
        return "frontify.svg"

    @property
    def title(self) -> "str":
        return "Frontify"

    @property
    def primary_color(self) -> "str":
        return "#2D3232"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Frontify</title>
     <path d="m23.13 15.777-2.588-1.495a.752.752 0 0
 1-.376-.649v-2.989a1.743 1.743 0 0 0-.872-1.508l-2.588-1.494a.755.755
 0 0 1-.375-.651V4.002a1.748 1.748 0 0 0-.871-1.511L12 .496 8.54
 2.491a1.748 1.748 0 0 0-.868 1.511v2.989a.755.755 0 0 1-.375.65L4.706
 9.137a1.746 1.746 0 0 0-.87 1.508v2.99a.75.75 0 0 1-.375.648l-2.59
 1.495A1.75 1.75 0 0 0 0 17.287v3.989l3.46 1.994a1.74 1.74 0 0 0 1.741
 0l2.589-1.494a.753.753 0 0 1 .75 0l2.589 1.494a1.745 1.745 0 0 0
 1.743 0l2.588-1.494a.753.753 0 0 1 .75 0L18.8 23.27a1.74 1.74 0 0 0
 1.741 0L24 21.276v-3.99a1.75 1.75 0 0 0-.87-1.51ZM15.343
 4.002v2.989a1.748 1.748 0 0 0 .872 1.508l2.588 1.495a.753.753 0 0 1
 .376.65v2.99a1.746 1.746 0 0 0 .87 1.507l2.589 1.495a.752.752 0 0 1
 .375.65v2.85l-10.517-6.07V1.928l2.468 1.425a.75.75 0 0 1
 .38.65zM1.367 16.636l2.589-1.495a1.748 1.748 0 0 0
 .871-1.508v-2.989a.752.752 0 0 1 .374-.65L7.79 8.499a1.748 1.748 0 0
 0 .871-1.508V4.002a.753.753 0 0 1 .375-.649l2.471-1.425v12.138L.993
 20.136v-2.85a.752.752 0 0 1 .374-.65Zm18.677 5.784a.753.753 0 0 1-.75
 0l-2.588-1.494a1.74 1.74 0 0 0-1.742 0l-2.588 1.494a.753.753 0 0
 1-.75 0l-2.589-1.494a1.743 1.743 0 0 0-1.743 0L4.706 22.42a.753.753 0
 0 1-.75 0l-2.468-1.425L12 14.919l10.512 6.07Z" />
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
