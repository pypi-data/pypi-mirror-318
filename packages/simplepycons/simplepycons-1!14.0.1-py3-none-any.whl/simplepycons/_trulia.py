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


class TruliaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "trulia"

    @property
    def original_file_name(self) -> "str":
        return "trulia.svg"

    @property
    def title(self) -> "str":
        return "trulia"

    @property
    def primary_color(self) -> "str":
        return "#0A0B09"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>trulia</title>
     <path d="M17.6958 8.9368a.6678.6678 0 0 0 .095 1.329.6678.6678 0
 0 0 .6678-.668.6678.6678 0 0
 0-.7628-.661zm-4.3956.2812v1.121h.7513v3.4726h-.7513v1.121h2.6262v-1.121h-.7513V9.218Zm-12.549.121v1.3814H.0001v1.1281h.7513v1.0852c0
 1.1799.9502 2.1362 2.1226 2.1362a2.1126 2.1126 0 0 0
 .4608-.0507v-1.115a1.1025 1.1025 0 0 1-.3837.0685c-.5958
 0-1.0789-.4689-1.0789-1.047v-1.0772H3.335v-1.1281H1.872V9.339Zm20.92
 1.2609c-1.1147-.005-2.0196.9806-2.019 2.1905.0005 1.21.9043 2.1952
 2.019 2.1905.0292 0 .0598-.0009.0877-.002.4221-.0111.8757-.2098
 1.113-.488v.4218H24v-4.2458h-1.1275l-.0005.4236c-.2385-.2791-.692-.477-1.113-.4879-.0292-.002-.0585-.002-.0878-.002zm-14.8245.0473c-.5173.003-.9275.153-1.2964.654l-.2277-.64h-1.098v1.1271h.5195v3.1444h1.118v-2.1983a.9887.9887
 0 0 1
 .9851-.9906h.339v-1.0966Zm9.6549.047v1.1172h.7513v3.121h1.8736v-1.117h-.7514l.001-3.1212zm-8.2605.0298v2.2125c0
 1.1773.9494 2.1315 2.1195 2.1315s2.1193-.9525
 2.1193-2.1298v-2.214h-1.1186v2.2539a1.0018 1.0018 0 1 1-2.001
 0v-2.254zm13.5857.9717c.5932 0 1.074.5008 1.0746
 1.1191.0005.6184-.4814 1.1192-1.0746 1.1192-.5933
 0-1.0742-.5008-1.075-1.1192-.0008-.6183.4817-1.1191 1.075-1.1191z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.trulia.com/newsroom/media/brand-l'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.trulia.com/newsroom/media/brand-l'''

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
