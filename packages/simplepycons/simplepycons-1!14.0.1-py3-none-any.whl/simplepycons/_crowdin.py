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


class CrowdinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "crowdin"

    @property
    def original_file_name(self) -> "str":
        return "crowdin.svg"

    @property
    def title(self) -> "str":
        return "Crowdin"

    @property
    def primary_color(self) -> "str":
        return "#2E3340"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Crowdin</title>
     <path d="M16.119 17.793a2.619 2.619 0 0
 1-1.667-.562c-.546-.436-1.004-1.09-1.018-1.858-.008-.388.414-.388.414-.388l1.018-.008c.332.008.43.47.445.586.128
 1.04.717 1.495 1.168 1.702.273.123.204.513-.362.528zm-5.695-5.287L8.5
 12.252c-.867-.214-.844-.982-.807-1.247a5.119 5.119 0 0 1
 .814-2.125c.545-.804 1.303-1.508 2.29-2.073 1.856-1.074 4.45-1.673
 7.31-1.673 2.09 0 4.256.27 4.29.27.197.025.328.213.333.437a.377.377 0
 0 1-.355.393l-.92-.01c-2.902 0-4.968.394-6.506 1.248-1.527.837-2.57
 2.117-3.287 4.012-.076.163-.335 1.12-1.24 1.022zm2.533 7.823c-1.44
 0-2.797-.622-3.825-1.746-.87-.96-1.397-1.931-1.493-3.164-.06-.813.3-1.094.788-1.044l1.988.218c.45.092.75.34.825.854.397
 2.736 2.122 3.814 3.15 4.046.18.042.292.157.283.365a.412.412 0 0
 1-.322.398c-.458.074-.936.073-1.394.073zm-4.101 2.418a14.216 14.216 0
 0 1-2.307-.214c-1.202-.214-2.208-.582-3.072-1.13C1.41 20.095.163
 17.786.014 15.048c-.037-.65-.11-1.89 1.427-1.797.638.033 1.653.343
 2.368.548.887.247 1.314.933 1.314 1.608 0 3.858 3.494 6.408 5.02
 6.408.654 0 .414.701.127.779-.502.136-1.15.153-1.413.153zM3.525
 11.419c-.605-.109-1.194-.358-1.768-.5C-.018 10.479.284 8.688.45
 8.196c1.617-4.757 6.746-6.35 10.887-6.773 3.898-.4 7.978-.092
 11.778.967.31.083
 1.269.327.718.891-.35.358-1.7-.016-2.073-.041-2.23-.167-4.434-.192-6.656.15-2.349.357-4.768
 1.099-6.71 2.665-.938.758-1.76 1.723-2.313
 2.866-.144.3-.256.6-.354.9-.11.327-.47 1.91-2.215
 1.6zm9.94.917c.332-1.488 1.81-3.848 6.385-3.686
 1.05.033.57.749.052.731-2.586-.09-3.815 1.578-4.457
 3.27-.219.546-.68.626-1.271.53-.415-.074-.866-.123-.71-.846Z" />
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
