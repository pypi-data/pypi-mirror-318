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


class YabaiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "yabai"

    @property
    def original_file_name(self) -> "str":
        return "yabai.svg"

    @property
    def title(self) -> "str":
        return "yabai"

    @property
    def primary_color(self) -> "str":
        return "#00364B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>yabai</title>
     <path d="M12.0752 0a3.2626 3.2626 0 0 0-2.3807.955L6.2164
 4.4313l-.5312-.5293c-1.2-1.055-2.8211.5135-1.744
 1.742l.5312.5313L.9765 9.6711c-1.2734 1.274-1.2734 3.339 0
 4.613l3.4939 3.4958-.0684.0664-.5156.5136c-1.0704 1.2058.4712 2.8158
 1.7067 1.7755l.5978-.594 3.5017 3.5017c1.2742 1.2747 3.3407 1.2747
 4.6149 0l8.7141-8.7141c1.2748-1.2742 1.2748-3.3407
 0-4.615l.002-.0019-3.486-3.488.58-.58c.4781-.4823.4781-1.2598
 0-1.742-.4815-.4818-1.2624-.4818-1.744
 0l-.5605.5604L14.3075.955A3.2626 3.2626 0 0 0 12.0752 0Zm-.0761
 1.7206c.394 0 .789.1505 1.0897.4511l3.5076 3.5056-4.566 4.568L7.433
 5.65l3.4783-3.4783a1.5334 1.5334 0 0 1 1.0878-.4511ZM5.691
 7.394l4.5934 4.5933-4.5954
 4.5778-3.4939-3.4978c-.602-.6017-.602-1.5777 0-2.1795zm12.626.0468
 3.4899 3.49c.6011.6014.6011 1.5762 0 2.1776l-8.7142
 8.7141c-.6016.6025-1.5779.6025-2.1795 0l-3.4997-3.4997Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/koekeishiya/yabai/blob/86c'''

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
