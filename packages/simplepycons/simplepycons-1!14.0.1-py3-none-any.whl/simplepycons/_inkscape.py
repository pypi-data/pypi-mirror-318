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


class InkscapeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "inkscape"

    @property
    def original_file_name(self) -> "str":
        return "inkscape.svg"

    @property
    def title(self) -> "str":
        return "Inkscape"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Inkscape</title>
     <path d="M7.666 14.871c.237.147 3.818.875 4.693
 1.02.303.064.088.376-.33.587-.943.251-5.517-1.607-4.363-1.607zm5.647-13.264l3.505
 3.56c.333.34.328.998.142 1.187l-1.74-1.392-.342
 2.061-1.455-.767-2.328 1.47-.771-3.1L9.073 6.79H7.16c-.78
 0-.871-.99-.163-1.698 1.237-1.335 2.657-2.696 3.429-3.485.776-.793
 2.127-.77 2.887 0zM9.786.97l-8.86 9.066c-2.993 3.707 2.038 3.276
 4.194 4.343.774.791-2.965 1.375-2.191 2.166.773.791 4.678 1.524 5.453
 2.314.773.791-1.584 1.63-.81 2.42.773.792 2.563.042 2.898 1.868.238
 1.304 3.224.56 4.684-.508.774-.791-1.48-.717-.706-1.508 1.923-1.967
 3.715-.714 4.373-2.686.325-.974-2.832-1.501-2.057-2.292 2.226-1.3
 9.919-2.146 6.268-5.796L13.85.97c-1.123-1.078-2.998-1.09-4.063
 0zm10.177 17.475c0 .45 3.314.745
 3.314-.106-.472-1.366-2.922-1.274-3.314.106zm-14.928 2.39c.784.679
 1.997-.169 2.36-1.116-.76-1.01-3.607.037-2.36
 1.116zm14.512-1.466c-1.011.908.114 1.828 1.111
 1.242.222-.225-.006-1.016-1.11-1.242Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://inkscape.org/gallery/=inkscape-brandi'''

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
