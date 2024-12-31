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


class DeepinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "deepin"

    @property
    def original_file_name(self) -> "str":
        return "deepin.svg"

    @property
    def title(self) -> "str":
        return "deepin"

    @property
    def primary_color(self) -> "str":
        return "#007CFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>deepin</title>
     <path
 d="M16.104.696c-1.724-.63-3.49-.8-5.205-.64-1.988.157-2.958.772-2.9.661-3.251
 1.16-6 3.657-7.272 7.157-2.266 6.234.944 13.128 7.168 15.398 6.228
 2.27 13.111-.945 15.378-7.179C25.54 9.86 22.33 2.966
 16.104.696zM8.305 22.145a10.767 10.767 0 0 1-1.867-.904c2.9.223
 6.686-.445 9.239-2.834 0 0 4.866-3.888 1.345-10.269 0 0 .568
 2.572-.156 4.687 0 0-.69 2.877-3.757 3.712-4.517
 1.231-9.664-1.93-11.816-3.463-.162-1.574-.018-3.2.56-4.788.855-2.352
 2.463-4.188 4.427-5.42-.49 3.436-.102 6.6.456 7.925.749 1.777 2.05
 3.85 4.59 4.115 2.54.267 3.94-2.11 3.94-2.11 1.304-1.98 1.508-4.823
 1.488-4.892-.02-.07-.347-.257-.347-.257-.877 3.549-2.323 4.734-2.323
 4.734-2.28
 2.201-3.895.675-3.895.675-1.736-1.865-.52-4.895-.52-4.895.68-2.064
 2.66-5.084 4.905-6.62.374.092.75.15 1.12.284a10.712 10.712 0 0 1
 3.554 2.16c-1.641.599-4.291 1.865-4.291 1.865-4.201 1.77-4.485
 4.446-4.485 4.446-.435 2.758 1.754 1.59 1.754 1.59 2.252-1.097
 3.359-4.516 3.359-4.516-.703-.134-1.257.08-1.257.08-.899 2.22-2.733
 3.132-2.733
 3.132-.722.382-.89-.293-.89-.293-.122-.506.522-.592.522-.592 1-.389
 1.639-1.439 1.784-1.868.144-.43.412-.464.412-.464a12.998 12.998 0 0 1
 2.619-.535c1.7-.209 4.303.602 4.303.602.584.235 1.144.41
 1.641.551.954 2.384 1.105 5.098.16 7.7-2.039 5.61-8.236 8.504-13.841
 6.462z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Deepi'''

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
