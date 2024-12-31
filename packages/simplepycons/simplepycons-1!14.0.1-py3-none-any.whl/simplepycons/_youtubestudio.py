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


class YoutubeStudioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "youtubestudio"

    @property
    def original_file_name(self) -> "str":
        return "youtubestudio.svg"

    @property
    def title(self) -> "str":
        return "YouTube Studio"

    @property
    def primary_color(self) -> "str":
        return "#FF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>YouTube Studio</title>
     <path d="M20.919
 13.176c.048-.384.084-.768.084-1.176s-.036-.792-.084-1.176l2.532-1.98a.605.605
 0 0 0 .144-.768l-2.4-4.152a.603.603 0 0 0-.732-.264l-2.988 1.2a8.767
 8.767 0 0 0-2.028-1.176l-.456-3.18A.585.585 0 0 0 14.403 0h-4.8c-.3
 0-.552.216-.588.504l-.456 3.18A9.22 9.22 0 0 0 6.531
 4.86l-2.988-1.2a.585.585 0 0 0-.732.264l-2.4 4.152a.592.592 0 0 0
 .144.768l2.532 1.98c-.048.384-.084.78-.084 1.176s.036.792.084
 1.176l-2.532 1.98a.605.605 0 0 0-.144.768l2.4
 4.152c.144.264.468.36.732.264l2.988-1.2c.624.48 1.296.876 2.028
 1.176l.456 3.18a.585.585 0 0 0 .588.504h4.8c.3 0
 .552-.216.588-.504l.456-3.18a9.22 9.22 0 0 0 2.028-1.176l2.988
 1.2c.276.108.588 0 .732-.264l2.4-4.152a.605.605 0 0
 0-.144-.768l-2.532-1.98zM9.603 15.6V8.4l6 3.6-6 3.6z" />
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
