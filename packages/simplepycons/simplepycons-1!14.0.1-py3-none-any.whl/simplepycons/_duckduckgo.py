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


class DuckduckgoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "duckduckgo"

    @property
    def original_file_name(self) -> "str":
        return "duckduckgo.svg"

    @property
    def title(self) -> "str":
        return "DuckDuckGo"

    @property
    def primary_color(self) -> "str":
        return "#DE5833"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DuckDuckGo</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0zm0 23C5.925 23 1 18.074 1 12S5.926 1 12 1s11
 4.925 11 11-4.925 11-11 11zm10.219-11c0 4.805-3.317 8.833-7.786
 9.925-.27-.521-.53-1.017-.749-1.438.645.249 1.93.718
 2.208.615.376-.144.282-3.149-.14-3.245-.338-.075-1.632.837-2.141
 1.209l.034.156c.078.397.144.993.03
 1.247-.001.004-.002.01-.004.013a.218.218 0 0
 1-.068.088c-.284.188-1.081.284-1.503.188a.516.516 0 0
 1-.064-.02c-.694.396-2.01
 1.109-2.25.971-.329-.188-.377-2.676-.329-3.288.035-.46 1.653.286
 2.442.679.174-.163.602-.272.98-.31-.57-1.389-.99-2.977-.733-4.105 0
 .002.002.002.002.002.356.248 2.73 1.05 3.91 1.027 1.18-.024
 3.114-.743
 2.903-1.323-.212-.58-2.135.51-4.142.324-1.486-.138-1.748-.804-1.42-1.29.414-.611
 1.168.116 2.411-.256 1.245-.371 2.987-1.035 3.632-1.397
 1.494-.833-.625-1.177-1.125-.947-.474.22-2.123.637-2.889.82.428-1.516-.603-4.149-1.757-5.3-.376-.376-.951-.612-1.603-.736-.25-.344-.654-.671-1.225-.977a5.772
 5.772 0 0
 0-3.595-.584l-.024.004-.034.004.004.002c-.148.028-.237.08-.357.098.148.016.705.276
 1.057.418-.174.068-.412.108-.596.184a.828.828 0 0
 0-.204.056c-.173.08-.303.375-.3.515.84-.086 2.082-.026
 2.991.246-.644.09-1.235.258-1.661.482-.016.008-.03.018-.048.028-.054.02-.106.042-.152.066-1.367.72-1.971
 2.405-1.611 4.424.323 1.824 1.665 8.088 2.29
 11.064-3.973-1.4-6.822-5.186-6.822-9.639C1.781 6.356 6.356 1.781 12
 1.781S22.219 6.356 22.219 12zM9.095 9.581a.758.758 0 1 0 0
 1.516.758.758 0 0 0 0-1.516zm.338.702a.196.196 0 1 1 0-.392.196.196 0
 0 1 0 .392zm4.724-1.043a.65.65 0 1 0 0 1.299.65.65 0 0 0
 0-1.3zm.29.601a.168.168 0 1 1 0-.336.168.168 0 0 1 0 .336zM9.313
 8.146s-.571-.26-1.125.09c-.554.348-.534.704-.534.704s-.294-.656.49-.978c.786-.32
 1.17.184
 1.17.184zm5.236-.052s-.41-.234-.73-.23c-.654.008-.831.296-.831.296s.11-.688.945-.55a.84.84
 0 0 1 .616.484z" />
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
