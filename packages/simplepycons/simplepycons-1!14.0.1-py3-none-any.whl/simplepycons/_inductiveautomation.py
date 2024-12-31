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


class InductiveAutomationIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "inductiveautomation"

    @property
    def original_file_name(self) -> "str":
        return "inductiveautomation.svg"

    @property
    def title(self) -> "str":
        return "Inductive Automation"

    @property
    def primary_color(self) -> "str":
        return "#445C6D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Inductive Automation</title>
     <path d="M16.72
 11.998c0-.616-2.647-4.598-2.647-4.598-.21-.362-.885-.362-1.507-.001-.622.361-.956.947-.745
 1.31l.294.506.821 1.425H9.004l-1.43-.002c-.418 0-.758.61-.76
 1.36v.004c.002.75.342 1.36.76 1.36l1.43-.001h3.932l-.82
 1.424-.295.507c-.21.362.123.949.745 1.31.622.36 1.297.36 1.507-.002 0
 0 2.647-3.982 2.647-4.598v-.004M12 19.473a7.472 7.472 0 1 1 0-14.945
 7.472 7.472 0 1 1 0 14.945zM21.937 12c0-.322-.015-.64-.046-.955L24
 9.63a12.032 12.032 0 0 0-.42-1.577l-2.534-.172a10.03 10.03 0 0
 0-.958-1.655l1.116-2.274a12.27 12.27 0 0 0-1.156-1.157L17.773
 3.91a9.909 9.909 0 0 0-1.656-.958L15.945.419A12.085 12.085 0 0 0
 14.37 0l-1.415 2.108a10.124 10.124 0 0 0-1.912 0L9.631 0A12.02 12.02
 0 0 0 8.05.422l-.17 2.531a9.905 9.905 0 0 0-1.657.958L3.95
 2.795c-.41.36-.797.746-1.156 1.157l1.119 2.274a9.976 9.976 0 0 0-.959
 1.655L.42 8.053A12.13 12.13 0 0 0 0 9.63l2.109 1.413a9.76 9.76 0 0 0
 0 1.913L0 14.369a12.1 12.1 0 0 0 .42 1.579l2.534.17c.268.584.588
 1.136.959 1.653l-1.12 2.275c.361.411.748.799 1.16
 1.158l2.274-1.117c.517.368 1.07.69 1.654.957l.17 2.534c.513.173
 1.038.317 1.578.422l1.415-2.11c.315.029.632.048.956.048.321 0
 .642-.02.957-.049L14.372 24a12.208 12.208 0 0 0
 1.573-.422l.172-2.534c.584-.267 1.14-.589 1.657-.957l2.274
 1.117c.41-.36.796-.744
 1.156-1.156l-1.115-2.274c.37-.518.69-1.07.957-1.656l2.532-.17a12.13
 12.13 0 0 0 .422-1.58l-2.108-1.412a10 10 0 0 0 .045-.956m.658
 6.056c.113 0 .315.021.315-.126
 0-.094-.125-.111-.225-.111h-.246v.237zm.432.555h-.156l-.276-.425h-.155v.425h-.13v-.922h.401c.167
 0 .329.045.329.243 0 .182-.126.25-.292.254zm.314-.457a.718.718 0 0
 0-.716-.712.718.718 0 0 0-.717.712c0 .398.33.715.717.715a.72.72 0 0 0
 .716-.715zm-1.563 0c0-.468.373-.841.847-.841a.84.84 0 0 1
 .847.841.84.84 0 0 1-.847.844.839.839 0 0 1-.847-.844" />
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
