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


class FreelancermapIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "freelancermap"

    @property
    def original_file_name(self) -> "str":
        return "freelancermap.svg"

    @property
    def title(self) -> "str":
        return "freelancermap"

    @property
    def primary_color(self) -> "str":
        return "#00CFD6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>freelancermap</title>
     <path d="M12 0C5.3723 0 0 5.3723 0 12s5.3723 12 12
 12l-.0115-1.3962H12c5.857 0 10.6038-4.7469
 10.6038-10.6038H24c0-6.6277-5.3723-12-12-12m0 21.2054c-5.0838
 0-9.2054-4.1216-9.2054-9.2054S6.9162 2.7923 12 2.7923s9.2054 4.1215
 9.2054 9.2054S17.0838 21.203 12
 21.203zm6.3254-4.597c3.577-5.0492.173-10.2115-2.8639-11.6146-3.6092.5747-6.8607
 3.9254-7.2323 7.9108 2.8177 4.8162 8.5039 4.223 10.0985
 3.7039m-9.9115-1.4493c.2653 1.6362.7246 3.247 1.703 4.4377
 3.4246.8839 6.45-.7823 7.9431-2.6423-3.15
 1.463-6.6623.623-9.6438-1.7954M4.7054 9.0715c-1.897 4.9939 1.3246
 9.1431 4.6754
 10.3039-1.0754-1.3108-1.8531-3.1639-2.0516-4.9985-1.4307-1.4307-2.4115-3.2492-2.6261-5.3054M14.31
 4.53c-3.09-1.0062-6.0508.1915-7.7423 1.7954.0438 2.0746.3761
 3.6946.9092 5.07.7316-3.48 3.5516-6.3416 6.8331-6.863" />
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
