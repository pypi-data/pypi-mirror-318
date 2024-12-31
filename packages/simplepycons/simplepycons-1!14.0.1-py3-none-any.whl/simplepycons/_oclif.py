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


class OclifIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "oclif"

    @property
    def original_file_name(self) -> "str":
        return "oclif.svg"

    @property
    def title(self) -> "str":
        return "oclif"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>oclif</title>
     <path d="M14.887 8.804a.583.583 0 0 0-.417-.172H.585A.586.586 0 0
 0 0 9.219v5.562c0 .325.262.587.585.587H14.47a.583.583 0 0 0
 .417-.172l2.633-2.774a.607.607 0 0 0 0-.837l-2.633-2.781zm-4.38
 1.684c.07-.066.162-.1.257-.097.06.001.119.017.171.047.055.03.1.073.134.125a.31.31
 0 0 1 .05.172.306.306 0 0 1-.05.173.367.367 0 0 1-.134.124.364.364 0
 0 1-.486-.124.316.316 0 0 1-.048-.173.326.326 0 0 1 .106-.247zm-6.804
 2.86a1.102 1.102 0 0 1-1.971 0 1.424 1.424 0 0
 1-.15-.66c-.002-.221.05-.44.153-.635.095-.185.238-.342.413-.453.348-.22.792-.22
 1.14 0
 .175.111.318.268.413.453.103.195.155.414.153.635.003.23-.048.456-.151.66zm2.465-1.083c-.142-.21-.381-.357-.645-.34a.544.544
 0 0 0-.318.1.688.688 0 0 0-.234.27 1.002 1.002 0 0 0-.084.422c0
 .135.029.268.084.39a.581.581 0 0 0
 .545.356c.089-.003.152-.01.191-.02a.567.567 0 0 0 .128-.054.858.858 0
 0 0 .292-.243l.332.385a1.223 1.223 0 0 1-.948.426 1.196 1.196 0 0
 1-.617-.16 1.136 1.136 0 0 1-.428-.45 1.348 1.348 0 0
 1-.155-.645c-.002-.226.05-.448.155-.648.098-.189.246-.347.428-.458.19-.115.407-.174.628-.172.19-.001.379.04.552.12a.968.968
 0 0 1 .404.345l-.31.376zm2.858
 1.618H7.14v-.446h.655V10.87h-.619v-.453h1.2v3.02h.65v.446zm2.581
 0H9.943v-.462h.574v-1.474h-.55v-.46h1.118v1.934h.514l.008.462zm2.812-2.8a1.2
 1.2 0 0 0-.264-.194.56.56 0 0 0-.245-.052.44.44 0 0
 0-.355.141.627.627 0 0
 0-.12.417v.098h.732v.456h-.729v1.934h-.557v-1.94h-.514v-.457h.514v-.1c-.005-.192.04-.382.132-.55a.885.885
 0 0 1
 .357-.345c.153-.08.324-.121.497-.119.298-.003.585.118.792.334l-.24.377zm-11.213
 1.18c.047.136.07.279.067.423.002.144-.02.286-.067.422a.637.637 0 0
 1-.194.286.458.458 0 0 1-.297.101.446.446 0 0 1-.291-.1.635.635 0 0
 1-.195-.279 1.272 1.272 0 0
 1-.067-.43c-.003-.144.02-.287.068-.422a.613.613 0 0 1
 .192-.273.455.455 0 0 1 .295-.088.477.477 0 0 1
 .297.094c.087.07.154.16.192.266zM24 15.088a.28.28 0 0
 1-.28.28h-4.67a.28.28 0 0 1-.279-.28v-.274a.28.28 0 0 1
 .28-.28h4.671a.28.28 0 0 1 .278.28v.274z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/oclif/oclif.github.io/blob'''

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
