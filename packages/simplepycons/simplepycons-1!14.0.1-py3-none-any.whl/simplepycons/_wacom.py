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


class WacomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wacom"

    @property
    def original_file_name(self) -> "str":
        return "wacom.svg"

    @property
    def title(self) -> "str":
        return "Wacom"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wacom</title>
     <path d="M7.2432 9.8765c-.4754
 0-.7006.05-.9445.1439l-.0438.0187.269.4754.0312-.0125c.1814-.0751.3816-.1001.7569-.1001h.4003c.588
 0 .9194.294.9194.8069v1.5762c0
 .5129-.3377.8069-.9194.8069h-.6568c-.6005 0-.8944-.244-.8944-.7443
 0-.4942.294-.7381.8944-.7381h.9132v-.5254h-.9382c-.8882
 0-1.4011.4628-1.4011 1.2697 0 .7819.538 1.2635 1.401
 1.2635h.7069c.982 0 1.4324-.6567
 1.4324-1.2635V11.14c0-.6067-.4504-1.2635-1.4324-1.2635zM9.7764
 11.14c0-.6067.4503-1.2635 1.4324-1.2635h.6129c.5004.0063.8257.075
 1.0884.2502l.0375.0188-.3065.444-.0312-.0187c-.2002-.119-.4441-.169-.857-.169H11.24c-.5942
 0-.9194.2877-.9194.807v1.5762c0 .5192.3252.8069.9194.8069h.5129c.4129
 0
 .663-.05.857-.169l.0312-.0187.3065.4441-.0375.025c-.269.169-.5942.244-1.0946.244h-.6067c-.9821
 0-1.4324-.6567-1.4324-1.2635zm6.5426 1.6513c0
 .5129-.3378.8069-.9195.8069h-.6505c-.5942
 0-.9194-.2878-.9194-.807V11.215c0-.513.3377-.8068.9194-.8068h.6505c.588
 0 .9195.2939.9195.8068zm-.9007-2.9085h-.6943c-.9883
 0-1.4386.6567-1.4386 1.2634V12.86c0 .6067.4503 1.2635 1.4323
 1.2635h.7006c.982 0 1.4324-.6568
 1.4324-1.2635v-1.714c.0062-.6067-.4441-1.2634-1.4324-1.2634zm3.4652.0125c.5692
 0 .907.1375 1.1697.4752.2627-.3377.6067-.4753 1.1696-.4753.8444 0
 1.3949.4816 1.3949
 1.226v2.9898h-.5317V11.19c0-.5191-.294-.7693-.8882-.7693-.5629
 0-.8757.2564-.8757.7193v2.971h-.5379V11.14c0-.463-.3127-.7193-.8757-.7193-.6004
 0-.8882.2502-.8882.7693v2.921h-.5379v-2.9899c.0063-.7443.5504-1.2259
 1.4011-1.2259zm4.6912.2563c.0438 0
 .075.0063.0938.0188.025.0125.0313.0375.025.0625 0
 .0313-.0125.0563-.0438.0688-.0187.0125-.0438.0125-.075.0125h-.0688v-.1626zm.1376-.0313c-.0313-.0125-.0688-.0187-.1251-.0187l-.1564-.0063v.4504h.0813v-.1752h.0626c.0438
 0 .0688 0
 .0875.0125.0313.0126.0438.0501.0438.1001v.0626h.0751v-.0063c-.0063-.0062-.0063-.0125-.0063-.025v-.0626c0-.025-.0062-.0437-.025-.0688-.0125-.025-.0375-.0375-.0751-.0437.0251
 0 .0501-.0063.0626-.0188.0313-.0188.0438-.05.0438-.0876
 0-.0563-.025-.0938-.0688-.1126zm-.4691.2065c0-.1.0312-.1814.1-.2502.0688-.0688.1564-.1.2502-.1064.1001
 0 .1814.0376.2502.1064.0688.0688.1001.1501.1001.2502 0
 .1-.0313.1813-.1001.2501-.0688.069-.1501.1064-.2502.1064-.1
 0-.1814-.0375-.2502-.1064-.0688-.0688-.1-.15-.1-.25zm.3502.4065c.1126
 0 .2064-.0375.2878-.1188.0813-.075.1188-.1752.1188-.294
 0-.1126-.0375-.2064-.1188-.2877-.0751-.0813-.1752-.1189-.2878-.1189s-.2064.0376-.2877.119c-.0813.0812-.1188.175-.1188.2876
 0 .1188.0375.2127.1188.294.0751.0813.1751.1188.2877.1188zm-18.996
 2.0954v-2.921l.5379-.0063v2.99c-.0063.7442-.5505 1.2258-1.4011
 1.2258-.5692
 0-.907-.1376-1.1697-.4754-.2627.3378-.6005.4754-1.1697.4754C.5504
 14.1172 0 13.6356 0 12.8913V9.9014l.5317.0063v2.921c0
 .5192.294.7694.8882.7694.5629 0
 .8756-.2565.8756-.7194v-2.971h.538v2.971c0
 .463.3127.7194.8756.7194.6005 0 .8882-.2502.8882-.7694z" />
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
