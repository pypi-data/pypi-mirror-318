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


class MikrotikIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mikrotik"

    @property
    def original_file_name(self) -> "str":
        return "mikrotik.svg"

    @property
    def title(self) -> "str":
        return "Mikrotik"

    @property
    def primary_color(self) -> "str":
        return "#293239"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mikrotik</title>
     <path d="M23.041 6.188a1.404 1.404 0 0
 0-.218-.36c-.24-.296-.634-.586-1.14-.864l-4.052-2.22L13.576.519C13.074.243
 12.61.065 12.22.013A1.772 1.772 0 0 0 12 0c-.432
 0-.974.192-1.576.52L6.37 2.74 2.317
 4.96c-.504.279-.9.569-1.14.867a1.59 1.59 0 0 0-.122.17 1.654 1.654 0
 0 0-.096.19c-.15.348-.22.816-.22 1.368v8.887c0 .66.1 1.2.316
 1.558.216.356.66.706 1.262 1.036l4.054 2.22 4.053
 2.223c.504.276.966.456 1.36.506.145.02.291.02.436 0 .39-.05.852-.228
 1.356-.506l8.107-4.443c.6-.33 1.046-.68
 1.262-1.036.036-.06.068-.123.096-.188.15-.348.22-.818.22-1.37V7.556c0-.552-.07-1.02-.22-1.368zM7.233
 16.618c0 .2-.218.33-.396.233l-1.45-.796a1.066 1.066 0 0
 1-.552-.934v-4.296c0-.2.216-.33.394-.235l1.728.947a.53.53 0 0 1
 .276.468v4.612zm11.934-1.497c0
 .39-.213.748-.554.936l-1.45.794a.266.266 0 0
 1-.394-.234v-5.692c0-.2-.217-.33-.395-.232l-2.62
 1.434c-.34.187-.552.545-.552.934v5.646a.532.532 0 0
 1-.278.468l-.41.224c-.32.176-.707.176-1.026 0l-.408-.224a.532.532 0 0
 1-.278-.468v-5.646c0-.389-.212-.747-.552-.934L4.835
 9.16v-.28c0-.388.212-.746.552-.934l.6-.328a1.064 1.064 0 0 1 1.022
 0l4.48 2.452c.318.176.704.176 1.021 0l2.07-1.134a.266.266 0 0 0
 0-.468L9.932 5.922a.266.266 0 0 1 0-.468l1.556-.852c.32-.176.707-.176
 1.026 0l6.1 3.34c.342.188.554.547.553.936v6.243z" />
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
