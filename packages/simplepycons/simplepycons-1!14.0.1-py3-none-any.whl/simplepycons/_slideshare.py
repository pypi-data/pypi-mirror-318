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


class SlideshareIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "slideshare"

    @property
    def original_file_name(self) -> "str":
        return "slideshare.svg"

    @property
    def title(self) -> "str":
        return "SlideShare"

    @property
    def primary_color(self) -> "str":
        return "#008ED2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SlideShare</title>
     <path d="M3.222.21C1.762.21 1.06 1.337 1.06
 2.497v7.883c-.53-.502-1.096-.15-1.058.295.038.439.59 1.546 1.436
 2.517.843.968 1.924 1.776 2.94 2.268a11.19 11.19 0 00-.491 3.598c.09
 1.096.378 1.95.903 2.75.918 1.407 2.32 1.985 3.674 1.985 1.209 0
 2.494-.563 2.698-2.373v-4.694c1.308.552 3.47.363
 4.47-.39.19-.14.326-.207.416-.113.095.09.106.166-.113.439a5.6 5.6 0
 01-3.103 1.965l.008 2.72a2.532 2.532 0 002.543 2.446c1.64.015
 2.48-.556 3.148-1.164.632-.567 1.399-1.754 1.558-3.243a10.128 10.128
 0 00-.454-3.926 10.358 10.358 0 002.948-2.268C23.213 12.5 24 11.185
 24
 10.675c0-.51-.556-.782-1.036-.302V2.497c0-.824-.48-2.29-2.135-2.29zm.423
 1.35H20.41c.756 0 1.17.28 1.17 1.224v8.904a8.73 8.73 0 01-3.555
 1.534c-1.606.352-2.94.087-3.666.148-.718.06-1.428.529-1.296
 1.79-.491-.154-1.236-.683-1.682-1.117-.438-.428-.87-.711-1.534-.692-1.013.03-1.663.102-2.57.01a9.656
 9.656 0 01-4.838-1.786V2.78c0-.87.378-1.22 1.206-1.22zm4.497
 4.988a2.994 2.994 0 100 5.987 2.993 2.993 0 000-5.983zm7.71 0a2.994
 2.994 0 100 5.987 2.993 2.993 0 000-5.983z" />
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
