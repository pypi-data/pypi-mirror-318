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


class SwaggerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "swagger"

    @property
    def original_file_name(self) -> "str":
        return "swagger.svg"

    @property
    def title(self) -> "str":
        return "Swagger"

    @property
    def primary_color(self) -> "str":
        return "#85EA2D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Swagger</title>
     <path d="M12 0C5.383 0 0 5.383 0 12s5.383 12 12 12c6.616 0
 12-5.383 12-12S18.616 0 12 0zm0 1.144c5.995 0 10.856 4.86 10.856
 10.856 0 5.995-4.86 10.856-10.856 10.856-5.996
 0-10.856-4.86-10.856-10.856C1.144 6.004 6.004 1.144 12 1.144zM8.37
 5.868a6.707 6.707 0 0 0-.423.005c-.983.056-1.573.517-1.735
 1.472-.115.665-.096 1.348-.143 2.017-.013.35-.05.697-.115
 1.038-.134.609-.397.798-1.016.83a2.65 2.65 0 0
 0-.244.042v1.463c1.126.055 1.278.452 1.37 1.629.033.429-.013.858.015
 1.287.018.406.073.808.156 1.2.259 1.075 1.307 1.435 2.575
 1.218v-1.283c-.203 0-.383.005-.558
 0-.43-.013-.591-.12-.632-.535-.056-.535-.042-1.08-.075-1.62-.064-1.001-.175-1.988-1.153-2.625.503-.37.868-.812.983-1.398.083-.41.134-.821.166-1.237.028-.415-.023-.84.014-1.25.06-.665.102-.937.9-.91.12
 0 .235-.017.369-.027v-1.31c-.16 0-.31-.004-.454-.006zm7.593.009a4.247
 4.247 0 0 0-.813.06v1.274c.245 0 .434 0
 .623.005.328.004.577.13.61.494.032.332.031.669.064 1.006.065.669.101
 1.347.217 2.007.102.544.475.95.941 1.283-.817.549-1.057 1.333-1.098
 2.215-.023.604-.037 1.213-.069
 1.822-.028.554-.222.734-.78.748-.157.004-.31.018-.484.028v1.305c.327
 0 .627.019.927 0 .932-.055 1.495-.507 1.68-1.412.078-.498.124-1
 .138-1.504.032-.461.028-.927.074-1.384.069-.715.397-1.01
 1.112-1.057a.972.972 0 0 0
 .199-.046v-1.463c-.12-.014-.204-.027-.291-.032-.536-.023-.804-.203-.937-.71a5.146
 5.146 0 0
 1-.152-.993c-.037-.618-.033-1.241-.074-1.86-.08-1.192-.794-1.753-1.887-1.786zm-6.89
 5.28a.844.844 0 0 0-.083 1.684h.055a.83.83 0 0 0
 .877-.78v-.046a.845.845 0 0 0-.83-.858zm2.911 0a.808.808 0 0
 0-.834.78c0 .027 0 .05.004.078 0 .503.342.826.859.826.507 0
 .826-.332.826-.853-.005-.503-.342-.836-.855-.831zm2.963 0a.861.861 0
 0 0-.876.835c0
 .47.378.849.849.849h.009c.425.074.853-.337.881-.83.023-.457-.392-.854-.863-.854z"
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
