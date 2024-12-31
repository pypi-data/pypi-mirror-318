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


class HivemqIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hivemq"

    @property
    def original_file_name(self) -> "str":
        return "hivemq.svg"

    @property
    def title(self) -> "str":
        return "HiveMQ"

    @property
    def primary_color(self) -> "str":
        return "#FFC000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HiveMQ</title>
     <path
 d="m12,0C5.38,0,0,5.38,0,12s5.38,12,12,12,12-5.38,12-12S18.62,0,12,0Zm0,1.01c6.06,0,10.99,4.93,10.99,10.99s-4.93,10.99-10.99,10.99S1.01,18.06,1.01,12,5.94,1.01,12,1.0Zm0,.95C6.47,1.97,1.97,6.47,1.97,12s4.5,10.03,10.03,10.03,10.03-4.5,10.03-10.03S17.53,1.97,12,1.97Zm-.9,3.79c.05,0,.1.04.12.09l.23.5c.38-.12.8-.12,1.18,0l.23-.5c.03-.07.12-.11.2-.07.07.03.1.12.07.19l-.21.46v.02c.2.1.39.23.55.39.3.29.49.67.56,1.09.02.11.03.23.03.34,0,.31-.07.62-.21.9,2.77-1.25,5.03-1.6,5.57-.85.48.85-.49,1.92-2.12,3.31l-.04-.04c-.11-.11-.1-.29.01-.4.62-.58,1.98-1.96,1.2-2.36-.87-.44-3.23.17-5.85,1.56,3.73,2.16,6.26,4.74,5.66,5.78-.38.65-1.94.56-3.94-.14l.07-.12c.07-.11.2-.16.33-.12,1.39.42,2.25.62,2.55.17.42-.72-1.7-3.22-4.99-5.12-.08-.05-.17-.1-.25-.14l-.25.14c-3.29,1.9-5.41,4.39-4.99,5.12.3.45,1.16.25,2.55-.17.12-.04.26.01.33.12l.07.12c-2,.71-3.56.79-3.94.14-.6-1.04,1.94-3.62,5.66-5.78-.72-.38-1.47-.72-2.23-1.02-.73-.28-3.08-1.07-3.71-.47-.2.19-.19.54.23,1.12.32.44.78.9,1.07,1.17.11.11.12.28.01.4l-.04.04c-.6-.51-2.83-2.3-2.1-3.32.8-1.12,4.78.52,5.5.85-.48-1.01-.06-2.21.94-2.69l-.02-.04-.2-.45c-.03-.07,0-.16.07-.2.02-.01.05-.02.08-.01Zm.22.96c-.69.32-1.08,1.06-.97,1.82.69-.32,1.08-1.06.97-1.82Zm1.42,0c-.12.75.27,1.49.97,1.82.12-.75-.28-1.49-.97-1.82Zm-.7,4.58c.78.46,1.54.95,2.27,1.49.13.4.2.81.18,1.23h-4.91c-.02-.42.05-.83.18-1.23.73-.53,1.49-1.03,2.27-1.49Zm-2.31,3.57h4.63c-.11.37-.29.72-.52,1.02h-3.58c-.24-.3-.42-.65-.52-1.02Zm1.3,1.88h2.02c-.31.32-.55.61-1.01,1.44-.46-.83-.7-1.12-1.01-1.44Z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.hivemq.com/company/hivemq-brand-r'''
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
