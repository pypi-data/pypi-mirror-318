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


class MuiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mui"

    @property
    def original_file_name(self) -> "str":
        return "mui.svg"

    @property
    def title(self) -> "str":
        return "MUI"

    @property
    def primary_color(self) -> "str":
        return "#007FFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MUI</title>
     <path d="M20.229 15.793a.666.666 0 0 0 .244-.243.666.666 0 0 0
 .09-.333l.012-3.858a.666.666 0 0 1 .09-.333.666.666 0 0 1
 .245-.243L23 9.58a.667.667 0 0 1 .333-.088.667.667 0 0 1
 .333.09.667.667 0 0 1 .244.243.666.666 0 0 1 .089.333v7.014a.667.667
 0 0 1-.335.578l-7.893 4.534a.666.666 0 0 1-.662
 0l-6.194-3.542a.667.667 0 0 1-.246-.244.667.667 0 0
 1-.09-.335v-3.537c0-.004.004-.006.008-.004s.008 0
 .008-.005v-.004c0-.003.002-.005.004-.007l5.102-2.93c.004-.003.002-.01-.003-.01a.005.005
 0 0 1-.004-.002.005.005 0 0 1-.001-.004l.01-3.467a.667.667 0 0
 0-.333-.58.667.667 0 0 0-.667 0L8.912 9.799a.667.667 0 0 1-.665
 0l-3.804-2.19a.667.667 0 0 0-.999.577v6.267a.667.667 0 0
 1-.332.577.666.666 0 0 1-.332.09.667.667 0 0 1-.333-.088L.336
 13.825a.667.667 0 0 1-.246-.244.667.667 0 0 1-.09-.336L.019
 2.292a.667.667 0 0 1 .998-.577l7.23 4.153a.667.667 0 0 0 .665
 0l7.228-4.153a.666.666 0 0 1 .333-.088.666.666 0 0 1 .333.09.667.667
 0 0 1 .244.244.667.667 0 0 1 .088.333V13.25c0
 .117-.03.232-.089.334a.667.667 0 0 1-.245.244l-3.785 2.18a.667.667 0
 0 0-.245.245.666.666 0 0 0-.089.334.667.667 0 0 0 .09.334.666.666 0 0
 0 .247.244l2.088 1.189a.67.67 0 0 0 .33.087.667.667 0 0 0
 .332-.089l4.457-2.56Zm.438-9.828a.666.666 0 0 0 .09.335.666.666 0 0 0
 .248.244.667.667 0 0 0 .67-.008l2.001-1.2a.666.666 0 0 0
 .237-.243.667.667 0 0 0 .087-.329V2.32a.667.667 0 0
 0-.091-.335.667.667 0 0 0-.584-.33.667.667 0 0 0-.334.094l-2
 1.2a.666.666 0 0 0-.238.243.668.668 0 0 0-.086.329v2.445Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/mui-org/material-ui/blob/3'''

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
            "Material-UI",
        ]
