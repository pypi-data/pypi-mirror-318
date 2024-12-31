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


class SolidIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "solid"

    @property
    def original_file_name(self) -> "str":
        return "solid.svg"

    @property
    def title(self) -> "str":
        return "Solid"

    @property
    def primary_color(self) -> "str":
        return "#2C4F7C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Solid</title>
     <path d="M11.558.788A9.082 9.082 0 0 0
 9.776.99l-.453.15c-.906.303-1.656.755-2.1 1.348l-.301.452-2.035
 3.528c.426-.387.974-.698 1.643-.894h.001l.613-.154h.001a8.82 8.82 0 0
 1 1.777-.206c2.916-.053 6.033 1.148 8.423 2.36 2.317 1.175 3.888 2.32
 3.987 2.39L24
 5.518c-.082-.06-1.66-1.21-3.991-2.386-2.393-1.206-5.521-2.396-8.45-2.343zM8.924
 5.366a8.634 8.634 0 0 0-1.745.203l-.606.151c-1.278.376-2.095
 1.16-2.43 2.108-.334.948-.188 2.065.487 3.116.33.43.747.813 1.216
 1.147L12.328 10h.001a6.943 6.943 0 0 1 6.013
 1.013l2.844-.963c-.17-.124-1.663-1.2-3.91-2.34-2.379-1.206-5.479-2.396-8.352-2.344zm5.435
 4.497a6.791 6.791 0 0 0-1.984.283L2.94 13.189 0
 18.334l9.276-2.992a6.945 6.945 0 0 1 7.408 2.314v.001c.695.903.89
 1.906.66 2.808l2.572-4.63c.595-1.041.45-2.225-.302-3.429a6.792 6.792
 0 0 0-5.255-2.543zm-3.031 5.341a6.787 6.787 0 0 0-2.006.283L.008
 18.492c.175.131 2.02 1.498 4.687 2.768 2.797 1.332 6.37 2.467 9.468
 1.712l.454-.152h.002c1.278-.376 2.134-1.162
 2.487-2.09.353-.93.207-2.004-.541-2.978a6.791 6.791 0 0
 0-5.237-2.548z" />
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
