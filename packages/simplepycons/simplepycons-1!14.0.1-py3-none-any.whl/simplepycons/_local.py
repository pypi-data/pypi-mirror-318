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


class LocalIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "local"

    @property
    def original_file_name(self) -> "str":
        return "local.svg"

    @property
    def title(self) -> "str":
        return "Local"

    @property
    def primary_color(self) -> "str":
        return "#51BB7B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Local</title>
     <path d="m4.49 11.97 6.682-6.681a.638.638 0 0 0
 .204-.476V.838a.7.7 0 0 0-.42-.624.68.68 0 0 0-.736.148L1.4
 9.193c-.94.94-1.388 1.85-1.4 2.805s.434 1.85 1.36 2.774l8.858
 8.86a.638.638 0 0 0 .476.203.39.39 0 0 0 .26-.082.68.68 0 0 0
 .42-.626v-4a.692.692 0 0 0-.204-.476L4.489 11.97h.002zm-2.64
 1.32c-.34-.45-.502-.872-.502-1.28.012-.57.34-1.182
 1.007-1.85l7.66-7.662v2.057l-7.06 7.06A4.355 4.355 0 0 0 1.85
 13.29zm8.166 8.205-6.451-6.45a.748.748 0 0
 0-.094-.12c-.204-.207-.816-.819.094-1.961l6.45
 6.449v2.082zM13.782.376a.668.668 0 0 0-.734-.15.68.68 0 0
 0-.422.626v4.015c.004.18.076.35.204.476l6.681 6.68-6.681
 6.682a.638.638 0 0 0-.204.476v3.96a.682.682 0 0 0
 1.156.49l8.817-8.817c.94-.94 1.389-1.85
 1.4-2.804.017-.952-.433-1.85-1.36-2.775L13.782.376zm.204
 4.205V2.5l6.451 6.448c.026.044.06.084.094.122.204.204.816.817-.094
 1.96l-6.449-6.45-.002.002zm7.647 9.267-7.66
 7.661v-2.04l7.06-7.077a4.451 4.451 0 0 0
 1.104-1.674c.34.45.504.872.504 1.28-.014.57-.34 1.17-1.008
 1.85zm-4.626-1.294H6.9a.516.516 0 0
 1-.516-.516v-.054c0-.286.23-.518.516-.518h10.11a.52.52 0 0 1
 .518.518v.054a.526.526 0 0
 1-.518.516h-.004zm-1.44-2.544v.056a.516.516 0 0
 1-.52.516H8.842a.516.516 0 0
 1-.518-.516v-.056c0-.285.232-.517.518-.517h6.205c.286 0
 .516.232.516.517h.002zm-1.92-1.987v.054a.516.516 0 0
 1-.517.518h-2.464a.516.516 0 0
 1-.516-.518v-.054c0-.286.232-.516.516-.516h2.464a.508.508 0 0 1
 .516.516zm-.517 7.443c.284 0 .516.232.516.518v.054a.516.516 0 0
 1-.516.516h-2.464a.516.516 0 0
 1-.516-.516v-.054c0-.286.232-.518.516-.518h2.464zm1.918-.912H8.843a.516.516
 0 0 1-.518-.516v-.054a.52.52 0 0 1 .518-.518h6.205c.286 0
 .516.232.516.518v.054a.516.516 0 0 1-.516.516z" />
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
