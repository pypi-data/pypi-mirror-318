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


class ArsTechnicaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "arstechnica"

    @property
    def original_file_name(self) -> "str":
        return "arstechnica.svg"

    @property
    def title(self) -> "str":
        return "Ars Technica"

    @property
    def primary_color(self) -> "str":
        return "#FF4E00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ars Technica</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0zM8.842 15.656H7.745l-.15-.98a3.457 3.457 0 0
 1-2.592 1.13c-1.33 0-2.16-.798-2.16-2.044 0-1.828 1.561-2.56
 4.636-2.876v-.315c0-.931-.548-1.247-1.396-1.247-.848
 0-1.745.283-2.543.632l-.183-1.18c.881-.35 1.712-.615 2.842-.615 1.779
 0 2.643.714 2.643 2.36v5.135zm3.191-4.337v4.337H10.67v-7.33h1.097L12
 9.824c.515-.831 1.363-1.58 2.576-1.646l.216
 1.313c-1.23.05-2.26.865-2.759 1.829zm6.2 4.487a6.017 6.017 0 0
 1-2.676-.698l.2-1.296a4.587 4.587 0 0 0 2.592.847c.93 0 1.496-.349
 1.496-.964s-.416-.93-1.745-1.246c-1.729-.432-2.41-.948-2.41-2.26
 0-1.314.98-2.028 2.593-2.028a5.933 5.933 0 0 1 2.41.498l-.217
 1.297a4.687 4.687 0 0 0-2.227-.632c-.83
 0-1.263.316-1.263.848s.366.764 1.53 1.063c1.81.466 2.625.981 2.625
 2.377s-1.014 2.194-2.908 2.194zM7.479 11.934v1.711c-.615.632-1.479
 1.03-2.177 1.03s-1.097-.215-1.097-.98c0-.764.565-1.496 3.274-1.761z"
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
