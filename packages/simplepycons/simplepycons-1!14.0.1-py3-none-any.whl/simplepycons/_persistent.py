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


class PersistentIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "persistent"

    @property
    def original_file_name(self) -> "str":
        return "persistent.svg"

    @property
    def title(self) -> "str":
        return "Persistent"

    @property
    def primary_color(self) -> "str":
        return "#FD5F07"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Persistent</title>
     <path d="M22.92 3.984a5.866 5.866 0 0 0-1.2-2.09A5.757 5.757 0 0
 0 19.814.49a5.505 5.505 0 0 0-4.542 0c-1.425.642-2.55 1.912-3.062
 3.413a5.942 5.942 0 0 0-.268 1.158 7.588 7.588 0 0 0-.047 1.167l.02
 2.247.034 4.496.011 2.248c.002.375-.002.75.004
 1.124.002.186.008.378.007.56.002.18-.01.36-.014.541a7.641 7.641 0 0
 1-.138 1.082c-.075.36-.189.71-.34 1.044a5.604 5.604 0 0 1-1.263
 1.792c-1.076.998-2.549 1.543-3.992 1.416a5.072 5.072 0 0 1-2.073-.605
 5.253 5.253 0 0 1-1.654-1.427 6.092 6.092 0 0 1-.594-.936 5.44 5.44 0
 0 1-.412-1.034 5.224 5.224 0 0
 1-.167-2.195c.053-.362.137-.72.248-1.063.115-.34.258-.668.428-.982.163-.305.356-.593.574-.86a4.31
 4.31 0 0 1 .7-.71c1.007-.846 2.343-1.21 3.707-1.214 1.412.002
 2.825.024 4.238.015l-.01-1.535c-1.408.03-2.815.128-4.22.235a7.174
 7.174 0 0 0-2.287.569 6.44 6.44 0 0 0-1.04.57 5.997 5.997 0 0 0-1.66
 1.646 6.194 6.194 0 0 0-.57 1.025 7.3 7.3 0 0 0-.62 2.267 7.553 7.553
 0 0 0 .152 2.412c.187.805.518 1.57.976 2.258a6.4 6.4 0 0 0 1.79
 1.788c.73.476 1.552.79
 2.412.92.108.02.215.03.322.041.106.012.213.024.326.027.112.007.223.011.335.01a5.842
 5.842 0 0 0 1.658-.24 6.783 6.783 0 0 0 1.253-.504c.402-.21.78-.47
 1.135-.76a7.046 7.046 0 0 0
 1.864-2.492c.05-.108.094-.216.136-.327a5.46 5.46 0 0 0 .219-.67 9.39
 9.39 0 0 0
 .25-1.384c.017-.233.04-.465.047-.697l.01-.302.015-.28.053-1.125.049-2.248.095-4.495.046-2.248.004-.282.002-.067.002-.047.005-.094a4.026
 4.026 0 0 1 .223-1.087 3.91 3.91 0 0 1 .754-1.252 3.525 3.525 0 0 1
 1.164-.856 3.421 3.421 0 0 1 1.402-.298c.487-.009.97.087
 1.416.282.457.2.867.491 1.205.858.34.372.614.812.79 1.296.178.492.257
 1.016.23 1.539a3.964 3.964 0 0 1-.378 1.529 3.765 3.765 0 0 1-2.35
 2.016 3.836 3.836 0 0
 1-.783.149l-.1.006c-.036.003-.06.006-.11.007l-.271.007-.543.015-2.02.056-.037
 1.766 2.057.028.543.007.27.004.29-.003a5.584 5.584 0 0 0 3.29-1.204
 5.812 5.812 0 0 0 1.523-1.861 6.19 6.19 0 0 0 .384-4.757" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.persistent.com/company-overview/b'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.persistent.com/company-overview/b'''

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
