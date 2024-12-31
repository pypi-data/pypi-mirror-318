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


class DatagripIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "datagrip"

    @property
    def original_file_name(self) -> "str":
        return "datagrip.svg"

    @property
    def title(self) -> "str":
        return "DataGrip"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DataGrip</title>
     <path d="M0 0v24h24V0Zm17.1797 2.9477a5.452 5.452 0 0 1 3.9047
 1.364L19.7078 5.972a3.672 3.672 0 0 0-2.596-1.0086c-1.6 0-2.8555
 1.408-2.8555 3.096v.0282c0 1.816 1.2517 3.1523 3.0117 3.1523a3.492
 3.492 0 0 0 2.064-.5921V9.2234h-2.2V7.336h4.3157v4.3157a6.436 6.436 0
 0 1-4.2438 1.5757c-3.096 0-5.2242-2.1797-5.2242-5.1117v-.0281a5.1 5.1
 0 0 1 5.2-5.1398zm-14.7438.1718h3.8758c3.12 0 5.2805 2.1439 5.2805
 4.9399v.028c0 2.8-2.1605 4.968-5.2805 4.968H2.436Zm4.075 1.9688a2.852
 2.852 0 0 0-.1992.003H4.6203v6h1.6914A2.832 2.832 0 0 0 9.304
 8.1235v-.036a2.852 2.852 0 0 0-2.793-2.9991Zm-4.303 14.407h9v1.5h-9z"
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
        return '''https://www.jetbrains.com/company/brand/logos'''

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
