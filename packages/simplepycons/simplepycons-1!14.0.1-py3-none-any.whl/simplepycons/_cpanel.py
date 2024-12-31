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


class CpanelIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cpanel"

    @property
    def original_file_name(self) -> "str":
        return "cpanel.svg"

    @property
    def title(self) -> "str":
        return "cPanel"

    @property
    def primary_color(self) -> "str":
        return "#FF6C2C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>cPanel</title>
     <path d="M4.586 9.346a.538.538 0 00-.34.113.561.561 0
 00-.197.299L2.74 14.654h.922a.528.528 0 00.332-.113.561.561 0
 00.2-.291l.968-3.604h.744a.677.677 0 01.317.077.703.703 0
 01.24.199.732.732 0 01.129.281.65.65 0 01-.01.326.698.698 0
 01-.676.526h-.385a.538.538 0 00-.337.113.561.561 0
 00-.2.291l-.24.896h1.201a1.939 1.939 0 001.62-.867 1.988 1.988 0
 00.265-.586l.027-.1a1.854 1.854 0 00.026-.907 1.973 1.973 0
 00-1.031-1.34 1.875 1.875 0 00-.88-.21H4.587zm18.447 0a.401.401 0
 00-.25.082.377.377 0 00-.14.217l-1.334 5.01a1.7 1.7 0 00.57-.096
 1.806 1.806 0 00.496-.266 1.74 1.74 0 00.385-.408 1.648 1.648 0
 00.234-.531l.996-3.696a.23.23 0 00-.045-.217.246.246 0
 00-.2-.095h-.712zM8.381 10.643l-.133.503a.564.564 0
 00-.006.26.544.544 0 00.1.221.552.552 0 00.185.154.53.53 0
 00.252.06h2.157a.101.101 0 01.084.038.098.098 0
 01.015.088l-.02.072-.324 1.201-.013.055a.172.172 0
 01-.067.105.205.205 0 01-.127.04H9.178a.147.147 0 01-.12-.057.136.136
 0 01-.027-.13c.022-.074.071-.112.147-.112h.808a.53.53 0
 00.332-.112.564.564 0 00.2-.293l.132-.498H8.84a1.131 1.131 0
 00-.38.065 1.152 1.152 0 00-.323.176 1.194 1.194 0 00-.256.271 1.052
 1.052 0 00-.156.346l-.028.1a1.095 1.095 0 00-.013.533 1.203 1.203 0
 00.212.464 1.141 1.141 0 00.918.453l2.157.006a.899.899 0
 00.875-.67l.525-1.95a1.101 1.101 0 00.01-.514 1.114 1.114 0
 00-.205-.444 1.149 1.149 0 00-.377-.312 1.048 1.048 0
 00-.498-.12H8.38zm-6.397.01a1.924 1.924 0 00-.638.107 1.989 1.989 0
 00-.553.295 1.962 1.962 0 00-.7 1.045l-.027.1a1.936 1.936 0
 00-.023.905 1.955 1.955 0 00.361.786 1.986 1.986 0 00.668.554 1.875
 1.875 0 00.88.21h.464l.266-.983a.23.23 0 00-.043-.215.239.239 0
 00-.198-.096h-.423a.702.702 0 01-.319-.074.67.67 0
 01-.24-.195.732.732 0 01-.127-.281.706.706 0 01.01-.34.73.73 0
 01.256-.377.675.675 0 01.42-.14h.697a.538.538 0 00.338-.114.561.561 0
 00.199-.297l.232-.89h-1.5zm11.08 0l-.982 3.689a.23.23 0
 00.045.217.238.238 0 00.195.095h.711a.413.413 0 00.248-.08.363.363 0
 00.143-.21l.644-2.41h.745a.678.678 0 01.318.075.708.708 0
 01.238.2.735.735 0 01.129.28.65.65 0 01-.01.327l-.398 1.506a.243.243
 0 00.24.312h.713a.403.403 0 00.244-.08.366.366 0
 00.143-.213l.332-1.248a1.897 1.897 0 00.029-.908 1.955 1.955 0
 00-.361-.79 1.987 1.987 0 00-.668-.554 1.889 1.889 0
 00-.885-.209h-1.813zm5.793 0a1.458 1.458 0 00-.488.081 1.489 1.489 0
 00-.752.58 1.493 1.493 0 00-.205.454l-.406 1.505a1.018 1.018 0
 00-.016.508 1.139 1.139 0 00.205.446 1.095 1.095 0 00.377.312 1.071
 1.071 0 00.498.115h2.502a.528.528 0 00.332-.113.561.561 0
 00.2-.291l.21-.791h-2.748a.2.2 0 01-.191-.252l.299-1.127a.34.34 0
 01.113-.162.281.281 0 01.18-.064h1.232a.153.153 0
 01.147.193l-.026.1c-.022.075-.071.113-.146.113h-.81a.538.538 0
 00-.339.111.526.526 0 00-.191.293l-.133.49h2.004a.887.887 0
 00.547-.181.864.864 0 00.32-.483l.12-.45a1.11 1.11 0 00.013-.513
 1.076 1.076 0 00-.203-.443 1.146 1.146 0 00-.375-.313 1.047 1.047 0
 00-.498-.119h-1.772Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://cpanel.net/company/cpanel-brand-guide'''

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
