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


class FireshipIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fireship"

    @property
    def original_file_name(self) -> "str":
        return "fireship.svg"

    @property
    def title(self) -> "str":
        return "Fireship"

    @property
    def primary_color(self) -> "str":
        return "#EB844E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fireship</title>
     <path
 d="M9.245.05c-.042-.035-.14-.035-.22-.05-.041.06-.098.113-.113.166a3.114
 3.114 0 0 0-.064.416 15.42 15.42 0 0 1-3.742 8.693c-1.258 1.474-2.51
 2.982-3.44 4.585-2.293 3.972-.249 8.031 4.763
 9.804.163.06.348.087.76.181-1.701-1.534-2.57-3.1-2.28-4.944.284-1.765
 1.172-3.337 2.525-4.77a1.043 1.043 0 0 1 .099.549c-.068 1.572.453
 2.96 2.063 4.055.741.507 1.41 1.081 2.079 1.644.684.57.884 1.263.688
 2.015-.09.366-.227.725-.378 1.171 1.145-.11 2.203-.264
 2.914-.9.68-.604 1.183-1.322 1.909-2.154.049.707.15 1.255.113
 1.8-.045.566-.22 1.126-.336 1.689 3.477-.525 6.546-3.934
 6.682-7.427.098-2.543-2.071-6.274-3.893-6.637l.302.688c.631 1.391.817
 2.8.416 4.256-.4 1.448-2.426 3.073-4.214 3.277.06-.144.087-.28.17-.39
 1.927-2.596 1.946-5.31.854-8.084C15.44 5.98 12.632 2.88 9.245.053Z"
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
        return '''https://github.com/fireship-io/fireship.io/bl
ob/987da97305a5968b99347aa748f928a4667336f8/hugo/layouts/partials/svg/'''

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
