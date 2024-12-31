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


class SystemSeventySixIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "system76"

    @property
    def original_file_name(self) -> "str":
        return "system76.svg"

    @property
    def title(self) -> "str":
        return "System76"

    @property
    def primary_color(self) -> "str":
        return "#585048"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>System76</title>
     <path d="M11.575.007A11.993 11.993 0 0 0 3.52 20.481l.124.121
 6.532-12.11H3.188l1.227 2.066a.632.632 0 0 1 .076.49.677.677 0 0
 1-.65.506.636.636 0 0 1-.544-.298L1.474 8.188a.633.633 0 0
 1-.095-.342v-.027a.648.648 0 0 1 .642-.628h9.256c.167 0
 .368.06.47.14l.01.008a.733.733 0 0 1 .22.942L4.908 21.388a.733.733 0
 0 1-.14.182 11.994 11.994 0 0 0 14.225.185h-5.632a.744.744 0 0
 1-.744-.744v-.015a.744.744 0 0 1 .744-.744h7.352a11.994 11.994 0 0
 0-.232-16.733 12.06 12.06 0 0
 0-1.618-1.358l-.003.006-.033.099c-.233.433-2.941 5.33-3.838
 6.951l-.329.595c-.753 1.302-1.099 2.767-.925 3.92a3.775 3.775 0 0 0
 .657 1.624 3.914 3.914 0 0 0 2.55 1.593 4.058 4.058 0 0 0 .682.058
 3.981 3.981 0 0 0 2.405-.798 3.792 3.792 0 0 0 1.48-2.412 3.784 3.784
 0 0 0-.7-2.892 4.015 4.015 0 0 0-2.583-1.581 4.377 4.377 0 0
 0-.177-.026.699.699 0 0 1-.614-.718.69.69 0 0 1 .233-.503.705.705 0 0
 1 .549-.172 5.41 5.41 0 0 1 3.735 2.182 5.18 5.18 0 0 1 .942 3.943
 5.18 5.18 0 0 1-2.18 3.418 5.393 5.393 0 0 1-3.088.963h-.001a5.479
 5.479 0 0 1-.915-.078 5.303 5.303 0 0 1-3.472-2.174 5.583 5.583 0 0
 1-.425-.706c-.717-1.416-.753-3.07-.102-4.785a18.44 18.44 0 0 1
 .758-1.678l4.078-7.45.096-.117.004-.008a12.04 12.04 0 0 0-.98-.467
 11.993 11.993 0 0 0-5.093-.94z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/system76/brand/blob/7a3174
0b54f929b62a165baa61dfb0b5164261e8/System76%20branding/system76-logo_s'''

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
