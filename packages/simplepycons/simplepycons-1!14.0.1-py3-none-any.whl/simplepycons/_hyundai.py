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


class HyundaiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hyundai"

    @property
    def original_file_name(self) -> "str":
        return "hyundai.svg"

    @property
    def title(self) -> "str":
        return "Hyundai"

    @property
    def primary_color(self) -> "str":
        return "#002C5E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hyundai</title>
     <path d="M12 18.1622c-6.6275 0-12-2.7586-12-6.163 0-3.4028
 5.3725-6.1614 12-6.1614 6.6278 0 12 2.7586 12 6.1614 0 3.4044-5.3722
 6.163-12 6.163zM7.6023 7.17C3.701 7.9784.973 9.8302.973 11.9844c0
 1.1929.8382 2.2932 2.248
 3.1757.1174.0724.1941.0862.251.0826.1019-.006.1593-.0698.201-.146.028-.0485.0631-.1225.0972-.1968.4601-1.0834
 2.0776-4.8333 4.2023-7.3758a1.1775 1.1775 0 0 0
 .1048-.1461c.046-.084.0356-.1513.0006-.192-.0593-.0647-.2247-.065-.4756-.016zM9.742
 8.8995c-1.1728 2.8492 1.0473 2.4961 1.6478 2.3637 1.0203-.2258
 1.9944-.6128 2.7746-.925 2.2216-.8887 3.4012-1.7804
 3.7925-2.123a1.9839 1.9839 0 0 0
 .1076-.0988c.0557-.058.0976-.1192.0976-.2002
 0-.0936-.081-.1687-.2374-.2231-.012-.0049-.0517-.021-.0641-.025-1.698-.5415-3.724-.8563-5.9016-.8563-.0168
 0-.0586-.0022-.1169
 0-.2608.0078-.5509.0664-.787.1888-.7777.4049-1.1163 1.4235-1.313
 1.899zm10.5851.0037c-.0268.0487-.0612.1224-.0962.1974-.4599
 1.0826-2.0774 4.831-4.2018
 7.3733-.0515.063-.0796.1031-.1042.1467-.0492.0846-.0388.1535 0
 .1935.0572.0641.2235.0654.474.0157 3.8998-.81 6.628-2.6606
 6.628-4.8149
 0-1.1925-.836-2.2928-2.2472-3.1745-.1161-.073-.1934-.0871-.25-.083-.1028.0067-.16.0699-.2026.1458zM14.258
 15.099c1.173-2.849-1.0483-2.494-1.6467-2.3622-1.0218.225-1.996.613-2.7757.924-2.2226.8883-3.4017
 1.782-3.7944
 2.1234-.0468.0428-.0833.0742-.1066.0995-.0564.0573-.0967.1178-.0967.2007
 0 .0923.08.1688.2362.2229.012.0048.0511.0213.0657.0255 1.696.54
 3.722.8557 5.9.8557.0177 0 .0592.0016.1178 0
 .2609-.0081.5522-.0677.7871-.1888.7781-.4052 1.1169-1.4234
 1.3133-1.9007z" />
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
