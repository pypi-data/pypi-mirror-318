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


class DailymotionIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dailymotion"

    @property
    def original_file_name(self) -> "str":
        return "dailymotion.svg"

    @property
    def title(self) -> "str":
        return "Dailymotion"

    @property
    def primary_color(self) -> "str":
        return "#0A0A0A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dailymotion</title>
     <path d="M21.823 7.327a11.928 11.928 0 0 0-2.606-3.814 12.126
 12.126 0 0 0-3.866-2.57A12.246 12.246 0 0 0 10.617 0H1.831a.602.602 0
 0 0-.609.603v3.764c0 .162.064.312.179.426l4.164 4.123a.612.612 0 0 0
 .439.177h4.56c.806 0 1.56.313 2.125.88.557.559.856 1.296.843
 2.075-.029 1.571-1.343 2.849-2.931 2.849h-6.74a.613.613 0 0
 0-.432.176.619.619 0 0 0-.178.427v3.764c0 .162.063.312.178.427l4.139
 4.099a.647.647 0 0 0 .476.21h2.572a12.276 12.276 0 0 0 4.733-.945
 12.145 12.145 0 0 0 3.866-2.571 11.959 11.959 0 0 0
 2.607-3.813c.633-1.479.956-3.051.956-4.67
 0-1.619-.321-3.19-.956-4.669l.001-.005ZM2.441 4.118V1.982l2.945
 2.755.001 2.297-2.946-2.916Zm4.975 17.813-2.945-2.917v-2.137l2.945
 2.755v2.299Zm-2.004-5.832h5.19c2.248 0 4.107-1.807 4.147-4.03a4.027
 4.027 0 0 0-1.192-2.937 4.203 4.203 0 0
 0-2.996-1.239H6.606V5.216h3.996c1.831 0 3.553.706 4.849 1.986a6.724
 6.724 0 0 1-.152 9.736 6.875 6.875 0 0 1-4.697 1.84H8.275L5.412
 16.1v-.001Zm15.289.1a10.753 10.753 0 0 1-2.345 3.431 10.91 10.91 0 0
 1-3.48 2.314 11.018 11.018 0 0 1-4.26.847H8.633v-2.814h1.916c2.145 0
 4.161-.802 5.675-2.254a7.88 7.88 0 0 0
 2.451-5.728c0-2.177-.87-4.21-2.451-5.728-1.514-1.454-3.528-2.254-5.675-2.254h-4.16L3.383
 1.202h7.234c1.479 0 2.911.285 4.259.847a10.957 10.957 0 0 1 3.48
 2.313 10.769 10.769 0 0 1 2.345 3.432c.571 1.33.86 2.743.86 4.202 0
 1.46-.289 2.873-.86 4.203Z" />
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
