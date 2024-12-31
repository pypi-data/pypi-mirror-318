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


class DribbbleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dribbble"

    @property
    def original_file_name(self) -> "str":
        return "dribbble.svg"

    @property
    def title(self) -> "str":
        return "Dribbble"

    @property
    def primary_color(self) -> "str":
        return "#EA4C89"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dribbble</title>
     <path d="M12 24C5.385 24 0 18.615 0 12S5.385 0 12 0s12 5.385 12
 12-5.385 12-12 12zm10.12-10.358c-.35-.11-3.17-.953-6.384-.438 1.34
 3.684 1.887 6.684 1.992 7.308 2.3-1.555 3.936-4.02 4.395-6.87zm-6.115
 7.808c-.153-.9-.75-4.032-2.19-7.77l-.066.02c-5.79 2.015-7.86
 6.025-8.04 6.4 1.73 1.358 3.92 2.166 6.29 2.166 1.42 0 2.77-.29
 4-.814zm-11.62-2.58c.232-.4 3.045-5.055
 8.332-6.765.135-.045.27-.084.405-.12-.26-.585-.54-1.167-.832-1.74C7.17
 11.775 2.206 11.71 1.756 11.7l-.004.312c0 2.633.998 5.037 2.634
 6.855zm-2.42-8.955c.46.008 4.683.026
 9.477-1.248-1.698-3.018-3.53-5.558-3.8-5.928-2.868 1.35-5.01
 3.99-5.676 7.17zM9.6 2.052c.282.38 2.145 2.914 3.822 6 3.645-1.365
 5.19-3.44 5.373-3.702-1.81-1.61-4.19-2.586-6.795-2.586-.825
 0-1.63.1-2.4.285zm10.335 3.483c-.218.29-1.935 2.493-5.724
 4.04.24.49.47.985.68 1.486.08.18.15.36.22.53 3.41-.43 6.8.26
 7.14.33-.02-2.42-.88-4.64-2.31-6.38z" />
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
