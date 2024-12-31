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


class ContentstackIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "contentstack"

    @property
    def original_file_name(self) -> "str":
        return "contentstack.svg"

    @property
    def title(self) -> "str":
        return "Contentstack"

    @property
    def primary_color(self) -> "str":
        return "#E74C3D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Contentstack</title>
     <path d="M18.564 10.108a.347.347 0 0 1-.364.368h-6.974a.35.35 0 0
 1-.369-.368v-.79a.35.35 0 0 1 .37-.368h6.964a.347.347 0 0 1
 .364.369zm3.085 2.29a.347.347 0 0 1-.368.37h-8.59a.343.343 0 0
 1-.363-.37v-.807a.342.342 0 0 1 .364-.364h8.514a.346.346 0 0 1
 .369.364zm2.35 2.35a.347.347 0 0 1-.37.368h-9.32a.342.342 0 0
 1-.364-.368v-.803a.342.342 0 0 1 .364-.37h9.321a.347.347 0 0 1
 .368.37zm0 2.352a.347.347 0 0 1-.37.364h-9.32a.343.343 0 0
 1-.364-.364v-.807a.342.342 0 0 1 .364-.37h9.321a.347.347 0 0 1
 .368.37zm-2.35 2.273a.351.351 0 0 1-.368.37h-8.589a.347.347 0 0
 1-.364-.37v-.807a.346.346 0 0 1 .364-.37h8.515a.351.351 0 0 1
 .368.37zm-3.085 2.349a.346.346 0 0 1-.364.368h-6.974a.351.351 0 0
 1-.369-.368v-.808a.347.347 0 0 1 .37-.365h6.964a.343.343 0 0 1
 .364.365zM5.354 3.087a.347.347 0 0 0 .37.364h6.97a.342.342 0 0 0
 .367-.365V2.28a.346.346 0 0 0-.368-.369h-6.97a.351.351 0 0
 0-.367.37ZM2.35 5.43a.342.342 0 0 0 .364.364h8.514a.346.346 0 0 0
 .368-.364v-.807a.351.351 0 0 0-.368-.37H2.712a.346.346 0 0
 0-.364.37ZM0 7.778a.342.342 0 0 0 .364.364h9.321a.342.342 0 0 0
 .364-.364V6.97a.346.346 0 0 0-.364-.37H.365a.347.347 0 0 0-.364.37Zm0
 2.33a.347.347 0 0 0 .364.37h9.321a.346.346 0 0 0
 .364-.37v-.79a.346.346 0 0 0-.364-.368H.365A.347.347 0 0 0 0
 9.319Zm2.347 2.291a.342.342 0 0 0 .365.368h8.513a.346.346 0 0 0
 .37-.368v-.808a.346.346 0 0 0-.37-.364H2.713a.342.342 0 0
 0-.365.364zm3.008 2.348a.346.346 0 0 0 .369.368h6.968a.346.346 0 0 0
 .37-.368v-.803a.346.346 0 0 0-.37-.37H5.725a.347.347 0 0 0-.37.37z"
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
