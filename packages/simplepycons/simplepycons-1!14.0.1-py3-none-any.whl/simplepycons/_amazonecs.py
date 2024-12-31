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


class AmazonEcsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "amazonecs"

    @property
    def original_file_name(self) -> "str":
        return "amazonecs.svg"

    @property
    def title(self) -> "str":
        return "Amazon ECS"

    @property
    def primary_color(self) -> "str":
        return "#FF9900"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Amazon ECS</title>
     <path d="m21.895 15.256-3.369-2.021V8.421a.42.42 0 0
 0-.209-.364l-4.843-2.825V1.159l8.42
 4.976Zm.635-9.724L13.267.06a.422.422 0 0 0-.635.362v5.053c0
 .15.08.288.208.363l4.844 2.826v4.81a.42.42 0 0 0 .205.362l4.21
 2.526a.42.42 0 0 0 .638-.361V5.895a.42.42 0 0 0-.207-.363ZM11.977
 23.1l-9.872-5.248V6.135l8.421-4.976v4.084L6.09 8.066a.422.422 0 0
 0-.195.355v7.158a.42.42 0 0 0 .226.373l5.665 2.948a.42.42 0 0 0 .387
 0l5.496-2.84 3.382 2.03-9.074 5.01Zm10.135-5.356-4.21-2.526a.42.42 0
 0 0-.411-.013l-5.51 2.847-5.244-2.729v-6.67l4.436-2.824a.422.422 0 0
 0 .195-.355V.42a.421.421 0 0 0-.635-.362L1.47 5.532a.421.421 0 0
 0-.207.363v12.21c0 .156.086.299.223.372l10.297 5.474a.421.421 0 0 0
 .401-.004l9.915-5.473a.422.422 0 0 0 .013-.73Z" />
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
        yield from [
            "Amazon Elastic Container Service",
            "AWS ECS",
            "AWS Elastic Container Service",
        ]
