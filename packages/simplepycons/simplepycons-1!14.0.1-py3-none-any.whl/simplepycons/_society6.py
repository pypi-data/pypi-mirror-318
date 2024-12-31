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


class SocietySixIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "society6"

    @property
    def original_file_name(self) -> "str":
        return "society6.svg"

    @property
    def title(self) -> "str":
        return "Society6"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Society6</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0zm7.928
 4.966l.042.876-.916.157c-.705.194-1.32.465-1.843.813s-.966.73-1.33
 1.148a6.147 6.147 0 0 0-.888 1.339l-.016.036c-.243.506-.459 1.04-.65
 1.599a4.992 4.992 0 0 1 1.31-.812l.033-.012c.521-.223 1.141-.335
 1.864-.335.839 0 1.543.296 2.111.884s.853 1.355.853 2.298c0
 1.409-.541 2.628-1.624 3.659s-2.414 1.547-3.992 1.547c-1.255
 0-2.256-.374-3.003-1.122s-1.12-1.743-1.12-2.981c0-2.363.84-4.387
 2.52-6.073s3.895-2.692 6.65-3.023zM7.925 9.103c.435 0 .838.027
 1.211.081.388.055.739.159
 1.065.307l-.024-.01c.286.13.524.322.705.56l.003.004c.169.232.252.513.252.844s-.118.614-.356.852c-.237.238-.549.356-.933.356-.332
 0-.607-.091-.828-.272s-.399-.394-.537-.642c-.137-.253-.247-.516-.327-.784s-.146-.493-.197-.674c-.401.024-.765.178-1.094.459s-.495.629-.495
 1.046c0
 .253.039.452.116.596s.184.265.311.358l.003.002c.162.115.348.217.544.296l.018.006c.151.069.431.177.714.279l.132.041c.778.288
 1.365.635 1.76 1.038.321.328.509.742.569 1.241-.008-.117.117
 1.109.018.183.002.056.006.113.006.171 0 .433-.097.847-.289
 1.245s-.464.728-.818.992a4.26 4.26 0 0
 1-1.336.646l-.03.007c-.516.147-1.172.221-1.967.221-.722
 0-1.318-.061-1.789-.184s-.845-.282-1.12-.474c-.281-.193-.473-.398-.575-.617s-.155-.425-.155-.617c0-.349.125-.655.373-.916s.58-.391.991-.391c.344
 0
 .631.092.863.278.236.193.43.426.574.691l.006.012c.136.244.259.528.352.824l.009.032c.035.09.106.322.172.556l.034.139c.647
 0 1.137-.144
 1.469-.436s.498-.691.498-1.196c0-.222-.05-.408-.15-.558s-.234-.283-.399-.398c-.166-.108-.377-.213-.635-.315s-.513-.198-.765-.289c-.693-.246-1.24-.587-1.644-1.023s-.605-.978-.605-1.628v-.013c0-.391.093-.76.259-1.087l-.006.014c.17-.34.434-.654.794-.944.355-.276.804-.496
 1.348-.661s1.179-.249 1.906-.249zm8.017 1.874c-.329
 0-.64.066-.933.199s-.605.397-.934.792c-.04.183-.109.534-.21
 1.055s-.152 1.162-.152 1.923c0 .778.123 1.384.365
 1.82s.566.655.968.655c.626 0 1.168-.432
 1.628-1.295h.002c.46-.864.69-1.912.69-3.144
 0-.618-.134-1.108-.402-1.468s-.608-.538-1.022-.538z" />
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
