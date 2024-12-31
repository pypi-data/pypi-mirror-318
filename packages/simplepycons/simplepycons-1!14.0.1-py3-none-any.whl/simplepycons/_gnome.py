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


class GnomeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gnome"

    @property
    def original_file_name(self) -> "str":
        return "gnome.svg"

    @property
    def title(self) -> "str":
        return "GNOME"

    @property
    def primary_color(self) -> "str":
        return "#4A86CF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GNOME</title>
     <path d="M19.703 0c-4.99 0-5.927 7.111-3.12 7.111 2.81 0
 8.113-7.111 3.12-7.111M11.99.872q-.119-.001-.25.016c-2.811.364-1.82
 5.25-.324 5.34 1.449.09 3.032-5.347.574-5.356M7.123 2.803a1.4 1.4 0 0
 0-.488.114c-2.259.933-.344 4.776.921 4.519 1.168-.24
 1.319-4.671-.433-4.632Zm-3.6 3.016a1.05 1.05 0 0 0-.634.215c-1.807
 1.248.607 4.269 1.671 3.799.93-.41.338-3.967-1.037-4.014m10.032
 2.309c-3.835.033-8.716 1.978-9.567 5.784C3.044 18.14 7.875 24 12.915
 24c2.48 0 5.34-2.24 5.875-5.077.409-2.163-4.81-1.295-4.623.137.225
 1.715-1.258 2.561-2.711 1.454-4.623-3.52 7.658-5.276
 6.847-10.086-.263-1.56-2.29-2.322-4.748-2.301Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://gitlab.gnome.org/Teams/Design/brand/-'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://wiki.gnome.org/Engagement/BrandGuidel'''

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
