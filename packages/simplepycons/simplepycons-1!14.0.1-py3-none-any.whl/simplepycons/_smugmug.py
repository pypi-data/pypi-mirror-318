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


class SmugmugIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "smugmug"

    @property
    def original_file_name(self) -> "str":
        return "smugmug.svg"

    @property
    def title(self) -> "str":
        return "SmugMug"

    @property
    def primary_color(self) -> "str":
        return "#6DB944"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SmugMug</title>
     <path d="M18.31 0l-.35.01c-1.55.13-2.46 1.2-2.6 2.28-.15 1.2.65
 2.4 2.58 2.28 2.15-.12 3.09-1.2
 3.1-2.28.02-1.15-1-2.28-2.73-2.29zM7.21.34A2.66 2.66 0 004.56
 2.6C4.41 3.73 5.12 4.87 7 4.85c2.23-.04 3.31-1.37
 3.16-2.57-.12-1-1.09-1.92-2.94-1.94zm12.35 8.71a7 7 0
 00-.4.02c-5.28.54-5.54.6-15.26.82C-.2 9.9.62 24 9.38 24c8.2 0
 18.12-15.15 10.18-14.95zm-1.1 2.7c3.18-.07-2.9 9.53-8.8 9.56-7.46
 0-6.44-8.8-5.18-8.85 8.67-.35 10.88-.64 13.98-.71Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.smugmughelp.com/articles/409-smug'''

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
