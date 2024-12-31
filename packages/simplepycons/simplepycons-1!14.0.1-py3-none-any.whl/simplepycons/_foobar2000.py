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


class FoobarTwoThousandIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "foobar2000"

    @property
    def original_file_name(self) -> "str":
        return "foobar2000.svg"

    @property
    def title(self) -> "str":
        return "foobar2000"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>foobar2000</title>
     <path d="M18.3824 7.6193 15.3809 0l-2.3955
 5.1661c-.5091-.1745-1.4618-.1757-1.9709 0L8.6191 0 5.6176
 7.6193c-.8457 2.1469-1.6218 4.3796 0 6.8113.597.8951 6.3758 9.5793
 6.3824 9.5694l6.3824-9.5694c1.6219-2.4317.8458-4.6644
 0-6.8113zm-5.0072
 7.2514c-.3362-.2978-.4172-.8447-.2281-1.54.1893-.696.626-1.4546
 1.2295-2.136.6035-.6814 1.3039-1.2064 1.972-1.4784.6673-.2717
 1.22-.2572 1.5562.0406.3362.2978.4172.8447.2281 1.5399-.1893.696-.626
 1.4546-1.2296 2.136-.6035.6814-1.3039 1.2064-1.9719
 1.4784-.6673.2717-1.2199.2573-1.5562-.0405zm.4448
 4.8335c-.1573.0906-.3757.0798-.4889-.1165l-1.3283-2.3038L12
 17.279l-1.3329 2.3114c-.0627.1087-.1625.1686-.2812.1686-.1385
 0-.2784-.0811-.348-.2018-.0601-.1042-.0583-.2219.005-.3313l1.5555-2.6884c.0825-.1425.232-.2275.3999-.2275h.0004c.1703.0001.3216.0864.4048.2308l1.5477
 2.6856c.1197.2073.0158.393-.1312.4778zm-4.7515-4.7929c-.6681-.272-1.3684-.797-1.9719-1.4784-.6035-.6814-1.0402-1.44-1.2295-2.136-.1892-.6952-.1081-1.2421.2281-1.5399.1762-.1561.4119-.2343.6924-.2343.2546
 0 .5463.0645.8638.1938.6681.272 1.3684.797 1.9719 1.4784.6036.6814
 1.0402 1.44 1.2295 2.136.1891.6952.1081 1.2421-.2281
 1.54-.3361.2976-.8888.312-1.5562.0404z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://hydrogenaud.io/index.php?topic=55604.'''

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
