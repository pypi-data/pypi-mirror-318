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


class EmbyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "emby"

    @property
    def original_file_name(self) -> "str":
        return "emby.svg"

    @property
    def title(self) -> "str":
        return "Emby"

    @property
    def primary_color(self) -> "str":
        return "#52B54B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Emby</title>
     <path d="M11.041 0c-.007 0-1.456 1.43-3.219 3.176L4.615
 6.352l.512.513.512.512-2.819 2.791L0 12.961l1.83 1.848c1.006 1.016
 2.438 2.46 3.182 3.209l1.351
 1.359.508-.496c.28-.273.515-.498.524-.498.008 0 1.266 1.264 2.794
 2.808L12.97 24l.187-.182c.23-.225 5.007-4.95
 5.717-5.656l.52-.516-.502-.513c-.276-.282-.5-.52-.496-.53.003-.009
 1.264-1.26 2.802-2.783 1.538-1.522 2.8-2.776
 2.803-2.785.005-.012-3.617-3.684-6.107-6.193L17.65
 4.6l-.505.505c-.279.278-.517.501-.53.497-.013-.005-1.27-1.267-2.793-2.805A449.655
 449.655 0 0011.041 0zM9.223 7.367c.091.038 7.951 4.608 7.957
 4.627.003.013-1.781 1.056-3.965 2.32a999.898 999.898 0 01-3.996
 2.307c-.019.006-.026-1.266-.026-4.629 0-3.7.007-4.634.03-4.625Z" />
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
