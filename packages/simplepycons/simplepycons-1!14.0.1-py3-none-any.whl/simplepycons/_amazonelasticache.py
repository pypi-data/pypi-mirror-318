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


class AmazonElasticacheIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "amazonelasticache"

    @property
    def original_file_name(self) -> "str":
        return "amazonelasticache.svg"

    @property
    def title(self) -> "str":
        return "Amazon ElastiCache"

    @property
    def primary_color(self) -> "str":
        return "#C925D1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Amazon ElastiCache</title>
     <path d="M16.714 21.024v-2.508c-1.086.701-3.041 1.033-4.905
 1.033-2.031 0-3.615-.355-4.524-.962v2.437c0 .726 1.692 1.476 4.524
 1.476 2.89 0 4.905-.778 4.905-1.476m-4.905-5.286c-2.031
 0-3.615-.355-4.524-.962v2.447c.014.723 1.703 1.469 4.524 1.469 2.882
 0 4.892-.774 4.905-1.47v-2.517c-1.086.702-3.041 1.033-4.905
 1.033zm4.905-2.327v-2.898c-1.086.701-3.041 1.033-4.905 1.033-2.031
 0-3.615-.354-4.524-.962v2.828c.014.723 1.703 1.468 4.524 1.468 2.882
 0 4.892-.773 4.905-1.47m-9.43-4.2v.004h.001v.005c.014.723 1.703 1.468
 4.524 1.468 3.147 0 4.892-.866
 4.905-1.47v-.003l.001-.003c0-.604-1.747-1.477-4.906-1.477-2.833
 0-4.525.75-4.525 1.477m10.287.011v4.181h.001v7.621c0 1.603-2.988
 2.333-5.763 2.333-3.268
 0-5.38-.916-5.38-2.333v-3.796l-.002-.013h.001v-3.798l-.001-.014h.001V9.225l-.001-.013c0-1.418
 2.113-2.335 5.382-2.335 2.776 0 5.763.73 5.763 2.335zm6-5.527A.43.43
 0 0 0 24 3.266V1.072a.43.43 0 0 0-.429-.429H.428A.43.43 0 0 0 0
 1.072v2.194c0 .237.191.429.428.429.523 0
 .949.423.949.943s-.426.943-.949.943A.43.43 0 0 0 0 6.009v8.778c0
 .237.191.429.428.429h4.286v-.857H2.57v-1.286h2.143v-.857H2.142a.43.43
 0 0 0-.428.428v1.715H.857V6.386a1.804 1.804 0 0 0
 1.377-1.748c0-.846-.587-1.557-1.377-1.75V1.5h22.286V2.89a1.805 1.805
 0 0 0-1.378 1.749c0 .845.588 1.556 1.378
 1.748v7.973h-.857v-1.715a.43.43 0 0
 0-.429-.428h-2.571v.857h2.142v1.286h-2.142v.857h4.285a.43.43 0 0 0
 .429-.429V6.01a.43.43 0 0 0-.429-.428.947.947 0 0
 1-.949-.943c0-.52.426-.943.95-.943zM6.857 6.644v-3.43a.43.43 0 0
 0-.428-.428H3.857a.43.43 0 0 0-.428.429V10.5c0
 .237.191.429.428.429h1.286v-.857h-.857v-6.43H6v3zm12.857
 3.429h-.428v.857h.857a.43.43 0 0 0 .428-.429V3.215a.43.43 0 0
 0-.428-.429H17.57a.43.43 0 0
 0-.428.429v3.429H18v-3h1.714zm-3.428-3.858v-3a.43.43 0 0
 0-.43-.429h-3a.43.43 0 0
 0-.428.429v2.571h.858V3.643h2.142v2.572zm-5.572-.429V3.643H8.571v2.572h-.857v-3c0-.237.192-.429.429-.429h3c.237
 0 .428.192.428.429v2.571z" />
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
        yield from [
            "AWS ElastiCache",
        ]
