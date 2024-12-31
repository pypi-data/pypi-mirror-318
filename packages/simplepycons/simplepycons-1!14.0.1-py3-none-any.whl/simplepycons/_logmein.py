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


class LogmeinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "logmein"

    @property
    def original_file_name(self) -> "str":
        return "logmein.svg"

    @property
    def title(self) -> "str":
        return "LogMeIn"

    @property
    def primary_color(self) -> "str":
        return "#45B6F2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LogMeIn</title>
     <path d="M12 0C5.372 0 0 5.373 0 12s5.372 12 12 12 12-5.373
 12-12S18.628 0 12 0zM5.379 4.768h1.74c.147 0 .288.004.424.01a.376.376
 0 01.303.152.684.684 0 01.11.364c.007.149.01.31.01.484v12.093c0
 .176.004.37.01.587.006.216-.024.377-.091.485-.054.094-.174.17-.363.222a.754.754
 0 01-.304.02 2.533 2.533 0 00-.323-.02H5.702c-.149
 0-.286-.006-.415-.02a.572.572 0 01-.314-.12.48.48 0 01-.12-.304 4.164
 4.164 0
 01-.02-.424V6.203c0-.188-.004-.41-.01-.667-.007-.255.024-.437.09-.545a.595.595
 0 01.264-.202c.04 0 .078-.004.11-.01a.536.536 0 01.092-.011zm10.527
 3.687c.201-.008.386-.001.548.019.565.032 1.053.144
 1.464.338.539.257.963.634 1.273
 1.133.095.148.168.307.222.475.055.169.11.34.164.515.026.108.042.21.05.304.005.094.023.19.05.284
 0 .08.007.134.02.16.027.19.04.385.04.587v5.661c0
 .257-.004.503-.01.738-.008.237-.105.39-.294.456a.91.91 0
 01-.283.04h-1.415c-.163 0-.307-.01-.435-.03a.418.418 0
 01-.293-.173.613.613 0 01-.09-.313 8.825 8.825 0
 01-.01-.416v-4.426c0-.5-.02-.961-.06-1.386-.042-.424-.163-.785-.365-1.082a1.427
 1.427 0 00-.668-.51c-.186-.095-.488-.156-.827-.156-.397
 0-.74.083-.912.207-.139.057-.26.124-.362.197-.433.31-.688.762-.77
 1.354-.08.594-.123 1.261-.123 2.002v4.125c0
 .121-.02.223-.06.304a.42.42 0
 01-.323.262c-.149.027-.33.04-.545.04H10.88c-.15
 0-.297-.006-.446-.02-.148-.013-.256-.06-.323-.142-.095-.12-.139-.294-.131-.525.006-.23.009-.446.009-.647V9.6c0-.147.004-.282.01-.403a.507.507
 0 01.112-.305.24.24 0
 01.132-.09c.06-.02.124-.037.191-.05h.102c.068-.014.138-.022.212-.022h1.06c.109
 0
 .214.005.316.012.1.006.19.023.271.05.095.04.16.1.193.181.03.072.03.147.054.24.056.23.118.486.291.508.08.01.159-.025.224-.09.031-.022.114-.11.14-.144.095-.114.28-.278.388-.346.078-.058.142-.1.202-.136.192-.134.483-.261.832-.36.014-.006.028-.012.042-.016.112-.036.225-.062.342-.077l.159-.029c.224-.038.442-.06.643-.068Z"
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
