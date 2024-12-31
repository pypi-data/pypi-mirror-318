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


class PlurkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "plurk"

    @property
    def original_file_name(self) -> "str":
        return "plurk.svg"

    @property
    def title(self) -> "str":
        return "Plurk"

    @property
    def primary_color(self) -> "str":
        return "#FF574D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Plurk</title>
     <path d="M12.9017 1.9056a10.0652 10.0652 0 00-7.8802 3.707
 10.1803 10.1803 0
 00-.283.357l.004-.003c.232-.196.473-.345.717-.445l.058-.023c.299-.112.602-.147.9-.088
 1.4401.289 2.1901 2.6091 1.6751 5.1832-.515 2.574-2.1 4.4271-3.54
 4.139-1.0101-.202-1.6781-1.405-1.8121-2.992v-.005.052c-.003.132-.003.266
 0
 .4v.073l.002.059c.005.149.013.296.024.443.005.067.012.134.019.2a10.0322
 10.0322 0 00.961 3.4431c.06.126.03.276-.078.363l-.277.226a.906.906 0
 00-.29.97c0 .006.003.01.006.017a.955.955 0
 00.059.142l.05-.039.23-.174a.2612.2612 0
 11.316.416l-.245.186-.037.028 1.177 1.4481a.91.91 0
 001.275.131l.258-.21a.298.298 0 01.374 0 10.0502 10.0502 0 006.5272
 2.181 10.0422 10.0422 0 005.5722-1.855.298.298 0
 01.38.025l.163.156a.909.909 0
 001.179.059l-.004-.004-.21-.197a.262.262 0 01.358-.382l.225.21
 1.26-1.326a.91.91 0 00-.033-1.282l-.263-.25a.297.297 0 01-.054-.36
 10.0602 10.0602 0 001.103-6.6712c.301-.278.853-.824
 1.0691-1.292.231-.502.29-1.02-.323-.792-.476.177-.842.291-1.286.19-1.417-3.5932-4.8472-6.1932-8.8513-6.4002a9.7102
 9.7102 0 00-.473-.014zM2.2645 6.2466a1.228 1.228 0 00-1.082 1.7641
 1.23 1.23 0 10.754
 2.236c.177-.124.306-.289.395-.47.186.342.46.627.778.823a5.5901 5.5901
 0 00.017.6001c.102 1.228.62 2.16 1.401 2.316 1.114.223 2.34-1.21
 2.738-3.2.3991-1.99-.181-3.7841-1.295-4.0071-.434-.087-.885.08-1.298.432-.45.383-.854.988-1.14
 1.73-.01-.002-.02-.003-.03-.007-.14-.04-.215-.131-.312-.152a1.23 1.23
 0 00-.926-2.065zm2.862 1.2441c.054 0 .107.004.16.015.726.143 1.104
 1.312.844 2.608-.259 1.2981-1.058 2.2301-1.783
 2.0851-.493-.098-.824-.67-.905-1.433.181.07.37.113.56.122.527.024.871-.154
 1.14-.513.346-.465.084-1.753-.374-1.92-.356-.13-.567.027-.884.05.16-.298.351-.544.557-.72.219-.185.453-.292.686-.295z"
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
