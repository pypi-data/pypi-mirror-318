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


class SogouIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sogou"

    @property
    def original_file_name(self) -> "str":
        return "sogou.svg"

    @property
    def title(self) -> "str":
        return "Sogou"

    @property
    def primary_color(self) -> "str":
        return "#FB6022"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sogou</title>
     <path d="M16.801 22.74L17.79 24c1.561-.676 2.926-1.62
 4.051-2.851l-.946-1.318c-1.11 1.289-2.475 2.279-4.08 2.909h-.014zM12
 22.199c-5.775 0-10.455-4.619-10.455-10.35C1.545 6.15 6.225 1.53 12
 1.53s10.456 4.65 10.456 10.35c0 2.55-.946 4.891-2.507 6.69l.945
 1.261C22.801 17.729 24 14.939 24 11.88 24 5.295 18.63 0 12 0S0 5.311
 0 11.85c0 6.57 5.37 11.88 12 11.88 1.71 0 3.33-.346
 4.801-.99l-.961-1.26c-1.2.45-2.49.719-3.84.719zM18
 12.646c-2.25-1.86-5.34-2.101-7.801-3.556-.75-.479-.148-1.395.602-1.425
 2.699-.45 5.369.63 7.889
 1.5l.151-2.655c-3.151-1.14-6.57-1.875-9.901-1.35-1.2.3-2.4.675-3.254
 1.56-1.171 1.2-.961 3.36.389 4.32 2.236 1.755 5.176 2.011 7.621
 3.36.96.39.555 1.68-.391 1.77-2.925.555-5.805-.721-8.325-2.1-.03
 1.02-.06 2.01-.06 3 3.195 1.409 6.75 2.069 10.2 1.529 1.17-.225
 2.37-.6 3.225-1.454 1.229-1.2 1.111-3.511-.33-4.5H18z" />
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
