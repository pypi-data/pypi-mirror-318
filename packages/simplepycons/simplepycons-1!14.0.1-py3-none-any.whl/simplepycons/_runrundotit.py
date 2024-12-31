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


class RunrundotitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "runrundotit"

    @property
    def original_file_name(self) -> "str":
        return "runrundotit.svg"

    @property
    def title(self) -> "str":
        return "Runrun.it"

    @property
    def primary_color(self) -> "str":
        return "#DB3729"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Runrun.it</title>
     <path d="M11.933
 10.995c.289-1.241.554-2.402.715-3.377.293-1.762.364-2.985.28-4.197h.134c2.995
 0 4.642 1.256 4.642 3.364 0 2.769-2.795 4.174-5.771 4.21Zm10.006
 7.318c-.544.701-1.352 1.4-2.306 1.4-1.844 0-3.433-2.808-3.71-6.624
 3.514-.662 6.575-3.086 6.575-6.823C22.498 3.18 19.313 0 13.55 0 6.478
 0 .471 3.84.471 8.648c0 1.696.886 3.249 2.396 3.249.874 0 1.775-.345
 2.36-1.167-.4-.767-.622-1.376-.575-2.277.086-1.613 1.982-3.354
 3.734-4.198.029 2.846-.402 5.014-1.105 8.305-.755 3.537-1.747
 6.57-1.747 9.087 0 1.073.502 2.353 1.773 2.353 1.351 0 2.533-.789
 3.302-1.663-.199-1.552-.226-3.313.25-6.255a55.23 55.23 0 0 1
 .636-3.187c.43 4.649 2.332 11.045 6.867 11.045 2.742 0 5.167-1.693
 5.167-3.918 0-1.012-.636-1.83-1.59-1.709" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://runrun.it/en-US/project-management-lo'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://runrun.it/en-US/project-management-lo'''

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
