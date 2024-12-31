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


class InfluxdbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "influxdb"

    @property
    def original_file_name(self) -> "str":
        return "influxdb.svg"

    @property
    def title(self) -> "str":
        return "InfluxDB"

    @property
    def primary_color(self) -> "str":
        return "#22ADF6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>InfluxDB</title>
     <path d="M23.778
 14.482l-2.287-9.959c-.13-.545-.624-1.09-1.169-1.248L9.87.051C9.74 0
 9.584 0 9.426 0c-.443 0-.909.18-1.222.443L.716 7.412C.3 7.776.092
 8.504.222 9.024l2.445 10.662c.13.545.624 1.092 1.169 1.248l9.775
 3.015c.13.051.285.051.443.051.443 0 .91-.18
 1.223-.443l8.007-7.435c.418-.39.624-1.092.494-1.64zM10.962
 2.417l7.175 2.21c.285.08.285.21 0
 .286l-3.77.858c-.285.08-.674-.05-.883-.26l-2.626-2.834c-.235-.232-.184-.336.104-.26zm4.47
 12.872c.079.286-.105.444-.39.365l-7.748-2.392c-.285-.079-.338-.313-.13-.52l5.93-5.514c.209-.209.443-.13.52.156zM2.667
 8.267l6.293-5.85c.21-.209.545-.18.754.025L12.86
 5.85c.209.21.18.545-.026.754l-6.293
 5.85c-.21.21-.545.181-.754-.025L2.64 9.024a.536.536 0
 01.026-.757zm1.536 9.284L2.54 10.244c-.08-.285.05-.34.234-.13L5.4
 12.949c.209.209.285.624.209.909L4.462 17.55c-.079.285-.208.285-.26
 0zm9.202 4.264l-8.217-2.522a.547.547 0
 01-.364-.675l1.378-4.421a.547.547 0 01.675-.365l8.216
 2.522c.285.079.443.39.364.675L14.08 21.45a.553.553 0
 01-.674.365zm7.279-5.98L15.2
 20.93c-.209.209-.31.13-.234-.155l1.144-3.694c.079-.285.39-.573.674-.624l3.77-.858c.288-.076.339.054.13.234zm.598-1.09l-4.523
 1.039a.534.534 0 01-.65-.39l-1.922-8.372a.534.534 0 01.39-.65L19.1
 5.335a.534.534 0 01.649.39l1.923 8.371c.079.31-.102.596-.39.65Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://influxdata.github.io/branding/logo/us'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://influxdata.github.io/branding/logo/do'''

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
