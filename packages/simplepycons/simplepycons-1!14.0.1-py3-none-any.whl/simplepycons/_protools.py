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


class ProToolsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "protools"

    @property
    def original_file_name(self) -> "str":
        return "protools.svg"

    @property
    def title(self) -> "str":
        return "Pro Tools"

    @property
    def primary_color(self) -> "str":
        return "#7ACB10"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pro Tools</title>
     <path d="M.505 15.452Q.27 14.63.14 13.762.01 12.891.01
 12q0-2.49.94-4.673.94-2.184 2.572-3.804Q5.155 1.902 7.339.938 9.523 0
 12.012 0q2.465 0 4.65.94 2.183.962 3.815 2.583 1.633 1.62 2.572
 3.804.94 2.184.94 4.673 0 .869-.118 1.714-.118.846-.352
 1.644.21.047.34.07l.13.024-1.363 3.429-.188-.012-.54-.106Q21.1 19.937
 20.02 20.9q-1.057.987-2.325 1.668-1.268.68-2.724
 1.056-1.433.376-2.96.376-1.55
 0-3.005-.376-1.433-.375-2.7-1.068-1.269-.693-2.35-1.656-1.08-.963-1.878-2.16-.282.094-.434.117l-.153.024-1.48-3.382.118.012.376-.059zM22.744
 12q0-2.23-.846-4.18-.845-1.95-2.301-3.405-1.456-1.456-3.429-2.301-1.949-.846-4.156-.846-2.231
 0-4.18.846-1.973.845-3.429 2.3Q2.947 5.872 2.102 7.82 1.256 9.77
 1.256 12q0 .751.106 1.491.106.74.317 1.444.892-.516 2.02-1.972
 1.127-1.456 1.808-2.912.352-.728.916-1.597.54-.869
 1.338-1.632.799-.763 1.855-1.256 1.057-.517 2.396-.517 1.315 0
 2.419.587 1.103.587 1.913 1.35.81.764 1.304
 1.492.516.727.657.986.165.282.47.94.329.633.728 1.361.4.728.822
 1.433.423.68.798
 1.033.259.258.564.446.305.188.61.329.212-.728.33-1.48.117-.751.117-1.526zM12.012
 22.732q1.338 0 2.583-.305 1.268-.33 2.383-.916 1.116-.587
 2.055-1.41.94-.821
 1.668-1.83-.94-.494-2.173-1.645-1.233-1.15-2.5-3.358-.142-.235-.494-.94-.352-.704-.857-1.455-.505-.752-1.115-1.339t-1.268-.587q-.681
 0-1.386.634-.704.61-1.303 1.386-.6.775-1.022
 1.503-.423.704-.54.916-1.174 2.066-2.477 3.205-1.304 1.139-2.29
 1.656.728 1.01 1.667 1.831.963.846 2.079 1.433 1.115.587 2.36.892
 1.268.329 2.63.329z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://cdn-www.avid.com/Content/fonts/avidmo'''

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
