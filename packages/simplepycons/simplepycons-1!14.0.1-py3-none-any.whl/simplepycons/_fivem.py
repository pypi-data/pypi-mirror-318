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


class FivemIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fivem"

    @property
    def original_file_name(self) -> "str":
        return "fivem.svg"

    @property
    def title(self) -> "str":
        return "FiveM"

    @property
    def primary_color(self) -> "str":
        return "#F40552"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FiveM</title>
     <path d="M22.4 24h-5.225c-.117
 0-.455-1.127-1.026-3.375-1.982-6.909-3.124-10.946-3.417-12.12l3.37-3.325h.099c.454
 1.42 2.554 7.676 6.299 18.768ZM12.342 7.084h-.048a3.382 3.385 0 0
 1-.098-.492v-.098a102.619 102.715 0 0 1
 3.272-3.275c.13.196.196.356.196.491v.05a140.694 140.826 0 0 1-3.322
 3.324ZM5.994 10.9h-.05c.67-2.12 1.076-3.209
 1.223-3.275L14.492.343c.08 0 .258.524.533
 1.562zm1.37-4.014h-.05C8.813 2.342 9.612.048 9.71 0h4.495v.05a664.971
 664.971 0 0 1-6.841 6.839Zm-2.69 7.874h-.05c.166-.798.554-1.418
 1.174-1.855a312.918 313.213 0 0 1 5.71-5.717h.05c-.117.672-.375
 1.175-.781 1.52zM1.598 24l-.098-.05c1.399-4.172 2.148-6.322
 2.248-6.45l6.74-6.694v.05C10.232 11.88 8.974 16.263 6.73 24Z" />
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
