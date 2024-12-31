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


class NoderedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nodered"

    @property
    def original_file_name(self) -> "str":
        return "nodered.svg"

    @property
    def title(self) -> "str":
        return "Node-RED"

    @property
    def primary_color(self) -> "str":
        return "#8F0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Node-RED</title>
     <path d="M3 0C1.338 0 0 1.338 0 3v6.107h2.858c1.092 0 1.97.868
 1.964 1.96v.021c.812-.095 1.312-.352 1.674-.683.416-.382.69-.91
 1.016-1.499.325-.59.71-1.244 1.408-1.723.575-.395 1.355-.644
 2.384-.686v-.45c0-1.092.88-1.976 1.972-1.976h7.893c1.091 0 1.974.884
 1.974 1.976v1.942c0 1.091-.883 2.029-1.974 2.029h-7.893c-1.092
 0-1.972-.938-1.972-2.03v-.453c-.853.037-1.408.236-1.798.504-.48.33-.774.802-1.086
 1.368-.312.565-.63 1.22-1.222 1.763l-.077.069c3.071.415 4.465 1.555
 5.651 2.593 1.39 1.215 2.476 2.275 6.3 2.288v-.46c0-1.092.894-1.946
 1.986-1.946H24V3c0-1.662-1.338-3-3-3zm10.276 5.41c-.369
 0-.687.268-.687.637v1.942c0 .368.318.636.687.636h7.892a.614.614 0 0 0
 .635-.636V6.047a.614.614 0 0 0-.635-.636zM0
 10.448v3.267h2.858a.696.696 0 0 0
 .678-.69v-1.942c0-.368-.31-.635-.678-.635zm4.821 1.67v.907A1.965
 1.965 0 0 1 2.858 15H0v6c0 1.662 1.338 3 3 3h18c1.662 0 3-1.338
 3-3v-1.393h-2.942c-1.092
 0-1.986-.913-1.986-2.005v-.445c-4.046-.032-5.598-1.333-6.983-2.544-1.437-1.257-2.751-2.431-7.268-2.496zM21.058
 15a.644.644 0 0 0-.647.66v1.942c0 .368.278.612.647.612H24V15z" />
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
