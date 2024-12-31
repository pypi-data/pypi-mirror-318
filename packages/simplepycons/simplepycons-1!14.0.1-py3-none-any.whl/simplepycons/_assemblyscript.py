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


class AssemblyscriptIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "assemblyscript"

    @property
    def original_file_name(self) -> "str":
        return "assemblyscript.svg"

    @property
    def title(self) -> "str":
        return "AssemblyScript"

    @property
    def primary_color(self) -> "str":
        return "#007AAC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AssemblyScript</title>
     <path d="M0 0v24h24V0h-9.225c0 1.406-1.04 2.813-2.756 2.813A2.766
 2.766 0 019.234 0zm18.204 10.947c.707 0 1.314.137
 1.82.412.517.264.96.717 1.33 1.361l-1.726
 1.108c-.19-.338-.395-.58-.617-.728a1.422 1.422 0 00-.807-.222c-.327
 0-.586.09-.776.27a.896.896 0 00-.285.68c0
 .337.106.596.317.775.222.17.57.36 1.045.57l.554.238c.474.2.891.411
 1.25.633.37.21.675.453.918.728.253.264.443.57.57.918.137.337.206.738.206
 1.203a3 3 0 01-.285 1.33c-.18.38-.433.701-.76.965a3.419 3.419 0
 01-1.171.601c-.443.127-.929.19-1.456.19a5.31 5.31 0 01-1.41-.174
 4.624 4.624 0 01-1.139-.475 3.922 3.922 0 01-.886-.712 4.48 4.48 0
 01-.602-.902L16.1 18.67c.242.39.527.712.855.966.337.253.78.38
 1.33.38.463 0 .827-.1 1.091-.301.275-.211.412-.475.412-.792
 0-.38-.143-.664-.428-.854-.285-.19-.68-.396-1.187-.618l-.554-.237a8.12
 8.12 0 01-1.092-.554 3.64 3.64 0 01-.839-.696 2.887 2.887 0
 01-.538-.903 3.375 3.375 0
 01-.19-1.187c0-.411.074-.796.222-1.155a2.91 2.91 0
 01.649-.934c.285-.264.628-.47 1.029-.617.4-.148.849-.222
 1.345-.222zm-8.796.032h.19l4.922
 10.858h-2.327l-.506-1.219H7.318l-.506 1.219H4.675zm.063 3.988a22.21
 22.21 0 01-.206.697l-.205.649a6.979 6.979 0 01-.222.585l-.776
 1.868h2.834l-.776-1.868a15.492 15.492 0 01-.237-.633 23.741 23.741 0
 01-.412-1.298z" />
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
