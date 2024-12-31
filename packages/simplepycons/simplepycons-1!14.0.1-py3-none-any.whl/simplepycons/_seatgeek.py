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


class SeatgeekIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "seatgeek"

    @property
    def original_file_name(self) -> "str":
        return "seatgeek.svg"

    @property
    def title(self) -> "str":
        return "SeatGeek"

    @property
    def primary_color(self) -> "str":
        return "#FF5B49"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SeatGeek</title>
     <path d="M11.866
 11.277h-.177l-.703-.001v-.001c-1.337-.002-3.426-.009-3.845-.011v-7.37c2.111.089
 4.044.121 4.044.121l.304 1.556c.001
 0-.745.007-2.361-.03v1.394l1.486.022v1.31L9.128 8.25v1.452c.832.008
 1.595.013 2.411.014l1.99-5.615c.3-.008 1.573-.041 1.886-.054l2.637
 7.225c-.661.003-1.331-.009-1.993-.006l-.448-1.302c-.76.008-1.52.013-2.281.016l-.445
 1.293c-.355 0-.685 0-1.019.004Zm2.607-4.625-.693
 2.015c.461-.004.921-.009
 1.38-.016l-.687-1.999Zm4.389-1.197c-.719.044-1.438.081-2.157.112l.307-1.594c1.904-.105
 3.8-.271 5.694-.497l.306 1.645c-.719.071-1.439.134-2.16.192l-.01
 5.953c-.66.006-1.32-.001-1.98.004V5.455ZM6.533 9.069c0 1.246-.901
 2.401-2.674 2.401-1.61 0-2.42-.752-2.42-.752V8.699c1.101 1.043 3.266
 1.745 3.266.482 0-.96-3.266-1.125-3.266-3.518 0-1.342 1.247-2.186
 2.675-2.186 1.009 0 1.855.193 2.065.258l-.083
 1.772c-.884-.521-2.801-.763-2.801.134 0 .992 3.239 1.002 3.238
 3.428Zm14.861
 11.155-1.957-3.596v3.433c-.673-.053-1.982-.133-1.982-.133V12.5l1.982.004c-.007
 1.059.008 2.118 0 3.176l2.028-3.18h2.233l-2.314 3.569L24
 20.525a90.598 90.598 0 0 0-2.606-.301ZM9.132 18.231c.892-.019
 1.785-.029 2.678-.029l-.307
 1.561c-.869.003-3.428.062-4.358.122v-7.374h4.038l.307
 1.536s-.973-.007-2.358-.008v1.399l1.481-.013v1.323l-1.481.018v1.465Zm5.162-.001c.707.015
 1.905.054 2.682.082l-.32 1.573a87.388 87.388 0 0
 0-4.349-.121v-7.253l4.051.002.306
 1.551-2.371-.015v1.389c.461.005.92.009
 1.379.017v1.321c-.459-.011-.919-.018-1.379-.025l.001 1.479ZM3.617
 15.549l2.604-.059v4.445s-.7.032-2.26.178C1.746 20.321 0 19.022 0
 16.468c0-3.034 2.222-3.993 4.225-3.993.868 0 1.379.016 1.667.031l.328
 1.723s-.58-.122-1.673-.122c-1.24 0-2.585.415-2.585 2.078 0 1.791.745
 2.392 2.556 2.228l-.001-1.536-1.206.059.306-1.387Z" />
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
