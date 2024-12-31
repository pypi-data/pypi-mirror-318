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


class CurlIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "curl"

    @property
    def original_file_name(self) -> "str":
        return "curl.svg"

    @property
    def title(self) -> "str":
        return "curl"

    @property
    def primary_color(self) -> "str":
        return "#073551"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>curl</title>
     <path d="M.803 14.8169c0-.5342.433-.9665.9665-.9665.5335 0
 .9665.4323.9665.9665 0 .5335-.433.9657-.9665.9657-.5335
 0-.9666-.4322-.9666-.9657m2.736
 0c0-.1963-.0532-.376-.1119-.5525-.2344-.7024-.876-1.2169-1.6575-1.2169-.1249
 0-.2344.0465-.3524.0708C.6149 13.2865 0 13.9646 0 14.817c0 .9764.7923
 1.7694 1.7695 1.7694.9772 0 1.7694-.793
 1.7694-1.7694m-1.7694-7.149c.5335 0 .9665.433.9665.9665 0
 .5335-.433.9665-.9665.9665-.5343 0-.9666-.433-.9666-.9665
 0-.5335.4323-.9665.9666-.9665m0 2.7359c.9772 0 1.7694-.7923
 1.7694-1.7694
 0-.1956-.0532-.376-.1119-.5525-.2344-.7024-.8767-1.2169-1.6575-1.2169-.1249
 0-.2344.0465-.3524.0716C.6149 7.104 0 7.782 0 8.6344c0 .9771.7923
 1.7694 1.7695 1.7694m13.221-5.694c-.5342
 0-.9665-.433-.9665-.9664a.966.966 0 01.9666-.9665c.5335 0
 .9658.4322.9658.9665 0 .5334-.4323.9664-.9658.9664m-9.6
 16.5133c-.5335 0-.9666-.433-.9666-.9665
 0-.5342.433-.9665.9666-.9665a.966.966 0 01.9665.9665c0
 .5335-.4323.9665-.9665.9665m9.6-19.2491c-.978 0-1.7695.7922-1.7695
 1.7694 0 .2085.0525.4025.1187.5882L5.039
 18.5581c-.803.1681-1.4179.8462-1.4179 1.6985 0 .9772.7923 1.7694
 1.7695 1.7694.9772 0 1.7694-.7922 1.7694-1.7694
 0-.1963-.0525-.3759-.111-.5525l8.3427-14.2728c.7778-.1865
 1.3683-.8531 1.3683-1.688 0-.977-.793-1.7693-1.7694-1.7693m7.24
 2.7359c-.5343 0-.9666-.433-.9666-.9665a.966.966 0 01.9665-.9665c.5335
 0 .9666.4322.9666.9665 0 .5334-.433.9665-.9666.9665M12.6313
 21.223c-.5343 0-.9665-.433-.9665-.9665a.966.966 0 01.9665-.9665c.5335
 0 .9658.4323.9658.9665 0 .5335-.4323.9665-.9658.9665M22.2305
 1.974c-.9772 0-1.7694.7922-1.7694 1.7694 0
 .2085.0525.4025.1187.5882l-8.3009
 14.2265c-.8021.1681-1.417.8462-1.417 1.6985 0 .9772.7922 1.7694
 1.7694 1.7694.9764 0 1.7687-.7922 1.7687-1.7694
 0-.1963-.0525-.3759-.1111-.5525l8.3427-14.2728C23.4094 5.2448 24
 4.5782 24 3.7433c0-.977-.7923-1.7693-1.7695-1.7693" />
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
