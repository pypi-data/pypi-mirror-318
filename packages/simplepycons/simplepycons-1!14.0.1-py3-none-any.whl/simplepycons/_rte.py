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


class RteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rte"

    @property
    def original_file_name(self) -> "str":
        return "rte.svg"

    @property
    def title(self) -> "str":
        return "RTÉ"

    @property
    def primary_color(self) -> "str":
        return "#00A7B3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>RTÉ</title>
     <path d="M1.983 12.857V9.038s.734-.018 1.615-.018c.131 0
 .258.01.373.016 1.41.115 1.992.883 1.992 1.807 0 1.036-.82
 1.819-1.992 1.986a3.5 3.5 0 0 1-.474.028zm2.84 1.244c1.736-.168
 3.197-1.446 3.197-3.102 0-1.763-1.018-3.324-4.049-3.45a9.497 9.497 0
 0 0-.393-.01c-2.098 0-3.537.1-3.537.1s.097 1.035.097 1.558v7.624C.138
 17.522 0 18.26 0 18.26h2.118s-.135-.737-.135-1.577v-3.101l1.988 2.08
 1.006 1.043c.62.677 1.702 1.555 1.702
 1.555h2.8s-1.253-.878-1.835-1.438zm19.055-7.198a8.123 8.123 0 0
 0-2.036-.284c-1.784 0-3.321.541-4.603 1.682l.02-1.261c1.36-.925
 2.9-1.34 4.583-1.34.738 0 1.378.1 2.056.276l-.02.927M11.282
 18.259s.117-.778.117-1.458V9.402h-.501c-.68 0-1.736
 0-2.516.077l-.066-1.718h8.124l-.041
 1.718c-.802-.077-1.838-.077-2.539-.077h-.617v7.399c0 .68.136
 1.458.136 1.458h-2.097m10.419-1.524c-1.838
 0-3.386-1.315-3.666-3.175h3.482c.385 0 1.222.082
 1.222.082V12.1s-.822.061-1.28.061h-3.424c.347-1.822 1.845-3.08
 3.666-3.08.96 0 2.139.438
 2.139.438l.023-1.622s-.84-.318-2.162-.318c-3.063 0-5.741 2.34-5.741
 5.32 0 3.223 2.678 5.4 5.74 5.4 1.44 0 2.3-.384
 2.3-.384l-.04-1.676c-.001 0-1.062.496-2.26.496Z" />
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
