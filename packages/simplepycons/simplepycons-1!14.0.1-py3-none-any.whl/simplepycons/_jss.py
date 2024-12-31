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


class JssIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jss"

    @property
    def original_file_name(self) -> "str":
        return "jss.svg"

    @property
    def title(self) -> "str":
        return "JSS"

    @property
    def primary_color(self) -> "str":
        return "#F7DF1E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>JSS</title>
     <path d="M0 2.5v19h19.2v-1.95c.506.263 1.124.42 1.857.42 1.687 0
 2.943-.877 2.943-2.475
 0-1.483-.852-2.143-2.36-2.79l-.444-.19c-.762-.33-1.092-.546-1.092-1.078
 0-.431.33-.761.85-.761.51 0 .838.215
 1.142.76l1.383-.887c-.585-1.029-1.396-1.422-2.525-1.422-.715
 0-1.312.207-1.754.555V2.5zm.36.359h18.48v9.182a2.266 2.266 0 00-.487
 1.432c0 .654.176 1.152.486 1.552v2.537l-1.018.592c.232.456.57.864
 1.018 1.177v1.81H.361zm14.188 8.268c-1.586 0-2.6 1.014-2.6 2.346 0
 1.445.85 2.13 2.132 2.675l.443.19c.81.355 1.293.57 1.293 1.18 0
 .508-.47.875-1.205.875-.876 0-1.371-.457-1.752-1.078l-1.443.839c.521
 1.03 1.587 1.816 3.236 1.816 1.687 0 2.943-.876 2.943-2.475
 0-1.483-.852-2.143-2.361-2.79l-.444-.19c-.762-.33-1.092-.546-1.092-1.078
 0-.431.33-.761.85-.761.51 0 .838.215
 1.143.76l1.382-.887c-.584-1.029-1.396-1.422-2.525-1.422zm-5.868.101v6.038c0
 .888-.368 1.116-.951 1.116-.61
 0-.864-.418-1.143-.913l-1.446.875c.419.886 1.242 1.622 2.664 1.622
 1.574 0 2.652-.837 2.652-2.676v-6.062zm10.52 4.173c.345.295.781.532
 1.286.747l.443.19c.81.355 1.293.57 1.293 1.18 0
 .508-.47.875-1.206.875-.876 0-1.37-.457-1.752-1.078l-.064.037z" />
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
