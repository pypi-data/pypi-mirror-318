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


class GetxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "getx"

    @property
    def original_file_name(self) -> "str":
        return "getx.svg"

    @property
    def title(self) -> "str":
        return "GetX"

    @property
    def primary_color(self) -> "str":
        return "#8A2BE2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GetX</title>
     <path d="M10.643.934c-.302.067-.928.29-1.386.503-2.167 1.05-3.485
 3.52-3.15 5.899a5.76 5.76 0 0 0 1.575 3.25c1.128 1.174 2.469 1.732
 4.134 1.744 1.642 0 2.994-.57 4.133-1.743C19.39 7 17.055 1.113
 12.095.867c-.492-.022-1.14 0-1.452.067zM13.77 3.17c.905.335 1.966
 1.374 2.178 2.145.213.793.1 1.82-.29 2.547-.86 1.575-2.816
 2.726-3.989 2.346-.536-.179-1.25-.994-1.642-1.855C9.18 6.464 8.9
 4.833 9.291 4.073c.592-1.15 2.715-1.575 4.48-.904ZM4.107
 11.86c-2.838.916-4.513 3.598-4.022 6.48.48 2.86 3.173 4.994 6.033
 4.77 2.033-.145 3.765-1.24 4.681-2.96.503-.96.681-1.676.681-2.815
 0-2.045-.971-3.799-2.737-4.894-1.24-.782-3.25-1.028-4.636-.58Zm2.436
 1.799c2.737.447 4.222 2.737 3.15 4.882-.436.86-1.352 1.732-2.29
 2.179-.637.29-.838.335-1.43.29-1.028-.067-1.486-.48-2.045-1.877-.67-1.642-.95-3.608-.614-4.245.413-.771
 1.117-1.162 2.413-1.33.067 0 .424.045.816.101zm9.842-1.743c-3.34
 1.173-4.837 4.882-3.273 8.077.435.894 1.463 1.944 2.38 2.425 2.356
 1.24 4.904.871 6.78-.995 3.05-3.016
 1.9-8.077-2.178-9.507-1.039-.368-2.67-.368-3.709 0zm3.419
 1.978c1.184.38 2.368 1.485 2.636 2.48.179.659.078 1.609-.223
 2.234-.548 1.129-1.91 2.145-3.251
 2.413-1.81.358-2.737-.882-3.15-4.19-.247-1.999.3-2.915
 1.91-3.16.67-.101 1.25-.046 2.078.223z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/simple-icons/simple-icons/'''

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
