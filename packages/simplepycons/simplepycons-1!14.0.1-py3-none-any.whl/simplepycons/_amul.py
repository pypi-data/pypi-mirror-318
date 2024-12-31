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


class AmulIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "amul"

    @property
    def original_file_name(self) -> "str":
        return "amul.svg"

    @property
    def title(self) -> "str":
        return "Amul"

    @property
    def primary_color(self) -> "str":
        return "#ED1D24"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Amul</title>
     <path d="M4.794
 11.772c-.104-.443-.546-1.492-.786-1.796-.04-.031-.062-.046-.078-.068l-.718
 1.748s.375.091.796.148c.271.03.558.03.786-.032zm17-1.593v3.536c0
 .7-.282.59-.385.613l1.209 1.018L24
 14.236c-.014-.086-.063-.171-.124-.195-.475.294-.443-.302-.443-.302V9.527c0-.528-.933-1.097-1.285-.986l-1.304
 1.297c.015.054.06.162.203.186.61-.56.747 0 .747.155zm-5.576
 2.184v1.5c0 .528-.2.428-.348.488.412.218.972.668 1.454
 1.011l1.446-.916 1.073.94
 1.266-1.236s-.016-.18-.17-.171c-.444.436-.575-.288-.575-.288v-1.833c0-.801-1.028-.98-1.244-.972l-1.035
 1.01a.4.4 0
 00.194.165c.484-.382.567.17.567.17v1.5c-.014.62-1.14.847-1.14.008v-2.09c-.095-.576-.912-.895-1.028-.794l-1.181.972c.055.093.06.204.207.187.523-.367.514.349.514.349zm-7.805-.287v1.632c0
 .45-.334.442-.44.465l1.274 1.104 1.227-1.08a.487.487 0
 00-.115-.178c-.203.107-.357.046-.357-.22v-1.654c.108-.512.838-.397.838-.047v1.696c-.018.34-.156.488-.31.535l1.156.956
 1.243-1.043c-.02-.085-.02-.16-.129-.2-.124.008-.357.25-.357-.288v-1.617c.256-.653.885-.31.91.055v1.516c-.009.357-.074.583-.366.683l1.204.94
 1.276-1.15c0-.077-.11-.157-.15-.178-.419.364-.396-.095-.402-.165v-2.09c-.017-.365-.7-1.125-1.61-.783l-.91.668c-.484-.824-1.19-.847-1.378-.8-.308.044-.962.838-1.038.713-.288-.713-1.053-.728-1.209-.706l-1.07.924c.054.117.141.132.2.155.289-.17.485-.132.513.157zm-5.571.491l-.334.906.79.506c.112.071.253.024.476-.18l.157.157c-.357.41-.73.8-1.096
 1.212-.482-.442-1.05-.877-1.594-.877-.628.013-1.213.62-.606
 1.717.017.022-.094.138-.156.09-.465-.395-.652-1.482-.286-2.095.256-.397.72-.785
 1.513-.693l.313-.85c-.287-.113-.598 0-.988.308.132-.67.551-1.136
 1.412-1.252l.882-2.114c-.467-.187-.903.04-1.12.436-.132-.017-.225-.063-.25-.147l.903-1.68c.44-.153.817-.153
 1.151-.048 1.376.436 2.067 2.76 3.098
 5.325.095.248.221.271.516-.046l.21.186-1.86 1.85-.856-2.558c0
 .022-.417.125-1.107.063a5.65 5.65 0 01-1.168-.216z" />
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
