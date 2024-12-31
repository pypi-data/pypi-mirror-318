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


class OdyseeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "odysee"

    @property
    def original_file_name(self) -> "str":
        return "odysee.svg"

    @property
    def title(self) -> "str":
        return "Odysee"

    @property
    def primary_color(self) -> "str":
        return "#EF1970"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Odysee</title>
     <path d="M11.965 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0
 12-12 12 12 0 0 0-3.209-8.167 7.272 7.272 0 0 1-.799
 3.218c-.548.957-2.281 2.77-3.264 3.699a.723.723 0 0 0 .056
 1.104c.996.74 2.658 2.151 2.788 3.422.176 1.835 1.6 4.02 1.675
 4.159a.67.67 0 0 1-.105.327 12.067 12.067 0 0 1-2.03 1.898 2.435
 2.435 0 0
 1-.807.126c-1.944-.04-1.526-1.866-1.712-2.905s-.78-3.085-2.716-2.788c0
 0 .484 4.243-1.489 5.546s-5.843 2.27-6.55-.408 2.46-2.384
 2.684-2.384c.223 0 2.233-.632
 1.267-2.53-.967-1.898-2.01-3.5-2.01-3.5a11.37 11.37 0 0 0-2.735 1.285
 5.42 5.42 0 0 0-1.061.82c-1.065 1.104-2.19 1.713-2.954 1.358a1.368
 1.368 0 0 1-.32-.221A11.926 11.926 0 0 1 .1 13.503c.43-.641
 2.082-2.038 3.696-2.906 1.304-.702 2.737-.988
 3.118-1.355-.671-2.235-1.882-5.703.832-7.33C9.881.634 12.69-.142
 13.77 2.958c1.08 3.1.802 3.796 1.267 3.796.465 0 1.608.223
 2.09-1.75.356-1.445.574-2.685 1.379-3.087A12 12 0 0 0 12 0a12 12 0 0
 0-.035 0zm-.498 2.125c-.353-.019-.78.05-1.303.224 0 0-1.895.52-1.749
 2.53.13 1.777 1.08 2.753 3.053 2.01 1.972-.737 2.31-1.264
 1.824-2.753-.364-1.117-.765-1.956-1.825-2.011zm.48.726a.249.249 0 0 1
 .183.07 1.58 1.58 0 0 1 .232.346.253.253 0 0 1-.197.37.253.253 0 0
 1-.233-.131 1.559 1.559 0 0 0-.148-.232.256.256 0 0 1 0-.353.249.249
 0 0 1 .163-.07zm3.529.152a.22.22 0 0 1 .192.103.22.22 0 0
 1-.07.305.22.22 0 1 1-.122-.408zM12.609 4.27a.253.253 0 0 1 .227.133
 1.5 1.5 0 0 1 .102.982.253.253 0 0 1-.246.205h-.049a.253.253 0 0
 1-.2-.295 1.013 1.013 0 0 0-.071-.697.253.253 0 0 1
 .237-.328zm-8.035.552a.12.12 0 0 1 .029.003.12.12 0 1
 1-.147.091.12.12 0 0 1 .118-.094zm15.77
 3.419.273.539.593.12-.539.275-.123.592-.272-.539-.592-.123.538-.272zm-17.767.535a.22.22
 0 0 1 .193.104.22.22 0 0 1-.07.304.22.22 0 1 1-.123-.408zm16.004
 2.79a.258.258 0 0 1 .062.007.258.258 0 1 1-.31.195.258.258 0 0 1
 .248-.202zM4.914 16.115a.17.17 0 0 1 .165.14.17.17 0 0
 1-.137.197.17.17 0 1 1-.028-.337zm9.769 4.094a.2.2 0 0 1 .036.004.2.2
 0 1 1-.233.15.2.2 0 0 1 .197-.154z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://odysee.com/@OdyseeHelp:b/odyseepressk'''

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
