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


class FanfouIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fanfou"

    @property
    def original_file_name(self) -> "str":
        return "fanfou.svg"

    @property
    def title(self) -> "str":
        return "Fanfou"

    @property
    def primary_color(self) -> "str":
        return "#00CCFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fanfou</title>
     <path d="m21.96.0655 1.369 2.082c-3.2662.9041-6.8623
 1.5142-10.7875 1.8302v3.8061H22.736c-.448 4.4272-1.616 7.9444-3.5041
 10.5525 1.239 1.475 2.8271 2.788 4.7682 3.9381l-1.7 1.6601a25.133
 25.133 0 0 1-4.5823-3.7402 20.9459 20.9459 0 0 1-4.9932
 3.7402l-1.528-1.726c2.143-1.2121 3.8151-2.4762
 5.0192-3.7932-1.599-2.5201-2.6441-5.2913-3.1352-8.3124h-.54c.07
 5.5593-.892 10.1604-2.8851 13.8056l-2.002-1.396c1.73-3.0302
 2.594-7.2944 2.594-12.7916V1.8966c4.2872-.167 8.1904-.776
 11.7125-1.8301Zm-1.8972 10.0384h-4.6102c.35 2.3001 1.115 4.4132
 2.2921 6.3353 1.184-1.861 1.9571-3.9732 2.3181-6.3353zM9.4054
 3.6227c-.123 1.984-.51 4.0441-1.159
 6.1772l-2.1461-.618c.308-.887.584-1.9551.83-3.2002H3.583C2.96 7.4998
 2.314 8.8299 1.646 9.9709L0 8.18C1.186 6.0817 2.138 3.3845
 2.8581.0924l2.2401.646a63.5656 63.5656 0 0 1-.764 2.8842Zm-.961
 15.7546c-1.6161 1.616-3.1532 2.9021-4.6102 3.8602L2.45
 21.3274c.255-.22.382-.554.382-1.002V8.4308h2.3451v10.8404c.623-.483
 1.396-1.185 2.3181-2.107z" />
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
