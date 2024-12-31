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


class YarnIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "yarn"

    @property
    def original_file_name(self) -> "str":
        return "yarn.svg"

    @property
    def title(self) -> "str":
        return "Yarn"

    @property
    def primary_color(self) -> "str":
        return "#2C8EBB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Yarn</title>
     <path d="M12 0C5.375 0 0 5.375 0 12s5.375 12 12 12 12-5.375
 12-12S18.625 0 12 0zm.768 4.105c.183 0
 .363.053.525.157.125.083.287.185.755
 1.154.31-.088.468-.042.551-.019.204.056.366.19.463.375.477.917.542
 2.553.334 3.605-.241 1.232-.755 2.029-1.131 2.576.324.329.778.899
 1.117 1.825.278.774.31 1.478.273 2.015a5.51 5.51 0 0 0
 .602-.329c.593-.366 1.487-.917 2.553-.931.714-.009 1.269.445 1.353
 1.103a1.23 1.23 0 0 1-.945
 1.362c-.649.158-.95.278-1.821.843-1.232.797-2.539 1.242-3.012
 1.39a1.686 1.686 0 0
 1-.704.343c-.737.181-3.266.315-3.466.315h-.046c-.783
 0-1.214-.241-1.45-.491-.658.329-1.51.19-2.122-.134a1.078 1.078 0 0
 1-.58-1.153 1.243 1.243 0 0
 1-.153-.195c-.162-.25-.528-.936-.454-1.946.056-.723.556-1.367.88-1.71a5.522
 5.522 0 0 1 .408-2.256c.306-.727.885-1.348
 1.32-1.737-.32-.537-.644-1.367-.329-2.21.227-.602.412-.936.82-1.08h-.005c.199-.074.389-.153.486-.259a3.418
 3.418 0 0 1 2.298-1.103c.037-.093.079-.185.125-.283.31-.658.639-1.029
 1.024-1.168a.94.94 0 0 1 .328-.06zm.006.7c-.507.016-1.001 1.519-1.001
 1.519s-1.27-.204-2.266.871c-.199.218-.468.334-.746.44-.079.028-.176.023-.417.672-.371.991.625
 2.094.625 2.094s-1.186.839-1.626 1.881c-.486 1.144-.338 2.261-.338
 2.261s-.843.732-.899 1.487c-.051.663.139 1.2.343
 1.515.227.343.51.176.51.176s-.561.653-.037.931c.477.25 1.283.394
 1.71-.037.31-.31.371-1.001.486-1.283.028-.065.12.111.209.199.097.093.264.195.264.195s-.755.324-.445
 1.066c.102.246.468.403 1.066.398.222-.005 2.664-.139
 3.313-.296.375-.088.505-.283.505-.283s1.566-.431
 2.998-1.357c.917-.598 1.293-.76
 2.034-.936.612-.148.57-1.098-.241-1.084-.839.009-1.575.44-2.196.825-1.163.718-1.742.672-1.742.672l-.018-.032c-.079-.13.371-1.293-.134-2.678-.547-1.515-1.413-1.881-1.344-1.997.297-.5
 1.038-1.297
 1.334-2.78.176-.899.13-2.377-.269-3.151-.074-.144-.732.241-.732.241s-.616-1.371-.788-1.483a.271.271
 0 0 0-.157-.046z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://github.com/yarnpkg/assets/tree/76d30c'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/yarnpkg/assets/blob/76d30c'''

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
