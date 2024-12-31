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


class SahibindenIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sahibinden"

    @property
    def original_file_name(self) -> "str":
        return "sahibinden.svg"

    @property
    def title(self) -> "str":
        return "Sahibinden"

    @property
    def primary_color(self) -> "str":
        return "#FFE800"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sahibinden</title>
     <path d="M0 0v24h24V0zm11.517 4.723c.563-.007 1.13-.004 1.69.063
 2.412.054 4.853 2.18 4.879
 4.508h-3.319c.009-.694-.603-1.555-1.279-1.732-1.105-.269-2.46-.355-3.43.294-.738.445-1.065
 1.672-.095 2.056 2.288 1.083 5.158.846 7.224 2.372 1.698 1.21 1.598
 3.666.274 5.086-1.718 1.84-4.636 2.132-7.099
 1.782-2.448-.117-4.755-2.245-4.819-4.562h3.311c-.056.832.638 1.557
 1.46 1.822 1.27.275 2.726.358 3.93-.19.96-.323
 1.024-1.544.284-2.103-1.595-.897-3.565-.924-5.297-1.518-2.012-.39-3.643-2.278-3.26-4.197.424-2.342
 3.127-3.727 5.546-3.681z" />
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
