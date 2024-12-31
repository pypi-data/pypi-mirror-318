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


class AliexpressIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "aliexpress"

    @property
    def original_file_name(self) -> "str":
        return "aliexpress.svg"

    @property
    def title(self) -> "str":
        return "AliExpress"

    @property
    def primary_color(self) -> "str":
        return "#FF4747"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AliExpress</title>
     <path d="M5.166 9.096a.022.022 0 0 0-.022.021c0
 .396-.32.717-.713.717a.021.021 0 0 0-.021.022c0
 .012.01.021.021.021.394 0 .713.322.713.718 0 .012.01.021.022.021.011
 0 .021-.01.021-.021A.717.717 0 0 1 5.9 9.88a.021.021 0 0 0
 0-.043.716.716 0 0 1-.713-.718v-.002a.021.021 0 0 0-.006-.015.022.022
 0 0 0-.015-.006zm-3.693.526L0
 13.462h.48l.355-.922h1.782l.354.922h.481L1.98
 9.622zm2.264.002v3.838h.491V9.624zm2.375
 0v3.838h2.413v-.502H6.613v-1.19H8.19v-.477H6.613v-1.166h1.773v-.502zm-4.386.592l.698
 1.82H1.028zm14.689.402a1.466 1.466 0 0
 0-.966.366V10.7h-.491v2.763h.49c.002-.477 0-.955.002-1.433a.969.969 0
 0 1 .965-.918zm4.18.007c-.053
 0-.105.003-.158.01-.315.031-.606.175-.753.377a.689.689 0 0
 0-.14.465c.007.2.066.357.233.496.184.147.42.2.657.259.311.067.426.095.546.186.08.07.133.127.136.27
 0 .25-.221.372-.42.41a.89.89 0 0
 1-.894-.344l-.371.288c.33.382.777.505 1.09.5.54-.01.891-.217
 1.029-.534.066-.153.063-.309.063-.38a.677.677 0 0
 0-.267-.545c-.228-.177-.583-.228-.636-.242-.437-.078-.658-.196-.697-.341-.043-.192.102-.35.297-.411a.76.76
 0 0 1 .857.277l.367-.247a1.166 1.166 0 0 0-.939-.494zm2.387 0c-.052
 0-.105.003-.157.01-.316.031-.607.175-.753.377a.689.689 0 0
 0-.14.465c.006.2.065.357.233.496.183.147.42.2.657.259.31.067.426.095.545.186.081.07.134.127.136.27.001.25-.221.372-.42.41a.89.89
 0 0 1-.894-.344l-.371.288c.33.382.777.505 1.09.5.541-.01.891-.217
 1.03-.534.065-.153.062-.309.062-.38a.677.677 0 0
 0-.267-.545c-.227-.177-.583-.228-.636-.242-.437-.078-.658-.196-.696-.341-.043-.192.101-.35.297-.411a.76.76
 0 0 1 .857.277l.367-.247a1.167 1.167 0 0 0-.94-.494zm-9.84.002a1.461
 1.461 0 0 0-1.42 1.117 1.305 1.305 0 0
 0-.041.327v2.833h.491v-1.813c.17.18.487.42.96.454a1.447 1.447 0 0 0
 1.208-.627 1.457 1.457 0 0 0-1.199-2.292zm4.804 0a1.448 1.448 0 0
 0-1.288 2.08c.255.53.811.87 1.412.833a1.452 1.452 0 0 0
 1.012-.51l-.363-.291a.968.968 0 0 1-1.106.273 1.01 1.01 0 0
 1-.602-.69h2.239l.002-.427a1.295 1.295 0 0
 0-1.306-1.268zm-9.2.08l1.062 1.377-1.062 1.378h.581l.779-1.01.778
 1.01h.581l-1.062-1.378 1.062-1.378h-.581l-.778
 1.01-.779-1.01zm-3.825.015v2.74h.49v-2.74zm8.233.37a.96.96 0 0 1
 .95.993.963.963 0 0 1-.863.998.962.962 0 0 1-1.034-.739c-.074-.382
 0-.746.307-1.019a.959.959 0 0 1 .64-.233zm4.79.015a.823.823 0 0 1
 .819.755h-1.76a.964.964 0 0 1 .94-.755z" />
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
