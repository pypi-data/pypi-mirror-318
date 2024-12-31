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


class FerrariNdotvdotIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ferrarinv"

    @property
    def original_file_name(self) -> "str":
        return "ferrarinv.svg"

    @property
    def title(self) -> "str":
        return "Ferrari N.V."

    @property
    def primary_color(self) -> "str":
        return "#EB2E2C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ferrari N.V.</title>
     <path d="M17.297 13.283v-1.745c0-.541-.297-.646-1.135-.646-.908
 0-1.222.122-1.222.751v.279h.768v-.227c0-.314.017-.367.419-.367.332 0
 .349.035.349.367v.628h-.803c-.628
 0-.82.297-.82.646h.785v-.017c0-.157.105-.297.262-.297h.593v.698c0
 .244-.122.297-.297.297h-.314c-.192
 0-.262-.122-.262-.297v-.384h-.785v.436c0
 .367.279.663.716.663h2.06v-.471h-.314v-.314zm6.389.332v-2.653h-1.169v.436h.332v2.217h-.332v.454H24v-.454h-.314zm-2.95-2.723c-.436
 0-.716.541-.908.768v-.716h-1.152v.436h.314v2.217h-.314v.471h1.431v-.471h-.297V12.41c0-.105.681-.96.681-.873v1.187h.803v-1.327c.001-.313-.191-.505-.558-.505M5.324
 12.393h-.82v-.838c0-.157.052-.244.244-.244h.349c.14 0
 .227.07.227.175v.907zm-.349-1.501h-.123c-.943
 0-1.187.209-1.187.751v1.745c0 .593.349.698 1.204.716h.087c.925-.017
 1.204-.087 1.204-.646v-.454h-.801v.227c0 .314-.052.332-.436.332-.454
 0-.436-.035-.419-.332v-.541H6.18v-1.17c-.001-.436-.333-.628-1.205-.628zm17.89-.489h.855v-.559h-.855v.559zm-22.743
 0h.489v3.299H0v.454h2.269v-.454h-.768v-1.466h.436v.419h.524v-1.309h-.524v.384h-.436v-1.327h20.701v-.559H.122v.559zm9.269.489c-.436
 0-.716.541-.908.768v-.716H7.331v.436h.314v2.217h-.314v.471h1.431v-.471h-.297V12.41c0-.105.681-.96.681-.873v1.187h.803v-1.327c0-.313-.192-.505-.558-.505m3.665
 0c-.436
 0-.716.541-.908.768v-.716h-1.152v.436h.314v2.217h-.314v.471h1.431v-.471h-.297V12.41c0-.105.681-.96.681-.873v1.187h.803v-1.327c.001-.313-.191-.505-.558-.505"
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
