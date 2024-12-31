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


class StrykerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "stryker"

    @property
    def original_file_name(self) -> "str":
        return "stryker.svg"

    @property
    def title(self) -> "str":
        return "Stryker"

    @property
    def primary_color(self) -> "str":
        return "#E74C3C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Stryker</title>
     <path d="M11.852 0C5.34.08.079 5.341 0 11.852h1.857v.296H0C.08
 18.66 5.34 23.921 11.852 24v-1.857h.296V24C18.66 23.92 23.921 18.66
 24 12.148h-1.857v-.296H24C23.92 5.34 18.66.079 12.148
 0v1.857h-.296Zm.505 2.83c1.44 0 2.561.31 3.373.894.812.583 1.441
 1.373 1.88
 2.371l.234.53-2.73.957-.191-.472c-.222-.545-.52-.973-.909-1.27-.384-.29-.924-.418-1.612-.418-.73
 0-1.332.162-1.8.505-.425.313-.61.817-.61 1.49 0
 .332.041.628.13.883.081.23.22.437.408.62.223.216.516.419.881.614.398.213.89.43
 1.481.65a18.254 18.254 0 0 1 1.756.784 6.345 6.345 0 0 1 1.545
 1.106A4.91 4.91 0 0 1 17.28 13.7c.26.624.399 1.382.399 2.277a4.88
 4.88 0 0 1-.427 2.013 5.054 5.054 0 0 1-1.183 1.657 5.57 5.57 0 0
 1-1.792 1.108 6.182 6.182 0 0 1-2.266.406c-.832
 0-1.56-.107-2.183-.316a5.6 5.6 0 0 1-1.638-.84 4.988 4.988 0 0
 1-1.145-1.198 6.109 6.109 0 0 1-.692-1.362l-.177-.496
 2.662-.998.18.517a4.164 4.164 0 0 0
 .38.797c.144.239.331.449.556.63.232.187.513.337.844.453.342.12.754.177
 1.238.177a3.654 3.654 0 0 0 .966-.132 2.295 2.295 0 0 0 .813-.403
 1.98 1.98 0 0 0 .569-.728c.154-.32.224-.711.224-1.173
 0-.505-.057-.925-.184-1.258a2.133 2.133 0 0
 0-.554-.81c-.278-.258-.641-.485-1.09-.688a57.733 57.733 0 0
 0-1.798-.774c-1.342-.548-2.325-1.22-2.962-1.997-.666-.814-1.007-1.814-1.007-3.009
 0-.656.122-1.273.364-1.85a4.245 4.245 0 0 1 1.079-1.527 5.073 5.073 0
 0 1 1.683-.992c.644-.234 1.383-.355 2.22-.355z" />
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
