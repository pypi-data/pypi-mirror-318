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


class JuceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "juce"

    @property
    def original_file_name(self) -> "str":
        return "juce.svg"

    @property
    def title(self) -> "str":
        return "JUCE"

    @property
    def primary_color(self) -> "str":
        return "#8DC63F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>JUCE</title>
     <path d="M12 0C5.383 0 0 5.383 0 12s5.383 12 12 12 12-5.383
 12-12S18.617 0 12 0zm0 22.402c-5.744
 0-10.417-4.667-10.417-10.404S6.256 1.595 12 1.595s10.417 4.666 10.417
 10.403S17.744 22.402 12 22.402zm8.097-5.04a9.77 9.77 0 0 1-2.5 2.572
 1.23 1.23 0 0 1-1.787-.42c-.97-1.794-1.75-3.59-2.468-5.391a.504.504 0
 0 1 .669-.648c1.729.749 3.503 1.46 5.414 2.04a1.227 1.227 0 0 1 .672
 1.847zm1.615-5.36c0 .596-.053 1.179-.156 1.746a1.235 1.235 0 0
 1-1.559.97c-2.01-.583-3.87-1.324-5.687-2.111l.002.001a.503.503 0 0 1
 .013-.93c1.802-.713 3.606-1.48 5.416-2.437.727-.385 1.62.04
 1.782.846.124.619.19 1.26.19 1.915zm-6.847 7.713c.383.726-.04
 1.61-.842 1.78a9.67 9.67 0 0 1-2.021.212 9.702 9.702 0 0 1-1.607-.132
 1.233 1.233 0 0 1-.98-1.56c.583-2.003 1.322-3.854
 2.107-5.666a.503.503 0 0 1 .93.014h.002c.704 1.78 1.468 3.565 2.411
 5.352zM9.181 4.276a1.232 1.232 0 0 1 .844-1.782 9.745 9.745 0 0 1
 3.692-.05c.722.129 1.176.852.973 1.557-.585 2.028-1.33 3.9-2.125
 5.73a.503.503 0 0
 1-.93-.013h-.001c-.715-1.81-1.49-3.623-2.453-5.442zm-5.374 2.51a9.759
 9.759 0 0 1 2.635-2.747 1.233 1.233 0 0 1 1.787.42c1.021 1.88 1.83
 3.763 2.578 5.65a.504.504 0 0
 1-.668.648c-1.802-.783-3.644-1.53-5.64-2.13a1.234 1.234 0 0
 1-.692-1.842zm6.864 7.223c-.763 1.753-1.486 3.55-2.072 5.488a1.23
 1.23 0 0 1-1.838.679 9.77 9.77 0 0 1-2.662-2.53 1.23 1.23 0 0 1
 .414-1.794c1.834-.99 3.67-1.783 5.51-2.513a.504.504 0 0 1
 .648.668v.002zm2.72-3.872c.775-1.777 1.51-3.6 2.103-5.57a1.23 1.23 0
 0 1 1.85-.672A9.791 9.791 0 0 1 20 6.497a1.23 1.23 0 0 1-.425
 1.779c-1.842.998-3.688 1.796-5.538 2.53a.504.504 0 0
 1-.648-.67zm-9.098 4.78a1.229 1.229 0 0 1-1.773-.81 9.735 9.735 0 0
 1-.103-3.683 1.234 1.234 0 0 1 1.56-.981c2.02.584 3.888 1.328 5.713
 2.119a.503.503 0 0 1-.014.93c-1.79.71-3.585 1.474-5.383 2.425z" />
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
