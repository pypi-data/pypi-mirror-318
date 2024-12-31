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


class MariadbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mariadb"

    @property
    def original_file_name(self) -> "str":
        return "mariadb.svg"

    @property
    def title(self) -> "str":
        return "MariaDB"

    @property
    def primary_color(self) -> "str":
        return "#003545"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MariaDB</title>
     <path d="M23.157
 4.412c-.676.284-.79.31-1.673.372-.65.045-.757.057-1.212.209-.75.246-1.395.75-2.02
 1.59-.296.398-1.249 1.913-1.249 1.988 0 .057-.65.998-.915
 1.32-.574.713-1.08 1.079-2.14 1.59-.77.36-1.224.524-4.102
 1.477-1.073.353-2.133.738-2.367.864-.852.449-1.515 1.036-2.203
 1.938-1.003 1.32-.972 1.313-3.042.947a12.264 12.264 0
 00-.675-.063c-.644-.05-1.023.044-1.332.334L0
 17.193l.177.088c.094.05.353.234.561.398.215.17.461.347.55.391.088.044.17.088.183.101.012.013-.089.17-.228.353-.435.581-.593.871-.574
 1.048.019.164.032.17.43.17.517-.006.826-.056 1.261-.208.65-.233
 2.058-.94 2.784-1.4.776-.5 1.717-.998
 1.956-1.042.082-.02.354-.07.594-.114.58-.107 1.464-.095
 2.587.05.108.013.373.045.6.064.227.025.43.057.454.076.026.012.474.037.998.056.934.026
 1.104.007
 1.3-.189.126-.133.385-.631.498-.985.209-.643.417-.921.366-.492-.113.966-.322
 1.692-.713 2.411-.259.499-.663 1.092-.934
 1.395-.322.347-.315.36.088.315.619-.063 1.471-.397 2.096-.82.827-.562
 1.647-1.691
 2.19-3.03.107-.27.22-.22.183.083-.013.094-.038.315-.057.498l-.031.328.353-.202c.833-.48
 1.414-1.262 2.127-2.884.227-.518.877-2.922 1.073-3.976a9.64 9.64 0
 01.271-1.042c.127-.429.196-.555.48-.858.183-.19.625-.555.978-.808.72-.505.953-.75
 1.187-1.205.208-.417.284-1.13.132-1.357-.132-.202-.284-.196-.763.006Z"
 />
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
