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


class JsdelivrIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jsdelivr"

    @property
    def original_file_name(self) -> "str":
        return "jsdelivr.svg"

    @property
    def title(self) -> "str":
        return "jsDelivr"

    @property
    def primary_color(self) -> "str":
        return "#E84D3D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>jsDelivr</title>
     <path d="M11.851 0L.811 4.02l1.56 14.7L11.85 24l9.6-5.28
 1.74-14.76zm.062 4.622a6.668 6.75 0 0 1 2.666.572 12.507 12.507 0 0
 0-2.59 1.95c-.045-.02-.092-.031-.138-.045a1.181 1.181 0 0
 0-.346-.056c-.071 0-.141.01-.21.021a8.91 8.91 0 0 1-.615-2.318 6.668
 6.75 0 0 1 1.171-.122 6.668 6.75 0 0 1 .062-.002zm-1.99.312a9.763
 9.763 0 0 0 .69 2.504 1.213 1.213 0 0 0-.328.825 1.202 1.202 0 0 0
 .18.63c-.937 1.294-1.656 2.803-1.905
 4.31-.01.056-.013.11-.02.166-.282.09-.515.284-.656.54-.987-.333-1.885-.968-2.615-2.022a6.668
 6.75 0 0 1-.026-.515 6.668 6.75 0 0 1 4.68-6.438zm5.507.709a6.668
 6.75 0 0 1 2.53 2.9c-.377.953-1.049 1.892-1.893 2.727a1.242 1.242 0 0
 0-.644-.184 1.243 1.243 0 0
 0-.768.27c-.462-.354-.91-.737-1.318-1.168-.333-.35-.637-.73-.921-1.123.19-.215.31-.494.31-.802
 0-.212-.061-.41-.159-.586 1.058-1.008 2.112-1.67 2.863-2.034zm-3.925
 1.982a.624.624 0 0 1 .346.114.624.624 0 0 1 .292.524.624.624 0 0
 1-.292.524.626.626 0 0 1-.346.113.634.634 0 0
 1-.638-.637c0-.355.283-.638.638-.638zm-.441 1.771a1.205 1.205 0 0 0
 .675.062c.036.05.075.097.112.148a11.438 11.438 0 0 0 .921 1.119
 12.103 12.103 0 0 0 1.446 1.277c-.032.11-.054.224-.054.342a1.236
 1.236 0 0 0 .066.38 9.91 9.91 0 0 1-2.118
 1.042c-.087.029-.173.052-.261.078a7.735 7.735 0 0 1-1.87.332 1.15
 1.15 0 0 0-.66-.773c.004-.024.005-.049.01-.073.219-1.333.873-2.73
 1.733-3.934zm7.272.19a6.668 6.75 0 0 1 .245 1.786 6.668 6.75 0 0
 1-.259 1.856 9.993 9.993 0 0 1-1.666-.63 1.243 1.243 0 0 0-.065-.713
 9.434 9.434 0 0 0 1.745-2.3zm-2.913 2.101c.367 0
 .657.291.657.658s-.291.657-.657.657c-.367
 0-.658-.29-.658-.657s.29-.658.658-.658zm.837 1.59a10.79 10.79 0 0 0
 1.802.688 6.668 6.75 0 0 1-6.149 4.157 6.668 6.75 0 0 1-.062-.004
 6.668 6.75 0 0 1-.042
 0c-.087-.042-.168-.08-.266-.129-.312-.154-.667-.352-.846-.5a3.796
 3.796 0 0 1-1.294-2.03c.21-.111.38-.284.487-.495a8.428 8.428 0 0 0
 1.96-.306 9.11 9.11 0 0 0 .513-.154 11.083 11.083 0 0 0
 2.341-1.13c.205.143.452.23.719.23a1.248 1.248 0 0 0
 .837-.328zm-10.707.116a5.761 5.761 0 0 0 2.212 1.298 1.146 1.146 0 0
 0 .857.87 4.602 4.602 0 0 0 1.24 2.222 6.668 6.75 0 0
 1-4.31-4.39zm3.327.464c.331 0
 .595.263.595.596s-.264.595-.595.595a.59.59 0 0 1-.596-.595.591.591 0
 0 1 .596-.596z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/jsdelivr/www.jsdelivr.com/
blob/eff02f3a8879cf7c7296840584e1293fe04e3a76/src/public/img/logo_hori'''

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
