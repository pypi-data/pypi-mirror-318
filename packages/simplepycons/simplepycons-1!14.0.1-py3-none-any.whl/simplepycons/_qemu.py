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


class QemuIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qemu"

    @property
    def original_file_name(self) -> "str":
        return "qemu.svg"

    @property
    def title(self) -> "str":
        return "QEMU"

    @property
    def primary_color(self) -> "str":
        return "#FF6600"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>QEMU</title>
     <path d="M12.003.064C5.376.064 0 5.407 0 12s5.376 11.936 12.003
 11.936c2.169 0 4.2-.57 5.955-1.57l.624 1.57h4.841l-1.893-4.679A11.845
 11.845 0 0024 12C24 5.407 18.63.064 12.003.064zM8.818
 2.03c.398.339.324.198.86.134.61-.397.893.942 1.147.195.748.097
 1.542.34 2.25.584a3.447 3.447 0 011.859
 1.128l-.014.007.35.463c.045.08.082.164.12.248.142 1.205 1.48 1.19
 2.377 1.625.767.272 1.69.686 1.785
 1.611-.193-.042-.941-.921-1.53-1.007a3.919 3.919 0
 01-1.094-.255L14.86 6.38v-.007a3.035 3.035 0
 01-.309-.053v.013l-2.927-.362c.048.033.1.077.148.12l3
 .585v-.007l.209.053.839.188c.166.016.334.043.47.067.856.236 1.868.194
 2.571.792-.184.352-1.21.153-1.719.108-.062-.012-.131-.023-.194-.034l-.034-.007c-.696-.113-1.411-.12-2.081.088h-.007a3.193
 3.193 0 00-.671.302c-.968.563-2.164.767-2.967 1.577-.787.847-.739
 2.012-.604 3.095h.033v.275c.013.095.028.19.04.282.41 2.19 1.5 4.2
 1.84 6.412.065.843.203 1.932.309
 2.618-.306-.091-.475-1.462-.544-1.007a38.196 38.196 0
 00-3.565-5.25c-.853-1.004-1.697-2.06-2.712-2.894-.685-.528-.468-1.55-.537-2.302-.23-.926-.094-1.848.06-2.773.313-.963.418-1.968.846-2.893.653-.581.669-1.63
 1.303-2.135.094.058.157.085.2.1l.068.008h.007c.09-.095-.888-1.116.02-.712.035-.537.854-.128.866-.597zm3.847
 2.182c-.323.009-.574.13-.645.335-.114.33.273.755.866.96.594.205
 1.168.109 1.282-.221.114-.33-.272-.762-.866-.967a1.842 1.842 0
 00-.637-.107z" />
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
