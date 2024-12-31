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


class SabanciIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sabanci"

    @property
    def original_file_name(self) -> "str":
        return "sabanci.svg"

    @property
    def title(self) -> "str":
        return "Sabanci"

    @property
    def primary_color(self) -> "str":
        return "#004B93"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sabanci</title>
     <path d="M5.3877 8.88a15.8031 15.8031 0 0
 0-1.5366.1053c-1.1437.1457-1.5395.6461-1.5395 1.8724 0 .9713.2576
 1.44.9035 1.661.3132.1092.8498.155 1.7434.155h1.6998a8.7053 8.7053 0
 0 1 .923.0194c.3787.0365.5629.2113.5629.5246 0
 .5463-.2429.6-2.4283.6a8.499 8.499 0 0
 1-1.1724-.0631c-.2768-.0656-.34-.1751-.3595-.6365H2.3386v.3595c0
 .8766.2959 1.3186.988 1.4935.4516.1214 1.0785.1579
 2.4723.1579a23.1753 23.1753 0 0 0 2.5834-.0925c1.1704-.1263
 1.6125-.6312 1.6125-1.8672
 0-.6386-.129-1.1-.3766-1.3768-.2865-.3302-.6651-.442-1.5879-.4856-.4978-.0195-.8668-.0294-.9713-.0294H5.308a3.181
 3.181 0 0 1-.7284-.036.471.471 0 0
 1-.4127-.4857c0-.34.1652-.4716.6265-.508.2866-.017 1.117-.046
 1.6998-.046 1.2652 0 1.44.0752
 1.44.6095h1.804c0-1.0612-.2037-1.4862-.8204-1.717-.4711-.1748-.9595-.211-2.7589-.211a15.8031
 15.8031 0 0 0-.7702-.0033Zm11.2217.0446-3.4603
 6.1508h2.1224l.59-1.0975h3.9677l.6071
 1.0975h2.0493l-3.3678-6.1508Zm1.236 1.3185 1.3379 2.4553H16.534ZM0
 12.0012a6.1532 6.1532 0 0 1 11.998-1.928 6.1556 6.1556 0 1 1 0
 3.8536A6.1532 6.1532 0 0 1 0 12.0012Z" />
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
