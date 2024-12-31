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


class GentooIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gentoo"

    @property
    def original_file_name(self) -> "str":
        return "gentoo.svg"

    @property
    def title(self) -> "str":
        return "Gentoo"

    @property
    def primary_color(self) -> "str":
        return "#54487A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gentoo</title>
     <path d="M9.94 0a7.31 7.31 0 00-1.26.116c-4.344.795-7.4
 4.555-7.661 7.031-.126 1.215.53 2.125.89 2.526.977 1.085 2.924 1.914
 4.175 2.601-1.81 1.543-2.64 2.296-3.457 3.154C1.403 16.712.543
 18.125.54 19.138c0 .325-.053 1.365.371 2.187.16.309.613 1.338 1.98
 2.109.874.494 2.119.675 3.337.501 3.772-.538 8.823-3.737 12.427-6.716
 2.297-1.9 3.977-3.739
 4.462-4.644.39-.731.434-2.043.207-2.866-.645-2.337-5.887-7.125-10.172-9.051A7.824
 7.824 0 009.94 0zm-.008.068a7.4 7.4 0 013.344.755c3.46 1.7 9.308
 6.482 9.739 8.886.534 2.972-9.931 11.017-16.297
 12.272-2.47.485-4.576.618-5.537-1.99-.832-2.262.783-3.916
 3.16-6.09a92.546 92.546 0
 012.96-2.576c.065-.069-5.706-2.059-5.89-4.343C1.221 4.634 4.938.3
 9.697.076c.08-.004.157-.007.235-.008zm-.112.52a5.647 5.647 0
 00-.506.032c-2.337.245-2.785.547-4.903 2.149-.71.537-2.016 1.844-2.35
 3.393-.128.59.024 1.1.448 1.458 1.36 1.144 3.639 2.072 5.509
 2.97.547.263.185.74-.698 1.505-2.227 1.928-5.24 4.276-5.45
 6.066-.099.842.19 1.988 1.213 2.574 1.195.685 3.676.238 5.333-.379
 2.422-.902 5.602-2.892 8.127-4.848 2.625-2.034 5.067-4.617
 5.188-5.038.148-.517.133-.996-.154-1.546-.448-.862-1.049-1.503-1.694-2.22-1.732-1.825-3.563-3.43-5.754-4.658C12.694
 1.242 11.417.564 9.82.588zm1.075 3.623c.546 0 1.176.173 1.853.5
 1.688.817 3.422 2.961-.015
 4.195-.935.336-3.9-.824-3.81-2.407.09-1.57.854-2.289
 1.972-2.288zm.285 1.367c-.317-.002-.575.079-.694.263-.557.861-.303
 1.472.212 1.862.192-.457 2.156.043 2.148.472a.32.32 0
 00.055-.032c1.704-1.282-.472-2.557-1.72-2.565z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.gentoo.org/inside-gentoo/foundati'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://wiki.gentoo.org/wiki/Project:Artwork/'''

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
