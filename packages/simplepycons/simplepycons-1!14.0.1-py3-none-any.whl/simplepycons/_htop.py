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


class HtopIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "htop"

    @property
    def original_file_name(self) -> "str":
        return "htop.svg"

    @property
    def title(self) -> "str":
        return "htop"

    @property
    def primary_color(self) -> "str":
        return "#009020"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>htop</title>
     <path d="M6.928 16.738v7.233h1.414v-7.233H6.928Zm10.912
 0v7.233h1.414v-7.233H17.84Zm2.179 0v7.233h1.414v-7.233h-1.414Zm-4.366
 0v7.233h1.414v-7.233h-1.414Zm-13.089
 0v7.233h1.415v-7.233H2.564Zm2.183 0v7.233h1.414v-7.233H4.747ZM24
 16.771l-.02
 7.178-2.16-.008v-1.257h.827v-4.745h-.814V16.76l2.167.011Zm-24-.009.02
 7.178 2.16-.008v-1.257h-.827v-4.744h.814v-1.18L0
 16.762Zm6.928-8.356v7.233h1.414V8.406H6.928Zm2.182
 0v7.233h1.414V8.406H9.11Zm2.181 0v7.233h1.414V8.406h-1.414Zm4.362
 0v7.233h1.414V8.406h-1.414Zm2.187 0v7.233h1.414V8.406H17.84Zm2.179
 0v7.233h1.414V8.406h-1.414Zm-17.455 0v7.233h1.415V8.406H2.564Zm2.183
 0v7.233h1.414V8.406H4.747Zm8.726 0v7.233h1.415V8.406h-1.415ZM24
 8.433l-.02 7.178-2.16-.008v-1.257h.827V9.601h-.814V8.422L24 8.433ZM0
 8.43l.02 7.178 2.16-.008v-1.257h-.827V9.599h.814v-1.18L0
 8.43ZM6.928.029v7.233h1.414V.029H6.928Zm8.725
 0v7.233h1.414V.029h-1.414Zm4.366 0v7.233h1.414V.029h-1.414Zm-2.179
 0v7.233h1.414V.029H17.84Zm-15.276 0v7.233h1.415V.029H2.564Zm2.183
 0v7.233h1.414V.029H4.747ZM24 .055l-.02
 7.178-2.16-.009V5.967h.827V1.223h-.814V.044L24 .055ZM0 .052.02
 7.23l2.16-.008V5.965h-.827V1.221h.814V.041L0 .052Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/htop-dev/htop/blob/03d5e47'''

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
