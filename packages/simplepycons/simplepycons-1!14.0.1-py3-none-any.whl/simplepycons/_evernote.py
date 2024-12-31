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


class EvernoteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "evernote"

    @property
    def original_file_name(self) -> "str":
        return "evernote.svg"

    @property
    def title(self) -> "str":
        return "Evernote"

    @property
    def primary_color(self) -> "str":
        return "#00A82D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Evernote</title>
     <path d="M8.222 5.393c0
 .239-.02.637-.256.895-.257.24-.652.259-.888.259H4.552c-.73 0-1.165
 0-1.46.04-.159.02-.356.1-.455.14-.04.019-.04
 0-.02-.02L8.38.796c.02-.02.04-.02.02.02-.04.099-.118.298-.138.457-.04.298-.04.736-.04
 1.472v2.647zm5.348 17.869c-.67-.438-1.026-1.015-1.164-1.373a2.924
 2.924 0 01-.217-1.095 3.007 3.007 0 013-3.004c.493 0
 .888.398.888.895a.88.88 0
 01-.454.776c-.099.06-.237.1-.336.12-.098.02-.473.06-.65.218-.198.16-.356.418-.356.697
 0 .298.118.577.316.776.355.358.829.557 1.342.557a2.436 2.436 0
 002.427-2.447c0-1.214-.809-2.29-1.875-2.766-.158-.08-.414-.14-.651-.2a8.04
 8.04 0 00-.592-.1c-.829-.1-2.901-.755-3.04-2.605 0 0-.611 2.785-1.835
 3.54-.118.06-.276.12-.454.16-.177.04-.374.06-.434.06-1.993.12-4.105-.517-5.565-2.03
 0
 0-.987-.815-1.5-3.103-.118-.558-.355-1.553-.493-2.488-.06-.338-.08-.597-.099-.836
 0-.975.592-1.631 1.342-1.73h4.026c.69 0 1.086-.18
 1.342-.42.336-.317.415-.775.415-1.312V1.354C9.05.617 9.703 0 10.669
 0h.474c.197 0 .434.02.651.04.158.02.296.06.533.12 1.204.298 1.46
 1.532 1.46 1.532s2.27.398 3.415.597c1.085.199 3.77.378 4.282 3.104
 1.204 6.487.474 12.775.415 12.775-.849 6.129-5.901 5.83-5.901
 5.83a4.1 4.1 0
 01-2.428-.736zm4.54-13.034c-.652-.06-1.204.2-1.402.697-.04.1-.079.219-.059.278.02.06.06.08.099.1.237.12.631.179
 1.204.239.572.06.967.1 1.223.06.04 0
 .08-.02.119-.08.04-.06.02-.18.02-.28-.06-.536-.553-.934-1.204-1.014z"
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
