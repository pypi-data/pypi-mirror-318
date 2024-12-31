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


class AsdaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "asda"

    @property
    def original_file_name(self) -> "str":
        return "asda.svg"

    @property
    def title(self) -> "str":
        return "ASDA"

    @property
    def primary_color(self) -> "str":
        return "#68A51C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ASDA</title>
     <path d="M21.7596 8.673h-2.475l-1.4114
 4.0851c.0632-.3392.0743-.6104.0743-.7283
 0-1.7114-.9805-3.3568-3.2843-3.3568h-2.6458l.0078
 4.0635c-.2287-1.1546-1.2835-1.4639-2.5952-1.8626-.4902-.151-.7594-.3908-.6612-.6143.0839-.1952.3845-.2564.7494-.206.5564.0796
 1.0008.2657
 1.4287.4986l.5847-1.449c-.1318-.065-1.0792-.6337-2.2665-.6337-1.6557
 0-2.7131.8078-2.7131 1.9999 0 1.0622.6542 1.6798 1.8572 2.026
 1.2938.3753 1.6218.5263
 1.5828.8984-.0335.3207-.8354.7113-2.7974-.4958l-.5829
 1.2062-1.7994-5.431H2.3382L0 15.4244h1.9502l.3777-1.09h2.2875l.3886
 1.0902h2.0473l-.2322-.6603c.6921.4 1.5504.7662 2.5772.7662 1.5728 0
 2.4231-.859 2.626-1.6823v1.5764h2.638c1.5727 0 2.3953-.7498
 2.8251-1.5524l-.5396 1.5524h1.9487l.39-1.0901h2.323l.3425
 1.09H24L21.7594 8.673Zm-18.996 4.1365.7272-2.3196.6889
 2.3196Zm11.2193.874v-3.2703h.465c.663 0 1.3867.2684 1.3867 1.6352 0
 1.2105-.6392 1.6351-1.381 1.6351zm5.773-.874.6936-2.292.7224 2.292z"
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
