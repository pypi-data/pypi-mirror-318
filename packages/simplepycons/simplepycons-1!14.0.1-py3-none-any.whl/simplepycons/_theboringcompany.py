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


class TheBoringCompanyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "theboringcompany"

    @property
    def original_file_name(self) -> "str":
        return "theboringcompany.svg"

    @property
    def title(self) -> "str":
        return "The Boring Company"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>The Boring Company</title>
     <path d="M0 6.959v.463h.424v1.625h.57V7.422h.445v-.463H0zm1.643
 0v2.088h.57v-.842h.742v.842h.57V6.959h-.57v.781h-.742V6.96h-.57zm2.287
 0v2.088h1.199V8.54h-.621v-.295h.596v-.508h-.596v-.312h.62v-.467H3.93zm17.91
 2.73c-1.31 0-2.22.902-2.22 2.217 0 1.316.932 2.211 2.208 2.211 1.522
 0 2.301-1.167
 2.154-2.492H21.83v.887h.867c-.071.455-.425.61-.87.61-.66
 0-1.02-.462-1.02-1.21-.012-.742.427-1.236 1.025-1.236.41 0
 .73.216.893.66l1.064-.457c-.345-.759-1.026-1.19-1.95-1.19zm-15.877.012c-1.375
 0-2.313.99-2.313 2.21 0 1.219.974 2.206 2.313 2.206 1.339 0 2.31-.987
 2.31-2.207 0-1.22-.935-2.209-2.31-2.209zm-5.875.13v4.171h1.687c1.153
 0 1.516-.615 1.516-1.268
 0-.494-.275-.86-.824-.986.278-.147.43-.473.43-.853
 0-.57-.317-1.065-1.07-1.065H.086zm8.816 0v4.171h1.123v-1.545l.993
 1.545h1.373v-.047l-1.274-1.66c.584-.133.889-.601.889-1.186
 0-.688-.49-1.279-1.24-1.279H8.904zm3.909
 0v4.171h1.105V9.83h-1.105zm1.931 0v4.171h1.125v-2.473l1.938
 2.473h1.113V9.83h-1.113v2.465L15.869
 9.83h-1.125zm-13.533.839h.187c.238 0 .457.114.457.39 0
 .27-.22.391-.457.391h-.187v-.781zm8.816.021h.307c.265 0
 .521.216.521.48 0 .266-.201.481-.521.481h-.307v-.96zm-8.816
 1.577h.25c.414-.002.693.138.693.421 0
 .271-.21.412-.513.416l-.43.006v-.843zm8.156 2.552c-.656
 0-1.103.498-1.103 1.112 0 .613.464 1.109 1.103 1.109.187 0
 .358-.042.508-.117v-.658h-.037a.54.54 0 0 1-.44.214.54.54 0 0
 1-.548-.548c0-.304.222-.551.548-.551a.54.54 0 0 1
 .444.217h.033v-.662a1.137 1.137 0 0 0-.508-.116zm1.918 0c-.692
 0-1.164.498-1.164 1.112 0 .613.49 1.109 1.164 1.109.674 0 1.162-.496
 1.162-1.11 0-.613-.47-1.11-1.162-1.11zm1.715.045-.352
 2.117h.57l.184-1.103.422 1.103h.285l.422-1.103.182
 1.103h.57l-.351-2.117-.563.004-.402 1.05-.403-1.05-.564-.004zm2.57
 0v2.112h.592v-.68h.324c.504 0 .717-.317.717-.71
 0-.388-.21-.722-.822-.722h-.81zm2.356 0-.81
 2.117h.626l.113-.34h.75l.114.34h.629l-.81-2.117h-.612zm1.594
 0v2.112h.568V15.74l.97
 1.237h.561v-2.112h-.562v1.244l-.97-1.244h-.567zm2.218 0 .785
 1.114v.998h.567v-.989l.79-1.123h-.689l-.38.574-.381-.574h-.692zm-5.576.485h.207c.31
 0 .318.478-.014.478h-.193v-.478zm-4.877.03c.337 0
 .565.248.565.552a.547.547 0 0 1-.565.548.548.548 0 0
 1-.566-.548c0-.304.23-.551.566-.551zm6.945.198.211.602h-.42l.21-.602z"
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
        return '''https://commons.wikimedia.org/wiki/File:The_B'''

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
