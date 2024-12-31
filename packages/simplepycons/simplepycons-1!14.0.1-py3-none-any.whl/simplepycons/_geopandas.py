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


class GeopandasIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "geopandas"

    @property
    def original_file_name(self) -> "str":
        return "geopandas.svg"

    @property
    def title(self) -> "str":
        return "GeoPandas"

    @property
    def primary_color(self) -> "str":
        return "#139C5A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GeoPandas</title>
     <path d="M12.0043 0C5.3911 0 0 5.3805 0 12c0 6.6108 5.3825 12
 12.0043 12C18.6263 24 24 18.6108 24
 12c0-6.6195-5.3824-12-11.9957-12Zm9.8288 12a9.7343 9.7343 0 0 1-.8234
 3.925v-7.85c.5288 1.1958.8235 2.53.8235 3.925zm-4.0996
 7.9798v-1.8715h-2.0889v3.0152a9.7946 9.7946 0 0 1-3.6403.7018c-.3033
 0-.6067-.0173-.91-.0433V9.1928H9.0054v12.1646c-3.961-1.2736-6.8385-4.9906-6.8385-9.366
 0-5.4239 4.4117-9.834 9.8374-9.834 2.6956 0 5.1485 1.0917 6.9253
 2.8592v13.8888h.0607c-.39.3986-.8148.7538-1.2568 1.0744zM15.6446
 9.2014h2.0889v4.3322h-2.0889zm-3.2849
 5.3372h2.0888v4.3322h-2.0888Zm0-8.9068h2.0888v4.3321h-2.0888Zm3.285
 9.1668h2.0888v2.0447h-2.0889Zm-3.285-3.5697h2.0888v2.0448h-2.0888Z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://geopandas.org/en/stable/about/logo.ht'''
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
