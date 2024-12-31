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


class StimulusIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "stimulus"

    @property
    def original_file_name(self) -> "str":
        return "stimulus.svg"

    @property
    def title(self) -> "str":
        return "Stimulus"

    @property
    def primary_color(self) -> "str":
        return "#77E8B9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Stimulus</title>
     <path d="M.704 0A.704.704 0 000 .704v2.824h5.648a3.064 3.064 0
 011.312.36l3.232 1.9a.4.4 0 010 .712l-1.536.904a1.308 1.308 0 01-1.2
 0l-1.2-.7a3.084 3.084 0 00-1.316-.36H0v4.236h4.94a3.028 3.028 0
 001.316-.36l10.8-6.344a3.008 3.008 0 011.312-.36H24V.692A.704.704 0
 0023.296 0zM19.06 6.352a3.084 3.084 0 00-1.316.36l-10.8 6.348a3.064
 3.064 0 01-1.312.36H0v4.236h4.94a3.084 3.084 0
 001.316-.36l10.8-6.348a3.064 3.064 0 011.312-.36H24V6.352h-3.376zm0
 7.072a3.084 3.084 0 00-1.316.36l-10.8 6.344a3.008 3.008 0
 01-1.312.36H0v2.824A.708.708 0 00.704 24h22.592a.708.708 0
 00.704-.7v-2.824h-5.648a3.008 3.008 0 01-1.312-.36l-3.232-1.896a.4.4
 0 010-.716l1.536-.9a1.308 1.308 0 011.2 0l1.2.696a3.028 3.028 0
 001.316.36H24v-4.236h-3.376z" />
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
