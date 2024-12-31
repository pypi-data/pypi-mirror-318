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


class ReactRouterIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "reactrouter"

    @property
    def original_file_name(self) -> "str":
        return "reactrouter.svg"

    @property
    def title(self) -> "str":
        return "React Router"

    @property
    def primary_color(self) -> "str":
        return "#CA4245"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>React Router</title>
     <path d="M12.118 5.466a2.306 2.306 0
 00-.623.08c-.278.067-.702.332-.953.583-.41.423-.49.609-.662
 1.469-.08.423.41 1.43.847 1.734.45.317 1.085.502 2.065.608 1.429.16
 1.84.636 1.84 2.197 0 1.377-.385 1.747-1.96
 1.906-1.707.172-2.58.834-2.765 2.117-.106.781.41 1.76 1.125 2.091
 1.627.768 3.15-.198 3.467-2.196.211-1.284.622-1.642 1.998-1.747
 1.588-.133 2.409-.675
 2.713-1.787.278-1.02-.304-2.157-1.297-2.554-.264-.106-.873-.238-1.35-.291-1.495-.16-1.879-.424-2.038-1.39-.225-1.337-.317-1.562-.794-2.09a2.174
 2.174 0 00-1.613-.73zm-4.785 4.36a2.145 2.145 0
 00-.497.048c-1.469.318-2.17 2.051-1.35 3.295 1.178 1.774 3.944.953
 3.97-1.177.012-1.193-.98-2.143-2.123-2.166zM2.089 14.19a2.22 2.22 0
 00-.427.052c-2.158.476-2.237 3.626-.106 4.182.53.145.582.145
 1.111.013 1.191-.318 1.866-1.456
 1.549-2.607-.278-1.02-1.144-1.664-2.127-1.64zm19.824.008c-.233.002-.477.058-.784.162-1.39.477-1.866
 2.092-.98 3.336.557.794 1.96 1.058 2.82.516 1.416-.874
 1.363-3.057-.093-3.746-.38-.186-.663-.271-.963-.268z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/ReactTraining/react-router
/blob/c94bcd8cef0c811f80b02777ec26fee3618f8e86/website/static/safari-p'''

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
