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


class JoplinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "joplin"

    @property
    def original_file_name(self) -> "str":
        return "joplin.svg"

    @property
    def title(self) -> "str":
        return "Joplin"

    @property
    def primary_color(self) -> "str":
        return "#1071D3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Joplin</title>
     <path d="m20.969 0h-8.904c-.084 0-.152.068-.152.152v2.827c0
 .095.077.172.172.172h1.221c.493 0
 .894.38.937.863v13.378h-.001l-.017.363-.05.282c-.011.044-.02.089-.033.132-.081.258-.208.497-.384.708-.007.007-.015.014-.021.021-.054.063-.11.123-.172.18-.063.057-.13.11-.2.16-.498.353-1.169.508-1.918.436-.955-.089-1.903-.523-2.669-1.22-.765-.696-1.242-1.558-1.34-2.427-.089-.778.144-1.462.655-1.927.002-.001.003-.002.004-.003.02-.018.041-.033.062-.05.366-.307.842-.493
 1.387-.544.006 0 .012-.001.017-.002l.298-.014.35.017c.008 0
 .016.002.024.003.499.05.993.199 1.462.425.01 0
 .022.003.036.011.143.079.17-.005.174-.061v-4.256c0-.122-.085-.23-.203-.256-2.527-.556-5.005.022-6.754
 1.615-1.528 1.389-2.267 3.395-2.027 5.502.213 1.876 1.176 3.679 2.712
 5.076 1.497 1.362 3.402 2.213 5.368 2.399.271.025.543.038.809.038
 1.877 0 3.619-.644 4.905-1.814 1.218-1.109 1.948-2.632
 2.055-4.288l.01-10.866h.001v-2.955c.011-.513.429-.926.945-.926h1.221c.095
 0 .172-.077.172-.172v-2.827c0-.084-.068-.152-.152-.152z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/laurent22/joplin/blob/45e3'''

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
