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


class WelcomeToTheJungleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "welcometothejungle"

    @property
    def original_file_name(self) -> "str":
        return "welcometothejungle.svg"

    @property
    def title(self) -> "str":
        return "Welcome to the Jungle"

    @property
    def primary_color(self) -> "str":
        return "#FFCD00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Welcome to the Jungle</title>
     <path d="M22.62
 3.783c-1.115-1.811-4.355-2.604-6.713-.265-.132.135-.306.548.218 1.104
 1.097 1.149 6.819 7.046 4.702 12.196-1.028 2.504-3.953
 2.073-5.052-2.076a23.184 23.184 0 0
 1-.473-9.367s.105-.394-.065-.52c-.117-.087-.305-.05-.547.33-.06.096-.048.076-.106.178l-.003.002c-1.622
 2.688-3.272 5.874-4.049
 7.07.38-1.803-.101-4.283-.85-6.359l-.142-.375c-.692-1.776-1.524-2.974-1.776-3.245-.03-.033-.105-.094-.353-.094H.398c-.49
 0-.448.412-.293.561 1.862 2.178 7.289 10.343 4.773
 18.355-.194.619.11.944.612.305 2.206-2.81 4.942-7.598
 6.925-11.187-.437 1.245-.822 2.63-1.028 4.083-.435 3.064.487 5.37
 1.162 6.58.345.619.803.998 1.988.824 6.045-.885 8.06-6.117 8.805-8.77
 1.357-4.839.363-7.568-.722-9.33" />
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
        yield from [
            "WTTJ",
        ]
