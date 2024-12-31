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


class PleskIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "plesk"

    @property
    def original_file_name(self) -> "str":
        return "plesk.svg"

    @property
    def title(self) -> "str":
        return "Plesk"

    @property
    def primary_color(self) -> "str":
        return "#52BBE6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Plesk</title>
     <path d="M6.102
 7.021v7.353h.736V7.02zm13.655.01v7.343h.735V7.032zm.735 4.633l2.479
 2.71h1.019l-2.574-2.731L24 9.122h-.987zm-4.008-2.636c-.536
 0-.972.125-1.31.378-.337.252-.505.609-.505 1.07 0
 .26.049.474.148.642.1.168.226.306.38.415.154.108.328.198.522.267.194.07.39.134.59.19.175.049.342.1.5.152.158.052.297.117.418.194.12.077.216.17.286.278.07.109.104.244.104.405
 0 .21-.095.388-.286.535-.19.147-.484.221-.88.221-.609
 0-1.104-.245-1.485-.735l-.572.504c.286.315.59.54.913.678.322.136.693.204
 1.11.204.272 0 .527-.033.766-.1a1.89 1.89 0
 00.621-.294c.176-.13.316-.288.419-.478.102-.189.153-.402.153-.64
 0-.26-.051-.474-.153-.646a1.46 1.46 0 00-.402-.436 2.284 2.284 0
 00-.545-.289 13.019 13.019 0
 00-.594-.205c-.161-.049-.317-.1-.467-.152a2.013 2.013 0
 01-.397-.184.923.923 0 01-.275-.252.598.598 0
 01-.104-.357c0-.203.075-.371.225-.504.15-.133.413-.2.787-.2.293 0
 .546.055.759.163.213.109.41.278.594.51l.011.01.54-.494c-.272-.315-.556-.535-.853-.661a2.586
 2.586 0 00-1.018-.19zm-14.688.041c-.588
 0-1.187.095-1.796.284v7.626h.725v-2.72c.182.048.364.087.546.115a3.539
 3.539 0
 001.586-.11c.336-.102.635-.261.898-.478.263-.217.474-.494.636-.83.16-.336.241-.739.241-1.208
 0-.385-.067-.742-.2-1.071a2.42 2.42 0 00-.572-.851 2.636 2.636 0
 00-.898-.557c-.35-.133-.739-.2-1.166-.2zm8.886 0c-.322
 0-.627.055-.914.163-.287.11-.54.275-.756.5a2.391 2.391 0
 00-.515.845c-.126.34-.189.74-.189 1.202 0
 .35.052.683.157.998.106.315.263.596.473.84.21.246.473.44.788.583.315.144.683.216
 1.103.216.455 0 .844-.068
 1.166-.205.322-.137.605-.338.85-.604l-.44-.462c-.204.224-.431.387-.683.488a2.226
 2.226 0 01-.84.153c-.554
 0-.992-.175-1.314-.526-.322-.35-.493-.822-.514-1.417h3.939c.013-.904-.176-1.592-.568-2.064-.392-.473-.973-.71-1.743-.71zm.031.62c.26
 0
 .487.04.683.121.196.08.355.187.478.32.122.133.217.295.284.484.066.189.1.392.1.609H9.074a2.126
 2.126 0
 01.494-1.103c.111-.126.264-.23.456-.31.193-.08.422-.12.688-.12zM1.86
 9.7c.616 0 1.094.188 1.434.563.34.374.51.866.51 1.475 0 .659-.185
 1.165-.552 1.518-.368.354-.863.53-1.486.53-.168
 0-.342-.018-.52-.057a4.836 4.836 0
 01-.52-.142V9.868c.182-.063.367-.107.557-.132.189-.024.38-.036.577-.036zm2.377
 6.588v.692H8.66v-.692z" />
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
