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


class GoogleCalendarIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlecalendar"

    @property
    def original_file_name(self) -> "str":
        return "googlecalendar.svg"

    @property
    def title(self) -> "str":
        return "Google Calendar"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Calendar</title>
     <path d="M18.316 5.684H24v12.632h-5.684V5.684zM5.684
 24h12.632v-5.684H5.684V24zM18.316 5.684V0H1.895A1.894 1.894 0 0 0 0
 1.895v16.421h5.684V5.684h12.632zm-7.207
 6.25v-.065c.272-.144.5-.349.687-.617s.279-.595.279-.982c0-.379-.099-.72-.3-1.025a2.05
 2.05 0 0 0-.832-.714 2.703 2.703 0 0 0-1.197-.257c-.6
 0-1.094.156-1.481.467-.386.311-.65.671-.793
 1.078l1.085.452c.086-.249.224-.461.413-.633.189-.172.445-.257.767-.257.33
 0 .602.088.816.264a.86.86 0 0 1 .322.703c0
 .33-.12.589-.36.778-.24.19-.535.284-.886.284h-.567v1.085h.633c.407 0
 .748.109 1.02.327.272.218.407.499.407.843 0
 .336-.129.614-.387.832s-.565.327-.924.327c-.351
 0-.651-.103-.897-.311-.248-.208-.422-.502-.521-.881l-1.096.452c.178.616.505
 1.082.977 1.401.472.319.984.478 1.538.477a2.84 2.84 0 0 0
 1.293-.291c.382-.193.684-.458.902-.794.218-.336.327-.72.327-1.149
 0-.429-.115-.797-.344-1.105a2.067 2.067 0 0
 0-.881-.689zm2.093-1.931l.602.913L15
 10.045v5.744h1.187V8.446h-.827l-2.158 1.557zM22.105
 0h-3.289v5.184H24V1.895A1.894 1.894 0 0 0 22.105 0zm-3.289
 23.5l4.684-4.684h-4.684V23.5zM0 22.105C0 23.152.848 24 1.895
 24h3.289v-5.184H0v3.289z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://fonts.gstatic.com/s/i/productlogos/ca'''

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
