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


class DiscoverIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "discover"

    @property
    def original_file_name(self) -> "str":
        return "discover.svg"

    @property
    def title(self) -> "str":
        return "Discover"

    @property
    def primary_color(self) -> "str":
        return "#FF6000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Discover</title>
     <path d="M14.58 12a2.023 2.023 0 1 1-2.025-2.023h.002c1.118 0
 2.023.906 2.023 2.023zm-5.2-2.001c-1.124 0-2.025.884-2.025 1.99 0
 1.118.878 1.984 2.007 1.984.319 0
 .593-.063.93-.221v-.873c-.296.297-.559.416-.895.416-.747
 0-1.277-.542-1.277-1.312 0-.73.547-1.306 1.243-1.306.354 0
 .622.126.93.428v-.873a1.898 1.898 0 0 0-.913-.233zm-3.352
 1.545c-.445-.165-.576-.273-.576-.479 0-.239.233-.422.553-.422.222 0
 .405.091.598.308l.388-.508a1.665 1.665 0 0 0-1.117-.422c-.673
 0-1.186.467-1.186 1.089 0 .524.239.792.936
 1.043.291.103.438.171.513.217a.456.456 0 0 1 .222.394c0
 .308-.245.536-.576.536-.354
 0-.639-.177-.809-.507l-.479.461c.342.502.752.724 1.317.724.771 0
 1.311-.513 1.311-1.249-.002-.603-.252-.876-1.095-1.185zM24
 10.3a.29.29 0 0 1-.288.291.29.29 0 0 1-.291-.291v-.003A.29.29 0 1 1
 24 10.3zm-.059.001a.235.235 0 0 0-.231-.239.234.234 0 0 0-.232.239c0
 .132.104.239.232.239a.235.235 0 0 0 .231-.239zM3.472
 13.887h.742v-3.803h-.742v3.803zm12.702-1.248l-1.014-2.554h-.81l1.614
 3.9h.399l1.643-3.9h-.804l-1.028 2.554zm2.166
 1.248h2.104v-.644h-1.362v-1.027h1.312v-.644h-1.312v-.844h1.362v-.644H18.34v3.803zm5.409-3.557l.11.138h-.097l-.094-.13v.13h-.08v-.334h.107c.081
 0
 .126.036.126.103.001.046-.025.08-.072.093zm-.006-.092c0-.029-.021-.043-.06-.043h-.014v.087h.014c.039
 0 .06-.014.06-.044zm-1.228 2.047l1.197
 1.602H22.8l-1.027-1.528h-.097v1.528h-.741v-3.803h1.1c.855 0 1.346.411
 1.346 1.123 0 .583-.308.965-.866
 1.078zm.103-1.038c0-.37-.251-.563-.713-.563h-.228v1.152h.217c.473-.001.724-.207.724-.589zm-19.487.742a1.91
 1.91 0 0 1-.69
 1.46c-.365.303-.781.439-1.357.439H.001v-3.803H1.09c1.202 0 2.041.781
 2.041
 1.904zm-.764-.006c0-.364-.154-.718-.411-.947-.245-.222-.536-.308-1.015-.308H.742v2.515h.199c.479
 0 .782-.092 1.015-.302.256-.228.411-.593.411-.958z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.discovernetwork.com/en-us/busines'''

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
