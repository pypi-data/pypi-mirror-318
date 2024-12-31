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


class WechatIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wechat"

    @property
    def original_file_name(self) -> "str":
        return "wechat.svg"

    @property
    def title(self) -> "str":
        return "WeChat"

    @property
    def primary_color(self) -> "str":
        return "#07C160"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WeChat</title>
     <path d="M8.691 2.188C3.891 2.188 0 5.476 0 9.53c0 2.212 1.17
 4.203 3.002 5.55a.59.59 0 0 1 .213.665l-.39
 1.48c-.019.07-.048.141-.048.213 0 .163.13.295.29.295a.326.326 0 0 0
 .167-.054l1.903-1.114a.864.864 0 0 1 .717-.098 10.16 10.16 0 0 0
 2.837.403c.276 0 .543-.027.811-.05-.857-2.578.157-4.972 1.932-6.446
 1.703-1.415 3.882-1.98
 5.853-1.838-.576-3.583-4.196-6.348-8.596-6.348zM5.785 5.991c.642 0
 1.162.529 1.162 1.18a1.17 1.17 0 0 1-1.162 1.178A1.17 1.17 0 0 1
 4.623 7.17c0-.651.52-1.18 1.162-1.18zm5.813 0c.642 0 1.162.529 1.162
 1.18a1.17 1.17 0 0 1-1.162 1.178 1.17 1.17 0 0
 1-1.162-1.178c0-.651.52-1.18 1.162-1.18zm5.34
 2.867c-1.797-.052-3.746.512-5.28 1.786-1.72 1.428-2.687 3.72-1.78
 6.22.942 2.453 3.666 4.229 6.884 4.229.826 0 1.622-.12
 2.361-.336a.722.722 0 0 1 .598.082l1.584.926a.272.272 0 0 0
 .14.047c.134 0 .24-.111.24-.247
 0-.06-.023-.12-.038-.177l-.327-1.233a.582.582 0 0 1-.023-.156.49.49 0
 0 1 .201-.398C23.024 18.48 24 16.82 24
 14.98c0-3.21-2.931-5.837-6.656-6.088V8.89c-.135-.01-.27-.027-.407-.03zm-2.53
 3.274c.535 0 .969.44.969.982a.976.976 0 0 1-.969.983.976.976 0 0
 1-.969-.983c0-.542.434-.982.97-.982zm4.844 0c.535 0
 .969.44.969.982a.976.976 0 0 1-.969.983.976.976 0 0
 1-.969-.983c0-.542.434-.982.969-.982z" />
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
