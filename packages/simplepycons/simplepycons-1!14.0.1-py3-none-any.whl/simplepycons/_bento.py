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


class BentoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bento"

    @property
    def original_file_name(self) -> "str":
        return "bento.svg"

    @property
    def title(self) -> "str":
        return "Bento"

    @property
    def primary_color(self) -> "str":
        return "#768CFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bento</title>
     <path d="M0 10.435c0-.256.051-.512.153-.758.233-.56.854-1.046
 2.095-2.018l6.206-4.856c1.241-.972 1.862-1.458 2.577-1.64.63-.16
 1.308-.16 1.938 0 .715.183 1.336.668 2.577 1.64l6.206 4.856c1.241.972
 1.862 1.458 2.095 2.018.102.246.153.502.153.758v3.13c0
 .256-.051.512-.153.758-.233.56-.854 1.046-2.095 2.017l-6.206
 4.857c-1.241.972-1.862 1.457-2.577 1.64-.63.16-1.308.16-1.938
 0-.715-.183-1.336-.668-2.577-1.64L2.248 16.34C1.007 15.37.386
 14.883.153 14.323A1.971 1.971 0 0 1 0
 13.565v-3.13Zm9.34-3.238.887.694c.62.485.93.728
 1.289.82.315.08.653.08.968 0 .358-.092.668-.335
 1.29-.82l.886-.694c.62-.486.93-.729 1.047-1.009a.975.975 0 0 0
 0-.758c-.116-.28-.427-.523-1.047-1.008l-.887-.694c-.62-.486-.93-.729-1.289-.82a1.984
 1.984 0 0 0-.968
 0c-.358.091-.668.334-1.29.82l-.886.694c-.62.485-.93.728-1.047
 1.008a.975.975 0 0 0 0 .758c.116.28.427.523 1.047 1.009Zm5.91
 4.625.887.694c.62.486.931.729 1.29.82.314.08.653.08.968 0
 .358-.091.668-.334 1.288-.82l.887-.694c.62-.485.931-.728
 1.047-1.008a.976.976 0 0 0
 0-.758c-.116-.28-.426-.523-1.047-1.009l-.887-.694c-.62-.485-.93-.728-1.288-.82a1.984
 1.984 0 0 0-.969
 0c-.358.092-.668.335-1.289.82l-.886.694c-.621.486-.931.729-1.047
 1.009a.975.975 0 0 0 0 .758c.116.28.426.523 1.047 1.008Zm-11.82 0
 6.797 5.32c.62.486.93.728 1.289.82.315.08.653.08.968 0
 .358-.092.668-.334 1.29-.82l.886-.694c.62-.486.93-.729
 1.047-1.009a.974.974 0 0 0
 0-.758c-.116-.28-.427-.523-1.047-1.008l-6.797-5.32c-.62-.485-.931-.728-1.29-.82a1.984
 1.984 0 0 0-.968
 0c-.358.092-.668.335-1.288.82l-.887.694c-.62.486-.931.729-1.047
 1.009a.975.975 0 0 0 0 .758c.116.28.426.523 1.047 1.008Z" />
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
