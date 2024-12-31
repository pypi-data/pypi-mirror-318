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


class VlcMediaPlayerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vlcmediaplayer"

    @property
    def original_file_name(self) -> "str":
        return "vlcmediaplayer.svg"

    @property
    def title(self) -> "str":
        return "VLC media player"

    @property
    def primary_color(self) -> "str":
        return "#FF8800"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>VLC media player</title>
     <path d="M12.0319 0c-.8823
 0-1.0545.136-1.0545.136-.1738.056-.3556.255-.4105.43L9.683
 3.3808c.4729.1729 1.3222.4266 2.2337.4266 1.0987 0 2.017-.3494
 2.3763-.5075L13.4352.566c-.055-.1755-.237-.3707-.4067-.4374 0
 0-.1142-.1286-.9966-.1286zm3.5645
 7.455c-.3601.34-1.3276.9373-3.6797.9373-2.2929
 0-3.189-.5678-3.5213-.9113l-1.3887 4.4227c.2272.3614 1.2539 1.5594
 4.8847 1.5594 3.7569 0 4.8539-1.3467 5.0649-1.6737zm-8.5897
 4.4487l-1.0025 3.1922H4.3428c-.2486 0-.5097.1932-.5826.4315l-2.334
 7.6317a.3962.3962 0 0 0-.0169.1537c-.0008.0053-.002.0099-.002.016 0
 .0839.0233.226.0233.226.0322.2456.2612.4452.5098.4452h20.1192c.2487 0
 .4768-.1994.5098-.4453 0 0 .0234-.142.0234-.226a.0245.0245 0 0
 0-.0025-.01.3201.3201 0 0 0 .0024-.0313.4096.4096 0 0
 0-.019-.1282l-2.3339-7.6318c-.0729-.2383-.334-.4314-.5826-.4314h-1.6636l.2005.6391c-.2407.4854-1.4886
 2.38-6.3027 2.38-4.6003 0-5.8288-1.73-6.1107-2.3072z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://code.videolan.org/videolan/vlc/-/blob
/1ce7f686ee17a028d2d79627ae69f22d905f2e23/extras/package/macosx/asset_'''

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
