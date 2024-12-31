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


class SiemensIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "siemens"

    @property
    def original_file_name(self) -> "str":
        return "siemens.svg"

    @property
    def title(self) -> "str":
        return "Siemens"

    @property
    def primary_color(self) -> "str":
        return "#009999"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Siemens</title>
     <path d="M1.478 10.016c.24 0 .59.046 1.046.14v.726a2.465 2.465 0
 0 0-.946-.213c-.41 0-.615.118-.615.354 0
 .088.041.16.124.216.069.045.258.14.568.286.446.208.743.388.89.541.176.182.264.417.264.705
 0 .415-.172.73-.516.949-.279.176-.64.264-1.085.264-.375
 0-.753-.046-1.133-.139v-.755c.41.135.774.203 1.09.203.437 0
 .655-.121.655-.362a.302.302 0 0
 0-.095-.227c-.065-.065-.232-.155-.5-.27-.481-.208-.795-.384-.94-.53a.999.999
 0 0 1-.284-.73c0-.377.137-.666.413-.864.272-.196.626-.294
 1.064-.294zm21.19 0c.246 0 .565.04.956.123l.09.016v.727a2.471 2.471 0
 0 0-.948-.213c-.409 0-.612.118-.612.354 0
 .088.04.16.123.216.066.043.256.139.57.286.443.208.74.388.889.541.176.182.264.417.264.705
 0 .415-.172.73-.514.949-.28.176-.643.264-1.087.264-.376
 0-.754-.046-1.134-.139v-.755c.407.135.77.203 1.09.203.437 0
 .655-.121.655-.362
 0-.09-.03-.166-.092-.227-.066-.065-.233-.155-.503-.27-.48-.206-.793-.382-.94-.53a.997.997
 0 0 1-.284-.732c0-.376.137-.664.413-.862.272-.196.627-.294
 1.064-.294zm-12.674.066l.92
 2.444.942-2.444h1.257v3.825h-.968v-2.708l-1.072
 2.747h-.632l-1.052-2.747v2.708H8.67v-3.825zm-5.587
 0v3.825H3.386v-3.825zm3.554
 0v.692H6.327v.864H7.75v.63H6.327v.908h1.677v.73h-2.66v-3.824zm8.707
 0v.692h-1.634v.864h1.422v.63h-1.422v.908h1.677v.73H14.05v-3.824zm1.898
 0l1.255 2.56v-2.56h.719v3.825h-1.15l-1.288-2.595v2.595h-.72v-3.825z"
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
