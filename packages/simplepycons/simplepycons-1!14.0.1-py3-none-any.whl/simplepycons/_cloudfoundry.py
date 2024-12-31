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


class CloudFoundryIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cloudfoundry"

    @property
    def original_file_name(self) -> "str":
        return "cloudfoundry.svg"

    @property
    def title(self) -> "str":
        return "Cloud Foundry"

    @property
    def primary_color(self) -> "str":
        return "#0C9ED5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cloud Foundry</title>
     <path d="M12.854 13.537c-.048 1.79.074 3.862.149 4.917.96.136
 1.633.456 1.633.83 0 .497-1.193 1.07-2.665
 1.07s-2.665-.573-2.665-1.07c0-.374.673-.694
 1.633-.83.075-1.055.197-3.127.15-4.917-.044-1.613-.779-3.091-1.676-3.821-.725-.59-1.174-1.427-1.166-2.354.016-1.765
 1.683-3.186 3.724-3.186s3.708 1.42 3.723 3.186c.008.927-.44
 1.763-1.165 2.354-.897.73-1.632 2.208-1.675 3.821zm6.214
 6.596c.287-.115.612-.177.951-.19-.007-.24-.166-.672-.303-.877-.56-.1-1.276-.313-1.658-.682a.48.48
 0 0 1-.186-.41c.026-.146.133-.253.278-.329a8.115 8.115 0 0
 0-1.08-.515 4.6 4.6 0 0
 1-1.697-.124c-.303-.09-.764-.24-.82-.549-.16-.03-.54-.083-.766-.112a4.048
 4.048 0 0 0-.07.31.815.815 0 0 0 .56.956c1 .291 1.756.77 1.974
 1.359.44 1.19-1.413 2.353-4.231 2.353-2.82
 0-4.673-1.163-4.233-2.353.213-.574.94-1.044 1.903-1.337a.863.863 0 0
 0
 .589-1.005l-.06-.283c-.291.03-.779.101-1.031.148-.019.313-.476.466-.76.564a4.65
 4.65 0 0 1-1.708.147 7.82 7.82 0 0
 0-1.052.535c.544.23.316.736-.09.97-.407.253-.842.409-1.38.51-.051.088-.111.298-.163.438-.016.136-.063.367-.053.459.645.02
 1.268.152 1.62.605.281.508-.024.976-.51 1.364.392.316.986.673
 1.45.868a4.82 4.82 0 0 1 2.715-.269c.718.16 1.506.581 1.742
 1.289.635.042 1.895.04 2.528-.041.182-.731.907-1.147
 1.606-1.326a4.803 4.803 0 0 1 2.712.193c.356-.18 1.03-.602
 1.306-.9-.474-.358-.873-.794-.63-1.325.085-.19.301-.33.547-.44zm-9.54-5.848s.418-1.586-1.4-3.632A4.99
 4.99 0 0 1 6.88 7.346a5.05 5.05 0 0 1 5.047-5.04c2.822-.065 5.168
 2.218 5.164 5.04a4.984 4.984 0 0 1-1.248 3.306c-1.614 1.616-1.4
 3.633-1.4 3.633a7.352 7.352 0 0 0
 4.956-6.898c.035-4.021-3.39-7.47-7.414-7.385-4.027-.083-7.447
 3.364-7.413 7.385a7.352 7.352 0 0 0 4.956 6.898z" />
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
