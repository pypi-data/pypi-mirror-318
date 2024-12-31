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


class HackTheBoxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hackthebox"

    @property
    def original_file_name(self) -> "str":
        return "hackthebox.svg"

    @property
    def title(self) -> "str":
        return "Hack The Box"

    @property
    def primary_color(self) -> "str":
        return "#9FEF00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hack The Box</title>
     <path d="m22.5106 6.4566.0008-.0123a.888.888 0 0
 0-.2717-.6384c-.0084-.0084-.018-.0155-.0267-.0235-.0186-.0166-.0371-.0333-.0572-.0484-.0193-.0147-.04-.0276-.0607-.0406-.0096-.006-.0182-.0131-.0281-.0188L12.4576.1266a.891.891
 0 0 0-.9223.0043L1.933
 5.6744c-.0107.0062-.0203.014-.0307.0205-.0073.0047-.015.008-.0223.0128-.007.0047-.013.0106-.02.0155a.8769.8769
 0 0 0-.147.1333l-.0026.003a.8872.8872 0 0
 0-.2218.5847l.0009.014c-.0002.0088-.0015.0176-.0015.0264v11.0708c0
 .3277.1802.6288.469.7836l9.5986
 5.5417c.0076.0044.0158.0075.0236.0117a.8754.8754 0 0 0
 .166.0687c.0134.004.0266.0083.0401.0117a.8793.8793 0 0 0
 .072.0142c.0117.0019.0232.0045.0349.006a.835.835 0 0 0 .2157
 0c.0117-.0015.0232-.0041.0348-.006a.9.9 0 0 0
 .072-.0142c.0135-.0034.0267-.0077.04-.0117a.895.895 0 0 0
 .0646-.0217.9134.9134 0 0 0
 .1015-.047c.0078-.0042.016-.0072.0236-.0117l9.5986-5.5417a.8888.8888
 0 0 0 .469-.7836V6.4779c0-.0071-.0012-.0142-.0014-.0213zM5.2543
 6.0822l6.5367-3.774a.4182.4182 0 0 1 .4182 0l6.5366 3.774a.4182.4182
 0 0 1 0 .7243l-6.5367 3.774a.4182.4182 0 0 1-.4182
 0l-6.5366-3.774a.4182.4182 0 0 1 0-.7243zm5.6134 14.3449a.4172.4172 0
 0 1-.626.3613L3.718 17.0218a.4173.4173 0 0
 1-.2086-.3613V9.1279a.4172.4172 0 0 1 .6258-.3613l6.524
 3.7666a.4172.4172 0 0 1 .2086.3614v7.5325zm9.623-3.7666a.4173.4173 0
 0 1-.2086.3613l-6.5239 3.7666a.4172.4172 0 0
 1-.6259-.3613v-7.5325c0-.149.0796-.2868.2087-.3614l6.5239-3.7666a.4172.4172
 0 0 1 .6258.3613v7.5326z" />
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
