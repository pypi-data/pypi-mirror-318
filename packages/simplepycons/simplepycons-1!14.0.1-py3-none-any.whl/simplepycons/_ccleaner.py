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


class CcleanerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ccleaner"

    @property
    def original_file_name(self) -> "str":
        return "ccleaner.svg"

    @property
    def title(self) -> "str":
        return "CCleaner"

    @property
    def primary_color(self) -> "str":
        return "#CB2D29"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CCleaner</title>
     <path d="M14.9388.9336C8.8759.9336 3.9622 5.8884 3.9622 12c0
 .5012.0322.9934.0971 1.4766.953-.7245 1.6108-1.4633
 1.9557-1.9004l-.129-.082L7.6596 9.082s.2811-.336.6836-.336c.129 0
 .2637.0279.3867.0763.123.0483.9893.4108
 1.5879.6601l3.3828-7.1855s.33-.6818
 1.0508-.6797c.1676.0005.342.0356.5644.125.2226.0894.4279.2665.543.4746.1152.208.138.4246.127.5977-.0198.1843-.0964.358-.1446.537l-1.6425
 4.1192c.3584-.0592.577-.0664.8164-.0664.4266 0 2.5709.099 4.3691
 2.0195.1086.1161.2144.2556.3184.3516.1684.1693.4444.1973.621-.0176l3.3106-3.8652c.1552-.1801.1313-.46.0098-.6348-.9985-1.3093-2.2822-2.3865-3.7578-3.1387-1.4863-.7583-3.1674-1.1855-4.9473-1.1855Zm-.1895
 1.1836c-.431-.0013-.5879.373-.5879.373l-3.5937
 7.6348c.0107.0043-1.7194-.7172-2.0117-.834-.0826-.0325-.1533-.045-.213-.045-.1895
 0-.2733.1212-.2733.1212l-1.4649 1.9922s4.5809 2.9223 4.6895
 3.0136c.1085.0914.2246.0997.2246.0997l2.539.4843s.301-2.3783.3653-2.8008c.0657-.4426-.2461-.5234-.2461-.5234s-1.0177-.4253-1.8653-.7793l3.0645-7.6875s.3896-.6968-.2832-.9785c-.1299-.0493-.2443-.07-.3438-.0703zm-8.3046
 9.7324c-.7392.944-2.8816 3.2924-6.3926 4.0078 0
 0-.0808.0222-.041.211.0397.1888.4932 1.6514 1.8632 3.0566 0 0
 .3304.3558.754.4687.422.113 1.2093.0852 1.6542 0 0
 0-.192.1734-.9336.6563a.1036.1036 0 0
 0-.043.1172c.0184.0619.08.144.2345.2539.2905.2074 1.2422.7988 1.8554
 1.0371 0 0 .2167.1492
 1.1035.1523h.8262l.6367-.3574-.2949.3574s.909.0236
 1.6582-.125c.2187-.0433.4267-.13.6133-.2539.6948-.4648 2.3624-1.9515
 3.7012-6.0449l-2.209-.4219c-.0882-.0153-.2857-.0648-.457-.209.0284.023-.6612-.4413-4.5293-2.9062zm13.252
 2.418c-1.4344 2.2332-4.1506 2.3157-4.5802
 2.3242-.4569.009-.883-.04-1.3203-.1504-1.307 3.5108-2.8423
 4.9127-3.58 5.4063a2.3336 2.3336 0 0 1-.129.08c1.4632.7292 3.1093
 1.1387 4.8516 1.1387 3.5888 0 6.7606-1.75
 8.7637-4.4336.2681-.3738.2908-.4488.2968-.5605.011-.2047-.1328-.3516-.1328-.3516l-3.4433-3.5117c-.371-.41-.7048-.0021-.7266.0586z"
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
