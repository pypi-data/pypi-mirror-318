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


class FantomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fantom"

    @property
    def original_file_name(self) -> "str":
        return "fantom.svg"

    @property
    def title(self) -> "str":
        return "Fantom"

    @property
    def primary_color(self) -> "str":
        return "#0928FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fantom</title>
     <path d="M10.9604.2299c.5833-.3065 1.4709-.3065 2.0542 0l5.9522
 3.1279c.3513.1846.5442.4597.5788.7437h.0057V19.824c-.0077.3097-.2025.6174-.5845.8182l-5.9522
 3.1279c-.5833.3065-1.4708.3065-2.0542
 0l-5.9521-3.1279c-.3804-.1999-.563-.5098-.572-.8182a1.1165 1.1165 0 0
 1-.0002-.0767V4.2025a.7965.7965 0 0
 1-.0002-.051l.0004-.05h.0026c.0265-.2871.2106-.5552.5694-.7437Zm7.6538
 12.643-5.5996 2.9427c-.5833.3066-1.4709.3066-2.0542
 0l-5.5874-2.936v6.9132l5.5874
 2.9207c.3155.1678.643.3313.9632.3521l.064.0021c.3336.0011.6575-.1674.986-.327l5.6406-2.973Zm-15.146
 6.6093c0 .6022.0703.9982.21
 1.2772.1158.2312.2896.4078.6068.6229l.0181.0122a7.138 7.138 0 0 0
 .2397.153l.1101.067.3381.2032-.4849.7976-.3784-.2275-.0636-.0388a8.4255
 8.4255 0 0
 1-.2847-.1817c-.9042-.6065-1.2414-1.2677-1.248-2.6433l-.0001-.0419Zm8.0507-10.8233a.855.855
 0 0 0-.121.0514l-5.9521 3.1279a.735.735 0 0
 0-.0179.0097l-.005.0029.0093.0053.0136.0073 5.9522 3.1279a.8546.8546
 0 0 0 .121.0514zm.9372 0v6.3839a.8538.8538 0 0 0
 .121-.0514l5.9521-3.128a.8117.8117 0 0 0
 .0179-.0096l.005-.003-.0094-.0052-.0136-.0073-5.9521-3.128a.8534.8534
 0 0 0-.121-.0513zm6.1581-3.4421-5.3394 2.806 5.3394 2.8059zM5.373
 5.2234v5.5987L10.7
 8.0227Zm7.204-4.1692c-.3095-.1627-.8695-.1627-1.179 0L5.4458
 4.182a.6432.6432 0 0 0-.0179.0097l-.005.003.0093.0052.0136.0074
 5.9522 3.1279c.3095.1626.8695.1626 1.179 0l5.9522-3.128a.643.643 0 0
 0
 .0179-.0097l.005-.0029-.0094-.0053-.0136-.0073zm6.9169.343.3784.2273.0636.0389c.1094.0672.2.125.2847.1817.9042.6065
 1.2414 1.2677 1.248
 2.6433l.0001.0419h-.9368c0-.6024-.0704-.9983-.2101-1.2773-.1158-.2312-.2896-.4078-.6068-.6228l-.0181-.0122a7.2984
 7.2984 0 0 0-.2397-.1532l-.1101-.067-.3381-.203z" />
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
