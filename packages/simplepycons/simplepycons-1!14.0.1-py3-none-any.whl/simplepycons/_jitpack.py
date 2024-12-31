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


class JitpackIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jitpack"

    @property
    def original_file_name(self) -> "str":
        return "jitpack.svg"

    @property
    def title(self) -> "str":
        return "JitPack"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>JitPack</title>
     <path d="M15.191 0c-2.03.393-3.466 1.199-4.325 2.318l2.883
 1.664a2.81 2.81 0 0 1
 1.882-.194c.181-1.091.048-2.358-.44-3.788Zm-4.94 3.06L5.83
 10.715l4.734 2.736
 1.113-1.925c-.505-.498-.716-1.256-.742-2.045-.032-.966.202-2.039.638-3.01.324-.72.759-1.387
 1.308-1.892L10.252 3.06h-.001Zm10.498.15c-1.494.289-2.665.803-3.522
 1.499a2.82 2.82 0 0 1 .777 1.731l2.874
 1.658c.543-1.305.533-2.948-.129-4.888Zm-18.361.409L.459 6.961l5.186
 2.173L8.737 3.78l-6.349-.161Zm12.539
 1.016c-.332.005-.64.115-.943.297-.608.364-1.163 1.085-1.543
 1.929-.38.844-.584 1.805-.558 2.588.026.782.271 1.325.652
 1.546h.001c.382.219.974.16 1.664-.208.69-.369 1.421-1.026
 1.962-1.776.541-.751.887-1.594.899-2.303.013-.708-.238-1.283-1.042-1.747-.402-.233-.759-.331-1.091-.326h-.001Zm2.991
 2.853c-.163.728-.524 1.438-.985 2.079-.623.863-1.433 1.602-2.285
 2.057-.699.373-1.464.57-2.15.378l-1.111 1.923 4.735 2.734
 4.419-7.656-2.623-1.515Zm2.756 3.185-3.09 5.356 4.476 3.406
 1.929-3.343-3.315-5.419Zm-14.066 1.59c-1.143.5-2.02 1.177-2.634
 2l4.449 2.57c.408-.945.561-2.039.432-3.272l-2.247-1.298Zm-3.055
 2.855-3.542
 6.13v1.899l4.365-7.554-.823-.475Zm8.613.354c-1.143.501-2.02
 1.177-2.634 2.001l4.449
 2.569c.409-.945.562-2.04.432-3.273l-2.247-1.296v-.001Zm-6.869.653L.722
 24h1.099l4.301-7.398-.825-.476v-.001Zm1.751 1.011L3.094
 24H4.19l3.68-6.389-.822-.475Zm2.077 1.2L5.911
 24h1.093l2.944-5.189-.823-.475Zm1.751 1.012L8.28
 24h1.086l2.333-4.179-.823-.473Zm1.751 1.01L10.647
 24h1.084l1.72-3.167-.824-.475Z" />
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
