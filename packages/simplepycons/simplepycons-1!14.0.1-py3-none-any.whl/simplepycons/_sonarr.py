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


class SonarrIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sonarr"

    @property
    def original_file_name(self) -> "str":
        return "sonarr.svg"

    @property
    def title(self) -> "str":
        return "sonarr"

    @property
    def primary_color(self) -> "str":
        return "#2596BE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>sonarr</title>
     <path d="M21.212 4.282c1.851 2.204 2.777 4.776 2.777 7.718 0
 2.848-.867 5.344-2.602 7.489a934.355 934.355 0 0
 1-2.101-2.095c-1.477-1.477-1.792-3.293-1.792-5.278 0-2.224.127-3.486
 1.577-4.935l2.478-2.478a13.209 13.209 0 0 0-.337-.421Zm-17.7
 16.193C1.708 18.678.6 16.59.188 14.213A11.84 11.84 0 0 1 .011
 12c0-.28.006-.548.017-.802 0-.026.007-.052.022-.078.153-2.601
 1.076-4.889 2.767-6.865-.108.127-.214.256-.316.387 0 0 1.351 1.346
 2.329 2.323 1.408 1.409 1.726 3.215 1.726 5.151 0 1.985-.249
 3.762-1.781 5.295-1.035 1.035-2.119 2.124-2.119
 2.124.112.136.229.271.349.404.029-.027 1.297-1.348 2.123-2.175
 1.638-1.637 1.928-3.528 1.928-5.648
 0-2.072-.365-3.997-1.873-5.504a620.045 620.045 0 0
 0-2.366-2.357c.168-.196.342-.388.523-.576l3.117 3.106-.194.195 1.903
 1.898.547-.549L6.81 6.432l-.196.196L3.495
 3.52c.01-.009.436-.416.643-.597.009.011 2.28 2.283 2.28 2.283 1.538
 1.537 3.5 1.955 5.621 1.955 2.18 0 4.134-.442 5.731-2.038.907-.908
 2.153-2.149 2.162-2.16.17.151.491.461.56.528l.013.013-3.111
 3.028-.001.002-.197-.194-1.876 1.903.552.543 1.875-1.903-.197-.194
 3.109-3.026c.193.203.377.41.553.619-.03.025-2.495 2.546-2.495
 2.546-1.556 1.556-1.723 2.9-1.723 5.288 0 2.121.361 4.054 1.939
 5.632a576.91 576.91 0 0 0 2.133
 2.124c-.183.208-.599.645-.613.66l-3.066-3.174.195-.196-1.995-1.986-.546.549
 1.995 1.986.195-.196 3.065
 3.172c-.021.019-.385.362-.552.506-.01-.013-1.974-1.978-1.974-1.978-1.842-1.842-3.299-2.039-5.731-2.039-2.338
 0-3.92.239-5.632 1.95-.944.944-2.078 2.085-2.089
 2.099-.275-.23-.649-.594-.649-.594l3.019-3.024.199.192
 1.854-1.925-.558-.538-1.854 1.926.199.191-3.016 3.022ZM12 8.672A3.33
 3.33 0 0 0 8.672 12 3.33 3.33 0 0 0 12 15.328 3.33 3.33 0 0 0 15.328
 12 3.33 3.33 0 0 0 12 8.672ZM4.52 2.6C6.665.867 9.162 0 12.011 0c2.88
 0 5.394.88 7.541 2.639 0 0-1.215 1.209-2.136 2.13-1.496 1.496-3.334
 1.892-5.377 1.892-1.985 0-3.829-.37-5.267-1.809L4.52 2.6Zm14.837
 18.909a9.507 9.507 0 0 1-.342.256C16.994 23.255 14.659 24 12.011
 24c-2.652 0-4.983-.745-6.993-2.235-.104-.074-.208-.15-.31-.227 0 0
 1.096-1.101 2.053-2.058 1.602-1.602 3.09-1.804 5.278-1.804 2.28 0
 3.651.166 5.377 1.892l1.941 1.941Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Sonarr/Sonarr/blob/913b845'''

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
