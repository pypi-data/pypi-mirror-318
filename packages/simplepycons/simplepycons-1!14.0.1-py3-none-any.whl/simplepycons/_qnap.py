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


class QnapIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qnap"

    @property
    def original_file_name(self) -> "str":
        return "qnap.svg"

    @property
    def title(self) -> "str":
        return "QNAP"

    @property
    def primary_color(self) -> "str":
        return "#0C2E82"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>QNAP</title>
     <path d="M1.3164 9.955C.438 9.955 0 10.3094 0 11.0177v1.9512c0
 .704.438 1.0566 1.3164
 1.0566h2.5703c0-.0061.1487.0049.377-.0293-.2145-.3087-.6112-.6434-.9825-.9121l-.0683-.0488H1.6133v-2.1133H3.744v1.793c.6399.1993
 1.0793.4554
 1.379.6992.0507-.1283.0761-.2763.0761-.4454v-1.9511c0-.6699-.3928-1.0238-1.1758-1.0606v-.002zm4.9649.0528c-.1551
 0-.274.044-.3575.1309-.1468.1535-.1164.3461-.1308.3535v3.5176h1.4453s-.0081-1.8582-.0117-2.4063c.0062-.036.0323-.088.1425-.0742
 0 0 .0426.0012.0606.0332.2786.445 2.1035 2.4473 2.1035
 2.4473h1.5v-4.002H9.5703v2.3281c-.022.0535-.095.044-.1308.006-.258-.399-1.2508-1.7643-1.5684-2.1993-.0202-.0243-.1248-.1348-.3555-.1348Zm6.584
 0c-.3665
 0-.6468.0763-.8438.2305-.202.1592-.3027.371-.3027.6387v3.1328h1.5273v-1.0664h2.1406v1.0664h1.5293V10.877c0-.2711-.0993-.4848-.2969-.6387-.197-.1542-.4793-.2305-.8457-.2305zm5.9179
 0c-.366
 0-.6481.0778-.8457.2324-.197.1533-.2976.361-.3027.6192v3.1504h1.5293v-1.045h2.4707c.6714
 0 1.0078-.268
 1.0078-.8085V10.873c0-.3081-.0845-.529-.248-.664-.2801-.2223-.743-.1877-.7032-.2012zm4.7246.0723c-.248.0126-.4473.2195-.4473.4707
 0 .259.2116.4687.4707.4687A.4684.4684 0 0 0 24
 10.5508c0-.2593-.2096-.4707-.4688-.4707-.008 0-.0154-.0004-.0234
 0zm.002.0683c.0068-.0003.0146 0 .0215 0
 .2213.0007.3998.1813.4004.4024a.3996.3996 0 0
 1-.4004.3984c-.221-.0005-.4001-.1777-.4004-.3984.0003-.2142.1675-.391.379-.4024zm-.1894.1407v.5332h.0722v-.2364c.0404-.0023.081.0013.1211.002.0326.0073.0642.0456.0684.0508.0452.0579.0807.1224.121.1836h.088l-.0918-.1445a.3512.3512
 0 0 0-.0586-.0703.1786.1786 0 0
 0-.043-.0274c.0514-.007.0887-.023.1133-.0488.0434-.0465.05-.1157.0137-.1758-.0217-.036-.0561-.0664-.166-.0664zm.0722.0586h.168c.1513
 0
 .134.1407.0586.168-.0737.0188-.1513.0064-.2266.0097zm-10.1465.7011h2.1407v1.1582H13.246zm5.8965
 0h1.9434v1.0371h-1.9434zm-16.3574 1.539c.4791.3043 1.3518.9071 1.6406
 1.4571h1.0879c-.1858-.3314-.814-1.1293-2.7285-1.457Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://marketing.qnap.com/resource/qnap-bran'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://marketing.qnap.com/resource/qnap-logo'''

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
        yield from [
            "Quality Network Appliance Provider",
        ]
