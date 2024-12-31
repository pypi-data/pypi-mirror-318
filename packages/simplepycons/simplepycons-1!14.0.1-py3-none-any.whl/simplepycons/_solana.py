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


class SolanaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "solana"

    @property
    def original_file_name(self) -> "str":
        return "solana.svg"

    @property
    def title(self) -> "str":
        return "Solana"

    @property
    def primary_color(self) -> "str":
        return "#9945FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Solana</title>
     <path d="m23.8764 18.0313-3.962 4.1393a.9201.9201 0 0
 1-.306.2106.9407.9407 0 0 1-.367.0742H.4599a.4689.4689 0 0
 1-.2522-.0733.4513.4513 0 0 1-.1696-.1962.4375.4375 0 0
 1-.0314-.2545.4438.4438 0 0 1 .117-.2298l3.9649-4.1393a.92.92 0 0 1
 .3052-.2102.9407.9407 0 0 1 .3658-.0746H23.54a.4692.4692 0 0 1
 .2523.0734.4531.4531 0 0 1 .1697.196.438.438 0 0 1
 .0313.2547.4442.4442 0 0 1-.1169.2297zm-3.962-8.3355a.9202.9202 0 0
 0-.306-.2106.941.941 0 0 0-.367-.0742H.4599a.4687.4687 0 0
 0-.2522.0734.4513.4513 0 0 0-.1696.1961.4376.4376 0 0
 0-.0314.2546.444.444 0 0 0 .117.2297l3.9649 4.1394a.9204.9204 0 0 0
 .3052.2102c.1154.049.24.0744.3658.0746H23.54a.469.469 0 0 0
 .2523-.0734.453.453 0 0 0 .1697-.1961.4382.4382 0 0 0
 .0313-.2546.4444.4444 0 0 0-.1169-.2297zM.46
 6.7225h18.7815a.9411.9411 0 0 0 .367-.0742.9202.9202 0 0 0
 .306-.2106l3.962-4.1394a.4442.4442 0 0 0 .117-.2297.4378.4378 0 0
 0-.0314-.2546.453.453 0 0 0-.1697-.196.469.469 0 0
 0-.2523-.0734H4.7596a.941.941 0 0 0-.3658.0745.9203.9203 0 0
 0-.3052.2102L.1246 5.9687a.4438.4438 0 0 0-.1169.2295.4375.4375 0 0 0
 .0312.2544.4512.4512 0 0 0 .1692.196.4689.4689 0 0 0 .2518.0739z" />
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
