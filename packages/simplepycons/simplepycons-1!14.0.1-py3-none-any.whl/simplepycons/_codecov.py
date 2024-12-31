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


class CodecovIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codecov"

    @property
    def original_file_name(self) -> "str":
        return "codecov.svg"

    @property
    def title(self) -> "str":
        return "Codecov"

    @property
    def primary_color(self) -> "str":
        return "#F01F7A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Codecov</title>
     <path d="M12.006.481C5.391.486.005 5.831 0 12.399v.03l2.042
 1.19.028-.018a5.82 5.82 0 013.308-1.02c.37 0 .733.034
 1.085.1l-.036-.006a5.69 5.69 0 012.874
 1.43l-.004-.002.35.326.198-.434c.192-.42.414-.814.66-1.173.1-.144.208-.29.332-.446l.205-.257-.252-.211a8.33
 8.33 0 00-3.836-1.807l-.052-.008a8.565 8.565 0
 00-4.08.251l.06-.016c.972-4.256 4.714-7.223 9.133-7.226a9.31 9.31 0
 016.6 2.713 9.196 9.196 0 012.508 4.498 8.385 8.385 0
 00-2.498-.379h-.154c-.356.006-.7.033-1.036.078l.045-.005-.042.006a8.103
 8.103 0 00-.39.06c-.057.01-.114.022-.17.033a8.102 8.102 0
 00-.392.09l-.138.034a9.21 9.21 0
 00-.483.144l-.03.01c-.354.12-.708.268-1.05.44l-.027.013c-.152.076-.305.16-.47.256l-.035.022a8.216
 8.216 0 00-2.108 1.8l-.011.014-.075.092a8.345 8.345 0
 00-.378.503c-.088.13-.177.269-.288.452l-.06.104a8.985 8.985 0
 00-.234.432l-.016.029c-.17.34-.317.698-.44 1.063l-.017.053a8.052
 8.052 0 00-.41 2.716v-.007.112a12 12 0 00.023.431l-.002-.037a11.676
 11.676 0 00.042.412l.005.042.013.103c.018.127.038.252.062.378.241
 1.266.845 2.532 1.745 3.66l.041.051.042-.05c.359-.424 1.249-1.77
 1.325-2.577v-.015l-.006-.013a5.56 5.56 0 01-.64-2.595c0-3.016
 2.37-5.521 5.396-5.702l.2-.007a5.93 5.93 0 013.47 1.025l.027.019L24
 12.416v-.03a11.77 11.77 0 00-3.51-8.423A11.962 11.962 0 0012.007.48z"
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
