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


class JetblueIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jetblue"

    @property
    def original_file_name(self) -> "str":
        return "jetblue.svg"

    @property
    def title(self) -> "str":
        return "JetBlue"

    @property
    def primary_color(self) -> "str":
        return "#001E59"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>JetBlue</title>
     <path d="M.779 9.795h.926v4.986a1.265 1.265 0 0 1-1.344
 1.256H0v-.869h.265c.316 0 .52-.147.52-.491V9.795M.779
 7.96h.926v.926H.779V7.96Zm2.444 3.748a.98.98 0 0 1 .971-1.081.98.98 0
 0 1 .97 1.081H3.223m2.867.762v-.762l.001-.074a1.877 1.877 0 0
 0-1.868-1.868h-.029c-.887 0-1.897.565-1.897 2.365 0 1.885 1.095 2.337
 2.043 2.337a2.117 2.117 0 0 0 1.665-.723l-.671-.564a1.452 1.452 0 0
 1-1.005.446c-.024.002-.048.002-.072.002a1.037 1.037 0 0
 1-1.029-1.131l2.862-.028Zm.734-4.047h.925v1.372h.672v.705h-.672v2.681c0
 .254.102.344.328.344h.344v.869h-.48a1.06 1.06 0 0
 1-1.129-1.128v-2.738H6.35v-.733h.462l.012-1.372Zm4.673 3.127a.981.981
 0 0 1 1.081.971.981.981 0 0 1-1.081.97H9.99V11.55h1.507m-2.483
 2.867h2.755a1.77 1.77 0 0 0 1.761-1.761l-.001-.073a1.449 1.449 0 0
 0-1.05-1.49c.588-.201.977-.768.954-1.389
 0-1.016-.655-1.732-1.913-1.732H9.019v6.456m2.393-5.587a.935.935 0 0 1
 1.034.925.936.936 0 0
 1-1.034.926H9.996V8.841h1.416Zm2.647-.881h.926v5.272c0
 .209.119.316.344.316h.316v.869h-.406c-.672
 0-1.18-.288-1.18-1.129V7.96Zm1.976 1.835h.925v2.737a.918.918 0 0 0
 .912.986.918.918 0 0 0 .911-.986V9.795h.926v4.599h-.926v-.491a1.466
 1.466 0 0 1-1.19.565 1.554 1.554 0 0
 1-1.542-1.547l.001-.05-.017-3.076Zm5.096 1.913a.97.97 0 0 1
 .971-1.072c.565 0 .943.372.971
 1.072h-1.942m2.868.762v-.762l.001-.074a1.877 1.877 0 0
 0-1.868-1.868h-.03c-.886 0-1.896.565-1.896 2.365 0 1.885 1.095 2.337
 2.037 2.337a2.12 2.12 0 0 0 1.66-.745l-.672-.565a1.448 1.448 0 0
 1-1.071.448 1.037 1.037 0 0 1-1.029-1.131l2.868-.005Z" />
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
