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


class AccusoftIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "accusoft"

    @property
    def original_file_name(self) -> "str":
        return "accusoft.svg"

    @property
    def title(self) -> "str":
        return "Accusoft"

    @property
    def primary_color(self) -> "str":
        return "#A9225C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Accusoft</title>
     <path d="M14.1774
 4.2143c-.3824.0022-4.0063.02-4.3665.0222-.618.0044-.776-.0044-.8738.109-.0511.06-.1334.1645.1535.5246.2868.358
 8.7775 11.221 8.9931
 11.481.2735.3313.527.4447.638.4625.178.0267.4003-.0667.5203-.1134.1179-.0467
 4.3243-1.7853
 4.4155-1.8342.14-.0756.1312-.289.0378-.4469-.0934-.16-.229-.3335-.3069-.429-.08-.0957-7.6903-9.1956-7.7703-9.2956-.1467-.1845-.3602-.3602-.4447-.389-.0845-.029-.2045-.0935-.996-.0912zm-4.0152
 5.1313s-.4492.06-.9427.5625c-.338.349-9.0776 8.9487-9.1243
 9.0154-.0423.06-.1468.1756-.0645.2401.0422.0333.4513-.1.6559-.1734.0289
 0 4.2931-1.3607
 4.2931-1.3607.02-.0222-.0022-.0022.0222-.02-.0133-.189-.0289-.9804-.0355-1.036-.02-.1579.0556-.2223.109-.258.0533-.0355.1533-.0755.1533-.0755l3.4706-1.265c.0222-.029
 3.3193-3.0638
 3.3838-3.1216v-.0422c-.029-.0222-.04-.06-.0645-.0867-.0156-.0067-1.8564-2.3856-1.8564-2.3789zm1.8497
 5.0624c-.1156.0089-.3601.029-.5424.109-.1823.08-5.4426 1.9787-5.6316
 2.052-.189.0734-.4269.1334-.4135.2846.0066.0934.0733.1.1734.1312.1.0333
 11.2786 2.5212 11.5477 2.5768.269.0556 1.1294.2934
 1.5763.2045.24-.0334.3535-.0934.4313-.14.0778-.0467 4.6422-2.8503
 4.7156-2.9037.0711-.0533.1223-.0889.1312-.1756.0044-.0333-.0912-.109-.1957-.1312a321.6128
 321.6128 0 0 0-1.1139-.2179l-.309-.0555s-4.311 1.8897-4.4065
 1.9342c-.12.0556-.2935.1-.4447.0867-.3157-.0289-.558-.2067-.9293-.6336l-2.1388-2.7724s-.936-.1512-1.2673-.1957c-.3313-.0445-1.0671-.16-1.1828-.1534z"
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
