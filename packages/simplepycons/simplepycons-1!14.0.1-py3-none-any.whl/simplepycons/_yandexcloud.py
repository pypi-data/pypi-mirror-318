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


class YandexCloudIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "yandexcloud"

    @property
    def original_file_name(self) -> "str":
        return "yandexcloud.svg"

    @property
    def title(self) -> "str":
        return "Yandex Cloud"

    @property
    def primary_color(self) -> "str":
        return "#5282FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Yandex Cloud</title>
     <path d="M12 0C5.38 0 0 5.38 0 12s5.38 12 12 12 12-5.38
 12-12S18.62 0 12 0zM7.163 20.618C4.152 18.927 2.12 15.702 2.12
 12c0-5.46 4.42-9.88 9.88-9.88 1.429 0 2.496.536 3.029
 1.187.534.65.684 1.715.5 3.253l-3.207.631c-2.905.532-4.506 2.148-5.06
 5.065-.07.406-.15.812-.226
 1.196-.031.157-.062.312-.09.46-.073.396-.143.773-.208
 1.124-.093.505-.177.957-.247 1.34-.324 1.884-.06 3.276.672
 4.242zm7.986-11.851c-.087.434-.167.867-.247
 1.302-.081.434-.16.868-.247 1.301-.396 2.05-1.364 2.996-3.42
 3.391l-2.391.474c.059-.296.119-.611.178-.927.022-.12.044-.241.067-.362.078-.421.157-.855.25-1.313.395-2.05
 1.344-2.996 3.399-3.391l2.411-.475zM12 21.88c-1.429
 0-2.496-.536-3.029-1.187s-.684-1.715-.5-3.253l3.18-.631c2.905-.532
 4.507-2.148
 5.08-5.046.069-.406.149-.812.226-1.196.031-.157.062-.311.09-.46.087-.471.171-.917.247-1.327.081-.432.154-.822.215-1.156.325-1.884.061-3.275-.671-4.242C19.848
 5.073 21.88 8.298 21.88 12c0 5.46-4.42 9.88-9.88 9.88z" />
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
