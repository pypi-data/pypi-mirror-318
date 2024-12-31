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


class ReactBootstrapIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "reactbootstrap"

    @property
    def original_file_name(self) -> "str":
        return "reactbootstrap.svg"

    @property
    def title(self) -> "str":
        return "React Bootstrap"

    @property
    def primary_color(self) -> "str":
        return "#41E0FD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>React Bootstrap</title>
     <path d="M7.679.6264c-.5006
 0-.948.1121-1.3298.333-.367.2125-.6755.5291-.917.9411-.2262.386-.393.856-.4957
 1.3964-.1978 1.0417-.155 2.3459.124
 3.7707.0353.1794.074.361.1157.5414a17 17 0 0
 0-.6444.209c-1.345.469-2.4699 1.0817-3.2528
 1.7723-.406.3576-.72.7357-.9349 1.1235C.1158 11.1263 0 11.5493 0
 11.9712c0 .846.4686 1.703 1.355 2.4806.8347.7323 2.015 1.3717 3.4123
 1.8496.1298.0441.262.087.3948.128a17 17 0 0 0-.1281.609c-.2658
 1.3994-.2968 2.6799-.0903 3.7032.1073.53.2776.9912.5063
 1.371.2432.4038.5519.7156.9174.9264.3851.222.8384.3346
 1.3472.3346.6927 0 1.4672-.2054 2.302-.6105.8184-.3971 1.6537-.9659
 2.4827-1.6905a13 13 0 0 0 .3909-.3556h.1963v-.0004h5.9501q1.3018 0
 2.2457-.38c.6305-.2529 1.1436-.5942
 1.5475-1.0227.4038-.4286.6983-.9399.8871-1.5339.1888-.589.2831-1.227.2831-1.9087.0005-1.1884-.2152-2.1719-.6416-2.9608q-.6346-1.1668-1.867-1.5139a.032.032
 0 0 1-.0202-.0321.034.034 0 0 1 .0154-.0303c.6118-.3401 1.082-.8245
 1.4115-1.4425q.498-.9348.498-2.2499c0-1.4464-.366-2.5224-1.0946-3.238-.7287-.7158-1.6988-1.0715-2.9064-1.0715h-6.5124a16
 16 0 0
 0-.308-.2819c-.8608-.7637-1.7192-1.363-2.552-1.7796C9.1688.8432
 8.3802.6264 7.679.6264m.0072 1.6994c.4338 0 .9952.1703
 1.623.4925.6806.3497 1.4185.8697 2.1341
 1.5051q.0666.0591.1361.1228c-.6294.696-1.2497 1.4694-1.846
 2.302-1.016.0992-1.9927.2474-2.9071.441a15 15 0 0
 1-.0925-.4342l-.0027-.0149c-.218-1.1138-.2711-2.1316-.1536-2.9418.1015-.6963.3287-1.194.6245-1.3653.1228-.0712.2858-.1072.4842-.1072m5.1605
 3.217v12.9119l-.7657-.9454-.5002-.6175c-.2525-.3117-.657-.8886-1.1391-1.624a29
 29 0 0
 1-.7951-1.2816l-.0145-.025c-.231-.3984-.4027-.7193-.5406-.977a39 39 0
 0 1-.5065-.9813l.03-.0583.0018-.0033a31 31 0 0 1
 .5659-1.0979l.0017-.003.2074-.4024.3063-.5075.002-.0033c.1143-.1947.233-.3912.3526-.584l.2108-.3482c.2806-.4645.5061-.8033.862-1.2943.1917-.2642.3735-.4962.6616-.8562l.0006-.0007.0142-.018.0055-.007c.117-.1491.235-.2961.3509-.4369l.0038-.0047.0023-.0028a83
 83 0 0 1 .6822-.8317zm2.3907.2519h3.8286c.6423 0 1.1336.1804
 1.4735.5363s.5097.9744.5097 1.8516c0 .7803-.1888 1.375-.5667
 1.7942-.378.419-.85.624-1.4169.624h-3.8284c-.0141
 0-.0256-.0149-.0256-.0332l.0002-4.7399c0-.0182.0113-.033.0256-.033M8.498
 8.6164a31.5 31.5 0 0 0-.7931 1.375 23 23 0 0 1-.4173-1.1595 23 23 0 0
 1 1.2104-.2155m-2.8646.6334c.288.8924.6483 1.8157 1.0715
 2.7477l.0002.0001c-.4297.9474-.795 1.8853-1.087 2.791a12 12 0 0
 1-.3005-.0982c-1.1617-.397-2.1292-.9097-2.798-1.4823-.5116-.4381-.817-.9003-.817-1.2364
 0-.345.3055-.7895.8384-1.2203.6203-.5016 1.503-.96 2.551-1.3252a15 15
 0 0 1 .5414-.1764m9.6038 3.5427h4.1484c.718 0 1.2696.2244
 1.67.692s.597 1.1257.597 1.9883c.0002.8771-.2004 1.5595-.5968
 2.037-.3932.4822-.952.7218-1.67.7218h-4.1486c-.0141
 0-.0256-.0148-.0256-.033v-5.373c0-.0183.0113-.033.0256-.033M7.7065
 14.001a31.4 31.4 0 0 0 .818 1.411 22 22 0 0
 1-1.251-.2087v-.0001c.1291-.3932.2742-.7959.433-1.2022m-.8937
 2.8444c.9022.1846 1.8901.3238 2.9408.414.602.8384 1.2275 1.617 1.8615
 2.317-.0783.0721-.1572.143-.2357.212-.9178.8022-1.8394 1.3821-2.6649
 1.6771l-.0171.0061c-.37.1306-.7003.1969-.9812.1969-.2073
 0-.3747-.036-.4975-.1067-.299-.1725-.5317-.6594-.6384-1.336-.1247-.7884-.081-1.7816.126-2.872l.0001.0001c.0323-.1692.0677-.3393.1064-.5085"
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
        return '''https://github.com/react-bootstrap/react-boot
strap/blob/be23c304fa40ddb209919b0faac1e5dd8cef53ad/www/static/img/log'''

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
