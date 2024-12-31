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


class GithubSponsorsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "githubsponsors"

    @property
    def original_file_name(self) -> "str":
        return "githubsponsors.svg"

    @property
    def title(self) -> "str":
        return "GitHub Sponsors"

    @property
    def primary_color(self) -> "str":
        return "#EA4AAA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GitHub Sponsors</title>
     <path d="M17.625 1.499c-2.32 0-4.354 1.203-5.625
 3.03-1.271-1.827-3.305-3.03-5.625-3.03C3.129 1.499 0 4.253 0 8.249c0
 4.275 3.068 7.847 5.828 10.227a33.14 33.14 0 0 0 5.616
 3.876l.028.017.008.003-.001.003c.163.085.342.126.521.125.179.001.358-.041.521-.125l-.001-.003.008-.003.028-.017a33.14
 33.14 0 0 0 5.616-3.876C20.932 16.096 24 12.524 24
 8.249c0-3.996-3.129-6.75-6.375-6.75zm-.919 15.275a30.766 30.766 0 0
 1-4.703 3.316l-.004-.002-.004.002a30.955 30.955 0 0
 1-4.703-3.316c-2.677-2.307-5.047-5.298-5.047-8.523 0-2.754 2.121-4.5
 4.125-4.5 2.06 0 3.914 1.479 4.544 3.684.143.495.596.797
 1.086.796.49.001.943-.302 1.085-.796.63-2.205 2.484-3.684 4.544-3.684
 2.004 0 4.125 1.746 4.125 4.5 0 3.225-2.37 6.216-5.048 8.523z" />
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
