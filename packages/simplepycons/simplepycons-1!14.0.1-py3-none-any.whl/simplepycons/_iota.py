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


class IotaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "iota"

    @property
    def original_file_name(self) -> "str":
        return "iota.svg"

    @property
    def title(self) -> "str":
        return "IOTA"

    @property
    def primary_color(self) -> "str":
        return "#131F37"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>IOTA</title>
     <path d="M6.4459 18.8235a.7393.7393 0 10-.7417-.7393.7401.7401 0
 00.7417.7393zm9.1863 2.218a1.1578 1.1578 0 10-1.1602-1.1578 1.1586
 1.1586 0 001.1602 1.1578zm-4.3951.392a.9858.9858 0
 10-.9882-.9849.9866.9866 0 00.9882.985zm2.494 2.07a1.1578 1.1578 0
 10-1.161-1.1578 1.1586 1.1586 0 001.161
 1.1578zm-4.5448-.3944a.9858.9858 0 10-.9873-.985.9866.9866 0
 00.9873.985zm-1.7035-2.1676a.8625.8625 0 10-.8649-.8601.8633.8633 0
 00.865.8601zm2.0492-1.6747a.8625.8625 0 10-.8634-.8657.8641.8641 0
 00.8634.8657zm3.631-.296a.9858.9858 0 10-.9882-.985.9866.9866 0
 00.9882.985zm-1.729-2.1428a.8625.8625 0 10-.8634-.8625.8641.8641 0
 00.8633.8625zm-2.939.32a.7393.7393 0 10-.741-.7393.7401.7401 0
 00.741.7394zm-2.5188-.32a.6161.6161 0 10-.6177-.616.6169.6169 0
 00.6177.616zm-.0248-1.7003a.5417.5417 0 10-.5433-.5417.5425.5425 0
 00.5433.5417zm2.0995.0248a.6161.6161 0 10-.6169-.616.6169.6169 0
 00.617.616zm2.37-.4672a.7393.7393 0 10-.74-.7394.741.741 0
 00.74.7394zm-.4688-1.9708a.6161.6161 0 10-.617-.616.6169.6169 0
 00.617.616zm-1.9508.7386a.5417.5417 0 10-.544-.5417.5425.5425 0
 00.544.5417zm-1.7779.2216a.4433.4433 0 10-.4448-.4433.4449.4449 0
 00.4448.4433zm2.4452-6.5515a.8625.8625 0 10-.8649-.8625.8633.8633 0
 00.865.8625zm2.2468-.0256a.7393.7393 0 10-.7409-.7385.7401.7401 0
 00.741.7385zm-.42-2.61a.7393.7393 0 10-.741-.7394.741.741 0
 00.741.7394zm-2.2468-.0008a.8625.8625 0 10-.865-.8618.8633.8633 0
 00.865.8618zm-2.618.5913a.9858.9858 0 10-.9898-.985.9858.9858 0
 00.9897.985zm.4192 2.6116a.9858.9858 0 10-.9874-.9858.9874.9874 0
 00.9874.9858zM3.1861 9.093a1.1578 1.1578 0 10-1.161-1.1578 1.1594
 1.1594 0 001.161 1.1578zm-1.8035 5.2465A1.3794 1.3794 0 100
 12.9602a1.381 1.381 0 001.3826 1.3794zm2.9637-2.3644a1.1578 1.1578 0
 10-1.1602-1.1578 1.1594 1.1594 0 001.1602
 1.1578zm2.8653-1.4034a.9858.9858 0 10-.9882-.9858.9866.9866 0
 00.9882.9858zm2.6172-.5921a.8625.8625 0 10-.8673-.8602.8625.8625 0
 00.8673.8602zm2.2476.0008a.7393.7393 0 10-.741-.7393.7401.7401 0
 00.741.7393zm.6913-2.4884a.6161.6161 0 10-.6177-.6153.6169.6169 0
 00.6177.6153zm-.4192-2.6133a.6161.6161 0 10-.6185-.616.6169.6169 0
 00.6185.616zm7.1612 11.4803a.6161.6161 0 10-.6178-.6153.6161.6161 0
 00.6178.6153zM13.755 5.599a.5425.5425 0 10-.5433-.5416.5417.5417 0
 00.5433.5416zm1.0378.8338a.4433.4433 0 10-.445-.4433.444.444 0
 00.445.4433zm-.593 1.7739a.5425.5425 0 10-.5432-.5417.5425.5425 0
 00.5433.5417zm-.2712 2.1675a.6161.6161 0 10-.6177-.616.6169.6169 0
 00.6177.616zm.0248 4.6312a.6161.6161 0 10-.6177-.616.6169.6169 0
 00.6177.616zm1.6787 1.1818a.5417.5417 0 10-.5433-.5417.5425.5425 0
 00.5433.5417zm1.1602 1.281a.4433.4433 0 10-.444-.4433.444.444 0
 00.444.4433zm1.309-.3472a.5417.5417 0 10-.5433-.5417.5417.5417 0
 00.5433.5417zm-1.0586-1.6971a.6161.6161 0 10-.6177-.6153.6161.6161 0
 00.6177.6153zm-1.7074-1.6507a.7393.7393 0 10-.7402-.7393.7401.7401 0
 00.7402.7393zm5.5569 1.3802a.7393.7393 0 10-.741-.7393.741.741 0
 00.741.7393zm-2.494-.9361a.7393.7393 0 10-.741-.7393.7401.7401 0
 00.741.7393zm3.7286-.8378a.8625.8625 0 10-.8642-.8617.8633.8633 0
 00.8642.8617zM16.5459 12a.8625.8625 0 10-.8633-.8625.8641.8641 0
 00.8634.8625zm3.087.4185a.8625.8625 0 10-.8642-.8618.8633.8633 0
 00.8642.8618zm3.383-1.4035a.9858.9858 0 10-.9874-.9857.9874.9874 0
 00.9873.9857zm-2.4693-.961a.9858.9858 0 10-.9881-.9849.9866.9866 0
 00.9881.985zm-3.0869-.4184a.9858.9858 0 10-.9874-.9857.9874.9874 0
 00.9874.9857zm3.4822-2.4884a1.1578 1.1578 0 10-1.1602-1.1578 1.1594
 1.1594 0 001.1602 1.1578zm-3.087-.4433a1.1578 1.1578 0
 10-1.161-1.1578 1.1586 1.1586 0 001.161 1.1578zm1.1603 16.0355a1.3794
 1.3794 0 10-1.3827-1.3778 1.3818 1.3818 0 001.3827
 1.3778zm-1.5555-19.484a1.3794 1.3794 0 10-1.3834-1.3795 1.3818 1.3818
 0 001.3834 1.3795z" />
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
