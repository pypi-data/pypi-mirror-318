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


class CodeiumIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codeium"

    @property
    def original_file_name(self) -> "str":
        return "codeium.svg"

    @property
    def title(self) -> "str":
        return "Codeium"

    @property
    def primary_color(self) -> "str":
        return "#09B6A2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Codeium</title>
     <path d="M1 0a1 1 0 0 0-1 1v22c0 .063.007.124.018.184L0
 23.199l.025.026c.103.443.5.775.975.775h22a1 1 0 0 0 1-1V1a1 1 0 0
 0-1-1H1zm.707 1h20.582l-2 2H3.707l-2-2zM23
 1.705v20.588l-2-2V3.705l2-2zM1 1.707l2 2v16.492l-2 2V1.707zM4
 4h16v16H4V4zm3.537 3c-1.006 0-1.51.535-1.51 1.605v2.297c0
 .4-.184.6-.554.6a.47.47 0 0 0-.344.139.512.512 0 0 0-.129.365.49.49 0
 0 0 .129.353.47.47 0 0 0 .344.139c.37 0 .554.2.554.6v2.297c0 1.07.504
 1.605 1.51 1.605.136 0 .248-.05.334-.148A.494.494 0 0 0 8
 16.498a.512.512 0 0 0-.129-.365.439.439 0 0 0-.334-.139c-.376
 0-.564-.199-.564-.6v-2.296c0-.46-.1-.823-.297-1.092.099-.138.173-.3.222-.485.05-.183.075-.389.075-.619V8.605c0-.4.188-.6.564-.6a.439.439
 0 0 0 .334-.138A.499.499 0 0 0 8 7.512a.53.53 0 0
 0-.129-.364A.425.425 0 0 0 7.537 7zm8.926 0a.425.425 0 0
 0-.334.148.53.53 0 0 0-.129.364.5.5 0 0 0 .129.355.439.439 0 0 0
 .334.139c.376 0 .564.199.564.6v2.296c0
 .23.025.436.075.62.049.183.123.346.222.484-.197.27-.297.632-.297
 1.092v2.297c0 .4-.188.6-.564.6a.439.439 0 0 0-.334.138.512.512 0 0
 0-.129.365c0 .145.043.262.129.354a.425.425 0 0 0 .334.148c1.006 0
 1.51-.535 1.51-1.605v-2.297c0-.4.184-.6.554-.6a.439.439 0 0 0
 .334-.139.475.475 0 0 0 .139-.353.492.492 0 0 0-.139-.365.439.439 0 0
 0-.334-.139c-.37
 0-.554-.2-.554-.6V8.605c0-1.07-.504-1.605-1.51-1.605zm-7.25
 6a.737.737 0 0 0-.496.227.717.717 0 0 0-.217.529.74.74 0 0 0
 .75.744.74.74 0 0 0 .75-.744.717.717 0 0 0-.217-.53A.71.71 0 0 0 9.25
 13h-.037zm2.75 0a.737.737 0 0 0-.496.227.717.717 0 0 0-.217.529.74.74
 0 0 0 .217.53c.152.143.33.214.533.214a.74.74 0 0 0 .75-.744.717.717 0
 0 0-.217-.53A.71.71 0 0 0 12 13h-.037zm2.75 0a.737.737 0 0
 0-.496.227.717.717 0 0 0-.217.529.74.74 0 0 0
 .217.53c.152.143.33.214.533.214a.74.74 0 0 0 .75-.744.717.717 0 0
 0-.217-.53.71.71 0 0 0-.533-.226h-.037zm-11.1 8h16.68l2 2H1.613l2-2z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Exafunction/codeium.vim/bl'''

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
            "Exafunction",
        ]
