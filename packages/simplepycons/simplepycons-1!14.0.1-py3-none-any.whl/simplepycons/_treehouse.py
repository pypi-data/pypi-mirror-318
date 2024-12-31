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


class TreehouseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "treehouse"

    @property
    def original_file_name(self) -> "str":
        return "treehouse.svg"

    @property
    def title(self) -> "str":
        return "Treehouse"

    @property
    def primary_color(self) -> "str":
        return "#5FCF80"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Treehouse</title>
     <path d="M20.3981 4.3857c-.8211-.448-2.0902.2986-2.8367
 1.6423l-1.4183 2.3888c-.5226.9704-.448 2.1648.224
 3.1353l.0746.0747c.6718.8958 1.493 1.7916 1.7916
 2.0902.1493.1493.2986.3732.3732.6718.224.8212-.224 1.717-1.1197
 1.941-.8212.2239-1.717-.224-1.941-1.1198-.0746-.224-.0746-.448-.0746-.5972.0747-.3733-.0746-.8958-.5972-1.493-.5225-.5226-1.493.5225-1.8662
 1.5676v.0747c-.2986 1.045-.5226 2.0155-.448 2.0902 0
 .0746.0747.0746.0747.1493.448.8958.1493 1.9409-.7465
 2.3888-.8958.4479-1.9409.1493-2.3888-.7465-.4479-.8958-.1493-1.941.7465-2.3888.0747
 0 .0747-.0747.1493-.0747.0747 0
 .224-.4479.448-1.0451.1492-.5225.2239-.7465.2985-.9704.0747-.2986.224-1.0451.1493-1.3437-.0746-.3733-.4479-.3733-.8211-.1493-.224.1493-.6719.5225-.8212.6718-.3732.2986-.6718.7465-.8211
 1.1198-.0747.1493-.224.3732-.3733.5225-.6718.5226-1.6423.4479-2.2395-.224-.5225-.6718-.4479-1.6422.224-2.2394.224-.1494.4479-.2987.6718-.2987.3733-.0746
 1.717-.8958 2.5381-1.493.1493-.0746.3733-.2986.448-.3732.2239-.2986
 0-.5226-.224-.5226-.6719.0747-1.4184.1493-1.5677.3733-.0746.0746-.1493.224-.2986.2986-.5972.4479-1.493.2986-1.9409-.2986-.4479-.5972-.2986-1.493.2986-1.9409.224-.224.5972-.2986.8212-.2986.5225
 0 1.8662.2986 2.9113.0746l.2986-.0746c1.1198-.224 2.4635-1.1944
 2.986-2.1649 0 0 .5226-.8958
 1.1198-2.0155.6718-1.1198.5972-2.3888-.0747-2.762l-1.269-.7466c-.6719-.3732-1.6423-.3732-2.3142
 0L2.1835 5.207C1.5117 5.58.9891 6.4758.9891 7.2223v9.5552c0
 .7465.5226 1.6423 1.1944 2.0156L10.843 23.72c.6719.3732 1.717.3732
 2.3142 0l8.6594-4.927c.6718-.3732 1.1944-1.269
 1.1944-2.0155V7.2224c0-.7465-.5226-1.6423-1.1944-2.0156 0
 0-.5972-.3732-1.4184-.8211z" />
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
