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


class WolframLanguageIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wolframlanguage"

    @property
    def original_file_name(self) -> "str":
        return "wolframlanguage.svg"

    @property
    def title(self) -> "str":
        return "Wolfram Language"

    @property
    def primary_color(self) -> "str":
        return "#DD1100"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wolfram Language</title>
     <path d="M14.335
 12.431c-.552.15-.615.18-1.164.337-.589-.337-1.107-.526-1.595-.463.057-.306.151-.525.245-.8
 1.036-.15 1.805.4 2.514.926zm5.308 7.201a10.795 10.795 0 0 1-1.907
 1.52h-.006l-3.702-4.613 3.07.336s1.47.151 1.807 0c.308-.117
 1.963-2.449
 1.963-2.449s-4.76-3.009-6.384-4.666c.188-2.793-.213-6.508-.213-6.478-1.193
 1.195-1.35 1.383-2.544 2.489-.52-1.688-.769-2.27-1.289-3.958-1.568
 1.289-2.763 3.464-3.62 6.016a12.29 12.29 0 0
 0-.55.656c-.113.157-.23.313-.345.475a16.126 16.126 0 0 0-1.101
 1.819c-.063.112-.125.231-.188.35-.913 1.788-1.676 3.79-2.338
 5.604A10.824 10.824 0 0 1 1.205 12c0-2.862 1.138-5.613
 3.163-7.64A10.785 10.785 0 0 1 12 1.202a10.8 10.8 0 0 1 7.642
 3.158A10.83 10.83 0 0 1 22.797 12a10.813 10.813 0 0 1-3.154 7.633M12
 6.691c.832-.801.951-.92 1.75-1.69.064 1.533.032 2.334-.062
 4.204-.463-.458-1.381-1.044-1.381-1.044S12.126 7.09 12 6.69m3.834
 15.463C9.218 24.547 4.436 20.14 3.417
 18.602c.006-.014.006-.027.006-.039.92-3.889 2.058-8.535
 3.884-9.91.955-1.655 1.231-4.113 2.943-5.401.432 1.288 1.107 3.958
 1.57 5.246 2.025 2.025 5.087 4.545 7.146
 5.59.212.12.489.98.489.98l-.825
 1.038-8.835-.887c-.2-.02-.394-.028-.594-.028-.569
 0-1.15.073-1.833.18.432-1.07 1.35-1.936
 1.35-1.936s-.855-.519-1.505-.605c.187-.432.681-.989.8-1.138-.244.087-2.026.888-2.208
 1.563.857.214 1.47.487 1.47.487s-.95.957-1.132 2.612c0 0 2.82-.43
 4.939-.153.063.03.094.03.125.03l1.102.031 3.509 5.84.027.046a.012.012
 0 0 1-.011.006m4.652-18.64A12.02 12.02 0 0 0 12 0C8.818 0 5.768 1.27
 3.516 3.515a12.025 12.025 0 0 0-3.513 8.484c0 3.183 1.27 6.235 3.512
 8.478a11.98 11.98 0 0 0 16.97 0 11.966 11.966 0 0 0
 3.512-8.478c0-3.181-1.26-6.233-3.511-8.484z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://company.wolfram.com/press-center/lang'''

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
