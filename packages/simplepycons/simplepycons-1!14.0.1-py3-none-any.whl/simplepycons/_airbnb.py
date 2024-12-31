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


class AirbnbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "airbnb"

    @property
    def original_file_name(self) -> "str":
        return "airbnb.svg"

    @property
    def title(self) -> "str":
        return "Airbnb"

    @property
    def primary_color(self) -> "str":
        return "#FF5A5F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Airbnb</title>
     <path d="M12.001
 18.275c-1.353-1.697-2.148-3.184-2.413-4.457-.263-1.027-.16-1.848.291-2.465.477-.71
 1.188-1.056 2.121-1.056s1.643.345 2.12 1.063c.446.61.558 1.432.286
 2.465-.291 1.298-1.085 2.785-2.412 4.458zm9.601 1.14c-.185
 1.246-1.034 2.28-2.2 2.783-2.253.98-4.483-.583-6.392-2.704
 3.157-3.951 3.74-7.028
 2.385-9.018-.795-1.14-1.933-1.695-3.394-1.695-2.944 0-4.563
 2.49-3.927 5.382.37 1.565 1.352 3.343 2.917 5.332-.98 1.085-1.91
 1.856-2.732
 2.333-.636.344-1.245.558-1.828.609-2.679.399-4.778-2.2-3.825-4.88.132-.345.395-.98.845-1.961l.025-.053c1.464-3.178
 3.242-6.79 5.285-10.795l.053-.132.58-1.116c.45-.822.635-1.19
 1.351-1.643.346-.21.77-.315 1.246-.315.954 0 1.698.558 2.016
 1.007.158.239.345.557.582.953l.558 1.089.08.159c2.041 4.004 3.821
 7.608 5.279 10.794l.026.025.533 1.22.318.764c.243.613.294 1.222.213
 1.858zm1.22-2.39c-.186-.583-.505-1.271-.9-2.094v-.03c-1.889-4.006-3.642-7.608-5.307-10.844l-.111-.163C15.317
 1.461 14.468 0 12.001 0c-2.44 0-3.476 1.695-4.535
 3.898l-.081.16c-1.669 3.236-3.421 6.843-5.303 10.847v.053l-.559
 1.22c-.21.504-.317.768-.345.847C-.172 20.74 2.611 24 5.98 24c.027 0
 .132 0 .265-.027h.372c1.75-.213 3.554-1.325 5.384-3.317 1.829 1.989
 3.635 3.104 5.382 3.317h.372c.133.027.239.027.265.027 3.37.003
 6.152-3.261 4.802-6.975z" />
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
