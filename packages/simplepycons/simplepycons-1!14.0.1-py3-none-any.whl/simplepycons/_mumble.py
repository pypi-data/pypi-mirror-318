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


class MumbleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mumble"

    @property
    def original_file_name(self) -> "str":
        return "mumble.svg"

    @property
    def title(self) -> "str":
        return "Mumble"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mumble</title>
     <path d="M12 .08A12 11.92 0 000 12a12 11.92 0 0012 11.92A12 11.92
 0 0024 12 12 11.92 0 0012 .08zM9.463 1.56c.393 0 .763.21.944.57-.013
 1.409-.007 2.819-.008
 4.23v.001c.013.303-.019.633.004.951.023.318.102.627.341.88.357.447.942.468
 1.45.446h-.003.003c.736.093 1.468-.476
 1.519-1.225v-.001c.013-1.74.008-3.479
 0-5.218.115-.387.562-.669.973-.617h.006c1.457-.108 3.002.616 3.661
 1.953l.001.002c.252.448.328 1.023.381 1.496v4.258a3.401 3.401 0
 00-.757-.174l-.037-.004V9.389h-.022v-.193c0-.148-.13-.265-.285-.265h-.36a.305.305
 0 00-.102.018c-.002-1.298.007-2.592-.01-3.895v-.001a2.212 2.212 0
 00-.571-1.358c-.337-.368-.801-.606-1.33-.567l-.03.002v3.995c.104
 1.115-.673 2.259-1.791
 2.469-.742.09-1.498.028-2.252.047h-.002c-1.184.1-2.306-.88-2.39-2.06-.027-1.475-.004-2.952-.012-4.428v-.032h-.032c-.508-.006-.945.241-1.26.606a2.247
 2.247 0 00-.534 1.319C6.94 6.383 6.95 7.71 6.948 9.04a.291.291 0
 00-.156-.045H6.44c-.154
 0-.28.118-.28.265v.122h-.007v-.217l-.036.004a3.394 3.394 0
 00-.733.166V5.273c.007-.371.045-.734.139-1.117.401-1.573 2.014-2.627
 3.604-2.588l.082.003.08.001h.003c.057-.01.114-.013.17-.013zM17.275
 9h.36c.122 0 .217.088.217.196v10.736c0
 .107-.095.196-.218.196h-.36c-.122
 0-.217-.089-.217-.196V9.196c0-.108.095-.196.218-.196zM6.44
 9.064h.353c.04 0 .079.011.11.03l.013.007a.186.186 0
 01.035.028c.034.035.054.08.054.131v10.737c0
 .108-.093.196-.212.196H6.44c-.12
 0-.212-.088-.212-.196V9.26c0-.108.093-.196.212-.196zm11.567.118c.055.007.11.016.164.025
 2.061.356 3.662 2.656 3.662 5.452 0 2.869-1.686 5.217-3.826
 5.476zM6.09 9.241v10.952c-2.14-.259-3.826-2.607-3.826-5.476 0-2.775
 1.578-5.063
 3.618-5.444l.011-.002.034-.006c.054-.009.108-.017.163-.024zM17.92
 19.883h.022v.326l.036-.004a3.35 3.35 0 00.371-.062.195.195 0
 01-.09.173l-.002.001v.001s-.618.496-.947.707c-.314.187-.49.338-.758.455a1.718
 1.718 0 01-.19.067.858.858 0 01-.14.032h-2.206a.134.134 0
 01-.02-.002.68.68 0
 00.052-.456h2.068s.127-.011.28-.085c.19-.091.39-.225.577-.347.209-.137.403-.283.607-.435.026-.02.05-.04.072-.06.148-.008.268-.12.268-.263zm-5.684.39c.487
 0 .928.115 1.244.299.317.184.506.433.506.705 0
 .271-.19.52-.506.705-.316.183-.757.299-1.244.299-.488
 0-.93-.116-1.245-.3-.317-.183-.506-.433-.506-.704
 0-.272.19-.521.506-.705.316-.184.757-.3 1.245-.3z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://github.com/mumble-voip/mumble/blob/d4'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/mumble-voip/mumble/blob/d4'''

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
