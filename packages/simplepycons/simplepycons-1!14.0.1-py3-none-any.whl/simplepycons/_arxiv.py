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


class ArxivIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "arxiv"

    @property
    def original_file_name(self) -> "str":
        return "arxiv.svg"

    @property
    def title(self) -> "str":
        return "arXiv"

    @property
    def primary_color(self) -> "str":
        return "#B31B1B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>arXiv</title>
     <path d="M3.8423 0a1.0037 1.0037 0 0
 0-.922.6078c-.1536.3687-.0438.6275.2938 1.1113l6.9185 8.3597-1.0223
 1.1058a1.0393 1.0393 0 0 0 .003 1.4229l1.2292 1.3135-5.4391
 6.4444c-.2803.299-.4538.823-.2971 1.1986a1.0253 1.0253 0 0 0
 .9585.635.9133.9133 0 0 0 .6891-.3405l5.783-6.126 7.4902
 8.0051a.8527.8527 0 0 0 .6835.2597.9575.9575 0 0 0
 .8777-.6138c.1577-.377-.017-.7502-.306-1.1407l-7.0518-8.3418
 1.0632-1.13a.9626.9626 0 0 0
 .0089-1.3165L4.6336.4639s-.3733-.4535-.768-.463zm0
 .272h.0166c.2179.0052.4874.2715.5644.3639l.005.006.0052.0055 10.169
 10.9905a.6915.6915 0 0 1-.0072.945l-1.0666
 1.133-1.4982-1.7724-8.5994-10.39c-.3286-.472-.352-.6183-.2592-.841a.7307.7307
 0 0 1 .6704-.4401Zm14.341 1.5701a.877.877 0 0 0-.6554.2418l-5.6962
 6.1584 1.6944 1.8319
 5.3089-6.5138c.3251-.4335.479-.6603.3247-1.0292a1.1205 1.1205 0 0
 0-.9763-.689zm-7.6557 12.2823 1.3186 1.4135-5.7864 6.1295a.6494.6494
 0 0 1-.4959.26.7516.7516 0 0
 1-.706-.4669c-.1119-.2682.0359-.6864.2442-.9083l.0051-.0055.0047-.0055z"
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
