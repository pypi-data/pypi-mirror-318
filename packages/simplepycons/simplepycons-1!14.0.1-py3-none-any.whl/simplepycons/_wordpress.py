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


class WordpressIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wordpress"

    @property
    def original_file_name(self) -> "str":
        return "wordpress.svg"

    @property
    def title(self) -> "str":
        return "WordPress"

    @property
    def primary_color(self) -> "str":
        return "#21759B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WordPress</title>
     <path d="M21.469 6.825c.84 1.537 1.318 3.3 1.318 5.175 0
 3.979-2.156 7.456-5.363 9.325l3.295-9.527c.615-1.54.82-2.771.82-3.864
 0-.405-.026-.78-.07-1.11m-7.981.105c.647-.03 1.232-.105
 1.232-.105.582-.075.514-.93-.067-.899 0 0-1.755.135-2.88.135-1.064
 0-2.85-.15-2.85-.15-.585-.03-.661.855-.075.885 0 0 .54.061
 1.125.09l1.68 4.605-2.37 7.08L5.354 6.9c.649-.03 1.234-.1
 1.234-.1.585-.075.516-.93-.065-.896 0 0-1.746.138-2.874.138-.2
 0-.438-.008-.69-.015C4.911 3.15 8.235 1.215 12 1.215c2.809 0 5.365
 1.072 7.286 2.833-.046-.003-.091-.009-.141-.009-1.06
 0-1.812.923-1.812 1.914 0 .89.513 1.643 1.06 2.531.411.72.89 1.643.89
 2.977 0 .915-.354 1.994-.821 3.479l-1.075 3.585-3.9-11.61.001.014zM12
 22.784c-1.059 0-2.081-.153-3.048-.437l3.237-9.406 3.315
 9.087c.024.053.05.101.078.149-1.12.393-2.325.609-3.582.609M1.211
 12c0-1.564.336-3.05.935-4.39L7.29 21.709C3.694 19.96 1.212 16.271
 1.211 12M12 0C5.385 0 0 5.385 0 12s5.385 12 12 12 12-5.385
 12-12S18.615 0 12 0" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://wordpressfoundation.org/trademark-pol'''
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
