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


class PretzelIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pretzel"

    @property
    def original_file_name(self) -> "str":
        return "pretzel.svg"

    @property
    def title(self) -> "str":
        return "Pretzel"

    @property
    def primary_color(self) -> "str":
        return "#1BB3A4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pretzel</title>
     <path d="M22.439.03 10.757 6.516a.305.305 0 0
 0-.142.236v5.426l2.72 1.704v-5.54a.303.303 0 0 1
 .143-.235l6.24-3.48a.286.286 0 0 1 .415.237V15.186a2.807 2.807 0 0
 1-1.38 2.555 2.827 2.827 0 0 1-2.909-.02l-6.24-3.951-.03-.03a5.569
 5.569 0 0 0-6.245.333 5.524 5.524 0 0 0-1.977 5.917 5.462 5.462 0 0 0
 2.662 3.331A5.656 5.656 0 0 0 6.676 24a5.961 5.961 0 0 0 1.597-.236
 5.544 5.544 0 0 0 3.43-2.919l.09-.236-2.308-1.474-.237.56a2.792 2.792
 0 0 1-1.74 1.478 2.836 2.836 0 0 1-2.189-.236 2.738 2.738 0 0
 1-1.36-1.704c-.413-1.42.414-2.949
 1.805-3.45.294-.105.604-.153.916-.142a2.834 2.834 0 0 1
 1.449.413l6.241 3.977h.03a5.558 5.558 0 0 0 2.898.797 5.968 5.968 0 0
 0 1.597-.236 5.572 5.572 0 0 0 2.896-2.049 5.544 5.544 0 0 0
 1.067-3.377V.266A.29.29 0 0 0 22.576 0a.293.293 0 0 0-.137.03z" />
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
