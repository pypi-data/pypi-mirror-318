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


class MihoyoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mihoyo"

    @property
    def original_file_name(self) -> "str":
        return "mihoyo.svg"

    @property
    def title(self) -> "str":
        return "miHoYo"

    @property
    def primary_color(self) -> "str":
        return "#4EA4DD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>miHoYo</title>
     <path d="M6.939 8.8a.65.65 0 0 0-.653.653.65.65 0 0 0
 .653.653.65.65 0 0 0 .653-.653.65.65 0 0 0-.653-.653m-5.506
 1.886A1.43 1.43 0 0 0 0 12.118v2.474a.59.59 0 0 0 .592.592.59.59 0 0
 0 .592-.592v-2.25a.464.464 0 0 1 .465-.464.464.464 0 0 1
 .465.465v2.249a.59.59 0 1 0 1.184 0v-2.25a.464.464 0 0 1
 .465-.464.464.464 0 0 1 .465.465v1.208c.001.914.736 1.649 1.65
 1.649s1.649-.735 1.649-1.649V11.49a.59.59 0 0 0-.592-.592.59.59 0 0
 0-.592.592v2.037a.464.464 0 0 1-.465.465.464.464 0 0
 1-.466-.465v-1.409a1.43 1.43 0 0 0-1.433-1.432c-.448
 0-.853.202-1.115.525-.033.04-.08.079-.158.079s-.125-.038-.158-.079a1.43
 1.43 0 0 0-1.115-.525M9.057 9.16a.59.59 0 0 0-.592.591v4.84a.59.59 0
 0 0 .592.593.59.59 0 0 0 .592-.592v-1.588a.27.27 0 0 1
 .27-.27h.636a.27.27 0 0 1 .27.27v1.588a.59.59 0 0 0 .591.592.59.59 0
 0 0 .592-.592V9.75a.59.59 0 0 0-.592-.592.59.59 0 0
 0-.592.592v1.465a.27.27 0 0 1-.269.27h-.637a.27.27 0 0
 1-.269-.27V9.751a.59.59 0 0 0-.592-.592m7.784 0a.286.286 0 0
 0-.203.47l1.166 2.11v2.853a.59.59 0 0 0 .592.592.59.59 0 0 0
 .592-.592v-2.853l1.166-2.11c.168-.233-.015-.47-.203-.47h-.606a.27.27
 0 0 0-.218.126l-.65
 1.188c-.017.03-.046.041-.077.041s-.063-.01-.08-.04l-.655-1.19a.27.27
 0 0 0-.218-.125zm-3.776 1.2c-.032
 0-.053.155-.053.368s.041.416.082.416c.04 0
 .04-.025.237-.196s.228-.171.228-.22-.073-.09-.245-.213c-.171-.122-.216-.155-.249-.155m3.437
 0c-.032
 0-.077.033-.249.155s-.245.164-.245.213.033.048.229.22.196.196.237.196.081-.204.081-.416-.02-.368-.053-.368m-1.718.343c-1.082
 0-1.96 1.006-1.96 2.245s.878 2.245 1.96 2.245 1.959-1.005
 1.959-2.245-.877-2.245-1.96-2.245m0 1.118c.541 0 .98.506.98 1.127 0
 .622-.438 1.126-.98
 1.126s-.979-.504-.979-1.126c0-.62.44-1.127.98-1.127m8.685-1.33c-.334
 0-.498.147-.596.22s-.18.147-.269.147c-.229
 0-.392-.155-.849-.155-1.082 0-1.96 1.005-1.96 2.245s.878 2.245 1.96
 2.245 1.96-1.005
 1.96-2.245c0-.452-.12-.894-.343-1.267-.037-.096-.05-.194-.05-.386
 0-.265.128-.46.27-.56a.8.8 0 0 1 .408-.138 1.2 1.2 0 0
 0-.53-.106m-1.715 1.33c.54 0 .98.505.98 1.127s-.439 1.126-.98
 1.126-.98-.504-.98-1.126c0-.62.44-1.126.98-1.127" />
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
