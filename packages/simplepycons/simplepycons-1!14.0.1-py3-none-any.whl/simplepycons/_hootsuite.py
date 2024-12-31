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


class HootsuiteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hootsuite"

    @property
    def original_file_name(self) -> "str":
        return "hootsuite.svg"

    @property
    def title(self) -> "str":
        return "Hootsuite"

    @property
    def primary_color(self) -> "str":
        return "#FF4C46"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hootsuite</title>
     <path d="M11.417 11.14c.505.75.28 1.572-.38
 2.017-.66.444-1.505.343-2.01-.407-.506-.75-.282-1.572.378-2.017.66-.444
 1.506-.343 2.012.407zm5.017-.274c-.66.444-.884 1.266-.379
 2.016.506.75 1.352.852
 2.012.407.66-.444.884-1.266.379-2.016-.506-.75-1.352-.852-2.012-.407zm7.422-7.086L19.03
 6.638l.236.272c2.224 2.613 3.591 6.409 4.247 8.606a4.362 4.362 0 0
 1-.638 3.8C21.449 21.295 18.398 24 12.369 24c-6.58
 0-10-3.25-11.644-5.251a3.117 3.117 0 0 1-.51-3.067c.909-2.444
 2.766-7.126 4.257-8.825a13.158 13.158 0 0 1
 2.897-2.478L2.4.534c-.27-.208-.034-.632.285-.513l8.077
 3.006c.38-.066.758-.1 1.13-.1 1.407 0 2.737.307 4.074
 1.084l7.744-.695c.266-.024.378.331.147.464zm-8.218 13.656a4.126 4.126
 0 0 1-3.316-.232c-.073-.037-.143.055-.087.115.457.49 1.273 1.35 1.766
 1.775.102.088.259.077.35-.023l1.369-1.512c.053-.059-.008-.15-.082-.123zm.24-1.156-1.796-2.018a.34.34
 0 0 0-.513.008l-1.44 1.716a.18.18 0 0 0 .031.262c.333.239 1.148.76
 1.942.76.734 0 1.402-.285 1.724-.447a.18.18 0 0 0
 .052-.281zm1.616-8.409c-.3-.034-.603.035-.862.188l-1.808
 1.07c-.45.268-1.02.231-1.432-.091L11.819 7.82a4.669 4.669 0 0
 0-1.776-.858c-2.698-.638-4.532.78-5.914 3.44-1.32 2.539-.583 6.184
 2.672 7.05 3.438.914 5.71-2.903 6.618-4.175a.439.439 0 0 1
 .712-.002c1.408 1.916 3.306 3.968 5.34 3.557 2.656-.535 2.342-3.905
 1.512-5.7-.735-1.588-1.83-3.074-3.49-3.262z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://hootsuite.widencollective.com/portals'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://hootsuite.widencollective.com/portals
/bafpk5oo/bafpk5oo/MediaKitAssets/c/b9e3a7bb-aca7-48d7-90ed-cff5898aaf'''

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
