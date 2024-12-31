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


class KumaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kuma"

    @property
    def original_file_name(self) -> "str":
        return "kuma.svg"

    @property
    def title(self) -> "str":
        return "Kuma"

    @property
    def primary_color(self) -> "str":
        return "#290B53"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kuma</title>
     <path d="M19.02 0c-1.118 0-1.935.362-2.474.946A.189.189 0 0 1
 16.35 1a16.824 16.824 0 0 0-2.634-.623.184.184 0 0 0-.205.158.181.181
 0 0 0 .003.07c.186.699 1.305 5.133 2.205 8.51.544 2.043-.866
 4.05-2.98 4.044h-1.31c-2.136 0-3.433-2.014-2.94-4.022.83-3.393
 1.968-7.792 2.152-8.517a.183.183 0 0 0-.13-.226.177.177 0 0
 0-.07-.005 14.358 14.358 0 0 0-3.048.698.188.188 0 0
 1-.208-.056C6.646.398 5.806.003 4.643.003c-2.254 0-3.287 1.473-3.287
 3.29 0 .952.905 2.24 1.766 3.253a.188.188 0 0 1 .034.18l-1.468
 4.259a.034.034 0 0 0 0 .011c-.038.148-.604 2.662 3.699 6.661 1.286
 1.2 5.77 5.52 6.576 6.293a.182.182 0 0 0 .251
 0l6.774-6.293c4.648-4.334 3.54-6.672 3.54-6.672L20.882 6.27a.183.183
 0 0 1 .028-.175c.733-.925 1.4-1.991 1.4-2.808C22.31 1.473 21.274 0
 19.02 0Zm-8.025 7.132a.525.525 0 0 0-.527.524l.217
 2.157v.003a.525.525 0 0 0 .526.524h1.755a.525.525 0 0 0
 .524-.53l.208-2.154a.525.525 0 0 0-.526-.524z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://cncf-branding.netlify.app/projects/ku'''

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
