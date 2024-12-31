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


class JcbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jcb"

    @property
    def original_file_name(self) -> "str":
        return "jcb.svg"

    @property
    def title(self) -> "str":
        return "JCB"

    @property
    def primary_color(self) -> "str":
        return "#0B4EA2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>JCB</title>
     <path d="M13.05 9.8643c.9723.0736 1.7257.3671
 2.3545.6843v-1.31s-1.2577-.3162-2.4408-.368c-4.1256-.1849-5.295
 1.4344-5.295 3.1292 0 1.6947 1.1694 3.3145 5.295 3.1296 1.1831-.0536
 2.4408-.3694
 2.4408-.3694v-1.3086c-.6193.3081-1.3826.6107-2.3545.683-1.6793.1272-2.6898-.6907-2.6898-2.1342
 0-1.4448 1.0105-2.2613 2.6898-2.1354m7.685
 4.1223c-.0513.0105-.1581.02-.215.02h-1.8005V12.376H20.52c.0568 0
 .1636.01.2149.02a.8056.8056 0 01.6325.7951c0
 .4162-.2872.721-.6325.796zm-2.0155-4.0374h1.6325c.059 0
 .1454.0077.1772.0137.3376.0572.6256.3307.6256.7392 0
 .409-.288.6815-.626.7392a1.571 1.571 0
 01-.1773.0137h-1.6311V9.9506zm3.4994 1.9856v-.0364c.9133-.1331
 1.4149-.726 1.4149-1.4199
 0-.8828-.7343-1.3916-1.7293-1.4416-.0772-.0032-.203-.011-.3044-.011h-5.3323v5.9467h5.7548c1.13
 0 1.9774-.6043 1.9774-1.5466
 0-.8701-.7724-1.4222-1.781-1.4917zm-17.8644.6788c0 .8787-.5906
 1.5311-1.6656 1.5311-.917
 0-1.8174-.2726-2.6889-.6938V14.76s1.4021.383 3.191.383c2.9714 0
 3.8374-1.125 3.8374-2.529V9.0266H4.3541v3.5876Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.global.jcb/en/about-us/brand-conc'''

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
