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


class AgoraIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "agora"

    @property
    def original_file_name(self) -> "str":
        return "agora.svg"

    @property
    def title(self) -> "str":
        return "Agora"

    @property
    def primary_color(self) -> "str":
        return "#099DFD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Agora</title>
     <path d="M13.4393 11.6804a1.351 1.351 0 1 1 1.3496-1.351 1.3523
 1.3523 0 0 1-1.3496 1.351m0-3.8006a2.4496 2.4496 0 1 0 2.4495 2.4496
 2.4537 2.4537 0 0
 0-2.4495-2.4496m4.0693.631-.0301.0301-.033.0315-.022-.0397-.0191-.033a1.17
 1.17 0 0 0-.8695-.6034l-.092-.0178v4.9019l.092-.0123a1.1383 1.1383 0
 0 0 1.008-1.1536v-1.285a1.362 1.362 0 0 1
 1.211-1.3428l.0728-.0082V7.8812l-.0878.0096a2.086 2.086 0 0
 0-1.2344.6227M2.4477 11.6817a1.351 1.351 0 1 1 1.351-1.3509 1.3523
 1.3523 0 0 1-1.351
 1.351m1.5731-3.3192-.0206.0274-.0205.0275-.0275-.0206-.026-.0206a2.4496
 2.4496 0 1 0-1.4785 4.404 2.4235 2.4235 0 0 0
 1.4785-.4978l.026-.0192.0275-.022.0204.0289.0206.0274a1.1685 1.1685 0
 0 0 .786.4718l.0905.0124v-4.902l-.0905.0124a1.17 1.17 0 0
 0-.786.4704m17.5298 3.3191a1.351 1.351 0 1 1 1.3523-1.3509 1.3523
 1.3523 0 0 1-1.351 1.351m2.3577-3.7896a1.1754 1.1754 0 0
 0-.7872.4704l-.0192.026-.0206.029-.0274-.0207-.026-.0206a2.4496
 2.4496 0 1 0-1.4786 4.4014 2.4235 2.4235 0 0 0
 1.4785-.498l.026-.0191.0275-.022.0206.0289.0192.0274a1.174 1.174 0 0
 0 .7872.4718L24 12.779V7.8798ZM7.9778 8.9785a1.351 1.351 0 1 1-1.3524
 1.351 1.3523 1.3523 0 0 1 1.355-1.351M9.5099 12.24a2.444 2.444 0 0 0
 .5006-3.2835 1.9775 1.9775 0 0 0-.1125-.1523 1.1877 1.1877 0 0 0
 .524-.8325l.0137-.0919H7.9683A2.4482 2.4482 0 0 0 6.4444 12.24a2.4427
 2.4427 0 0 0-.2935.2743l.7461.823a1.351 1.351 0 1 1 1.7831
 1.9613l.7475.8229a2.4469 2.4469 0 0 0 .07-3.876" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/AgoraIO/Docs-Source/blob/8
49872dd0496bada0a2dceecb3f79663e3b2d323/assets/images/others/agora-log'''

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
