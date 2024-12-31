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


class AmazonLunaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "amazonluna"

    @property
    def original_file_name(self) -> "str":
        return "amazonluna.svg"

    @property
    def title(self) -> "str":
        return "Amazon Luna"

    @property
    def primary_color(self) -> "str":
        return "#9146FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Amazon Luna</title>
     <path d="M21.757 15.4031a4.5796 4.5796 0 0
 0-.8157-.3675h-.0038c-.0431-.015-.0863-.0244-.1294-.0375-.5081-.1556-2.4-.8494-3.4782-2.8126v.002l-1.9256-3.334c-.81-1.4212-.6732-3.6844-.585-4.5413a4.519
 4.519 0 0 0 .0393-.3244.2659.2659 0 0 0
 .0038-.0206h-.0019c.0056-.077.0113-.152.0113-.2307-.002-1.9388-1.5732-3.512-3.512-3.512s-3.512
 1.5732-3.512 3.512c0
 .0769.0075.1538.0113.2307h-.0038s.0019.0168.0056.045c.0075.09.0188.1762.032.2643.09.8363.2455
 3.1876-.6057 4.624h.0018l-2.7582
 4.7757v-.0037l-.0318.0581-.2588.45c-.0206.0375-.0356.0769-.0562.1144-.285.4931-.72
 1.2057-1.1982 1.8507-.3994.54-1.0238 1.0725-1.637
 1.4325l.0076.002c-.0563.028-.1144.0524-.1688.0862a2.3952 2.3952 0 0
 0-.8625.8737c-.6694 1.1588-.2719 2.642.8869 3.3114.6056.3506
 1.2975.4012 1.9182.2119l-.0038.0056c1.0688-.3732 2.237-.7014
 2.8351-.8382 1.0032-.2288 2.4882-.285 3.332-.2963h.96c4.2845.0412
 6.4558 1.8582 6.4558 1.8582l.0038-.0038c.1744.1387.3544.27.5531.3844
 2.1451 1.2394 4.8902.5043 6.1277-1.6426
 1.245-2.145.51-4.8901-1.637-6.1277zm-5.0308 2.267c-.4482.7743-1.0857
 1.1568-2.1432 1.2375-1.0575.0806-1.2863.1425-3.2232.1425-1.937
 0-2.2295-.06-3.2232-.1425-.992-.0825-1.695-.4632-2.1432-1.2376-.4482-.7744-.4107-1.6594
 0-2.475.4106-.8157.6731-1.4457 1.4363-2.7676.7631-1.322 1.0669-1.8226
 1.785-2.8145.72-.9919 1.2488-1.2375 2.1432-1.2375.8944 0 1.4644.3319
 2.1432 1.2375.6788.9057.8719 1.2563 1.7138 2.7151s1.0556 1.952 1.5075
 2.867c.4557.915.45 1.7006.0038 2.475z" />
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
