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


class DashlaneIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dashlane"

    @property
    def original_file_name(self) -> "str":
        return "dashlane.svg"

    @property
    def title(self) -> "str":
        return "Dashlane"

    @property
    def primary_color(self) -> "str":
        return "#0E353D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dashlane</title>
     <path d="M20.89
 7.7189c0-.1488-.1488-.2976-.3575-.3571l-2.502-.9221c-.4166-.1786-.8932.0297-.8932.3277V17.25c0
 .1487.1488.3273.2977.3868l2.5614.9222c.3872.1487.8936-.0596.8936-.3873zm-4.676-3.663c0-.1492-.1489-.298-.3576-.3575l-2.5015-.9221c-.417-.1786-.8936.0297-.8936.3278v6.3723c0
 .1488.1487.3273.2976.3873l2.5614.9221c.3873.1492.8937-.0595.8937-.3869zm0
 11.4663c0-.1488-.1489-.2975-.3576-.3571l-2.5015-.9221c-.417-.1786-.8936.0297-.8936.3277v6.3724c0
 .1488.1487.3273.2976.3869l2.5614.922c.3873.1493.8937-.0594.8937-.3872zm-4.6761
 1.281c0-.1489-.1488-.298-.3575-.3576l-2.5015-.9221c-.4192-.1786-.8937.0297-.8937.3277v6.7903c0
 .1487.1488.3277.2977.3872l2.5614.9222c.3872.1493.8936-.0595.8936-.387zm0-15.4579c0-.1488-.1488-.2976-.3575-.3571L8.6789.066c-.4192-.1786-.8937.0297-.8937.3277v6.7903c0
 .1492.1488.3277.2977.3873l2.5614.922c.3872.1488.8936-.0594.8936-.3872zm-4.6752.2683c0-.1488-.1488-.298-.3575-.3576L4.0037.334C3.5867.1553
 3.11.3636 3.11.6617v21.7409c0
 .1487.1488.3273.298.3868l2.561.9222c.3874.1488.8937-.0595.8937-.3874z"
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
        return '''https://brandfolder.com/dashlane/brandkitpart'''

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
