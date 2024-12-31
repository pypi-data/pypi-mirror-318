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


class CyclingSeventyFourIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cycling74"

    @property
    def original_file_name(self) -> "str":
        return "cycling74.svg"

    @property
    def title(self) -> "str":
        return "Cycling '74"

    @property
    def primary_color(self) -> "str":
        return "#111111"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cycling '74</title>
     <path d="M5.283 9.033c-.042-.354.425-.74.87-1.057.636-.453
 1.682-.82 2.892-.962 1.093-.127 2.099-.045 2.816.189.632.206
 1.263.503 1.31.906.046.4-.496.836-1.06
 1.182-.644.394-1.606.708-2.703.837-1.206.14-2.306.025-3.03-.267-.509-.206-1.053-.473-1.095-.828zm16.77-1.542c.365-.022.742.614
 1.05 1.216.438.861.772 2.244.87 3.818.087 1.422-.038 2.715-.307
 3.62-.236.798-.566 1.586-.981
 1.61-.413.026-.837-.712-1.169-1.47-.379-.867-.662-2.137-.75-3.563-.096-1.57.066-2.98.395-3.89.23-.639.527-1.319.893-1.341zm-8.16
 6.443c-.022-.336.362-.674.726-.948.522-.391 1.367-.677
 2.335-.74.874-.055 1.674.082 2.238.345.496.233.989.552
 1.014.935.024.382-.422.762-.882
 1.055-.525.336-1.302.576-2.179.632-.966.063-1.839-.111-2.406-.43-.399-.225-.824-.51-.846-.849zM18.16
 6.41c.288.177.343.685.357 1.14.02.65-.233 1.503-.74
 2.327-.457.745-1.028 1.317-1.568
 1.624-.476.271-1.02.488-1.347.287-.327-.2-.38-.782-.355-1.326.028-.622.279-1.392.737-2.14.505-.822
 1.149-1.434 1.736-1.71.413-.196.89-.379 1.18-.202zM.382
 6.211c.294-.168.771.04 1.183.257.588.31 1.228.967 1.722
 1.834.447.784.685 1.582.704 2.219.015.56-.048 1.155-.382
 1.345-.333.19-.876-.056-1.349-.353-.54-.34-1.107-.952-1.555-1.738C.211
 8.91-.028 8.027.003 7.363c.021-.467.085-.984.38-1.152zm11.85
 4.283c.32.188.341.828.32 1.406-.032.827-.398 1.948-1.054 3.066-.593
 1.01-1.305 1.814-1.958
 2.277-.575.407-1.225.756-1.589.542-.362-.212-.375-.948-.301-1.645.084-.797.44-1.813
 1.036-2.826.655-1.115 1.453-1.979 2.159-2.41.496-.303 1.066-.598
 1.387-.41Z" />
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
