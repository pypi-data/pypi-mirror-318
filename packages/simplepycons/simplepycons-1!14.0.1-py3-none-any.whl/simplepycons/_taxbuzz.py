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


class TaxbuzzIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "taxbuzz"

    @property
    def original_file_name(self) -> "str":
        return "taxbuzz.svg"

    @property
    def title(self) -> "str":
        return "TaxBuzz"

    @property
    def primary_color(self) -> "str":
        return "#ED8B0B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TaxBuzz</title>
     <path d="M1.79 6.255c3.939-2.066 5.753.089
 5.753.089-2.289-.952-5.753-.089-5.753-.089zm6.556.089c-1.245-1.204-.595-4.787-.595-4.787-1.754
 3.27.595 4.787.595 4.787zm14.821 8.8s.312.728.505 1.606l-8.548
 6.452-2.343-6.373c-.704.236-2.667.723-5.506.055-3.598-.847-3.835-1.516-4.995-2.319-1.16-.803-1.962-2.497-2.156-3.152-.193-.654-.208-1.918.297-2.825.505-.907
 1.903-1.501 1.903-1.501s.818-.342 2.988-.446c2.172-.104 3.614.639
 3.614.639s-.788-2.601-.238-4.727S10.903.829 10.903.829s1.606.416
 2.943 2.602c.885 1.445 1.177 2.263 1.274 2.654 1.535-.355 3.389-1.046
 5.349-2.304 0 0 .954 2.695 3.531 10.785l-.833.578zm-11.551-7.76l.55
 1.412c4.765.238 7.938-2.453 7.938-2.453l-.327-.847c-4.177 2.84-8.161
 1.888-8.161 1.888zm-.776-5.66s1.182 1.691 2.096 4.62c0 0 .981.085
 1.762-.227-.001 0-1.506-4.237-3.858-4.393zm-.569
 6.734l.557.112-.825-2.364c2.071.228 2.341.138
 2.341.138-.424-1.959-1.84-4.675-1.84-4.675-.958.144-1.136 1.293-1.136
 1.293-.703 3.267.903 5.496.903 5.496zm-8.942.602c6.69 1.16 9.968
 3.769 9.968 3.769L9.891 9.033S8.469 7.505 5.209
 7.436c-3.244-.067-3.88 1.624-3.88 1.624zm11.016
 6.657l-.728-1.951c-4.62-3.2-10.354-4.504-10.354-4.504s-.156.19-.212
 1.026c-.056.836.346 1.628.948 2.598s1.762 1.594 2.564 2.099c.803.505
 2.839.978 4.616 1.12 1.787.14 3.166-.388
 3.166-.388zm.579-4.705c5.337-.268 7.79-2.787
 7.79-2.787l-.446-1.257c-3.345 2.869-7.879 2.497-7.879 2.497l.535
 1.547zm.996 2.527c4.668-.788 7.344-3.479
 7.344-3.479l-.387-1.189c-3.226 2.81-7.671 2.78-7.671 2.78l.714
 1.888zm.967 2.713c3.925-1.527 7.024-4.382
 7.024-4.382l-.39-1.137c-3.267 2.754-7.403 3.456-7.403 3.456l.769
 2.063zm7.648-2.386l-.479-1.316c-2.341 2.33-6.946 4.393-6.946
 4.393l.751 1.94 6.674-5.017zm-18.01 3.077c3.687 3.062 8.08.461
 8.08.461-4.72 1.085-8.08-.461-8.08-.461z" />
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
