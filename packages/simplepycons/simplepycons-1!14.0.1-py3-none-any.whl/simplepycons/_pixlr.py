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


class PixlrIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pixlr"

    @property
    def original_file_name(self) -> "str":
        return "pixlr.svg"

    @property
    def title(self) -> "str":
        return "Pixlr"

    @property
    def primary_color(self) -> "str":
        return "#3EBBDF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pixlr</title>
     <path d="M8.264 14.391a17.698 17.698 0 0 1-2.645-.299A16.016
 16.016 0 0 1 0 11.821v.284c0 6.052 4.483 11.043 10.311 11.85a48.568
 48.568 0 0
 1-1.808-7.816c-.075-.552-.164-1.135-.239-1.748Zm6.276-4.633c.374-.418.613-.941.688-1.494.015-.12.03-.24.03-.344a2
 2 0 0 0-.24-1.016 1.34 1.34 0 0
 0-.657-.628c-1.195-.582-2.615.658-3.123 1.69 0 0 0 .014-.015.014-.717
 1.36-.523 3.542-.523 3.542a8.27 8.27 0 0 0
 2.929-1.031c.329-.195.642-.434.911-.733zM12 .045C6.486.045 1.853
 3.765.463 8.847c.105.134.643.433.733.493.254.164.523.329.792.493
 1.11.647 2.897 1.47 5.155 1.749.314.06.643.074.957.074
 0-.12-.015-.239-.015-.358-.015-.583.015-1.18.074-1.764.03-.239.045-.463.09-.702.015-.045.015-.105.03-.15v-.044c.374-2.003
 1.42-3.781 3.362-4.648 2.003-.882 4.29-.523 5.545 1.36a5.218 5.218 0
 0 1-.12 5.484c-1.315 2.048-3.631 3.034-6.067 3.363a44.26 44.26 0 0 0
 .642 4.035 48.25 48.25 0 0 0 .882
 3.511c.015.06.03.12.06.18.194.672.418 1.345.642 2.002C19.278 23.328
 24 18.217 24 12.015 23.97 5.41 18.605.045 12 .045" />
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
