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


class BataIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bata"

    @property
    def original_file_name(self) -> "str":
        return "bata.svg"

    @property
    def title(self) -> "str":
        return "Bata"

    @property
    def primary_color(self) -> "str":
        return "#DD282E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bata</title>
     <path d="M17.397 13.003c.244-1.308 1.795-1.974
 2.936-1.91.436.025.82.154
 1.039.41.09-.09.18-.192.269-.282.051-.051.205-.038.346-.013.154.026.32.09.423.09.103
 0 .36-.077.603-.115.243-.039.461-.026.423.064l-.218.538-.705
 1.73c-.141.347.41.257
 1.166-.55.129.09.193.102.321.423-.654.564-1.27.961-2.128
 1.256-.77.27-1.346-.115-1.526-.756-1.102 1.025-2.628
 1.013-3.064-.141-.718.359-1.564.73-1.923.833-.282.077-.526.141-.77.141-.384
 0-.794-.346-.666-.872-.628.282-1.128.462-1.846.705-.77.27-1.218-.025-1.398-.666-1.102
 1.025-2.628
 1.013-3.064-.141-.436.205-1.025.513-1.577.73-.884.398-1.923.321-2.692-.487l.257-.397c.359.384.807.372
 1.153.051.372-.333.603-.974.436-1.513-.077-.23-.333-.41-.833-.384l.154-.41c.5-.013.897-.09
 1.115-.398.308-.449.308-1.128-.346-1.115a1.34 1.34 0 0
 0-.41.077c-.116.333-.308.73-.475 1.14-.371.95-.782 2-1.256
 2.68-.564.808-1.18.962-1.667.936-.512-.039-.91-.192-1.474-.692
 0-.218.013-.308.064-.577.218.269.898.564 1.115.243.488-.718
 1.026-2.102 1.436-3-.359.116-.705.346-1.18.68
 0-.051-.153-.18-.153-.334.77-.884 2.115-1.423 3.026-1.615 1.397-.295
 2.884.128 3.115 1.013.154.59-.538 1.14-1.192
 1.218.372.218.769.602.872
 1.077.05.23.038.487-.039.73.218-.102.487-.23.654-.307.27-1.885
 3.192-2.487
 3.987-1.59l.27-.282c.05-.051.204-.038.346-.013.153.026.32.09.423.09.102
 0 .359-.077.602-.115.244-.039.462-.026.423.064l-.91 2.269c-.205.513
 1.308-.398
 1.397-.449l.654-1.384-.666.012.115-.564h.744c.128-.166.153-.359.32-.474.218-.167.718-.077.949-.23.205-.129.359-.321.538-.629.154-.256.744-.192.628.051l-.512
 1.295h.653c.308.013.039.539-.307.539l-.539.012-.628
 1.629c-.205.5.59.025
 1.192-.32zm-6.012-1.115c-.077-.244-.282-.308-.475-.295-.436.051-.859.538-1.077.872-.346.538-.269
 1.346.295 1.192.577-.154 1.36-1.41 1.257-1.77zm9.666
 0c-.077-.244-.282-.308-.474-.295-.436.051-.86.538-1.077.872-.346.538-.27
 1.346.295 1.192.577-.154 1.359-1.41 1.256-1.77Z" />
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
