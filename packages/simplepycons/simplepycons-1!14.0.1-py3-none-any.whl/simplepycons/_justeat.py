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


class JustEatIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "justeat"

    @property
    def original_file_name(self) -> "str":
        return "justeat.svg"

    @property
    def title(self) -> "str":
        return "Just Eat"

    @property
    def primary_color(self) -> "str":
        return "#F36D00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Just Eat</title>
     <path d="M11.196.232a1.376 1.376 0 0 1 1.528 0 33.157 33.157 0 0
 1 3.384 2.438s.293.203.301-.14a5.367 5.367 0 0 1 .079-1.329.606.606 0
 0 1 .562-.39s1.329.066 2.173.179c.377.05.671.352.711.73 0 0 .543
 3.62.665 4.925 0 0 .105.664 1.067 1.79 0 0 1.953 2.735 2.18 3.259 0 0
 .454.946-.523 1.074 0 0-1.783.18-1.955.22a.446.446 0 0
 0-.39.484s-.094 6.296-.555 9.32c0 0-.121 1.2-.782 1.173 0
 0-1.833-.059-2.259-.047 0 0-.183 0-.156-.246 0 0 .934-9.817.301-14.78
 0 0-.028-.64-.516-.782 0 0-.445-.18-.871.391a15.574 15.574 0 0 0-2.9
 8.86s-.05 1.563.188 1.953c0 0 .148.274.907.336l.96.13s.176 0
 .16.233c0 0-.218 2.88-.28 3.393a1.018 1.018 0 0
 1-.071.34s-.035.098-.336.086c0 0-4.236-.03-4.713 0 0 0-.2
 0-.242-.105-.043-.106-.294-3.717-.286-4.229a.255.255 0 0 1 .149-.25
 2.548 2.548 0 0 0 1.172-1.871c.052-.548.06-1.098.024-1.646 0 0
 .156-5.522.195-6.41 0 0 .031-.3-.36-.355a.364.364 0 0 0-.437.27v.03c0
 .032-.274 3.643-.223 5.081 0 0 .094.942-.558.961 0
 0-.634.095-.665-.69 0 0 .047-3.542.203-5.292a.39.39 0 0
 0-.348-.391.39.39 0 0 0-.437.316.065.065 0 0 0 0 .031s-.274 3.39-.223
 5.179c0 0 .078.868-.614.836 0 0-.578.066-.61-.704 0 0
 .157-4.85.2-5.224A.39.39 0 0 0 6.647 9h-.039a.391.391 0 0
 0-.418.325.167.167 0 0 0 0 .035s-.258 5.8-.223 7.503c0 0-.023 1.751
 1.27 2.462 0 0 .192.11.196.277 0 0 .145 3.076.277 4.069 0 0
 .047.238-.164.238L4.291 24a.67.67 0 0 1-.665-.633 72.876 72.876 0 0
 1-.601-9.829.5.5 0 0 0-.391-.535S.969 12.85.566 12.749a.692.692 0 0
 1-.422-1.02A33.497 33.497 0 0 1 11.197.232Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://justeattakeaway.com/newsroom/en-WW/me'''

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
