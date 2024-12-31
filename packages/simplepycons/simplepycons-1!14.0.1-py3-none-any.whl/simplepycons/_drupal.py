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


class DrupalIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "drupal"

    @property
    def original_file_name(self) -> "str":
        return "drupal.svg"

    @property
    def title(self) -> "str":
        return "Drupal"

    @property
    def primary_color(self) -> "str":
        return "#0678BE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Drupal</title>
     <path d="M15.78 5.113C14.09 3.425 12.48 1.815 11.998 0c-.48
 1.815-2.09 3.425-3.778 5.113-2.534 2.53-5.405 5.4-5.405 9.702a9.184
 9.185 0 1018.368 0c0-4.303-2.871-7.171-5.405-9.702M6.72
 16.954c-.563-.019-2.64-3.6 1.215-7.416l2.55 2.788a.218.218 0
 01-.016.325c-.61.625-3.204 3.227-3.527
 4.126-.066.186-.164.18-.222.177M12 21.677a3.158 3.158 0
 01-3.158-3.159 3.291 3.291 0 01.787-2.087c.57-.696 2.37-2.655
 2.37-2.655s1.774 1.988 2.367 2.649a3.09 3.09 0 01.792 2.093A3.158
 3.158 0 0112
 21.677m6.046-5.123c-.068.15-.223.398-.431.405-.371.014-.411-.177-.686-.583-.604-.892-5.864-6.39-6.848-7.455-.866-.935-.122-1.595.223-1.94C10.736
 6.547 12 5.285 12 5.285s3.766 3.574 5.336 6.016c1.57 2.443 1.029
 4.556.71 5.253" />
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
