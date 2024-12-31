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


class RelianceIndustriesLimitedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "relianceindustrieslimited"

    @property
    def original_file_name(self) -> "str":
        return "relianceindustrieslimited.svg"

    @property
    def title(self) -> "str":
        return "Reliance Industries Limited"

    @property
    def primary_color(self) -> "str":
        return "#D1AB66"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Reliance Industries Limited</title>
     <path d="M7.65 18.44c.717-1.506 1.356-3.046 1.661-4.787.119 1.818
 1.2 3.435 1.72 5.177.199.842.214 1.714-.107 2.584-.349.948-.911
 1.759-1.582 2.488C7.528 21.936 6.97 20.11 7.65 18.44zm11.547
 3.765c-.825.623-1.902.716-2.744.311 0
 0-.229-.093-.439-.34-1.6-1.868-3.215-3.725-4.828-5.583 1.431.264
 3-.438
 3.805-1.712.81-1.212.777-2.942.016-4.154-.916-1.324-2.695-1.758-4.19-1.555-2.588.373-4.447
 2.722-5.026 5.182-.595 2.799-.166 5.44.761 7.932a6.87 6.87 0 0 0 .856
 1.538c-2.727-1.215-5.137-3.45-6.402-6.457-1.4-3.232-1.372-7.324.294-10.606C2.608
 4.225 4.923 1.876 7.789.884c1.157-.49 2.47-.746
 3.81-.786h.716c1.91.057 3.838.55 5.435 1.466 3.548 1.807 6.232 6.3
 6.244 10.314.123 4.153-1.674 7.915-4.797 10.327z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.ril.com/news-media/resource-cente'''

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
