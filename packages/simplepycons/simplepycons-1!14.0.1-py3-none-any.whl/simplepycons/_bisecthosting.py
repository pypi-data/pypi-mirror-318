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


class BisecthostingIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bisecthosting"

    @property
    def original_file_name(self) -> "str":
        return "bisecthosting.svg"

    @property
    def title(self) -> "str":
        return "BisectHosting"

    @property
    def primary_color(self) -> "str":
        return "#0D1129"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>BisectHosting</title>
     <path d="M22.083 5.023 13.02.302a2.717 2.717 0 0 0-2.488 0L1.917
 4.789A2.06 2.06 0 0 0 .805 6.623l.006 10.76c0 .773.426 1.476 1.112
 1.834l8.59 4.479c.38.198.813.304 1.245.304v-.002c.432 0 .862-.108
 1.244-.306l9.083-4.735a2.053 2.053 0 0 0 1.11-1.835V6.857a2.06 2.06 0
 0 0-1.112-1.834zm.222 12.103c.003.441-.24.847-.632 1.05l-9.085
 4.736a1.81 1.81 0 0 1-1.664 0l-8.59-4.48a1.184 1.184 0 0
 1-.637-1.048L1.691 6.625c0-.44.246-.844.636-1.048l8.615-4.491a1.828
 1.828 0 0 1 1.666 0l9.063 4.725c.39.205.634.608.634
 1.048v10.267zM4.666 9.2v1.088L9.86 9.44V7.954L4.666
 9.2zm4.111-.54.604-.132v.552l-.604.106V8.66zm-3.455.76
 2.55-.562v.494l-2.55.46V9.42zm4.541
 6.74v-1.486l-5.195-.85v1.088l5.195
 1.248zm-1.986-.904-2.553-.562v-.395l2.553.46v.497zm1.506.33-.602-.132v-.526l.602.106v.552zm11.583-8.827-2.33-1.214-1.853.694V4.58L13.69
 2.966a4.133 4.133 0 0 0-3.827 0l-6.83 3.561a.298.298 0 0
 0-.16.26l.007 10.401c0 .11.06.21.16.26l6.805 3.547c1.2.626 2.627.626
 3.827 0l3.1-1.614v-1.66l1.852.694 2.348-1.225a.298.298 0 0 0
 .16-.262l-.006-9.908a.288.288 0 0 0-.16-.26zM4.398
 10.871V8.75l5.541-1.494a.23.23 0 0 1 .29.22V9.83c0
 .204-.152.38-.356.402l-5.475.64v-.001zm5.477 3.01a.404.404 0 0 1
 .359.4v2.355a.23.23 0 0 1-.29.22l-5.542-1.494v-2.12l5.473.64zm3.137
 6.962s.428-.612.48-1.74V14.62s.042-1.68-1.334-2.601c1.376-.92
 1.336-2.6 1.336-2.6V5.096c0-1.272-.488-1.975-.488-1.975l3.307
 1.725v5.061c0 .076.06.14.136.146l2.14.154a.15.15 0 0 0
 .16-.148V6.12l1.967 1.02v9.684L18.75 17.85v-4.247a.15.15 0 0
 0-.16-.148l-2.14.156a.148.148 0 0 0-.137.148v5.366l-3.3 1.72v-.002z"
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
