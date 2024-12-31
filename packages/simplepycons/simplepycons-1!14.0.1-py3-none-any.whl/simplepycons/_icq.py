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


class IcqIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "icq"

    @property
    def original_file_name(self) -> "str":
        return "icq.svg"

    @property
    def title(self) -> "str":
        return "ICQ"

    @property
    def primary_color(self) -> "str":
        return "#24FF00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ICQ</title>
     <path d="M10.189 0a3.784 3.784 0 0 0-3.055 5.93l1.741 2.562a1.855
 1.855 0 0 0 3.334-.13l1.454-2.929h-.006A3.784 3.784 0 0 0 10.189
 0zm9.173 4.496a4.235 4.235 0 0 0-1.662.306 4.23 4.23 0 0 0-1.817
 1.396l-2.214 2.837c-.025.032-.05.063-.074.096l-.01.012a2.088 2.088 0
 0 0 1.509 3.306l3.614.536-.003-.007a4.259 4.259 0 0 0 4.532-5.807
 4.264 4.264 0 0 0-3.875-2.675zM3.586 7.242A3.154 3.154 0 0 0 .55
 9.628a3.151 3.151 0 0 0 3.903 3.804l2.539-.737a1.545 1.545 0 0 0
 .742-2.673L5.79 8.118v.005a3.13 3.13 0 0 0-2.204-.881zM13.9
 13.959a1.886 1.886 0 0 0-1.858 2.233l.387 3.263.005-.003a3.846 3.846
 0 0 0 6.134 2.574 3.846 3.846 0 0 0-.9-6.645l-2.877-1.197a1.89 1.89 0
 0 0-.89-.225zm-5.55.08c-.377 0-.75.104-1.076.3L4.06
 16.018l.006.003a4.21 4.21 0 0 0-1.593 1.485 4.24 4.24 0 0 0 1.342
 5.843 4.239 4.239 0 0 0 5.845-1.332 4.21 4.21 0 0 0
 .647-2.172l.108-3.45a2.079 2.079 0 0 0-2.062-2.356z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:ICQNe'''

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
