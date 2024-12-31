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


class AmazonCognitoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "amazoncognito"

    @property
    def original_file_name(self) -> "str":
        return "amazoncognito.svg"

    @property
    def title(self) -> "str":
        return "Amazon Cognito"

    @property
    def primary_color(self) -> "str":
        return "#DD344C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Amazon Cognito</title>
     <path d="M2.127 10.203h5.531v-.85h-5.53zm19.034
 6.181.602.601-3.16 3.155a.426.426 0 0 1-.601 0l-1.59-1.587.602-.6
 1.289 1.286zm1.958 2.341a4.05 4.05 0 0 1-2.288
 3.181c-.688.326-1.45.45-2.211.357a4 4 0 0 1-2.017-.842 4.04 4.04 0 0
 1-1.507-3.675 4.06 4.06 0 0 1 2.167-3.12 4 4 0 0 1 2.332-.417 4.04
 4.04 0 0 1 3.111 2.18c.369.722.511 1.53.413 2.336m.346-2.721a4.888
 4.888 0 0 0-9.214 1.64 4.89 4.89 0 0 0 1.823 4.442 4.88 4.88 0 0 0
 5.122.587 4.95 4.95 0 0 0 1.629-1.247 4.9 4.9 0 0 0 1.139-2.599 4.9
 4.9 0 0 0-.5-2.823M6.382 12.752h1.701v-.85H6.382zm-4.255
 0h3.404v-.85H2.127zM1.76 1.706h19.03c.5 0 .908.496.908
 1.105v3.143h-1.276V3.83a.425.425 0 0 0-.426-.425H10.21a.425.425 0 0
 0-.425.425v2.124H.85V2.811c0-.6.417-1.105.91-1.105zM15.11 5.83c.988 0
 1.792.794 1.792 1.77a1.76 1.76 0 0 1-.927 1.547 1.82 1.82 0 0 1-1.733
 0 1.76 1.76 0 0 1-.923-1.546c0-.977.803-1.771 1.792-1.771zM.85
 15.046V6.804h8.935v7.222c0
 .235.19.425.425.425h4.448v-.85h-3.553A3.865 3.865 0 0 1 13.9
 9.963c.752.352 1.65.355 2.414 0a3.9 3.9 0 0 1 2.24
 1.716l.728-.44a4.76 4.76 0 0 0-2.206-1.9 2.6 2.6 0 0 0
 .676-1.737c0-1.445-1.186-2.62-2.643-2.62s-2.642 1.175-2.642 2.62c0
 .65.247 1.261.67 1.733a4.7 4.7 0 0 0-2.501
 2.481V4.255h8.934v6.797h.851V6.804h1.276v6.372h.852V2.811c0-1.077-.79-1.954-1.76-1.954H1.759C.79.857
 0 1.734 0 2.81v12.235c0 1.078.79 1.955 1.76
 1.955h11.43v-.85H1.759c-.492 0-.908-.506-.908-1.105z" />
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
        yield from [
            "AWS Cognito",
        ]
