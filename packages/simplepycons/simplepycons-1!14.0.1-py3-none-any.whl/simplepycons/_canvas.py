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


class CanvasIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "canvas"

    @property
    def original_file_name(self) -> "str":
        return "canvas.svg"

    @property
    def title(self) -> "str":
        return "Canvas"

    @property
    def primary_color(self) -> "str":
        return "#E72429"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Canvas</title>
     <path d="M.4403 15.4142a13.7061 13.7061 0 0 1-.4362-3.4403 13.7
 13.7 0 0 1 .4362-3.4401c1.7144.2103 3.0438 1.6686 3.0438 3.44 0
 1.771-1.3287 3.23-3.0438 3.4404zm3.9728-3.4403c0 .6004.4866 1.0873
 1.0872 1.0873.601 0 1.088-.487
 1.088-1.0873s-.487-1.088-1.088-1.088c-.6006 0-1.0872.4876-1.0872
 1.088zM23.56 8.5338c-1.7151.2103-3.044 1.6686-3.044 3.44 0 1.771
 1.3289 3.23 3.044 3.4404a13.7313 13.7313 0 0 0
 .436-3.4403c0-1.1883-.1518-2.3413-.436-3.4401zm-6.148 3.44c0
 .6005.4865 1.0874 1.0877 1.0874.6002 0 1.088-.487
 1.088-1.0873s-.4878-1.088-1.088-1.088c-.6012 0-1.0877.4876-1.0877
 1.088zm-5.4347 8.5465c-1.7709 0-3.229 1.33-3.44 3.044a13.7364 13.7364
 0 0 0 3.441.4357c1.1885 0 2.3403-.1515
 3.44-.4357-.2107-1.714-1.6687-3.044-3.441-3.044zm.001-3.1046c-.6012
 0-1.0878.4876-1.0878 1.0883s.4866 1.0882 1.0878 1.0882c.6 0
 1.087-.4874 1.087-1.0882s-.487-1.0883-1.087-1.0883zm0-13.936c1.7713 0
 3.2295-1.3292 3.4399-3.0438A13.7353 13.7353 0 0 0 11.9782 0c-1.1887
 0-2.3412.1519-3.441.4359.211 1.7146 1.6691 3.0438 3.441 3.0438zm0
 .9291c-.6012 0-1.0878.4866-1.0878 1.0876 0 .6002.4866 1.0876 1.0878
 1.0876.6 0 1.087-.4874 1.087-1.0876
 0-.601-.487-1.0876-1.087-1.0876zm6.032 13.5965c-1.2514 1.2523-1.344
 3.2211-.2825 4.582a13.762 13.762 0 0 0
 4.8636-4.8654c-1.3608-1.0597-3.3299-.9673-4.5812.2834zm-.6568-2.1948c-.425-.4245-1.1135-.4245-1.539
 0-.4243.4252-.4243 1.1136 0 1.5383.4255.4253 1.114.4253 1.539 0
 .424-.4247.424-1.1131 0-1.5383zM5.9648 5.9603c1.2516-1.2513
 1.3437-3.2206.2825-4.5813a13.7677 13.7677 0 0 0-4.8644 4.8643c1.3612
 1.0616 3.3306.9687 4.582-.283zm.6567.6572c-.424.4247-.424 1.1139 0
 1.5383.4245.4246 1.114.4246 1.5382 0 .4248-.4244.4248-1.1136
 0-1.5383-.4243-.4243-1.1137-.4243-1.5382 0zm15.9625-.3857a13.7597
 13.7597 0 0 0-4.8637-4.8642c-1.0614 1.3609-.969 3.33.2823 4.5818
 1.2517 1.2507 3.2204 1.3436 4.5814.2824zM17.346
 8.1443c.4237-.4248.4237-1.1135
 0-1.5383-.425-.4247-1.1145-.4247-1.5388 0-.4241.4248-.4241 1.1135 0
 1.5383.4243.4243 1.1137.4243 1.5388 0zM1.3772 17.7087a13.763 13.763 0
 0 0 4.8647
 4.8654c1.0613-1.3608.9685-3.3297-.2833-4.5818-1.2512-1.251-3.2204-1.3436-4.5814-.2836zm5.2385-1.9115c-.4238.4247-.4238
 1.1136 0 1.5384.425.4246 1.1141.4246 1.5382 0 .425-.4248.425-1.1137
 0-1.5384-.4241-.4245-1.1131-.4245-1.5382 0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.instructure.com/about/brand-guide'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.instructure.com/about/brand-guide'''

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
