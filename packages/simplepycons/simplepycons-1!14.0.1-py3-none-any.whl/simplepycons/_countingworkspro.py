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


class CountingworksProIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "countingworkspro"

    @property
    def original_file_name(self) -> "str":
        return "countingworkspro.svg"

    @property
    def title(self) -> "str":
        return "CountingWorks PRO"

    @property
    def primary_color(self) -> "str":
        return "#2E3084"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CountingWorks PRO</title>
     <path d="M11.327.512c-3.806.034-7.447 3.19-7.181 7.75.102
 1.547.88 3.382 2.981 5.733a.365.365 0 0 0 .635-.23l.053-2.266a.36.36
 0 0 0-.1-.255 5.047 5.047 0 0 1 3.407-8.502c2.27-.104 4.011 1.236
 4.753 2.744.34.693.527 1.45.55 2.222a.357.357 0 0 0
 .343.344c.482.015.962.064 1.437.147a.359.359 0 0 0 .424-.344 7.237
 7.237 0 0 0-2.769-5.788C15.02 1.404 13.564.52 11.327.512zm4.94
 8.362a14.8 14.8 0 0 0-2.515.26.364.364 0 0 0-.17.635l1.695
 1.435a.36.36 0 0 0 .316.073 5.026 5.026 0 0 1 3.123.281c1.78.787 2.92
 2.414 3.042 4.304.208 3.187-2.48 5.539-5.277 5.37a5.032 5.032 0 0
 1-1.751-.412.365.365 0 0 0-.443.115c-.289.385-.603.75-.94
 1.094a.367.367 0 0 0 .09.573c1.887 1.073 3.936 1.16 6.014.32
 3.303-1.304 4.63-4.523
 4.545-6.847-.096-2.641-1.48-5.072-4.085-6.402-.921-.47-2.04-.812-3.643-.799zm-12.931
 1.2a.364.364 0 0 0-.152.052c-1.41.827-2.216 2.057-2.798
 3.777-.285.892-.386 1.51-.386 2.436a7.276 7.276 0 0 0 7.157
 7.141c1.129.017 2.104-.235 2.962-.583 1.45-.62 3.142-1.597
 4.65-4.912a.363.363 0 0 0-.459-.489l-2.365.867a.357.357 0 0
 0-.195.174 5.03 5.03 0 0 1-2.268 2.224C6 22.428 2.473 19.784 2.235
 16.74c-.145-1.741.494-3.053
 1.37-3.982.293-.308.41-.477.663-.662a.36.36 0 0 0 .098-.471 9.173
 9.173 0 0 1-.653-1.326.366.366 0 0 0-.377-.225z" />
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
