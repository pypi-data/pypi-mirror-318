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


class EclipseMosquittoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "eclipsemosquitto"

    @property
    def original_file_name(self) -> "str":
        return "eclipsemosquitto.svg"

    @property
    def title(self) -> "str":
        return "Eclipse Mosquitto"

    @property
    def primary_color(self) -> "str":
        return "#3C5280"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Eclipse Mosquitto</title>
     <path d="M1.353 11.424c0 2.637.964 5.105 2.636
 7.013l-1.007.903A11.968 11.968 0 010 11.424C0 8.065 1.38 5.029 3.604
 2.85l.05.045L6.637 5.57a7.942 7.942 0 00-1.433 9.963l1.03-.923a6.59
 6.59 0 011.416-8.132l1.02.915.909.814.941.844a2.778 2.778 0 00-1.311
 2.367c0 1.23.795 2.273 1.899 2.646l.095 1.297a4.024 4.024 0
 01-2.483-6.27l-.9-.809-.004-.003a5.233 5.233 0 00.205 6.546l-3.023
 2.71a9.291 9.291 0 01-.21-11.97L3.777 4.66a10.599 10.599 0 00-2.407
 6.14l-.006.008.005.004c-.011.203-.017.406-.017.612zm11.54 2.639a2.793
 2.793 0 00.588-5.013l.941-.844.908-.814 1.021-.915a6.59 6.59 0
 011.417 8.132l1.029.923a7.942 7.942 0
 00-1.433-9.963l2.981-2.673.05-.045A11.964 11.964 0 0124 11.424c0
 2.98-1.095 5.769-2.982 7.916l-1.007-.903a10.61 10.61 0
 002.619-7.625l.005-.004-.006-.007a10.598 10.598 0
 00-2.407-6.141l-1.008.904a9.291 9.291 0 01-.211
 11.97l-3.023-2.71a5.233 5.233 0 00.205-6.546l-.004.003-.9.808a4.024
 4.024 0 01-2.482 6.27zM12 21.149l.335-4.571.271-3.712a1.56 1.56 0
 10-1.212 0l.271 3.712Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/eclipse/mosquitto/blob/75f'''

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
