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


class ApacheNetbeansIdeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "apachenetbeanside"

    @property
    def original_file_name(self) -> "str":
        return "apachenetbeanside.svg"

    @property
    def title(self) -> "str":
        return "Apache NetBeans IDE"

    @property
    def primary_color(self) -> "str":
        return "#1B6AC6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apache NetBeans IDE</title>
     <path d="M22.8575
 6.1211c-.0092-.0866-.0486-.1598-.121-.2104C22.7381 5.9098 12.1194.032
 12.1185.03a.2487.2487 0 00-.2372 0c-.003 0-10.6129 5.8784-10.6145
 5.8797-.0744.0497-.1156.1241-.1243.2124v11.8365c.0149.0565.0178.1253.071.161.0183.0788
 10.6175 5.7985 10.6694 5.8507a.2456.2456 0 00.2343 0c.0025-.0017
 10.6135-5.7957
 10.6147-5.7984.0748-.0489.115-.1262.1256-.2133V6.1211zm-17.633
 9.3292L1.6323 17.534V6.5401l3.5922
 2.011zm13.551-6.8993l3.5922-2.0109v10.9938l-3.5922-2.0836zm-.7407-.1455c-2.0115
 1.1316-4.0232 2.263-6.0348 3.3943a125706.698 125706.698 0
 01-6.0349-3.3943L12 4.9349zM5.7143 15.4473V8.8265l6.0408
 3.398v6.5444l-6.0408-3.3216zm6.5305
 3.3216v-6.5444l6.0409-3.398v6.6208c-2.0135 1.1074-4.0272
 2.2145-6.0408 3.3216zM12 .5247l10.1094 5.5984-3.5771
 2.003-6.4104-3.6858a.2418.2418 0 00-.2439 0L5.4676
 8.126l-3.577-2.003L12 .5248zM5.4728 15.8731l6.2823
 3.4547v4.014L1.8868 17.952zm6.772 7.4686v-4.014l6.2824-3.4546 3.586
 2.0789z" />
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
