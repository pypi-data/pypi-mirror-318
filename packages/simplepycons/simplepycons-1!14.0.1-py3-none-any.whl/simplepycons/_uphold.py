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


class UpholdIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "uphold"

    @property
    def original_file_name(self) -> "str":
        return "uphold.svg"

    @property
    def title(self) -> "str":
        return "Uphold"

    @property
    def primary_color(self) -> "str":
        return "#49CC68"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Uphold</title>
     <path d="M14.2743 22.3319a7.8524 7.8522 0 0
 1-2.2207.3336h-.1067a7.7804 7.7802 0 0 1-2.2367-.339.668.668 0 1
 0-.379 1.2812A9.267 9.2668 0 0 0 11.9469 24h.1067a9.155 9.1547 0 0 0
 2.5997-.3897.6673.6673 0 1
 0-.379-1.2784zm5.8266-16.4224V5.8694a8.5224 8.5221 0 0
 0-16.2066.0267v.016c-.7527 2.2126-.4805 5.1752.734 7.935 1.6601 3.774
 4.6735 6.4056 7.3426 6.4056h.0747c2.669 0 5.6825-2.6236 7.3426-6.4056
 1.1985-2.7544 1.4707-5.7224.7127-7.9377zM16.1854
 2.68c-1.3506-.0508-2.8186.5338-4.1852
 1.676-1.3825-1.1422-2.8505-1.7268-4.201-1.676a7.2305 7.2303 0 0 1
 8.3862 0zm-3.0908 15.9953a2.597 2.597 0 0 1-2.2047
 0c-2.2767-1.0489-2.7358-5.266-1.0062-9.2a11.9788 11.9785 0 0 1
 2.1165-3.2776 11.888 11.8878 0 0 1 2.1113 3.2776c1.7189 3.934 1.2598
 8.1511-1.017
 9.2zm-7.26-5.3567c-1.089-2.4715-1.3345-5.071-.6832-6.9901.347-1.0062.9315-1.7215
 1.6868-2.0712 1.1824-.5471 2.7145-.1601 4.1825 1.0276a13.2573 13.257
 0 0 0-2.3568 3.6512c-1.169 2.669-1.428 5.3887-.8888 7.5053a12.6594
 12.6591 0 0 1-1.9404-3.1228Zm12.3152 0a12.7262 12.7258 0 0 1-1.9404
 3.1254c.5338-2.1192.2669-4.8522-.8888-7.5079a13.2573 13.257 0 0
 0-2.3568-3.6512c1.468-1.1877 2.9973-1.5747 4.1798-1.0276.758.3497
 1.3345 1.0676 1.6895 2.0712.6592 1.9057.403 4.5186-.694 6.9901z" />
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
