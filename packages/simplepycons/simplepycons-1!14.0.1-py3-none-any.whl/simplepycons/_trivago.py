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


class TrivagoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "trivago"

    @property
    def original_file_name(self) -> "str":
        return "trivago.svg"

    @property
    def title(self) -> "str":
        return "trivago"

    @property
    def primary_color(self) -> "str":
        return "#E32851"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>trivago</title>
     <path d="M7.8112 0a.2537.2537 0 0 0-.1336.0416L2.8311
 3.1804a.4265.4265 0 0 0-.1947.3579v9.285c0
 .141.1144.2554.2555.2554h5.1808l10.358-5.7274a.4263.4263 0 0 0
 .22-.3732V1.6774c0-.1949-.2092-.3182-.3797-.2239L8.0727
 7.0923V.2563c0-.1521-.1265-.2589-.2615-.2563zm.0172
 14.7072-4.9307.0002c-.1457 0-.2607.1216-.2555.2672C2.822 19.9896
 6.9445 24 12.0032 24c5.059 0 9.18-4.01
 9.3602-9.0246.0053-.1461-.1102-.2682-.2564-.2682h-4.9319c-.1312
 0-.2442.1073-.2545.238-.1592 2.025-1.8517 3.6185-3.9173 3.6185-2.4784
 0-3.4806-2.1046-3.4808-2.105-.3197-.6025-.4129-1.1898-.4394-1.5183a.255.255
 0 0 0-.2547-.2332Z" />
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
