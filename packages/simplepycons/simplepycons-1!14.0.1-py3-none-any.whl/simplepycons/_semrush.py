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


class SemrushIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "semrush"

    @property
    def original_file_name(self) -> "str":
        return "semrush.svg"

    @property
    def title(self) -> "str":
        return "Semrush"

    @property
    def primary_color(self) -> "str":
        return "#FF642D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Semrush</title>
     <path d="M20.698 11.911c0 .444-.226.516-.79.516-.596
 0-.706-.1-.77-.554-.118-1.152-.896-2.13-2.201-2.24-.418-.034-.518-.19-.518-.706
 0-.48.074-.708.446-.708 2.265.01 3.833 1.832 3.833 3.69v.002zm3.3
 0c0-3.456-2.338-7.11-7.74-7.11H5.52c-.218 0-.354.11-.354.31 0
 .109.082.209.156.26.388.31.97.654 1.73 1.036.743.372 1.323.616
 1.903.852.246.1.336.208.336.344 0 .19-.136.308-.4.308H.372c-.254
 0-.372.164-.372.326 0 .136.044.254.162.372.69.726 1.796 1.596 3.4
 2.604 1.466.91 2.98 1.74 4.533
 2.492.236.11.308.236.308.372-.008.154-.126.28-.4.28H4.1c-.216
 0-.344.12-.344.3 0 .1.08.226.19.326.888.808 2.311 1.688 4.207 2.494
 2.53 1.08 5.094 1.721 7.98 1.721 5.465 0 7.867-4.087
 7.867-7.289l-.002.002zm-7.133 5.104c-2.794 0-5.132-2.276-5.132-5.114
 0-2.794 2.33-5.04 5.132-5.04 2.863 0 5.111 2.24 5.111 5.04a5.086
 5.086 0 0 1-5.111 5.114z" />
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
