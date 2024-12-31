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


class AegisAuthenticatorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "aegisauthenticator"

    @property
    def original_file_name(self) -> "str":
        return "aegisauthenticator.svg"

    @property
    def title(self) -> "str":
        return "Aegis Authenticator"

    @property
    def primary_color(self) -> "str":
        return "#005E9D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Aegis Authenticator</title>
     <path d="m6.9487 19.8732-.0074.0133a1.483 1.483 0 0 0-.0013
 1.469l.3165.5565c.2639.4638.7563.75 1.2897.75h.0163c1.139 0
 1.853-1.2301
 1.2883-2.219l-.325-.5697c-.5693-.9974-2.0074-.9974-2.577-.0002m3.4905-6.1074a1.483
 1.483 0 0 0-.0013 1.4688l3.7964 6.6769c.2639.4638.756.7503
 1.2897.7503h.0156c1.139 0 1.853-1.2301
 1.2883-2.219l-3.8118-6.677c-.5693-.9974-2.0077-.9974-2.5768
 0m.3275-11.692L.1972 20.4648c-.5618.9775.1438 2.1969 1.2713
 2.1969a1.467 1.467 0 0 0 1.2734-.7393l7.9513-13.9285c.5632-.9867
 1.9861-.9855 2.548.0026l7.9175 13.9239a1.466 1.466 0 0 0
 1.2746.7416h.0982c1.1255 0 1.8313-1.2152 1.2736-2.193L13.3116
 2.0776c-.5616-.9844-1.98-.9867-2.5448-.0039" />
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
