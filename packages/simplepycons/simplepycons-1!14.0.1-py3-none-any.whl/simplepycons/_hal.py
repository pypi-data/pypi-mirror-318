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


class HalIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hal"

    @property
    def original_file_name(self) -> "str":
        return "hal.svg"

    @property
    def title(self) -> "str":
        return "HAL"

    @property
    def primary_color(self) -> "str":
        return "#B03532"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HAL</title>
     <path d="M18.794 5.327c.48.485 1.118.75 1.797.755h.009a2.5 2.5 0
 0 0 1.58-.553 12.106 12.106 0 0 0-3.548-3.615 2.555 2.555 0 0 0 .162
 3.413zm-.647.71A7.056 7.056 0 0 1 16.058.624a11.977 11.977 0 0
 0-2.64-.62 9.685 9.685 0 0 0 2.834 7.933 9.918 9.918 0 0 0 7.002
 2.893h.036c.238 0 .476-.01.71-.027-.09-.92-.283-1.81-.566-2.66a7.269
 7.269 0 0 1-5.287-2.106zm4.6 7.322a21.564 21.564 0 0 1-7.142-4.717
 21.175 21.175 0 0 1-5.283-8.61 12.31 12.31 0 0 0-2.605.66 23.879
 23.879 0 0 0 5.992 9.85 24.16 24.16 0 0 0 8.027 5.3c.49.198.988.383
 1.487.549.323-.827.557-1.694.696-2.597-.39-.13-.786-.278-1.172-.435zm-1.316
 6.145L4.54 2.493a12.037 12.037 0 0 0-1.913 1.882l16.907
 17.029c.7-.562 1.334-1.2 1.896-1.9zm-10.974-5.885a24.16 24.16 0 0
 0-8.027-5.3c-.57-.23-1.145-.436-1.725-.624a11.954 11.954 0 0 0-.67
 2.6 21.564 21.564 0 0 1 8.53 5.224 21.239 21.239 0 0 1 5.216
 8.405c.903-.135 1.77-.369
 2.596-.692-.18-.553-.377-1.1-.602-1.644a23.767 23.767 0 0
 0-5.318-7.969zm-2.542 2.606A9.91 9.91 0 0 0 0 13.372c.103.921.314
 1.806.61 2.65.09-.004.18-.004.27-.004 1.865 0 3.729.705 5.144
 2.111a7.056 7.056 0 0 1 2.097 5.044c0 .081-.004.167-.004.248.844.287
 1.734.48 2.65.575.022-.27.036-.54.036-.814a9.688 9.688 0 0
 0-2.888-6.957zm-2.538 2.61a2.55 2.55 0 0 0-3.437-.162 12.106 12.106 0
 0 0 3.63 3.535c.35-.445.543-.993.548-1.568a2.523 2.523 0 0
 0-.741-1.806z" />
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
