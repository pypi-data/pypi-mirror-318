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


class CivicrmIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "civicrm"

    @property
    def original_file_name(self) -> "str":
        return "civicrm.svg"

    @property
    def title(self) -> "str":
        return "CiviCRM"

    @property
    def primary_color(self) -> "str":
        return "#81C459"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CiviCRM</title>
     <path d="M22.565
 9.054c.248-.477.45-1.125.235-1.786-.25-.766-.939-1.275-2.051-1.511l-7.052-1.5L6.496.405C6.418.363
 5.717 0 4.951 0 4.38 0 3.888.198 3.527.571c-.337.349-.539.834-.603
 1.444a3.184 3.184 0 0 0-.199-.006c-1.089 0-1.648.456-1.926.839C.369
 3.44.315 4.241.638 5.23l2.649 8.118.251 7.033c.044 1.222.719 2.536
 2.098 2.537.264 0 .537-.051.82-.15.328.556.92 1.232 1.864 1.232.666 0
 1.324-.357 1.956-1.063l5.11-5.697 6.783-4.283c.147-.094 1.444-.95
 1.398-2.229-.022-.642-.362-1.202-1.002-1.674zM7.396
 20.166l-2.328-7.134-.316-8.847 8.326 1.771 6.771 3.622-5.63
 6.279-6.823 4.309zM20.377
 7.51c.545.116.709.279.72.313.021.063-.017.196-.087.344l-1.623-.868.99.211zM4.951
 1.792c.269 0
 .607.145.7.193l1.738.929-2.693-.573c.013-.323.08-.484.12-.526.012-.011.062-.023.135-.023zm-2.61
 2.882c-.195-.595-.093-.773-.092-.774.019-.026.167-.099.476-.099.083 0
 .159.005.221.011l.109 3.05-.714-2.188zm2.988 15.642l-.029-.798.514
 1.574a.68.68 0 0 1-.178.034c-.146 0-.293-.5-.307-.81zm3.614
 1.424c-.414.463-.62.468-.622.468-.058
 0-.185-.132-.301-.317l1.818-1.148-.895.997zm12.27-10.299l-1.445.913
 1.695-1.89c.249.174.313.298.314.329.006.133-.287.468-.564.648z" />
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
