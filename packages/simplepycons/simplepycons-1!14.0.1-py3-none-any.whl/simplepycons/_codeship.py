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


class CodeshipIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codeship"

    @property
    def original_file_name(self) -> "str":
        return "codeship.svg"

    @property
    def title(self) -> "str":
        return "Codeship"

    @property
    def primary_color(self) -> "str":
        return "#004466"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Codeship</title>
     <path d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372
 12-12S18.628 0 12 0zm0 1.334c.824 0 1.636.191 2.373.56a.53.53 0 0 1
 .294.474v1.519a15.985 15.985 0 0 0-5.334
 0V2.368c0-.2.114-.384.294-.474A5.304 5.304 0 0 1 12 1.334zm5.143
 4.595c.114.043.19.152.19.274v2.122A20.956 20.956 0 0 0 12
 6.648c-1.951.344-3.794.943-5.333
 1.677V6.203c0-.122.076-.231.19-.274a14.648 14.648 0 0 1
 5.038-.933c1.926-.024 3.725.37 5.248.933zM12 8s3.752.625 6.411
 2.482c.145.101.18.299.084.448-1.104 1.74-1.97 3.922-2.596 5.838
 1.252-1.28 2.24-2.085 4.1-2.101.9 0 1.598.202 2.185.516C20.42 20.618
 15.503 22.72 12 22.667c-4.337.02-8.32-2.702-9.914-6.723.8-.709
 1.74-1.277 3.247-1.277.92 0 1.626.212
 2.22.537-.554-1.475-1.236-2.994-2.048-4.274a.33.33 0 0 1
 .084-.448C8.248 8.625 12 8 12 8zm0 1.333c-1.333 2 0 8 0 8s1.333-6
 0-8z" />
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
