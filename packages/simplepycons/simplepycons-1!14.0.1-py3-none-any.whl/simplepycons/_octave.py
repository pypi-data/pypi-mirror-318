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


class OctaveIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "octave"

    @property
    def original_file_name(self) -> "str":
        return "octave.svg"

    @property
    def title(self) -> "str":
        return "Octave"

    @property
    def primary_color(self) -> "str":
        return "#0790C0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Octave</title>
     <path d="M10.5.007c-2.414-.09-4.658.715-6.286 2.485C2.913 3.906
 2.188 5.75 1.987 7.77h-.42C.703 7.77 0 8.473 0 9.335v4.743c0 .863.702
 1.567 1.565 1.567h2.091a16.899 16.899 0 002.57 3.687c4.46 4.848
 10.696 6.036 14.561 3.016h2.102c.577 0 1.05-.473 1.05-1.05V18.43a1.03
 1.03 0
 00-.257-.668c.858-3.433-.045-7.642-2.52-11.219.002-.017.01-.032.01-.049V4.482a.822.822
 0 00-.816-.819h-1.703C16.142 1.372 13.218.11 10.5.007zm1.75
 2.18c1.78-.01 3.69.62 5.425 1.85a.797.797 0 00-.15.445v2.013c0
 .449.368.82.816.82h2.016a.788.788 0 00.392-.116c2.248 3.302 2.735
 7.322 1.24 10.18h-1.964c-.579 0-1.052.475-1.052 1.051v1.794c-2.991
 1.3-7.005.222-9.964-2.992a12.743 12.743 0
 01-1.55-2.098c.256-.279.416-.647.416-1.056V9.335c0-.862-.702-1.565-1.565-1.565H5.9c.238-1.364.781-2.612
 1.688-3.596 1.225-1.331 2.88-1.98 4.661-1.988zm6.091 2.01h2.016c.162
 0 .283.123.283.285v2.013c0 .163-.12.285-.283.285H18.34a.28.28 0
 01-.285-.285V4.482a.28.28 0 01.285-.285zM1.566 8.303h4.743c.578 0
 1.033.456 1.033 1.032v4.743c0 .577-.455 1.033-1.032 1.033H1.567a1.024
 1.024 0 01-1.034-1.032V9.335c0-.576.455-1.032 1.032-1.032zm18.459
 9.61h2.865c.29 0 .52.226.52.518v2.865a.512.512 0
 01-.52.519h-2.865a.51.51 0 01-.519-.519v-2.864a.51.51 0 01.519-.518z"
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
