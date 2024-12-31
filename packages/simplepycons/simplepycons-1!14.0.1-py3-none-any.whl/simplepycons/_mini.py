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


class MiniIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mini"

    @property
    def original_file_name(self) -> "str":
        return "mini.svg"

    @property
    def title(self) -> "str":
        return "Mini"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mini</title>
     <path d="M0 9.1723h7.5563c.48-.749 1.1108-1.3428
 1.8935-1.7828.7822-.4393 1.6314-.659 2.5484-.659.9163 0 1.7673.2203
 2.5526.6615.7852.4412 1.4154 1.035 1.8892
 1.7803H24l-.7483.7483h-6.3994a4.278 4.278 0 0 1
 .299.8886h5.2333l-.7483.749h-4.3692c.0129.1932.019.3396.019.4393 0
 .0997-.0061.2468-.019.44h3.4904l-.7489.7483h-2.8572a4.0661 4.0661 0 0
 1-.299.8844h2.264l-.7582.7483H16.44c-.4738.7464-1.104 1.3421-1.8892
 1.7858-.7853.4437-1.6363.6652-2.5526.6652-.917
 0-1.7662-.2209-2.5484-.6627-.7827-.4425-1.4135-1.0388-1.8935-1.7883H5.6418l-.744-.7483h2.2597a4.093
 4.093 0 0
 1-.296-.8844H4.0062l-.7582-.7483h3.4898c-.0129-.1932-.019-.3403-.019-.44
 0-.0997.0061-.2461.019-.4393h-4.36l-.7581-.749h5.2418a4.306 4.306 0 0
 1 .296-.8886H.7483zm7.8437 1.0714c-.2382.5581-.3575 1.1428-.3575
 1.7538 0 .6111.1193 1.1963.3575 1.7545.2381.5575.5594 1.0394.963
 1.4443.4038.405.8838.7268 1.44.9662.5564.2393 1.1404.3587
 1.7515.3587.6104 0 1.195-.1194 1.7532-.3587.5575-.2394 1.0388-.5613
 1.4424-.9662.4037-.405.725-.8868.9656-1.4443.24-.5582.36-1.1434.36-1.7545
 0-.611-.12-1.1957-.36-1.7538-.2406-.5582-.5619-1.0388-.9656-1.4425-.4036-.403-.8849-.7243-1.4424-.9637-.5582-.2393-1.1428-.3587-1.7532-.3587-.6111
 0-1.1951.1194-1.7514.3587-.5563.2394-1.0363.5607-1.44.9637-.4037.4037-.725.8843-.9631
 1.4425zm.5538 2.9421h.4677l-.0135-1.7729.5661
 1.773.52-.0032.5557-1.7606v1.7637h.4991v-2.3766l-.7028-.0006-.603
 1.8954-.6148-1.893-.6745-.0018zm3.133 0h.4953v-2.3766h-.4953zm1.0332
 0h.477v-1.712l.9488
 1.712h.5754v-2.3766h-.4677v1.7219l-.9489-1.7219h-.5846zm2.5483
 0h.4862v-2.3766h-.4862z" />
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
