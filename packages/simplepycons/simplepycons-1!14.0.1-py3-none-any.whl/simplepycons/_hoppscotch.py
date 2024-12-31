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


class HoppscotchIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hoppscotch"

    @property
    def original_file_name(self) -> "str":
        return "hoppscotch.svg"

    @property
    def title(self) -> "str":
        return "Hoppscotch"

    @property
    def primary_color(self) -> "str":
        return "#09090B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hoppscotch</title>
     <path d="M15.632 4.746a8.894 8.894 0 0 1 5.29 7.938c1.867 1.47
 3.723 3.527 2.86 5.465-.968 2.174-4.415 2.085-8.334.985A7.113 7.113 0
 0 1 5.063 14.51C1.623 12.334-.75 9.832.218 7.658c.863-1.939
 3.634-1.936 5.975-1.532a8.894 8.894 0 0 1 9.439-1.38ZM1.862 8.39c-.47
 1.056 2.056 4.054 8.972 7.133 6.916 3.08 10.834 2.95 11.304
 1.894.39-.874-1.212-2.554-3.046-3.856-1.426-1.02-3.38-2.143-5.929-3.278-.694-.309-.964-1.133-.673-1.788.292-.655.933-1.093
 2.282-1.156.635-.002.718-.178.747-.329.036-.233-.287-.47-.62-.618-2.647-1.179-5.888-.685-8.134
 1.68-2.195-.491-4.514-.556-4.903.318Zm11.083
 5.666c-.24.54-.98.735-1.651.436s-1.02-.979-.78-1.518c.24-.54.979-.735
 1.65-.436.671.299 1.021.979.78 1.518zm4.02 2.327c.703.202 1.404-.093
 1.566-.658.162-.564-.276-1.186-.98-1.387-.702-.202-1.403.093-1.565.658-.162.564.276
 1.186.98 1.387zM7.218 9.737c.62.388.87 1.106.559
 1.604-.311.498-1.066.588-1.686.2-.62-.387-.87-1.105-.56-1.604.312-.498
 1.067-.588 1.687-.2Z" />
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
