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


class CnnIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cnn"

    @property
    def original_file_name(self) -> "str":
        return "cnn.svg"

    @property
    def title(self) -> "str":
        return "CNN"

    @property
    def primary_color(self) -> "str":
        return "#CC0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CNN</title>
     <path d="M23.9962 15.514c0 2.0638-2.6676
 3.0547-4.0789.6576-.1012-.173-2.3252-4.0032-2.3252-4.0032v3.3457c0
 2.0637-2.6663
 3.0546-4.0776.6575-.1025-.173-2.3253-4.0032-2.3253-4.0032v3.1547c0
 1.4318-.8498 2.2073-2.1791 2.2073H5.5299a5.5299 5.5299 0
 010-11.0598h1.7946v1.328H5.5299a4.2019 4.2019 0 100
 8.4038h3.4494a.8973.8973 0 00.8794-.878V8.524a.2692.2692 0
 01.1935-.273c.141-.0384.2897.0487.3987.2333l2.1522 3.7084c1.251
 2.1573 2.0728 3.5738 2.083
 3.5892.2807.4742.6986.5576.9973.4755a.7973.7973 0
 00.582-.787v-6.945a.2705.2705 0
 01.191-.2744c.1397-.0384.287.0487.3947.2333l1.9946 3.4366 2.242
 3.8648c.2191.3717.5242.5038.7896.5038a.7691.7691 0
 00.2063-.0282.7986.7986 0 00.591-.791V6.4707H24zM8.0026
 13.9695V8.4857c0-2.0638 2.6675-3.0546 4.0788-.6563.1025.173 2.3253
 4.002 2.3253 4.002V8.4856c0-2.0638 2.6662-3.0546
 4.0775-.6563.1026.173 2.3253 4.002 2.3253
 4.002V6.4705H22.14v8.9999a.2705.2705 0
 01-.1935.2743c-.141.0384-.2897-.0487-.3987-.2333a1360.4277 1360.4277
 0
 01-2.2406-3.8622l-1.9946-3.434c-.2794-.4744-.696-.5577-.9921-.477a.7986.7986
 0 00-.5833.7858v6.9464a.2718.2718 0
 01-.1935.2743c-.1423.0384-.291-.0487-.3987-.2333-.0192-.032-1.069-1.8407-2.083-3.5892a6211.7971
 6211.7971 0
 00-2.1535-3.711c-.2794-.4755-.6973-.5575-.996-.4768a.7999.7999 0
 00-.5845.7858v6.8002a.3717.3717 0 01-.3487.3474h-3.452a3.6712 3.6712
 0 010-7.3424H7.322v1.328H5.5427a2.3432 2.3432 0 100
 4.6864H7.636a.364.364 0 00.3666-.3705Z" />
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
