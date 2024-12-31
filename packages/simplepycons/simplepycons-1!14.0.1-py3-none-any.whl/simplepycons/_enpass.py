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


class EnpassIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "enpass"

    @property
    def original_file_name(self) -> "str":
        return "enpass.svg"

    @property
    def title(self) -> "str":
        return "Enpass"

    @property
    def primary_color(self) -> "str":
        return "#0D47A1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Enpass</title>
     <path d="M12.023 1.3366c2.6912 0 5.3825-.008 8.0745.004a3.8428
 3.8428 0 0 1 2.9636 1.3079A3.7223 3.7223 0 0 1 24 4.9469a9.6627
 9.6627 0 0 1-.2783 2.319c-.3571 2.0539-.7288 4.1038-1.0939
 6.155-.3147 1.7665-.6162 3.5355-.9474 5.3006-.4644 2.038-2.1287
 3.5843-4.1953 3.8978a6.3255 6.3255 0 0
 1-.7428.0444c-3.1458.003-6.2916.003-9.4375
 0-2.4536-.0049-4.551-1.7673-4.9784-4.1834A3553.0608 3553.0608 0 0 0
 .4209 7.9092C.2949 7.2115.1559 6.5178.057 5.8148c-.3576-2.05
 1.0018-4.0057 3.048-4.3848a5.003 5.003 0 0 1 .9713-.0888c2.6489-.0075
 5.2978-.009 7.9467-.0046zM9.8874 18.0225c-.0302.6861.5343 1.2506
 1.2204 1.2204h1.7472c.7367.071 1.3552-.548 1.2834-1.2847 0-1.3775
 0-2.7556-.0067-4.133a.385.385 0 0 1 .218-.385c1.7016-1.0082
 2.525-3.025 2.0155-4.936-.66-2.3766-3.103-3.7856-5.4906-3.1664a4.2099
 4.2099 0 0 0-3.0345 2.5005c-.7947 2.0883-.0042 4.4472 1.8883
 5.635a.2895.2895 0 0 1 .1636.287c-.0073 1.4795-.0046 2.7056-.0046
 4.2622Z" />
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
