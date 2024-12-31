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


class XdotorgIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "xdotorg"

    @property
    def original_file_name(self) -> "str":
        return "xdotorg.svg"

    @property
    def title(self) -> "str":
        return "X.Org"

    @property
    def primary_color(self) -> "str":
        return "#F28834"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>X.Org</title>
     <path d="M19.94 1.9l-9.092 11.874 4.598 6.392a14.29 14.29 0 0
 1-2.56.228c-2.387
 0-4.582-.577-6.316-1.542l6.556-8.627-6.031-8.311L2.23 1.91 9.8
 12.48l-4.332 5.66c-1.692-1.266-2.729-2.965-2.729-4.832 0-2.13
 1.348-4.042 3.48-5.342l-.655-.999C2.22 8.386 0 10.876 0 13.71c0 2.432
 1.635 4.61 4.212 6.075l-1.765 2.307h1.661l1.299-1.709c1.892.83 4.158
 1.314 6.592 1.314a17.43 17.43 0 0 0
 4.188-.501l.65.903h4.865l-1.729-2.422C22.443 18.214 24 16.082 24
 13.71c0-2.94-2.39-5.512-5.948-6.9l-.217.311c3.099 1.214 5.195 3.531
 5.195 6.188 0 2.202-1.44 4.17-3.698 5.47l-5.153-7.22 7.382-9.658zM12
 5.755c-.586 0-1.212.046-1.775.1 1.004 1.309 1.836 2.417 2.795
 3.676-.538-1.157-1.644-2.268-1.261-2.839.378-.565 1.075-.47 1.128-.47
 1.118 0 2.194.127 3.2.36l.235-.324C14.98 5.91 13.523 5.754 12 5.754z"
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
        return '''https://commons.wikimedia.org/wiki/File:X.Org'''

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
