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


class PinterestIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pinterest"

    @property
    def original_file_name(self) -> "str":
        return "pinterest.svg"

    @property
    def title(self) -> "str":
        return "Pinterest"

    @property
    def primary_color(self) -> "str":
        return "#BD081C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pinterest</title>
     <path d="M12.017 0C5.396 0 .029 5.367.029 11.987c0 5.079 3.158
 9.417 7.618 11.162-.105-.949-.199-2.403.041-3.439.219-.937
 1.406-5.957 1.406-5.957s-.359-.72-.359-1.781c0-1.663.967-2.911
 2.168-2.911 1.024 0 1.518.769 1.518 1.688 0 1.029-.653 2.567-.992
 3.992-.285 1.193.6 2.165 1.775 2.165 2.128 0 3.768-2.245 3.768-5.487
 0-2.861-2.063-4.869-5.008-4.869-3.41 0-5.409 2.562-5.409 5.199 0
 1.033.394 2.143.889 2.741.099.12.112.225.085.345-.09.375-.293
 1.199-.334
 1.363-.053.225-.172.271-.401.165-1.495-.69-2.433-2.878-2.433-4.646
 0-3.776 2.748-7.252 7.92-7.252 4.158 0 7.392 2.967 7.392 6.923 0
 4.135-2.607 7.462-6.233 7.462-1.214 0-2.354-.629-2.758-1.379l-.749
 2.848c-.269 1.045-1.004 2.352-1.498 3.146 1.123.345 2.306.535
 3.55.535 6.607 0 11.985-5.365 11.985-11.987C23.97 5.39 18.592.026
 11.985.026L12.017 0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://business.pinterest.com/en/brand-guide'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://business.pinterest.com/en/brand-guide'''

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
