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


class MullerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "muller"

    @property
    def original_file_name(self) -> "str":
        return "muller.svg"

    @property
    def title(self) -> "str":
        return "Müller"

    @property
    def primary_color(self) -> "str":
        return "#F46519"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Müller</title>
     <path d="M17.433 14.671c-.056-1.287-.138-2.808-.138-3.013
 0-.623.097-2.252.21-2.64.138-.47.76-.582.76-1.133
 0-.868-1.388-.91-1.996-.91-1.833 0-1.843.414-2.553 1.711-.5.914-1.067
 2.584-1.496
 2.487-.613-.138-1.471-2.405-1.956-3.217-.419-.704-.388-.98-2.012-.98-1.113
 0-2.4.189-2.4.98 0 .567.792.664.93.95.153.322.209.75.209 1.578 0
 2.002-.128 3.288-.24 4.447-.107 1.134-.94.486-.94 1.272 0 .72
 1.261.76 1.747.76.54 0 2.027-.03 2.027-.816
 0-.746-.889-.056-.889-1.532 0-.455-.138-2.283.291-2.283.25 0
 .399.419.485.598l.802 1.797c.832 1.864.945 1.833 1.17
 1.864.439.056.939-1.522 1.245-2.155.332-.705.777-1.92 1.205-1.92.486
 0 .21 2.375.154 2.61-.097.444-.72.525-.72 1.01 0 .884 1.9.828
 2.471.828.608 0 2.507.04 2.507-.884
 0-.623-.832-.403-.873-1.409zm5.004-4.157c-.75.787-1.317 1.15-2.343
 1.492 1.031.362 1.598.735 2.343 1.531 1.297 1.39 1.609 2.635 1.548
 4.632v5.81h-5.827c-1.833.016-3.104-.31-4.498-1.536-.843-.74-1.241-1.307-1.66-2.35-.347
 1.032-.715 1.604-1.511 2.35-1.39 1.312-2.748 1.65-4.647
 1.537H.005v-5.811c-.05-1.772.312-3.12 1.553-4.504.766-.858
 1.358-1.261 2.435-1.66-1.077-.382-1.67-.776-2.435-1.618C.29 9.003.015
 7.68.005 5.842V.001h5.837c1.9-.016 3.15.29 4.534 1.542.848.77 1.241
 1.368 1.624 2.446.429-1.083.848-1.675 1.726-2.446C15.105.343
 16.386.052 18.158 0h5.827v5.841c.092 1.87-.225 3.284-1.548
 4.672zm-.893-8.042h-3.79c-1.68-.04-2.88.22-4.197 1.317-.76.634-1.123
 1.119-1.531
 2.017-.383-.893-.736-1.378-1.471-2.017-1.312-1.138-2.41-1.297-4.259-1.317H2.512l-.005
 3.784c-.02 1.532.169 2.599 1.088 3.87.669.925 1.22 1.384 2.252
 1.87-1.037.505-1.588.98-2.252 1.924-.888 1.262-1.088 2.155-1.072
 3.794v3.769h3.773c1.793-.01 2.957-.158 4.274-1.302.73-.639
 1.083-1.124 1.456-2.017.413.898.78 1.378 1.542 2.017 1.312 1.093
 2.446 1.378 4.187
 1.312h3.789v-3.779c-.01-1.521-.082-2.568-.97-3.824-.685-.965-1.282-1.44-2.375-1.895
 1.098-.47 1.69-.955 2.375-1.93.878-1.25.934-2.323.97-3.794z" />
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
