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


class ZdfIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zdf"

    @property
    def original_file_name(self) -> "str":
        return "zdf.svg"

    @property
    def title(self) -> "str":
        return "ZDF"

    @property
    def primary_color(self) -> "str":
        return "#FA7D19"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ZDF</title>
     <path d="M7.014 4.987A7.02 7.02 0 000 12.005a7.017 7.017 0
 0013.271 3.174h2.915c.696 0 1.324-.044
 1.962-.553.461-.365.749-.884.883-1.56v2.103h1.336v-2.473h3.153v-1.1h-3.16l.02-.445c.005-.724.226-1.162
 1.277-1.162H24V8.876h-2.818c-1.517 0-2.141.85-2.141
 2.18v.129c-.254-1.565-1.185-2.31-2.889-2.31h-2.855a7.018 7.018 0
 00-6.283-3.888zM8.02 8.876h3.436c1.742 0 1.992 1.219 1.992 1.9 0
 .725-.298 1.873-1.992 1.873h-.844c-1.056 0-1.281.38-1.281
 1.104v.336h3.945v1.074H7.982v-1.558c0-1.335.625-2.123
 2.137-2.123h.873c.691 0 1.1-.14 1.1-.725
 0-.605-.409-.772-1.12-.772h-2.95v-1.11zm6.63 1.113h1.472c1.157 0
 1.574.496 1.574 2.04 0 1.542-.412 2.036-1.574 2.036H14.65z" />
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
