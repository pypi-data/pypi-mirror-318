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


class ScratchIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "scratch"

    @property
    def original_file_name(self) -> "str":
        return "scratch.svg"

    @property
    def title(self) -> "str":
        return "Scratch"

    @property
    def primary_color(self) -> "str":
        return "#4D97FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Scratch</title>
     <path d="M11.406
 11.312c-.78-.123-1.198-.654-.99-2.295l.023-.198c.175-1.426.321-1.743.996-1.706.198.013.426.14.654.33.211.247.68.568.945
 1.204.19.466.254.77.281 1.098l.042.402v-.002a.68.68 0 0 0
 1.342-.007c.008-.044.176-4.365.176-4.436
 0-.38-.302-.69-.68-.696a.685.685 0 0 0-.682.688c0 .009-.001.605-.014
 1.206-.536-.592-1.223-1.123-1.994-1.17-2.058-.11-2.283 1.811-2.419
 2.918l-.02.196c-.278 2.189.441 3.569 2.13 3.837 1.838.293 3.063.72
 3.074 1.868.007.446-.224.903-.627 1.254a2.163 2.163 0 0 1-1.749.507
 3.233 3.233 0 0
 1-.539-.141c-.24-.136-.847-.51-1.154-.942-.26-.364-.35-.937-.378-1.3.004-.163.005-.27.005-.283a.69.69
 0 0 0-.669-.703.689.689 0 0 0-.696.682c0 .013-.017 1.367-.066
 2.183-.07 1.313 0 2.426 0 2.474.028.382.35.67.727.644a.681.681 0 0 0
 .635-.733c0-.006-.033-.545-.029-1.29a5.21 5.21 0 0 0 1.938.773 3.451
 3.451 0 0 0 2.856-.82c.713-.619 1.122-1.464
 1.11-2.32-.024-2.555-2.865-3.004-4.228-3.222M14.174 0a5.51 5.51 0 0
 0-2.724.723h-.112c-2.637 0-4.937 1.392-6.15 3.728-.728 1.393-.9
 2.75-.999 3.579-.012.089-.018.17-.028.262-.12.974-.123 1.904-.01
 2.772a5.824 5.824 0 0 0-.625 2.529v.016a58.919 58.919 0 0 1-.057 1.95
 29.72 29.72 0 0 0-.008 2.94l.013.209C3.698 21.676 6.159 24 9.083
 24a5.516 5.516 0 0 0 3.463-1.21 8.357 8.357 0 0 0
 5.195-2.08c1.826-1.587 2.859-3.845
 2.83-6.19-.013-1.362-.346-2.638-.978-3.763.117-1.273.221-4.996.221-5.03
 0-3.103-2.484-5.67-5.539-5.727zm.056 2.675c1.642.03 2.978 1.412 2.978
 3.081 0 .038-.145 4.497-.215 4.883a3.152 3.152 0 0 1-.203.69c.756.89
 1.165 2 1.175 3.256.021 1.555-.681 3.076-1.926 4.16a5.763 5.763 0 0
 1-3.8 1.444 5.986 5.986 0 0 1-.718-.048 3.386 3.386 0 0 1-.172.215
 2.97 2.97 0 0 1-2.264 1.038c-1.573
 0-2.897-1.255-3.013-2.856l-.008-.122a27.366 27.366 0 0 1
 .005-2.662c.039-.679.06-1.831.062-2.08a3.124 3.124 0 0 1
 .783-2.025c-.237-.835-.312-1.836-.167-3.02l.024-.212c.083-.695.208-1.72.72-2.7.765-1.473
 2.168-2.318 3.848-2.318a4.568 4.568 0 0 1 .824.07c.546-.5 1.27-.81
 2.067-.794Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/LLK/scratch-link/blob/027e
3754ba6db976495e905023d5ac5e730dccfc/Assets/Windows/SVG/Windows%20Tray'''

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
