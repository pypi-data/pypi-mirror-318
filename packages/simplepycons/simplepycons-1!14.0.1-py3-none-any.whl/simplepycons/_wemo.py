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


class WemoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wemo"

    @property
    def original_file_name(self) -> "str":
        return "wemo.svg"

    @property
    def title(self) -> "str":
        return "WEMO"

    @property
    def primary_color(self) -> "str":
        return "#72D44C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WEMO</title>
     <path d="M4.3014 0C1.925 0 0 1.9254 0 4.302v15.3965C0 22.0728
 1.925 24 4.3014 24H19.697c2.3757 0 4.3026-1.9272
 4.3026-4.3015H24V4.3019C24 1.9258 22.0731 0 19.6974 0zm12.912
 4.1665c2.0881 0 3.7885 1.621 3.7885 3.6134 0
 .0947-.004.1877-.011.2799l-.0157.1756H14.651l.1142.3244c.3537.9944
 1.337 1.6628 2.4478 1.6628.8293 0 1.6137-.383
 2.0992-1.0237l.109-.1462.9896.6745-.12.1603c-.7109.9427-1.8618
 1.5054-3.0775 1.5054-2.0907 0-3.7912-1.6207-3.7912-3.613 0-1.9924
 1.7005-3.6134 3.7912-3.6134zm-13.9374.132h1.2095V8.729c0 .7302.5934
 1.3236 1.324 1.3236.7298 0 1.3243-.5934
 1.3243-1.3236V4.2986h1.2069v4.4303c0 .7302.5941 1.3236 1.3247
 1.3236.7298 0 1.3236-.5934 1.3236-1.3236V4.2986h1.2095v4.4303c0
 1.3964-1.136 2.5319-2.5331 2.5319-.648
 0-1.2892-.26-1.7604-.7137l-.1683-.1624-.168.1624c-.4712.4537-1.112.7137-1.7592.7137-1.3971
 0-2.5335-1.1355-2.5335-2.532zm13.9373 1.0248c-.987
 0-1.8822.5172-2.3362
 1.3484l-.1946.3586h5.0588l-.1946-.3586c-.4536-.8315-1.3478-1.3484-2.3334-1.3484zm-.0015
 7.2326c2.0893 0 3.7895 1.6217 3.7895 3.6137 0 1.993-1.7002
 3.6138-3.7895 3.6138-2.0903 0-3.789-1.621-3.789-3.6138 0-1.992
 1.699-3.6137 3.789-3.6137zm-11.403.1328c.6482 0 1.2906.2597
 1.7618.7134l.1668.1624.1687-.1624c.4719-.4537 1.1125-.7134
 1.7593-.7134 1.396 0 2.5323 1.1363 2.5323
 2.532v4.4303h-1.208v-4.4303c0-.7302-.5945-1.3247-1.324-1.3247-.7309
 0-1.3243.5945-1.3243
 1.3247v4.4303H7.1338v-4.4303c0-.7302-.5934-1.3247-1.325-1.3247-.7295
 0-1.323.5945-1.323 1.3247v4.4303h-1.209v-4.4303c0-1.3953 1.1367-2.532
 2.532-2.532zm11.403 1.0383c-1.422 0-2.579 1.096-2.579 2.443 0 1.3466
 1.157 2.4423 2.579 2.4423 1.4224 0 2.5782-1.0957 2.5782-2.4423
 0-1.347-1.1561-2.443-2.5782-2.443Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:WeMoA'''

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
