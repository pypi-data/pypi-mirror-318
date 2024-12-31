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


class FireflyIiiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fireflyiii"

    @property
    def original_file_name(self) -> "str":
        return "fireflyiii.svg"

    @property
    def title(self) -> "str":
        return "Firefly III"

    @property
    def primary_color(self) -> "str":
        return "#CD5029"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Firefly III</title>
     <path d="M10.107 0s.917 3.103-.842 4.91c-1.76 1.807-1.57
 3.803-.856 4.754.713.951.665 1.664.095
 2.187-.57.523-1.046.904-1.379.048-.333-.856-.713-.856-.856-1.284a43.535
 43.535 0 0 0-.428-1.189s-.903 1.427-1.474 2.283c-.57.855-.57
 2.187-.19 2.9.38.713.238 1.569-.047 2.757-.286 1.189.095 2.996 1.426
 3.709 1.331.713 2.948 1.283 3.66 1.949.714.666 2.378 1.284 4.518.808
 2.14-.475 4.85-2.662 5.324-4.136 0 0 1.237-1.379
 1-3.185-.239-1.807-1.095-1.76-1.475-3.138-.38-1.38.823-1.04-.19-3.406
 0 0-.452-1.127-2.168-1.939-1.102-.521-.352-2.88-2.3-5.258C11.974.393
 10.106 0 10.106 0zm-.326 11.753c1.373-.01 2.14 1.376 2.14 1.376
 1.78-.216 3.533.152 4.374.94.531.498.965.956 1.181
 1.834-.1-.034-.282-.08-.52-.076a1.875 1.875 0 0
 0-.902.256s-.99-.333-1.52.097c-.55.446-.604.968-.576 1.586 0 0
 .476-1.628 1.68-1.208 0 0-.852 1.5.472 1.762 0 0
 .313-.002.57-.158.247-.148.44-.424.361-.92 0 0-.16-.494-.577-.794 0 0
 .378-.267 1.096-.104.035.238.056.503.063.802.047 2.057-1.326
 3.402-1.326 3.402v.927c-.167.334-.445.445-1.39.445-.946
 0-1.076-.26-1.076-.26v-.185c-1.446.186-2.234 0-2.234 0 0 .167 0
 .195-.14.334-.138.139-1
 .148-1.65.055-.649-.092-.574-.407-.574-.407v-.946a3.663 3.663 0 0
 1-1.354-1.873l-.61.012c-.334
 0-.477-.428-.477-.428v-1.379c0-.428.428-.523.428-.523l.594-.045c.201-1.426
 1.688-2.522
 1.688-2.522l-.083-1.966c.125-.023.246-.033.362-.034zm-.548
 4.716a.352.352 0 0 0-.353.352.352.352 0 0 0 .353.352.352.352 0 0 0
 .352-.352.352.352 0 0
 0-.352-.352zm6.85.301s.124.031.39.469c.257.425-.182.635-.182.635-.827.063-.208-1.104-.208-1.104z"
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
        return '''https://docs.firefly-iii.org/explanation/more'''

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
