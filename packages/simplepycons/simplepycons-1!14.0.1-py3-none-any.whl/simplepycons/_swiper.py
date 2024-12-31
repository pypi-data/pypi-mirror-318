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


class SwiperIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "swiper"

    @property
    def original_file_name(self) -> "str":
        return "swiper.svg"

    @property
    def title(self) -> "str":
        return "Swiper"

    @property
    def primary_color(self) -> "str":
        return "#6332F6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Swiper</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0zm4.884 17.908a4.328 4.328 0 0 1-1.092 1.488 4.817
 4.817 0 0
 1-1.644.936c-.632.216-1.308.324-2.028.324s-1.368-.1-1.944-.3c-.576-.2-1.088-.464-1.536-.792s-.832-.704-1.152-1.128a6.563
 6.563 0 0
 1-.768-1.284l1.68-1.008c.144.336.332.66.564.972.232.312.5.588.804.828a3.697
 3.697 0 0 0 2.328.792c.4 0 .788-.056
 1.164-.168.376-.112.708-.28.996-.504.288-.224.52-.5.696-.828.176-.328.264-.716.264-1.164
 0-.432-.084-.804-.252-1.116a2.955 2.955 0 0 0-.684-.84 5 5 0 0
 0-1.032-.672c-.4-.2-.832-.412-1.296-.636a44.725 44.725 0 0
 1-1.644-.816 7.592 7.592 0 0 1-1.488-1.008 4.752 4.752 0 0
 1-1.068-1.332c-.272-.504-.408-1.092-.408-1.764
 0-.56.104-1.116.312-1.668a4.474 4.474 0 0 1 .912-1.476c.4-.432.9-.784
 1.5-1.056s1.3-.408 2.1-.408c.592 0 1.14.076 1.644.228a5.98 5.98 0 0 1
 2.412 1.38c.304.288.552.568.744.84l-1.512 1.224a4.172 4.172 0 0
 0-1.284-1.188 4.204 4.204 0 0 0-.924-.408 3.634 3.634 0 0
 0-1.08-.156c-.464 0-.868.072-1.212.216a2.692 2.692 0 0
 0-.876.576c-.24.24-.42.516-.54.828-.12.312-.18.628-.18.948 0
 .4.088.748.264 1.044.176.296.424.572.744.828s.712.504
 1.176.744c.464.24.984.488 1.56.744.64.288 1.22.588
 1.74.9.52.312.96.652 1.32 1.02.36.368.636.784.828 1.248.192.464.288
 1.008.288 1.632 0 .736-.132 1.396-.396 1.98z" />
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
