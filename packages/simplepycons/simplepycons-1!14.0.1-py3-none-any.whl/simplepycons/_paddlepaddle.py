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


class PaddlepaddleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "paddlepaddle"

    @property
    def original_file_name(self) -> "str":
        return "paddlepaddle.svg"

    @property
    def title(self) -> "str":
        return "PaddlePaddle"

    @property
    def primary_color(self) -> "str":
        return "#0062B0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PaddlePaddle</title>
     <path d="M12.17185 4.8315c-.6339 0-1.15033.51448-1.15033
 1.14833s.51643 1.15033 1.15033 1.15033 1.14833-.51643
 1.14833-1.15033-.51448-1.14833-1.14833-1.14833zm9.9916 0c-.6339
 0-1.15033.51448-1.15033 1.14833s.51643 1.15033 1.15033 1.15033c.6339
 0 1.14833-.51643 1.14833-1.15033S22.7973 4.8315 22.16345
 4.8315zM6.67238 8.00711c-.0331 0-.06258.01885-.07617.04883l-1.95298
 4.29274H.75286c-.05136 0-.09805.02932-.11913.07616l-.62691
 1.39832c-.02155.04809.01363.10351.0664.10351h3.85327l-2.32796
 5.1208c-.02545.0559.01465.12108.07617.12108h1.6561c.0331 0
 .06438-.02064.07812-.05078l4.9977-10.99134c.02529-.0559-.01481-.11913-.07617-.11913zm3.4783
 0c-.02484 0-.0483.01431-.0586.0371l-.58004
 1.28513c-.01905.04216.01237.08984.05859.08984h1.02334c.21703-.00312.37745.01142.55466.03906.82499.12818
 1.33602.73302 1.32412 1.5351-.01124.75786-.64035 1.36123-1.39832
 1.36123H7.40865c-.06245 0-.11876.03691-.14452.09374l-.60935
 1.33972c-.0295.0648.0188.13671.08984.13671h4.28495c1.77679 0
 3.1942-1.5331
 2.99592-3.2986-.1616-1.43981-1.34012-2.56875-2.81033-2.61894-.01327-.00047-.02641.0011-.03906.0039a.06152.06152
 0 0 0-.02148-.0039zm6.4762 0c-.0331
 0-.06438.0187-.07812.04883l-4.9977
 10.99134c-.0253.0559.01676.12108.07812.12108h1.6561c.03294 0
 .06259-.0208.07617-.05078l4.9997-10.99134c.02545-.0559-.01661-.11913-.07813-.11913zm3.4783
 0c-.02498 0-.04633.01431-.05664.0371l-.58005
 1.28513c-.01889.04216.01058.08984.05664.08984h1.02334c.21717-.00312.37744.01142.55465.03906.825.12818
 1.33782.73302 1.32612 1.5351-.0114.75786-.64034 1.36123-1.39831
 1.36123h-3.66778c-.06246 0-.11876.03691-.14452.09374l-.60935
 1.33972c-.02934.0648.01864.13671.08984.13671h4.28494c1.7766 0
 3.1961-1.5331
 2.99782-3.2986-.16159-1.43981-1.34222-2.56875-2.81233-2.61894-.01343-.00047-.02642.0011-.03906.0039a.0611.0611
 0 0 0-.02148-.0039z" />
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
