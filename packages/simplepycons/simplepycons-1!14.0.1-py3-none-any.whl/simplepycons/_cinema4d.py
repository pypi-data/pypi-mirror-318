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


class CinemaFourDIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cinema4d"

    @property
    def original_file_name(self) -> "str":
        return "cinema4d.svg"

    @property
    def title(self) -> "str":
        return "Cinema 4D"

    @property
    def primary_color(self) -> "str":
        return "#011A6A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cinema 4D</title>
     <path d="M12.052 0C5.394-.007-.003 5.412 0 11.976.003 18.654
 5.475 23.981 11.978 24c6.535.02 12.057-5.306
 12.022-11.998-.009-1.665-.53-5.371-1.84-5.276-1.98.145-2.159
 4.12-2.377 5.407-.417 2.46-1.346 5.08-2.953 6.99-1.88 2.359-4.697
 3.634-7.662
 3.158-3.55-.564-5.893-3.278-6.68-5.201-.753-1.723-1.035-4.162-.07-6.324
 1.16-2.766 3.734-4.632 6.28-5.584 2.006-.827 4.103-1.151 5.357-1.375
 2.516-.5 2.855-1.463
 2.814-2.149-.015-.252-.256-.724-.785-.943C15.03.269 13.268.001 12.052
 0zm5.098 1.342c.139.398.088.85-.148 1.256-.325.56-.972 1.05-1.897
 1.29-1.636.428-2.976.554-4.34.96-1.312.39-3.397 1.018-5.316
 2.552-.268.842-.341 1.892-.369 2.662.15 5.014 4.557 8.884 9.17
 8.682.853-.037 1.921-.261 2.912-.68a13.56 13.56 0 0 0
 1.387-2.683l.002-.002v-.002c.424-1.03.606-1.836.8-2.793.32-1.565.202-2.88
 1.012-4.758.251-.582.71-1.113
 1.258-1.346.25-.105.522-.133.79-.072-.89-2.471-3.115-4.326-5.26-5.066z"
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
