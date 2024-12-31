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


class GltfIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gltf"

    @property
    def original_file_name(self) -> "str":
        return "gltf.svg"

    @property
    def title(self) -> "str":
        return "glTF"

    @property
    def primary_color(self) -> "str":
        return "#87C540"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>glTF</title>
     <path d="M23.154
 9.357h-.205v.533h-.179v-.533h-.206v-.154h.59zm.08-.154h.263l.119.458h.002l.118-.458H24v.687h-.169v-.522h-.001l-.145.522h-.137l-.144-.522h-.002v.522h-.168zM9.671
 16.29c-.742.832-2.001 1.293-4.483 1.208C2.094 16.427 0 14.366 0
 11.998 0 8.53 4.497 5.72 10.043 5.721c3.621 0 6.788 1.263 8.555
 3.061-1.619-1.073-4.052-1.691-6.767-1.691C6.959 7.091 3.01 9.289 3.01
 12c0 1.7 1.552 3.198 3.911
 4.079v-.001c.006.002.011.005.017.007.06.022.12.044.182.066.056.017.113.031.173.043.165.032.322.048.473.048q.45
 0
 .762-.156t.516-.429c.136-.183.234-.403.295-.661s.091-.544.091-.859v-.365h-.021c-.079.171-.179.32-.3.445q-.183.189-.414.312c-.154.082-.319.145-.494.188-.176.043-.349.064-.521.064-.416
 0-.777-.075-1.085-.225-.308-.151-.566-.355-.774-.613-.207-.257-.363-.556-.467-.896s-.155-.7-.155-1.08c0-.329.042-.666.128-1.01.086-.343.229-.658.43-.945.2-.286.465-.521.795-.703.329-.183.734-.274
 1.214-.274.35 0
 .673.077.966.231.294.154.523.385.688.693h.01v-.795h.87v5.08c0
 .909-.217 1.584-.629 2.046m-.375-3.689c.061-.258.091-.516.091-.774
 0-.243-.028-.483-.085-.719-.058-.237-.149-.45-.274-.639-.126-.19-.289-.342-.489-.457-.201-.114-.444-.172-.73-.172-.294
 0-.545.056-.752.167-.208.111-.378.259-.51.446-.133.186-.23.401-.291.644-.06.244-.091.498-.091.763
 0
 .25.025.501.075.751.05.251.136.479.258.683s.283.368.484.494c.2.125.451.188.751.188.301
 0
 .557-.063.768-.188.211-.126.382-.29.511-.494.128-.204.223-.435.284-.693m.798
 4.213c.604.072 1.095.095 1.738.095 2.704 0 5.128-.607
 6.746-1.673-1.771 1.785-4.93 3.044-8.537 3.043-.933
 0-1.836-.079-2.693-.228 1.28-.214 2.22-.76
 2.746-1.237m5.554-2.082h-1.311v-4.415h-1.644V9.194h4.599v1.123h-1.644zm3.637
 0h-1.31V9.194h4.046v1.123h-2.736v1.036h2.395v1.123h-2.395zm-8.222-6.917h.913v6.902h-.913z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.khronos.org/files/legal/Khronos-L'''
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
