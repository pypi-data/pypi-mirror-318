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


class OneAndOneIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "1and1"

    @property
    def original_file_name(self) -> "str":
        return "1and1.svg"

    @property
    def title(self) -> "str":
        return "1&1"

    @property
    def primary_color(self) -> "str":
        return "#003D8F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>1&amp;1</title>
     <path d="M0 0v24h24V0zm11.717 5.792c1.564 0 2.671 1.04 2.671
 2.468 0 1.044-.428 1.819-1.746 2.915l1.952
 2.648c.163-.147.303-1.046.274-1.777-.003-.087-.022-.341-.04-.62h1.814c0
 .244.024.595.024.683 0 1.426-.224 2.327-.909 3.198L17.2
 17.22h-2.232l-.503-.678c-.823.659-1.546.905-2.713.898-2.284-.013-3.857-1.173-4.005-3.239-.089-1.235.737-2.506
 2.32-3.42C9.049 9.477 8.84 9.025 8.84 8.207c0-1.392 1.191-2.415
 2.878-2.415zm-9.424.134h4.064v11.296H4.1V7.735H2.293zm14.45
 0h4.065v11.296H18.55V7.735h-1.807zm-5.036 1.49c-.545
 0-.931.358-.931.845 0 .47.14.726.79 1.562.772-.557 1.058-1.075
 1.058-1.58 0-.504-.354-.828-.917-.828zm-.517 4.811c-1.002.663-1.404
 1.31-1.386 1.919.03.928.806 1.522 1.948 1.522.703 0 1.174-.257
 1.579-.594z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.united-internet.de/en/newsroom/me'''

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
