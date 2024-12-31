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


class SphereOnlineJudgeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "spoj"

    @property
    def original_file_name(self) -> "str":
        return "spoj.svg"

    @property
    def title(self) -> "str":
        return "Sphere Online Judge"

    @property
    def primary_color(self) -> "str":
        return "#337AB7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sphere Online Judge</title>
     <path d="M11.143.056c-.522.127-.713.219-2.28
 1.114-.88.506-1.68.957-1.76
 1.008-.202.113-.417.236-.59.337-.587.337-3.293 1.893-3.453
 1.973-1.05.581-1.72 1.453-2.013 2.587-.084.34-.084 9.532 0 9.865.282
 1.131.957 2 2.013 2.587.152.084 2.866 1.64 3.453
 1.973.173.102.388.224.59.337.085.051.882.507 1.774 1.012C10.89 24.005
 10.89 24 12.01 24c1.11 0 1.125-.004 3-1.076.818-.468 1.546-.885
 1.626-.928.072-.047.203-.119.283-.164l.295-.17c.08-.046.21-.118.286-.163.582-.337
 3.293-1.893 3.44-1.973 1.05-.582 1.72-1.454
 2.013-2.587.084-.341.084-9.532
 0-9.866-.282-1.13-.957-2-2.013-2.586a860.394 860.394 0 0
 1-3.726-2.137l-.295-.17c-.08-.046-.21-.118-.283-.164-.076-.042-.809-.46-1.626-.928C13.183.047
 13.117.022 12.09.004c-.51-.013-.763.004-.95.051zm3.014 4.32c.838.156
 2.493.759 2.493.91 0 .03-.207.62-.46 1.313-.384 1.058-.472 1.26-.536
 1.251-.047 0-.3-.1-.566-.218-.92-.4-1.48-.515-2.546-.51-1.19
 0-1.773.21-2.027.732-.088.186-.109.287-.109.548 0
 .414.093.616.421.924.304.279.734.502 1.507.788 2.44.899 3.346 1.36
 4.026 2.093.759.806 1.04 1.707.995 3.187-.021.83-.101 1.172-.41
 1.786-.64 1.291-1.92 2.04-3.906
 2.28-.472.059-.813.067-1.706.051-1.135-.021-1.494-.059-2.347-.244-.801-.173-2.16-.696-2.226-.852-.018-.05.838-2.586.893-2.64.01-.008.212.072.452.182
 1.16.518 2.04.7 3.4.704 1.07 0 1.626-.131
 2.026-.494.275-.244.355-.434.374-.894.017-.371.013-.406-.114-.663a1.533
 1.533 0 0
 0-.354-.464c-.304-.265-1.232-.717-2.187-1.055-.953-.34-1.36-.51-1.893-.776-1.176-.594-1.947-1.453-2.253-2.52-.088-.294-.096-.417-.094-1.171
 0-.798.01-.864.12-1.223.35-1.142 1.032-1.946 2.12-2.506a6.482 6.482 0
 0 1 1.613-.523c.218-.039.446-.076.507-.084a21.5 21.5 0 0 1
 1.2-.005c.881.013 1.19.03 1.573.101z" />
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
            "SPOJ",
        ]
