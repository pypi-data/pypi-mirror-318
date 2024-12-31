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


class CadillacIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cadillac"

    @property
    def original_file_name(self) -> "str":
        return "cadillac.svg"

    @property
    def title(self) -> "str":
        return "Cadillac"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cadillac</title>
     <path d="M2.787
 9.414h2.104l-.398-.719h7.139v.717h.238v-.965H2.135l.652.967zm.202.948h8.879v-.719H2.874l.115.719zm2.255
 1.204h-2.06l-.16-.981h8.846v.981h-.239v-.751H5.169l.075.751zm3.299.692h3.326v.515H8.543v-.515zm3.589-3.811h3.357v1.444h-3.357V8.447zm-8.469
 5.569c.054.086.155.186.49.281.146.037.305.074.515.122l.08.019H8.31v-.51H3.616c.013.03.028.06.046.088h.001zm4.647-.779H3.459l-.238-1.44H8.31v1.44zm.232
 2.021c1.243.253 2.457.488
 3.329.63V13.47H8.542V15.258zm12.276-3.692h-5.1v-1.445h5.333l-.233
 1.445zm-5.1-2.66v.513l5.485-.002.344-.511h-5.829zM0 7.306l1.616
 2.369c.177 1.006.64 3.599.693 3.85l.006.032c.148.706.239 1.139 1.59
 1.473 1.825.45 5.997 1.323 8.094 1.664 2.097-.341 6.271-1.215
 8.097-1.664 1.35-.334 1.44-.767
 1.589-1.473l.006-.032c.053-.253.516-2.844.693-3.85L24 7.306H0zm21.454
 2.335-.277 1.717c-.16.994-.267 1.657-.32
 1.951l-.007.035-.012.07c-.127.692-.183 1.002-.91
 1.205-1.516.373-5.908 1.31-7.927
 1.626-2.018-.316-6.41-1.254-7.925-1.626-.727-.203-.783-.513-.91-1.206l-.019-.104c-.053-.288-.156-.93-.31-1.89v-.001L2.55
 9.64 1.276 7.75h21.45l-1.272 1.89v.001zm-9.084
 3.132h-.238v-.976h8.65l-.16.978h-2.004c.031-.171.09-.659.099-.73H12.37v.728zm-.238.942h8.322l.134-.716h-8.456v.716zm0-3.129h3.358v.516h-3.358v-.516zm0
 3.342v1.959c2.115-.36 6.223-1.205
 7.718-1.592.338-.087.438-.193.492-.279a.448.448 0 0 0
 .045-.088h-8.255zm2.296
 1.282-.415.082c-.21.042-.665.125-1.065.199l-.577.106v-1.422h5.88c-.27.33-.812.437-3.823
 1.035z" />
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
