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


class MojeekIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mojeek"

    @property
    def original_file_name(self) -> "str":
        return "mojeek.svg"

    @property
    def title(self) -> "str":
        return "Mojeek"

    @property
    def primary_color(self) -> "str":
        return "#7AB93C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mojeek</title>
     <path d="M22.141 16.488c-.53 0-.824-.353-.824-1.147
 0-.795.49-4.182.68-5.736.35-2.885-1.313-4.976-3.725-4.976-1.912
 0-3.37.756-4.514 1.973-.776-1.173-1.648-1.973-3.343-1.973-1.652
 0-2.676.605-3.684 1.574C6.189 5.138 5.222 4.63 3.777 4.63 2.578
 4.629.967 5.23 0 5.825l1.077 2.44c.734-.409 1.336-.718 1.853-.718.566
 0 .902.408.808 1.262-.09.824-1.09 10.268-1.09
 10.268H5.9s.638-6.061.863-7.885c.264-2.137 1.299-3.49 2.774-3.49
 1.294 0 1.735 1.018 1.642 2.21-.08 1.037-1.025 9.165-1.025
 9.165h3.27s.72-6.738.946-8.408c.293-2.17 1.692-2.967 2.57-2.967 1.443
 0 1.882 1.18 1.747 2.299-.11.91-.5 4.118-.62 5.782-.147 2.058.824
 3.589 2.663 3.589 1.206 0 2.412-.344
 3.27-.835l-.703-2.413c-.41.177-.797.364-1.155.364" />
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
