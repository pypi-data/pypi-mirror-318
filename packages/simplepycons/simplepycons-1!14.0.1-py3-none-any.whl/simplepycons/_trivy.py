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


class TrivyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "trivy"

    @property
    def original_file_name(self) -> "str":
        return "trivy.svg"

    @property
    def title(self) -> "str":
        return "Trivy"

    @property
    def primary_color(self) -> "str":
        return "#1904DA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Trivy</title>
     <path d="M4.375 7.311 1.962 5.918a.1.1 0 0 1
 0-.174L11.828.047a.343.343 0 0 1 .344 0l9.864 5.696a.1.1 0 0 1 0
 .175L19.624 7.31a.962.962 0 0
 1-.052-.074c-.914-1.478-2.124-2.592-3.596-3.31-4.088-1.994-9.164-.505-11.6
 3.385ZM12.262 23.899v-3.14c5.693-2.087 9.01-7.766
 7.588-12.985l2.436-1.42a.1.1 0 0 1 .151.088v11.645a.1.1 0 0
 1-.05.087l-9.973 5.812a.1.1 0 0 1-.152-.087Zm-.559-3.141v3.14a.1.1 0
 0 1-.151.086l-9.933-5.81a.114.114 0 0 1-.056-.099V6.436a.1.1 0 0 1
 .15-.087l2.44 1.41c-1.455 5.307 1.846 10.993 7.55 13ZM7.013 8.834
 4.807 7.561c2.306-3.665 7.094-5.066 10.95-3.186 1.385.676 2.526 1.727
 3.39 3.124l.04.062-2.195 1.268a5.57 5.57 0 0
 0-2.429-2.307c-2.603-1.27-5.901-.253-7.552 2.311Zm9.337
 5.2c.813-1.371 1.088-2.99.798-4.685l2.255-1.314c1.245 4.86-1.864
 10.169-7.14 12.192v-3.072c1.86-.67 3.272-1.747 4.087-3.12ZM4.6
 8.018l2.27 1.31c-.225 1.571.112 3.204.951 4.606.919 1.536 2.225 2.629
 3.881 3.25v3.045C6.327 18.25 3.297 13.042 4.601 8.017Zm5.303
 2.486-2.459-1.42c1.52-2.34 4.53-3.268 6.9-2.112a5.075 5.075 0 0 1
 2.216 2.108l-2.471 1.427a2.311 2.311 0 0 0-2.03-1.195c-.825
 0-1.645.43-2.156 1.192Zm4.338.522 2.443-1.408c.22 1.51-.043
 2.945-.765 4.162-.735 1.238-1.998 2.224-3.658 2.856v-2.631c1.25-.691
 1.968-1.771 1.98-2.979ZM8.25 13.676A6.576 6.576 0 0 1 7.34 9.6l2.446
 1.412c-.016 1.271.73 2.437 1.917 2.997v2.624a6.977 6.977 0 0
 1-3.453-2.956Zm3.853-.148-.137.073-.157-.075c-1.023-.504-1.524-1.606-1.557-2.417a1.99
 1.99 0 0 1 .004-.23 2.153 2.153 0 0 1 1.163-.957c.508-.178 1.034-.153
 1.444.071.6.327.84.797.86.86.008.156.004.253.004.256-.038.981-.63
 1.863-1.624 2.419Z" />
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
