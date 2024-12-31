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


class GoogleAppsScriptIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googleappsscript"

    @property
    def original_file_name(self) -> "str":
        return "googleappsscript.svg"

    @property
    def title(self) -> "str":
        return "Google Apps Script"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Apps Script</title>
     <path d="M12.363 2.54a3.136 3.136 0 0 0-.376.022 2.864 2.864 0 0
 0-1.589.828c-.562.58-.82 1.115-.773 1.943-.01.264.193 1.023.272 1.274
 1.115 3.546 2.09 6.75 3.26
 10.279.08.246.168.486.267.72.02.047.035.046.048-.004.077-.297.174-.612.29-.945.894-2.576
 1.772-5.14 2.633-7.696a.345.345 0 0 0 .004-.217 163.054 163.054 0 0
 0-1.49-4.572 2.603 2.603 0 0
 0-.704-.933c-.55-.46-1.166-.694-1.842-.7Zm9.078.117a2.734 2.734 0 0
 0-2.878 1.828l-4.576 13.289a2.734 2.734 0 0 0 1.695
 3.475l.12.04a2.734 2.734 0 0 0 3.475-1.694L23.85 6.307a2.734 2.734 0
 0 0-1.695-3.476c-.233-.1-.506-.124-.716-.174ZM12.375 3.96a1.396 1.396
 0 1 1 0 2.791 1.395 1.395 0 0 1 0-2.79zm8.809.07a1.402 1.402 0 1 1 0
 2.803 1.402 1.402 0 0 1 0-2.803zM5.419 7.605a2.853 2.853 0 0
 0-.468.052 2.683 2.683 0 0 0-1.337.627 2.62 2.62 0 0 0-.924 1.833
 3.808 3.808 0 0 0 0 .648 2.52 2.52 0 0 0 .673
 1.52c.221.238.465.454.732.648 3.043 2.21 6.08 4.43 9.108 6.664a.78.78
 0 0 0 .158.089c.03-.043.032-.098.007-.167a17.409 17.409 0 0
 0-.317-1.066 532.752 532.752 0 0 1-2.02-6.251 41.91 41.91 0 0
 0-.497-1.477c-.967-.849-2.078-1.6-3.023-2.302A3.848 3.848 0 0 0 6.153
 7.7a2.388 2.388 0 0 0-.734-.094Zm.02 1.424a1.398 1.398 0 1 1 0 2.796
 1.398 1.398 0 0 1 0-2.796zm-2.458
 6.792c-.733-.006-1.375.202-1.927.622a2.72 2.72 0 0 0-.95 1.45 2.78
 2.78 0 0 0-.09 1.04 2.74 2.74 0 0 0 .695 1.583c.664.578 1.26.85 2
 .945 1.42-.005 2.84-.012 4.262-.02h.418c2.277-.003 4.513-.002
 6.706.003.148.005.28.003.392-.01.06-.005.091-.031.092-.077a10.656
 10.656 0 0 0-.834-.653 488.746 488.746 0 0 1-6.57-4.815.236.236 0 0
 0-.14-.047c-1.34-.003-2.691-.01-4.054-.02zm-.19 1.418a1.402 1.402 0 1
 1 0 2.803 1.402 1.402 0 0 1 0-2.803zm13.874.002a1.4 1.4 0 1 1 0 2.8
 1.4 1.4 0 0 1 0-2.8z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/simple-icons/simple-icons/'''

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
