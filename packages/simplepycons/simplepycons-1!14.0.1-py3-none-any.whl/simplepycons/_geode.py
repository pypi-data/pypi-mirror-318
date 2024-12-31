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


class GeodeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "geode"

    @property
    def original_file_name(self) -> "str":
        return "geode.svg"

    @property
    def title(self) -> "str":
        return "Geode"

    @property
    def primary_color(self) -> "str":
        return "#8D7ACF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Geode</title>
     <path d="M12 0c-.30206 0-.60438.09583-.85742.28906L.5957
 8.34375c-.4705.3593-.66703.97346-.49218 1.53906l4.05664
 13.1211c.1829.59168.7303.99609 1.3496.99609h12.98047c.61931 0
 1.1667-.40441
 1.34961-.9961l4.05664-13.12109c.17485-.5656-.02168-1.17975-.49218-1.53906l-.97266-.74219-1.11914
 3.51758-3.07031
 9.99024c-.12005.3903-.48032.65624-.88868.65624H6.57813c-.40836
 0-.76863-.26593-.88868-.65624l-3.36132-10.9336c-.11419-.37133.01411-.77514.32226-1.01172l8.74805-6.7168a.93.93
 0 0 1 .10937-.07226L13.55273.82031l-.6953-.53125C12.60437.09583
 12.30205 0 12 0m.06836 4.75781c-.16254
 0-.32493.05197-.46094.15625l-6.52344
 5.0039c-.25142.19277-.35688.52145-.26367.82423l.4336 1.4082
 2.19726-1.61914 4.31445-3.37695c.13717-.10727.33159-.10727.46875
 0l4.70508 3.68164c.12315.09628.17407.25661.1289.40625l-1.80858
 5.99219c-.0483.15993-.19619.26953-.36329.26953H9.10352a.377.377 0 0
 1-.07618-.0078H6.9004l.42774
 1.39257c.0979.3179.39196.53516.7246.53516h8.0332c.33265 0
 .62477-.21725.72266-.53516l2.50977-8.14648c.09321-.30278-.01225-.63146-.26367-.82422l-6.5254-5.00392c-.136-.10428-.29839-.15625-.46093-.15625Z"
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
        return '''https://github.com/geode-sdk/website/blob/a6a'''

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
