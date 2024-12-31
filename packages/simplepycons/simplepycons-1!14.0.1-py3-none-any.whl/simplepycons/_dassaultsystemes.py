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


class DassaultSystemesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dassaultsystemes"

    @property
    def original_file_name(self) -> "str":
        return "dassaultsystemes.svg"

    @property
    def title(self) -> "str":
        return "Dassault Systèmes"

    @property
    def primary_color(self) -> "str":
        return "#005386"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dassault Systèmes</title>
     <path d="M21.1854 8.0254c1.064.192 1.9321.34
 2.1311.79.223.51-.936.541-1.52.552-2.7992.054-4.4862.11-4.5712
 1.061-.11 1.2241 1.196 2.4572 2.486 4.1852 1.1781 1.577 2.5172 3.1351
 2.1322 4.5862-.482 1.809-2.6991 2.192-4.8102
 2.192-2.0211.001-3.9382-.323-4.7432-.482-1.002-.199-.852-.694-.585-.853.298-.178
 2.002-.182 3.187-.252.9751-.058 3.8052-.056
 4.2463-.781.54-.889-.783-2.4081-2.0001-4.0002-1.519-1.984-3.1862-4.0341-2.3031-5.5322
 1.14-1.936 4.4842-1.803 6.3502-1.466m-13.6905 2.95c1.772-.104
 3.9261.206 5.1342 1.1301a2.172 2.172 0 01.78 2.2771c-.698
 2.7521-3.3041 6.0833-9.0933 8.6434-1.8411.813-3.2892
 1.125-3.5932.906-.326-.234.624-2.052.909-2.6541.9251-1.952
 2.0791-3.8532 3.2052-5.5952.414-.64 1.055-1.7521
 1.634-1.6621.519.08-.089 1.26-.488 2.011-.672 1.2601-2.523
 4.7603-1.912 4.9693 1.35.462 7.6803-4.3542
 6.7462-7.0363-.432-1.245-3.1801-1.363-4.9122-1.363-.787
 0-2.508.186-2.603-.417-.102-.5561 2.613-1.1161
 4.192-1.2101M11.8672.013c2.068-.098 4.5141.342 4.9702 1.8021.747
 2.3901-3.0402 5.8772-6.3383
 7.5873-.809.42-1.3.536-1.504.507-.195-.027-.225-.221-.162-.355.118-.252.65-.764
 1.361-1.322 3.7151-2.9001 4.9232-5.0282
 4.2212-5.8903-.45-.552-2.3321-.937-4.2872-.937-.53
 0-1.925.123-2.068-.367C7.942.634 9.814.108 11.866.012" />
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
