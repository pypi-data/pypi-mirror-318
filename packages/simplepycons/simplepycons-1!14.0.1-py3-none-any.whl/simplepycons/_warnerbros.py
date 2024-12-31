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


class WarnerBrosdotIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "warnerbros"

    @property
    def original_file_name(self) -> "str":
        return "warnerbros.svg"

    @property
    def title(self) -> "str":
        return "Warner Bros."

    @property
    def primary_color(self) -> "str":
        return "#004DB4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Warner Bros.</title>
     <path d="M16.5798 10.2379c-.5236 0-.9992.201-2.4648
 1.2525v5.6593c2.5407-2.8547 3.2641-4.808
 3.2641-5.81-.0026-.7013-.3264-1.1018-.7993-1.1018zm.1998-3.7564c0-1.0047-1.1458-1.8286-2.6646-1.9284v5.234c1.9165-1.1267
 2.664-2.2566
 2.664-3.3056zm4.5098-2.2211c-.0246-.0998-.05-.1373-.0999-.15l-1.796-.4763-.249-1.0268c-.0127-.0503-.0254-.0878-.0747-.0998l-1.8439-.501-.2238-.9773a.1372.1372
 0 00-.1-.1253L12.1154.0111a.6414.6414 0 00-.2372
 0l-4.789.8928a.1372.1372 0
 00-.0998.1253l-.2245.9773-1.8432.5003c-.05.012-.062.0496-.0747.0998l-.249
 1.0268-1.7914.477c-.0493.0127-.0746.0502-.0992.15a12.9347 12.9347 0
 00-.2245 2.4301c0 7.214 3.737 13.4768 9.3174 17.209A.2493.2493 0 0012
 24a.2493.2493 0 00.1999-.1005c5.5803-3.7322 9.3173-9.995
 9.3173-17.209a12.9906 12.9906 0 00-.2284-2.4301zm-9.9922 16.3208c0
 .0503-.05.075-.0992.0248-1.3703-1.5774-2.2916-3.5058-2.9144-5.6097l-.9466.6028c-.2491.1755-.4483.1005-.5995-.1748-1.2704-2.254-2.0924-5.9614-2.167-8.565a.4522.4522
 0 01.1246-.3255 11.8352 11.8352 0
 011.0958-1.1521c.0746-.075.1499-.0255.1499.0998 0 3.2057.5475 6.1858
 1.4195
 8.1396.0746.15.1492.15.2492.075l.2737-.1754c-.5229-2.329-.822-5.4343-.7474-9.0158
 0-.1253.0253-.1755.1-.225a8.7268 8.7268 0
 011.195-.6264c.1246-.0502.1499-.0247.1499.075-.0706 5.2086.3544
 8.8136 1.2743
 11.6938.0247.075.0993.0495.0993-.0255-.05-1.0516-.05-1.978-.05-3.1053l-.0493-8.991c0-.0998.0247-.15.1246-.1748a9.9022
 9.9022 0 011.245-.2257.0664.0664 0 01.0557.019.0672.0672 0
 01.019.056zm1.4949.0248c-.05.0503-.1.0255-.1-.0248V2.9757a.0672.0672
 0 01.019-.056.0664.0664 0 01.0557-.019c3.3373.2257 5.4797 1.6283
 5.4797 3.6565a3.4113 3.4113 0 01-.872 2.2774c1.0958.3007 1.5195
 1.1273 1.5195 2.2292.002 1.9538-1.4176 5.185-6.1 9.5422Z" />
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
