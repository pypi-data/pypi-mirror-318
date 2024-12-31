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


class ZaloIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zalo"

    @property
    def original_file_name(self) -> "str":
        return "zalo.svg"

    @property
    def title(self) -> "str":
        return "Zalo"

    @property
    def primary_color(self) -> "str":
        return "#0068FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zalo</title>
     <path d="M12.49 10.2722v-.4496h1.3467v6.3218h-.7704a.576.576 0
 01-.5763-.5729l-.0006.0005a3.273 3.273 0 01-1.9372.6321c-1.8138
 0-3.2844-1.4697-3.2844-3.2823 0-1.8125 1.4706-3.2822
 3.2844-3.2822a3.273 3.273 0 011.9372.6321l.0006.0005zM6.9188
 7.7896v.205c0 .3823-.051.6944-.2995
 1.0605l-.03.0343c-.0542.0615-.1815.206-.2421.2843L2.024
 14.8h4.8948v.7682a.5764.5764 0
 01-.5767.5761H0v-.3622c0-.4436.1102-.6414.2495-.8476L4.8582
 9.23H.1922V7.7896h6.7266zm8.5513 8.3548a.4805.4805 0
 01-.4803-.4798v-7.875h1.4416v8.3548H15.47zM20.6934 9.6C22.52 9.6 24
 11.0807 24 12.9044c0 1.8252-1.4801 3.306-3.3066 3.306-1.8264
 0-3.3066-1.4808-3.3066-3.306 0-1.8237 1.4802-3.3044
 3.3066-3.3044zm-10.1412 5.253c1.0675 0 1.9324-.8645 1.9324-1.9312
 0-1.065-.865-1.9295-1.9324-1.9295s-1.9324.8644-1.9324 1.9295c0
 1.0667.865 1.9312 1.9324 1.9312zm10.1412-.0033c1.0737 0 1.945-.8707
 1.945-1.9453 0-1.073-.8713-1.9436-1.945-1.9436-1.0753
 0-1.945.8706-1.945 1.9436 0 1.0746.8697 1.9453 1.945 1.9453z" />
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
