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


class WikidotggIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wikidotgg"

    @property
    def original_file_name(self) -> "str":
        return "wikidotgg.svg"

    @property
    def title(self) -> "str":
        return "wiki.gg"

    @property
    def primary_color(self) -> "str":
        return "#FF1985"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>wiki.gg</title>
     <path d="M5.8326 3.7604c-1.2353.33-2.4875 1.3283-3.0713
 2.4451-.2961.5754-2.4875 7.3356-2.699 8.334-.1354.643-.0423 1.726.203
 2.4451.7277 2.0898 2.6145 3.3928 4.9243 3.3928 1.599 0 2.6313-.3892
 3.892-1.4806 1.2268-1.0576 2.259-1.4638 3.5112-1.3622 1.1337.0846
 1.8952.4315 2.9613 1.3622 1.506 1.3199 3.249 1.7006 5.051 1.0999
 1.2523-.4146 2.276-1.2945
 2.8598-2.4452.4485-.8969.5754-1.5399.5246-2.5467-.0338-.8038-.093-1.0153-1.1845-4.3573-.6261-1.9291-1.2268-3.7143-1.3199-3.9597-.4146-1.0407-1.2437-1.9544-2.276-2.496-.956-.5076-1.3283-.5668-3.4774-.5668-1.1506
 0-1.8698.0338-1.8275.0761.0508.0423.5246.33 1.0576.643.533.3046
 1.0407.6346 1.1253.7361.0846.1016.1438.3131.1438.5077 0
 .4061-.093.4992-1.3114 1.3368l-.9307.6346 1.6668.0423c1.6076.0423
 1.6668.0507 1.8783.2453.2623.2454.2284.1608 1.4976 4.0697 1.0999
 3.4012 1.1422 3.6043.753
 4.0189-.5161.55-1.0322.4822-1.8191-.2115-.3215-.2793-.77-.6346-1.0068-.7954-3.122-2.056-7.2256-1.8021-10.0938.6261-.956.8123-1.0153.8461-1.5652.8461-.2877
 0-.6092-.0592-.753-.1269-.2877-.1523-.5839-.5838-.5839-.863
 0-.1015.5077-1.7937 1.1338-3.7566.8968-2.8344 1.1845-3.6128
 1.3537-3.7904.22-.22.237-.22 1.9376-.2793.9391-.0253 1.8613-.093
 2.0475-.1522.4146-.127 2.1998-1.1423
 2.4198-1.3792.1776-.1946.2115-.5415.0677-.846-.1016-.2285-1.6668-1.1761-2.3522-1.43-.5245-.1945-4.0273-.2114-4.738-.0168zm13.368
 1.379c.33.3385.3385.753.0085
 1.1169-.406.4569-1.1337.3215-1.3706-.2538-.3384-.8292.7192-1.4976
 1.3622-.863z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wiki.gg/wiki/Category:Wiki.gg'''

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
