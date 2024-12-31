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


class GodotEngineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "godotengine"

    @property
    def original_file_name(self) -> "str":
        return "godotengine.svg"

    @property
    def title(self) -> "str":
        return "Godot Engine"

    @property
    def primary_color(self) -> "str":
        return "#478CBF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Godot Engine</title>
     <path d="M9.5598.683c-1.096.244-2.1812.5831-3.1983
 1.0951.023.8981.081 1.7582.199
 2.6323-.395.253-.81.47-1.178.766-.375.288-.7581.564-1.0971.9011-.6781-.448-1.3962-.869-2.1352-1.2411C1.3532
 5.6934.608 6.6186 0 7.6546c.458.7411.936 1.4352 1.4521
 2.0942h.014v6.3565c.012 0 .023 0
 .035.003l3.8963.376c.204.02.364.184.378.3891l.12 1.7201
 3.3994.242.234-1.587c.03-.206.207-.358.415-.358h4.1114c.208 0
 .385.152.415.358l.234 1.587 3.3993-.242.12-1.72a.4196.4196 0
 01.378-.3891l3.8954-.376c.012 0
 .023-.003.035-.003v-.5071h.002V9.7498h.014c.516-.659.994-1.3531
 1.4521-2.0942-.608-1.036-1.3541-1.9611-2.1512-2.8192-.739.372-1.4571.793-2.1352
 1.2411-.339-.337-.721-.613-1.096-.901-.369-.296-.7841-.5131-1.1781-.7661.117-.8741.175-1.7342.199-2.6323-1.0171-.512-2.1012-.851-3.1983-1.095-.438.736-.838
 1.533-1.1871
 2.3121-.414-.069-.829-.094-1.2461-.099h-.016c-.417.005-.832.03-1.2461.099-.349-.779-.749-1.576-1.1881-2.3121l.001-.001zM6.4765
 9.9889c1.2971 0 2.3492 1.0511 2.3492 2.3482s-1.052 2.3482-2.3492
 2.3482c-1.296 0-2.3482-1.051-2.3482-2.3482 0-1.297 1.0511-2.3482
 2.3482-2.3482zm11.049 0c1.296 0 2.3482 1.0511 2.3482 2.3482s-1.0511
 2.3482-2.3482 2.3482-2.3492-1.051-2.3492-2.3482c0-1.297 1.051-2.3482
 2.3492-2.3482zm-10.824.9301c-.861 0-1.559.698-1.559 1.5591s.698
 1.5582 1.559 1.5582c.8611 0 1.5592-.698 1.5592-1.5582
 0-.86-.697-1.559-1.5591-1.559zm10.598 0c-.8611 0-1.5582.698-1.5582
 1.5591s.697 1.5582 1.5581 1.5582c.8611 0 1.5592-.698 1.5592-1.5582
 0-.86-.697-1.559-1.5592-1.559zm-5.2985.453c.417 0
 .757.308.757.6871v2.1622c0
 .379-.339.687-.757.687s-.756-.308-.756-.687V12.059c0-.379.339-.687.756-.687zM1.4601
 16.9464c.002.377.006.789.006.871 0 3.7014 4.6944 5.4795 10.5269
 5.5005h.014c5.8325-.02 10.5259-1.7991 10.5259-5.5004
 0-.084.005-.495.007-.871l-3.5023.338-.121 1.729a.421.421 0
 01-.389.3901l-4.1814.296a.4203.4203 0
 01-.415-.358l-.238-1.6141h-3.3863l-.238 1.6141a.4192.4192 0
 01-.4451.357l-4.1513-.296c-.208-.015-.375-.181-.389-.389l-.12-1.7292-3.5044-.337z"
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
