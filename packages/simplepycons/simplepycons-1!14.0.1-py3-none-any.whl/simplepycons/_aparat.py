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


class AparatIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "aparat"

    @property
    def original_file_name(self) -> "str":
        return "aparat.svg"

    @property
    def title(self) -> "str":
        return "Aparat"

    @property
    def primary_color(self) -> "str":
        return "#ED145B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Aparat</title>
     <path d="M12.0014 1.5938C2.7317 1.5906-1.9119 12.7965 4.641
 19.3515c2.975 2.976 7.4496 3.8669 11.3374 2.257 3.8877-1.61
 6.4228-5.4036 6.4228-9.6116
 0-5.7441-4.6555-10.4012-10.3997-10.4031zM6.11 6.783c.5011-2.5982
 3.8927-3.2936 5.376-1.1028 1.4834 2.1907-.4216 5.0816-3.02
 4.5822-1.6118-.3098-2.6668-1.868-2.356-3.4794zm4.322 8.9882c-.5045
 2.5971-3.8965 3.288-5.377 1.0959-1.4807-2.1922.427-5.0807
 3.0247-4.5789 1.612.3114 2.6655 1.8714 2.3524
 3.483zm1.2605-2.405c-1.1528-.2231-1.4625-1.7273-.4917-2.3877.9708-.6604
 2.256.18 2.0401 1.3343-.1347.7198-.8294 1.1924-1.5484 1.0533zm6.197
 3.8375c-.501 2.5981-3.8927 3.2935-5.376
 1.1028-1.4834-2.1908.4217-5.0817 3.0201-4.5822 1.6117.3097 2.6667
 1.8679 2.356
 3.4794zm-1.9662-5.5018c-2.5981-.501-3.2935-3.8962-1.1027-5.3795
 2.1907-1.4834 5.0816.4216 4.5822 3.02-.3082 1.6132-1.8668
 2.6701-3.4795 2.3595zm-2.3348 11.5618l2.2646.611c1.9827.5263
 4.0167-.6542 4.5433-2.6368l.639-2.4016a11.3828 11.3828 0 0 1-7.4469
 4.4274zM21.232 3.5985l-2.363-.6284a11.3757 11.3757 0 0 1 4.3538
 7.619l.6495-2.4578c.5194-1.9804-.6615-4.0076-2.6403-4.5328zM.6713
 13.8086l-.5407 2.04c-.5263 1.9826.6542 4.0166 2.6368
 4.5432l2.1066.5618a11.3792 11.3792 0 0
 1-4.2027-7.145zM10.3583.702L8.1498.1261C6.166-.4024 4.1296.7785 3.603
 2.763l-.5512 2.082A11.3757 11.3757 0 0 1 10.3583.702Z" />
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
