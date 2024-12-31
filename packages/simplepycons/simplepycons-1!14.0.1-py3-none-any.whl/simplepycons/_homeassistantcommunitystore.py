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


class HomeAssistantCommunityStoreIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "homeassistantcommunitystore"

    @property
    def original_file_name(self) -> "str":
        return "homeassistantcommunitystore.svg"

    @property
    def title(self) -> "str":
        return "Home Assistant Community Store"

    @property
    def primary_color(self) -> "str":
        return "#41BDF5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Home Assistant Community Store</title>
     <path d="M1.63.47a.393.393 0 0 0-.39.39v2.417c0
 .212.177.39.39.39h20.74c.213 0 .39-.178.39-.39V.859a.393.393 0 0
 0-.39-.39zm-.045 4.126a.41.41 0 0 0-.407.337l-1.17 6.314C0 11.274 0
 11.3 0 11.327v2.117c0 .23.186.416.416.416h23.168c.23 0
 .416-.186.416-.416v-2.126c0-.027 0-.053-.009-.08l-1.169-6.305a.41.41
 0 0 0-.407-.337zM1.7 14.781a.457.457 0 0 0-.46.46v7.829c0
 .257.203.46.46.46h14.108c.257 0
 .46-.203.46-.46v-6.589c0-.257.204-.46.461-.46h4.02c.258 0
 .461.203.461.46v6.589c0 .257.204.46.46.46h.62a.456.456 0 0 0
 .461-.46v-7.829a.458.458 0 0 0-.46-.46zm1.842 1.55h7.847c.212 0
 .39.177.39.39V21.6c0 .212-.178.39-.39.39H3.542a.393.393 0 0
 1-.39-.39v-4.88c0-.221.178-.39.39-.39Z" />
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
