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


class AppsmithIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "appsmith"

    @property
    def original_file_name(self) -> "str":
        return "appsmith.svg"

    @property
    def title(self) -> "str":
        return "Appsmith"

    @property
    def primary_color(self) -> "str":
        return "#2A2F3D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Appsmith</title>
     <path d="M16.15
 12.723v-1.845h-1.163v.422h.61v1.423h-.61v.421h1.774v-.421zm5.69
 1.167v-.421H24v.421zm-.66-2.852q.213.214.213.604v1.502h-.552v-1.41q0-.43-.426-.43a.48.48
 0 0
 0-.36.152q-.147.151-.147.419v1.27h-.552v-3.023h.552v1.06q.259-.356.69-.356.37
 0 .582.212zm-2.475.262h-.706v1.225q0
 .11.06.153.058.044.198.043h.404v.422c-.12.012-.432.017-.505.017q-.368
 0-.538-.138-.17-.138-.17-.441V11.3h-.513v-.422h.514v-.756h.55v.756h.706zm-4.447-.255q.208.22.209.602v1.497h-.553v-1.41q0-.43-.39-.43a.427.427
 0 0
 0-.343.152q-.129.151-.13.441v1.247h-.547v-1.41q0-.43-.395-.43a.421.421
 0 0
 0-.336.152q-.13.152-.13.442v1.247h-.552v-2.267h.536v.325q.232-.377.644-.377.518
 0 .703.421.254-.421.702-.421.374 0 .582.22zm-5.83
 1.379h.541q.022.21.138.299.117.087.367.087.448 0 .448-.272a.215.215 0
 0 0-.097-.189q-.096-.066-.347-.11l-.259-.043q-.742-.123-.742-.685
 0-.32.246-.503.245-.182.694-.182.97 0
 1.001.767h-.522q-.009-.202-.127-.288-.118-.086-.351-.085-.396
 0-.396.263a.207.207 0 0 0
 .088.178q.088.063.29.099l.285.043q.413.075.6.238.186.162.186.452 0
 .342-.263.527-.263.184-.742.184-.993.001-1.037-.78zm-.77-1.278q.272.325.272.865t-.272.86q-.276.324-.742.324-.466
 0-.703-.346v1.154h-.552v-3.125h.531v.325q.246-.377.725-.377.463 0
 .74.32zm-.874 1.594q.272 0 .43-.198.157-.197.153-.548
 0-.347-.151-.53-.152-.182-.433-.182-.276 0-.43.19-.153.188-.153.54 0
 .355.158.54.148.188.425.188zm-1.972-1.594q.272.325.272.865t-.272.86q-.276.324-.742.324-.466
 0-.703-.346v1.154h-.552v-3.125h.531v.325q.246-.377.725-.377.464 0
 .74.32zm-.874 1.594q.272 0 .43-.198.158-.197.153-.548
 0-.347-.151-.53-.152-.182-.433-.182-.276 0-.43.19-.153.188-.153.54 0
 .355.158.54.15.188.426.188zm-2.331.404q-.04-.07-.062-.276-.228.33-.728.33-.374
 0-.595-.18Q0 12.837 0 12.516q0-.62.87-.706l.342-.03a.504.504 0 0 0
 .245-.082.215.215 0 0 0
 .075-.178q0-.145-.094-.213-.095-.068-.319-.068-.241
 0-.347.081c-.07.055-.111.147-.122.28H.105q.048-.773 1.019-.774.944 0
 .944.681v1.207q0
 .3.092.43zm-.237-.484q.162-.143.162-.41v-.207a.473.473 0 0
 1-.26.092l-.298.034q-.22.027-.313.103a.27.27 0 0 0-.094.222.276.276 0
 0 0 .098.227q.099.081.283.081.26 0 .422-.142Zm14.282-2.142a.29.29 0 0
 1-.09-.214.307.307 0 0 1 .307-.307.29.29 0 0 1 .215.09.3.3 0 0 1
 .087.217.29.29 0 0 1-.09.215.295.295 0 0 1-.213.087.3.3 0 0
 1-.216-.088z" />
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
