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


class SkyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sky"

    @property
    def original_file_name(self) -> "str":
        return "sky.svg"

    @property
    def title(self) -> "str":
        return "Sky"

    @property
    def primary_color(self) -> "str":
        return "#0072C9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sky</title>
     <path d="M7.387 13.656c0 1.423-.933 2.454-2.823
 2.675-1.35.147-3.337-.025-4.294-.148-.025-.147-.074-.343-.074-.49
 0-1.252.663-1.522 1.3-1.522.664 0 1.694.123 2.455.123.834 0
 1.104-.295 1.104-.565 0-.368-.343-.515-1.006-.638l-1.767-.343C.785
 12.453 0 11.423 0 10.343c0-1.325.933-2.454 2.798-2.65 1.398-.148
 3.116.024 4.049.122.024.172.049.32.049.491 0 1.252-.663 1.522-1.276
 1.522-.491 0-1.227-.099-2.086-.099-.884 0-1.227.246-1.227.54 0
 .32.343.442.883.54l1.718.32c1.742.294 2.479 1.3 2.479 2.527m3.092
 1.521c0 .761-.295 1.203-1.792 1.203-.196
 0-.368-.025-.54-.05V6.22c0-.76.27-1.57 1.767-1.57.196 0
 .393.024.565.049zm6.085 3.927c.197.098.59.22 1.105.245.859.025
 1.325-.319 1.693-1.08L24 7.913a2.5 2.5 0 0 0-.957-.22c-.589
 0-1.399.122-1.914 1.325l-1.497
 3.534-2.945-4.81c-.196-.05-.662-.148-1.006-.148-1.03 0-1.62.393-2.233
 1.031l-2.871 3.141 2.306 3.632c.418.663.982 1.006 1.89 1.006.589 0
 1.104-.147 1.325-.245l-2.773-4.196 1.963-2.086 3.24 5.08Z" />
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
