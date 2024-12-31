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


class CrewUnitedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "crewunited"

    @property
    def original_file_name(self) -> "str":
        return "crewunited.svg"

    @property
    def title(self) -> "str":
        return "Crew United"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Crew United</title>
     <path d="M11.871 3.9121c-1.1458.046-2.2306.7013-2.7714
 1.8027-.4605.9306-.4404 2.0292.0488
 2.9454-.8955-.524-1.8989-.7774-3.0273-.7774-.2207
 0-.4365.014-.6524.0332-3.3577.3502-5.7885 3.3541-5.4335 6.707.3261
 3.1131 2.9584 5.4716 6.0859
 5.4668l.7148-.043c.2063-.024.4177-.0574.6192-.1054.0336-.0096.068-.0138.1015-.0234.8059-.1967
 1.5686-.5559 2.2305-1.0547l3.5352-2.8496c2.2353 2.523 6.0912 2.7567
 8.6191.5215 2.5279-2.2353 2.7587-6.0913.5234-8.6192a6.1236 6.1236 0 0
 0-4.5722-2.0527c-.3454 0-.6907.0284-1.0313.086L13.422
 4.2323l.0059.0098a3.2322 3.2322 0 0 0-1.5567-.33ZM16.3146 6.75l6.668
 3.2617c1.0792 2.811-.3268 5.9627-3.1329
 7.0371-.6236.2447-1.2903.3653-1.957.3653-1.5494
 0-3.0215-.6565-4.0528-1.8125l1.2852-1.0371c1.0025 1.2567 2.8302
 1.4673 4.0918.4648 1.2615-1.0025
 1.4674-2.8303.4648-4.0918-1.0025-1.2615-2.8302-1.4674-4.0918-.4648a2.9102
 2.9102 0 0 0-.787.9687l-3.2696-1.6113a.6395.6395 0 0
 1-.207-.8828c.1727-.283.5327-.3831.83-.2344l.4415.2148.5937.2891a5.4475
 5.4475 0 0 1 3.123-2.4668Zm.3457 1.2813a4.6724 4.6724 0 0 0-2.4278
 1.209l.6328.3163c.5469-.4652 1.214-.7676 1.9239-.8828ZM6.121
 8.5351c3.0076 0 5.4492 2.4357 5.4492 5.4433.0048 2.763-2.0629
 5.0899-4.8066
 5.416l-.6719.039c-3.0076-.019-5.4285-2.4748-5.414-5.4823.0191-2.7678
 2.1099-5.0854 4.8632-5.3828.1919-.0192.3882-.0284.58-.0332Zm4.8398
 1.7265 5.2871 2.5137-4.6093
 3.8379c.9881-2.077.7229-4.5288-.6778-6.3516z" />
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
