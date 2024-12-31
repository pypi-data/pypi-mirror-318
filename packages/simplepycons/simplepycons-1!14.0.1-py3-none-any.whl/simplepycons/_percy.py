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


class PercyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "percy"

    @property
    def original_file_name(self) -> "str":
        return "percy.svg"

    @property
    def title(self) -> "str":
        return "Percy"

    @property
    def primary_color(self) -> "str":
        return "#9E66BF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Percy</title>
     <path d="M13.235 2.4s.569 1.169.616 1.547c0
 0-1.856-.646-4.458-.891 0 0 1.25.872 1.734 1.538 0 0-1.84-.093-4.586
 0 0 0 1.561.634 2.252 1.215 0 0-3.26.331-5.103.862 0 0 2.076.73 2.652
 1.276 0 0-2.648.754-5.316 2.294 0 0 1.482.26 2.642.766 0 0-1.478
 1.033-3.668 3.852 0 0 1.62-.309 2.73-.222 0 0-1.407 1.644-2.141 4.158
 0 0 .813-.518 1.602-.706 0 0 .084 2.998 1.724 3.478v-.002a.774.774 0
 0 0 .225.034c.08 0 .163-.012.248-.036.52-.15.915-.663
 1.37-1.256.15-.195.303-.395.466-.59.2-.284.438-.54.706-.762.58-.478
 1.38-.84 2.358-.695 1.1.093 1.78 1.189 2.327 2.07.283.458.659 1.27
 1.289 1.27.696 0 .94-.834 1.25-1.862.292-.97.726-1.891 1.29-2.732
 1.085-1.617 2.474-2.495 4.14-3.36 1.595-.83 3.102-1.614
 3.858-2.803.379-.594.567-1.325.558-2.169a6.966 6.966 0 0
 0-.31-1.909c-.139-.455-.505-.902-.939-.72a3.417 3.417 0 0
 1-1.151.256c-.858-.805-3.379-2.4-5.038-3.303 0 0 .202.592.482 1.699 0
 0-1.787-1.396-3.81-2.296zm0 2.7 3.81.945-1.233.255zM9.957
 6.67l4.571.354-1.388.46Zm6.955
 1.082-.678.514-2.383.134zm-5.784.514-1.088.73-3.018-.287Zm4.505
 1.206-1.105.617-3.002-.176zm-8.282.77-.679 1.312-2.982
 1.313zm4.135.533-.77 1.265-3.853.942zm-5.845 2.354-.118 1.313L3.6
 16.2zm11.31 3.151c-1.093 1.127-2.002 2.806-2.232 4.121.39.58.746.867
 1.08.873h.012c.346 0
 .575-.233.68-.693.077-.343.094-.813.114-1.36.029-.844.067-1.894.346-2.94zm-7.904
 2.512c-1.018.011-2.008.83-2.506
 1.532v.001c.283.64.587.953.925.953a.53.53 0 0 0
 .082-.007c.46-.072.886-.963 1.242-1.825a19.8 19.8 0 0 0 .257-.654z"
 />
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
