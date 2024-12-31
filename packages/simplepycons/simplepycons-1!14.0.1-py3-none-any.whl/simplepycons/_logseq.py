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


class LogseqIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "logseq"

    @property
    def original_file_name(self) -> "str":
        return "logseq.svg"

    @property
    def title(self) -> "str":
        return "Logseq"

    @property
    def primary_color(self) -> "str":
        return "#85C8C8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Logseq</title>
     <path d="M19.3
 9.838c-2.677-1.366-5.467-1.56-8.316-.607-1.738.58-3.197 1.58-4.267
 3.088-1.031 1.452-1.45 3.071-1.184 4.837.268 1.781 1.164 3.228 2.505
 4.4C9.96 23.231 12.24 23.942 15.092 24c.41-.053 1.157-.103 1.883-.255
 2.004-.418 3.754-1.325 5.08-2.915 1.621-1.942 2.108-4.148
 1.272-6.562-.704-2.034-2.138-3.467-4.027-4.43ZM7.515
 6.295c.507-2.162-.88-4.664-2.988-5.37-1.106-.37-2.156-.267-3.075.492C.61
 2.114.294 3.064.271
 4.146c.009.135.016.285.029.435.01.102.021.205.042.305.351 1.703 1.262
 2.98 2.9 3.636 1.912.766 3.808-.244
 4.273-2.227Zm4.064-1.146c1.075.377 2.152.31 3.22-.033.94-.3
 1.755-.793
 2.341-1.609.803-1.117.5-2.387-.717-3.027-.6-.317-1.246-.438-1.927-.48-.47.076-.95.117-1.41.234-1.068.27-2.002.781-2.653
 1.7-.495.697-.64 1.45-.174 2.227.303.504.779.799 1.32.988Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/logseq/logseq/blob/c4d15ec'''

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
