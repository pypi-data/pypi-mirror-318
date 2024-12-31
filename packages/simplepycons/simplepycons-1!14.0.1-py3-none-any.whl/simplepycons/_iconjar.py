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


class IconjarIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "iconjar"

    @property
    def original_file_name(self) -> "str":
        return "iconjar.svg"

    @property
    def title(self) -> "str":
        return "IconJar"

    @property
    def primary_color(self) -> "str":
        return "#16A5F3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>IconJar</title>
     <path d="M5.15 5.875c-.492 0-.936-.453-.936-.954 0-1.155
 2.858-2.01 6.11-2.01.295 0 .492 0 .492-.25
 0-.452-.985-.602-.985-1.355C9.831.502 10.767 0 11.95 0c1.183 0
 2.12.502 2.12 1.306 0 .753-.986.853-.986 1.355 0 .151.148.251.492.251
 3.252 0 6.16.803 6.16 2.009a.944.944 0 01-.937.953H5.151zm14.732
 4.568c1.183.753 1.626 2.109 1.43 3.365l-1.38 7.58C19.636 22.897
 18.354 24 16.826 24H7.17c-1.526
 0-2.808-1.104-3.104-2.611l-1.38-7.581a3.307 3.307 0
 011.48-3.315c.69-.501.836-1.355
 0-1.656-1.184-.452-.938-1.908.245-1.908h7.193c1.133 0 2.514.853 2.514
 3.615 0 2.762-1.282 2.51-1.282 4.468 0 .854.69 1.758 1.527 1.859
 1.43.15 2.267-.402 2.267-2.41 0-2.06-1.182-3.013-1.182-4.72 0-2.059
 1.28-2.863 2.118-2.863h2.07c1.182 0 1.43 1.457.246 1.909-.837.35-.69
 1.205 0 1.656z" />
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
