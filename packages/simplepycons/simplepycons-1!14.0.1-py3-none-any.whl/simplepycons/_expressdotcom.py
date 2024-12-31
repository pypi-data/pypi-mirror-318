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


class ExpressdotcomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "expressdotcom"

    @property
    def original_file_name(self) -> "str":
        return "expressdotcom.svg"

    @property
    def title(self) -> "str":
        return "Express.com"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Express.com</title>
     <path d="M18.904 10.081c-.774 0-1.484.362-1.484 1.24 0
 .536.367.893 1.041 1l.756.123c.27.046.408.139.408.323 0
 .316-.44.417-.68.417-.433 0-.734-.169-1.05-.455l-.693.45c.494.54
 1.02.74 1.636.74.678 0 1.664-.203 1.664-1.295
 0-.694-.597-.92-1.32-1.037l-.348-.057c-.346-.056-.506-.152-.506-.345
 0-.235.307-.367.516-.367.382 0
 .735.168.974.458l.688-.496c-.409-.454-1-.699-1.602-.699Zm3.494
 0c-.775 0-1.484.362-1.484 1.24 0 .536.367.893 1.04
 1l.755.123c.27.046.408.139.408.323 0 .316-.437.417-.678.417-.433
 0-.735-.169-1.05-.455l-.694.45c.494.54 1.02.74 1.637.74.677 0
 1.662-.203 1.662-1.295
 0-.694-.596-.92-1.32-1.037l-.346-.057c-.348-.056-.506-.152-.506-.345
 0-.235.307-.367.516-.367.382 0
 .733.168.972.458l.69-.496c-.408-.454-1.001-.699-1.602-.699ZM0
 10.185v3.632h2.824v-.705H.91v-.857h1.646v-.703H.909v-.664h1.765v-.703zm3.285
 0 1.2 1.677-1.399 1.955h1.098l.86-1.357.837 1.357h1.11L5.6
 11.862l1.194-1.677H5.707l-.658 1.107-.662-1.107Zm3.988
 0v3.632h.918v-1.174H8.9c1.244 0 1.513-.745 1.513-1.23
 0-.72-.36-1.228-1.34-1.228zm3.386 0v3.632h.908v-1.306h.577l.712
 1.306h1.016l-.832-1.459c.454-.132.75-.51.75-.98
 0-.816-.499-1.193-1.314-1.193zm3.492
 0v3.632h2.824v-.705h-1.918v-.857h1.648v-.703h-1.648v-.664h1.766v-.703zm-5.972.672h.74c.415
 0 .586.2.586.562 0 .28-.147.55-.56.55h-.766Zm3.388
 0h.83c.291.005.485.153.485.49 0 .336-.194.484-.485.49h-.83z" />
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
