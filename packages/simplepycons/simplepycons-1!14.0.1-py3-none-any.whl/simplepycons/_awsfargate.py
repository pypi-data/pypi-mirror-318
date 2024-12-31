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


class AwsFargateIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "awsfargate"

    @property
    def original_file_name(self) -> "str":
        return "awsfargate.svg"

    @property
    def title(self) -> "str":
        return "AWS Fargate"

    @property
    def primary_color(self) -> "str":
        return "#FF9900"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AWS Fargate</title>
     <path d="M17.647 19.54v-2.28l1.412-.565v2.28Zm-2.353-2.845
 1.412.565v2.28l-1.412-.564Zm-2.823
 6.14v-2.281l1.411-.565v2.28Zm-2.353-2.846
 1.411.565v2.28l-1.411-.564Zm-2.824-.449v-2.28l1.412-.565v2.28Zm-2.353-2.845
 1.412.565v2.28l-1.412-.564Zm1.883-1.13L7.91 16l-1.086.434L5.737
 16ZM12 18.86l1.086.434-1.086.434-1.086-.434Zm5.176-3.294
 1.087.434-1.087.434L16.09 16Zm2.528-.003-2.353-.941a.476.476 0 0
 0-.35 0l-2.352.94a.471.471 0 0 0-.296.438v2.787l-2.178-.871a.476.476
 0 0 0-.35 0l-2.178.871V16a.471.471 0 0
 0-.296-.437l-2.353-.941a.476.476 0 0 0-.35 0l-2.352.94A.471.471 0 0 0
 4 16v3.294a.47.47 0 0 0 .296.437l2.353.941a.476.476 0 0 0 .35
 0l2.177-.871v2.787c0 .193.118.365.296.437l2.353.942a.476.476 0 0 0
 .35 0l2.353-.942a.471.471 0 0 0 .296-.437v-2.787l2.178.871a.476.476 0
 0 0 .35 0l2.352-.94a.471.471 0 0 0 .296-.438V16a.471.471 0 0
 0-.296-.437Zm4.06-5.71c0 2.75-6.06 4.235-11.764 4.235-5.703
 0-11.765-1.484-11.765-4.235 0-1.313 1.457-2.47
 4.101-3.256l.269.902C2.49 8.128 1.176 9.03 1.176 9.853c0 1.558 4.445
 3.294 10.824 3.294s10.824-1.736
 10.824-3.294c0-.823-1.314-1.725-3.429-2.354l.269-.902c2.644.787 4.1
 1.943 4.1 3.256ZM12 .975l4.807 1.849L12 4.672 7.193 2.824Zm4.979
 9.304c-.888.397-2.378.86-4.508.921V5.5l5.176-1.99v5.736c0
 .448-.262.853-.668 1.033ZM6.353 9.246V3.51l5.176
 1.99v5.7c-2.13-.062-3.62-.524-4.51-.922a1.126 1.126 0 0
 1-.666-1.032Zm.284 1.891c1.036.464 2.807 1.017 5.363 1.017 2.556 0
 4.327-.553 5.361-1.016a2.068 2.068 0 0 0
 1.227-1.892V2.824c0-.195-.12-.37-.301-.44L12.169.031a.475.475 0 0
 0-.338 0L5.713 2.384a.471.471 0 0 0-.301.44v6.422c0 .82.481 1.562
 1.225 1.891Z" />
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
