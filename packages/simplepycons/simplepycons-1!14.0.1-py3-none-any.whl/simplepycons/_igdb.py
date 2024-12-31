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


class IgdbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "igdb"

    @property
    def original_file_name(self) -> "str":
        return "igdb.svg"

    @property
    def title(self) -> "str":
        return "IGDB"

    @property
    def primary_color(self) -> "str":
        return "#9147FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>IGDB</title>
     <path d="M24 6.228c-8 .002-16 0-24 0v11.543a88.875 88.875 0 0 1
 2.271-.333 74.051 74.051 0 0 1 17.038-.28c1.57.153 3.134.363
 4.69.614V6.228zm-.706.707v10.013a74.747 74.747 0 0 0-22.588
 0V6.934h22.588ZM7.729 8.84a2.624 2.624 0 0 0-1.857.72 2.55 2.55 0 0
 0-.73 1.33c-.098.5-.063 1.03.112 1.51.177.488.515.917.954
 1.196.547.354 1.224.472 1.865.401a3.242 3.242 0 0 0
 1.786-.777c-.003-.724.002-1.449-.002-2.173-.725.004-1.45-.002-2.174.003.003.317
 0 .634.001.951h1.105c.002.236 0
 .473.002.71-.268.196-.603.286-.932.298-.32.02-.65-.05-.922-.225a1.464
 1.464 0 0 1-.59-.744c-.18-.499-.134-1.085.163-1.53.23-.355.619-.61
 1.043-.647a1.8 1.8 0 0 1
 1.012.206c.152.082.286.192.424.295.228-.281.461-.559.692-.838a3.033
 3.033 0 0
 0-.595-.403c-.418-.212-.892-.285-1.357-.283Zm11.66.086c-.093
 0-.187.002-.28 0-.68.002-1.359-.004-2.038.003.003 1.666 0 3.332.002
 4.998h2.497c.239-.002.478-.034.709-.097.276-.076.546-.208.742-.422.194-.208.297-.492.304-.776.016-.278-.032-.572-.195-.804-.175-.252-.453-.408-.734-.514.211-.122.407-.285.521-.505.134-.246.149-.535.117-.807a1.156
 1.156 0 0 0-.436-.73c-.264-.207-.599-.304-.93-.334a2.757 2.757 0 0
 0-.279-.012Zm-16.715 0v5.002h1.102V8.927c-.368-.002-.735 0-1.102
 0zm8.524 0v5.002h2.016a2.87 2.87 0 0 0 1.07-.211 2.445 2.445 0 0 0
 1.174-.993c.34-.555.429-1.244.292-1.876a2.367 2.367 0 0
 0-.828-1.338c-.478-.387-1.096-.577-1.707-.584h-2.017zm6.949.967c.392.002.784-.001
 1.176.002.183.011.38.054.51.19.11.112.136.28.112.43a.436.436 0 0
 1-.22.316 1.082 1.082 0 0
 1-.483.116c-.365.002-.73-.001-1.094.001-.002-.351
 0-.703-.001-1.054zm-5.031.026c.28 0
 .567.053.815.19.274.149.491.396.607.685.113.272.138.574.107.865a1.456
 1.456 0 0 1-.335.786 1.425 1.425 0 0
 1-.865.466c-.168.031-.34.022-.51.023h-.632V9.92h.813zm5.03
 1.948h1.36c.174.006.354.035.505.127.11.066.191.18.212.308.025.15.004.32-.099.44-.102.12-.258.176-.409.2-.172.032-.348.02-.522.022-.35-.001-.698.002-1.047-.001v-1.096z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:IGDB_'''

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
