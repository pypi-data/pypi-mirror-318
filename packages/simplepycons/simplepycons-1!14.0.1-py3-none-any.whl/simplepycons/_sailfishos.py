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


class SailfishOsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sailfishos"

    @property
    def original_file_name(self) -> "str":
        return "sailfishos.svg"

    @property
    def title(self) -> "str":
        return "Sailfish OS"

    @property
    def primary_color(self) -> "str":
        return "#053766"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sailfish OS</title>
     <path d="M23.98132 5.10497a.31172.31172 0 0
 0-.40763-.17385l-2.3379.81527a24.35014 24.35014 0 0
 1-3.1292.82126c-2.16405.39565-3.71666-1.3368-3.71666-1.3368a.3237.3237
 0 0 0-.35968-.1019 4.83167 4.83167 0 0 0-.45559.17384 13.1462 13.1462
 0 0 1 1.70247-4.7957c.10211-.10285.10211-.26881 0-.37166a.36567.36567
 0 0 0-.40763-.1139 27.1736 27.1736 0 0 0-4.19623 2.60166c-2.87742
 2.236-4.47798 4.51395-4.6758 6.7979-.14987 1.85833 1.07303 3.07524
 2.24198 4.19623l.20382.19783a4.50795 4.50795 0 0 1-.28774
 3.59077c-1.04306 2.30193-3.35699 4.31013-6.25838
 5.39516-.91118.34768-1.6785.59946-1.6785.59946-.15467.05152-.24352.21354-.20381.37166A.3237.3237
 0 0 0 .32056 24H.3985a34.28921 34.28921 0 0 0
 6.59408-2.35588l.59947-.29974c3.71666-1.93026 5.70088-4.19623
 5.92867-6.68999.15586-1.58857-.7853-2.65561-1.79838-3.59677
 1.29483-1.79838 5.49107-3.2251
 5.52104-3.2251l4.14228-1.43871c1.32481-.41962 2.3439-.82126
 2.39785-.84524a.29973.29973 0 0 0 .17984-.41963zM12.9692
 5.6265a10.23281 10.23281 0 0 0-3.51285 2.72755 3.29105 3.29105 0 0
 1-.2278-1.54062c.15587-1.70846 1.98422-3.69268
 2.26597-3.99241a29.92513 29.92513 0 0 1 2.7935-1.75643 12.8045
 12.8045 0 0 0-1.3488 4.5619ZM5.25413 21.74602a10.61047 10.61047 0 0 0
 3.51285-4.09432 5.74284 5.74284 0 0 0 .5575-2.87742 3.03927 3.03927 0
 0 1 .86922 2.25997c-.2278 2.18205-2.92537 3.74065-2.94935
 3.76462-.64742.3417-1.31282.65342-1.99022.94715zm7.60717-7.14558c-.14986
 1.71446-1.24688 3.17715-2.74553 4.38806a4.0104 4.0104 0 0 0
 .6774-1.88231c.15585-1.63653-.98912-2.7755-2.11011-3.86653-1.121-1.09102-2.18804-2.15806-2.06215-3.72266.15586-1.83435
 1.30083-3.47088 2.69758-4.85564a5.2393 5.2393 0 0 0-.76132
 2.1281c-.20382 2.00819 1.14497 3.24908 2.31392 4.3401 1.16895 1.09102
 2.1101 1.96024 1.98422 3.47088zm-1.65451-4.0164a9.38757 9.38757 0 0
 1-1.4507-1.57058c1.09702-1.75643 3.59677-2.9014
 4.32812-3.19513a5.14938 5.14938 0 0 0 2.84744
 1.39674c-.61145.2218-4.3401 1.53462-5.72486 3.36898z" />
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
