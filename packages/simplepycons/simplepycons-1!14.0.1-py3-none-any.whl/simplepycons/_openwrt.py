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


class OpenwrtIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "openwrt"

    @property
    def original_file_name(self) -> "str":
        return "openwrt.svg"

    @property
    def title(self) -> "str":
        return "OpenWrt"

    @property
    def primary_color(self) -> "str":
        return "#00B5E2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OpenWrt</title>
     <path d="m12 0c-3.906 0-7.4465 1.5949-10.006 4.1543l1.6953
 1.6953c2.1278-2.1278 5.069-3.4395 8.3105-3.4395 3.2416 0 6.1833
 1.3122 8.3105
 3.4395l1.6953-1.6953c-2.56-2.5594-6.0999-4.1543-10.006-4.1543zm0
 4.3203c-2.7091 0-5.1685 1.1138-6.9473 2.8926l1.6953
 1.6953c1.346-1.346 3.2079-2.1777 5.252-2.1777 2.0435 0 3.9053 0.83172
 5.252
 2.1777l1.6953-1.6953c-1.7782-1.7782-4.2381-2.8926-6.9473-2.8926zm-7.7285
 3.7559c-1.3295 1.6792-2.1113 3.7906-2.1113 6.084 0 5.4189 4.4216
 9.8398 9.8398 9.8398 5.4183 0 9.8398-4.4209 9.8398-9.8398
 0-2.2934-0.79833-4.4048-2.1113-6.084l-1.7129 1.7129c0.8974 1.2298
 1.4297 2.7427 1.4297 4.3711 0 4.1053-3.34 7.4473-7.4453 7.4473-4.1052
 0-7.4473-3.342-7.4473-7.4473 0-1.6284 0.53174-3.1413
 1.4297-4.3711l-1.7109-1.7129zm7.7285 0.56641c-1.5128 0-2.8928
 0.61633-3.9062 1.6133l1.6953 1.6953c1.2219-1.2195 3.2006-1.2195
 4.4219 0l1.6953-1.6953c-1.0354-1.0361-2.4416-1.6176-3.9062-1.6133zm0
 3.8887c-0.8997 0-1.6289 0.72911-1.6289 1.6289 0 0.8992 0.72921 1.6289
 1.6289 1.6289 0.8998 0 1.6289-0.72971
 1.6289-1.6289-0.0019-0.8992-0.72971-1.6277-1.6289-1.6289z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://openwrt.org/docs/guide-graphic-design'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://openwrt.org/docs/guide-graphic-design'''

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
