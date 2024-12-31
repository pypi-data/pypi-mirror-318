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


class RavelryIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ravelry"

    @property
    def original_file_name(self) -> "str":
        return "ravelry.svg"

    @property
    def title(self) -> "str":
        return "Ravelry"

    @property
    def primary_color(self) -> "str":
        return "#EE6E62"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ravelry</title>
     <path d="M23.9718
 10.9238c-.0597-.51098-.084-1.02918-.1851-1.53174-.1227-.61046-.2793-1.21823-.4755-1.80886-.34288-1.03247-.84358-1.9895-1.52577-2.84163-.2955-.3691-.59489-.73971-.92998-1.07185-.699-.69252-1.47808-1.28586-2.32827-1.78481-.88588-.52-1.81527-.9414-2.80316-1.21913-.54449-.153-1.10068-.26842-1.65627-.37632-.3351-.06493-.67949-.08236-1.01938-.12264-.0156-.0018-.0297-.01773-.0444-.02735-.5319.0003-1.06379.0003-1.59568.0003-.1191.01924-.2376.04569-.3576.0568-.57748.05381-1.13818.18667-1.69287.35078-.68279.20169-1.33498.47912-1.96527.80825-.66029.34506-1.28548.74813-1.88187
 1.19388-.3048.22783-.6063.46258-.88829.71747-.50279.45507-1.00678.91104-1.47897
 1.39707-.6378.65676-1.18769 1.38595-1.66288 2.17196C1.05934
 7.533.71345 8.2628.46776 9.03978c-.1773.56118-.3054 1.13197-.3801
 1.7178-.0744.58431-.1062 1.17043-.0768 1.75565.0336.66577.0951
 1.32944.2187 1.9886.1713.91345.4392 1.79083.82679
 2.63394.3207.69703.72149 1.34267 1.18618
 1.95344.3897.51187.83099.97476 1.30258 1.40428.63239.5759 1.32508
 1.07546 2.06487 1.5116.87719.51728 1.79787.92937 2.76266
 1.24918.65639.21762 1.32808.37271
 2.00847.48603.3.0499.60659.06192.90988.09258.0204.0021.0393.01834.0588.02765h1.59568c.1239-.01924.2472-.04629.372-.05651.80728-.06583
 1.58667-.2636 2.34686-.52961.85018-.29787 1.66557-.6784
 2.41916-1.17705.4818-.31861.95849-.64624
 1.42018-.9931.2859-.21491.54299-.4695.80579-.71447.1959-.18275.38369-.37452.56879-.56839.59639-.6261
 1.11118-1.31471 1.55307-2.05773.4716-.79292.8577-1.62611
 1.10219-2.51671.1413-.51459.2445-1.04.3468-1.5642.051-.2609.0618-.5299.0924-.79502.0018-.01563.0177-.02976.0273-.04448v-1.8314c-.0096-.02946-.0246-.058-.0282-.08807zm-7.96218-.05682s-.81899-.14728-1.40698-.14728c-1.34398
 0-1.65897.7364-1.65897
 1.8305v4.62885H9.31072V7.75303h3.63295v1.57802c.441-1.32554
 1.32298-1.78842 3.06595-1.78842z" />
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
