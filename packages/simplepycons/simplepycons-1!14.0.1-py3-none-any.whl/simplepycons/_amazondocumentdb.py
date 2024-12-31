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


class AmazonDocumentdbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "amazondocumentdb"

    @property
    def original_file_name(self) -> "str":
        return "amazondocumentdb.svg"

    @property
    def title(self) -> "str":
        return "Amazon DocumentDB"

    @property
    def primary_color(self) -> "str":
        return "#C925D1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Amazon DocumentDB</title>
     <path d="m16.5053 21.0947.7158.4632C16.2526 23.0316 13.0947 24
 9.3895 24c-4.6316 0-8.1263-1.4737-8.1263-3.4105V3.3685C1.2632 1.7262
 4.1263 0 9.4737 0c5.3474 0 8.2105 1.7263 8.2105
 3.3684v2.9053h-.8421V4.8842c-1.221 1.0105-3.7053 1.8105-7.3684
 1.8105-3.6632 0-6.1474-.8-7.3684-1.8105v4.8c.3368 1.179 3.2 2.3579
 7.242 2.3579q1.0948 0
 2.1053-.1263l.1263.842q-1.0947.1264-2.2315.1264c-3.2421
 0-5.9369-.7158-7.2421-1.8105v4.5052c.3368 1.1369 3.2 2.3158 7.242
 2.3158q1.0527 0 2.1053-.0842l.1263.8q-1.1368.1263-2.2315.1263c-3.2421
 0-5.9369-.7157-7.2421-1.8105v3.6632c0 1.221 2.9894 2.5684 7.2842
 2.5684 3.7894 0 6.442-1.0526 7.1158-2.0632zm-14.4-17.7263c0 1.179
 3.0315 2.4842 7.3684 2.4842 4.3368 0 7.3684-1.3052 7.3684-2.4842
 0-1.221-3.0316-2.5263-7.3684-2.5263-4.3369 0-7.3684 1.3053-7.3684
 2.5263zm20.6315 7.6632v9.0947c0 .2526-.1684.421-.421.421h-8c-.2526
 0-.421-.1684-.421-.421V9.2211c0-.2106.1684-.4211.421-.4211h4.6316l-.7158-.8421h-5.179V18.021h.421v.842h-.842c-.2527
 0-.421-.1684-.421-.421V7.5368c0-.2105.1683-.421.421-.421h5.8105c.1263
 0 .2526.0842.2947.1684L20.0421 8.8h.4632q.1684 0 .2947.1263l1.8105
 1.8105q.1263.1264.1263.2948zm-.842.7158h-2.1053c-.2527
 0-.421-.1685-.421-.421V9.642h-4.6317v10.0632h7.158zm-2.4422.9684c.2527
 0 .4632.0842.5895.2526.2526.3369.2105.8.2105.9684 0 .8843.5053
 1.0527.5474 1.0948.1684.042.2947.2105.2947.421 0
 .1685-.1263.3369-.2947.379-.0421 0-.5474.2105-.5474 1.0947 0
 .5053-.2526 1.0526-.8
 1.0526h-.2947v-.842h.2105c0-.0422.0421-.1264.0421-.2106
 0-.7579.2527-1.221.5053-1.5158-.2526-.2526-.5053-.7579-.5053-1.5158v-.3368h-.2526v-.8421zm.758-1.8105h1.3473L20.2947
 9.642h-.0842zm-2.737 1.8105h.337v.842h-.2527v.2106c0 .758-.2526
 1.221-.5474 1.5158.2948.2947.5474.7579.5474 1.5158q0
 .0421-.0421.0842v.2947h.2947v.8422h-.3368c-.2105
 0-.421-.1264-.5895-.2948-.2526-.2947-.2105-.8-.1684-.9684-.0421-.8842-.5053-1.0526-.5895-1.0526-.1684-.0421-.2947-.2527-.2947-.421
 0-.1685.1263-.337.3368-.379.0421-.0421.5474-.2106.5474-1.1369-.0421-.4631.2105-1.0526.7579-1.0526z"
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
        yield from [
            "AWS DocumentDB",
        ]
