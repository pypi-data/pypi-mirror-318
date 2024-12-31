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


class ArchiveOfOurOwnIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "archiveofourown"

    @property
    def original_file_name(self) -> "str":
        return "archiveofourown.svg"

    @property
    def title(self) -> "str":
        return "Archive of Our Own"

    @property
    def primary_color(self) -> "str":
        return "#990000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Archive of Our Own</title>
     <path d="M18.417 9.883c-.687 1.116-1.823 1.722-2.99
 1.855-4.227.484-6.047-4.149-3.469-6.728 2.31-2.31 7.082-.9 7.005
 2.899-.011.611-.166 1.357-.546 1.974zm-6.459-2.029c.142 3.596 4.764
 3.682 5.687 1.054.815-2.324-1.12-4.199-3.19-3.897-1.523.221-2.553
 1.411-2.497 2.843zM23.123
 6.003c.284-.131.697-.412.837-.246.211.251-.459.475-.748.664-.918.6-1.731
 1.227-2.477 2.049-.959 1.059-1.944 2.376-2.55 3.818.618.032 3.021.157
 3.6 1.481.464 1.062-.387 2.156-1.32 2.627.663.414 1.81.945 1.745
 1.898-.158 2.343-3.696
 2.241-5.178.695-.244-.289-.358-.482-.25-.578.151-.134.326.186.676.476.225.187.377.251.572.354
 1.301.683 3.339.403
 3.478-.792.064-.554-.664-.955-1.217-1.204-.498-.224-1.514-.386-1.494-.952.02-.554.524-.45
 1.03-.65.55-.217 1.004-.901
 1.003-1.116-.005-.905-2.062-.888-3.221-.92-.275.606-.471 1.226-.692
 2.158-.139.583-.151 1.897-.748
 2.029-.737.164-1.014-.477-1.455-.991-.594-.69-1.436-1.637-1.942-2.223-3.033
 1.002-5.392 2.091-8.256 3.712-1.311.742-2.063 1.59-2.545
 1.354-.396-.194-.339-.633-.147-.887.393-.521.927-1.225
 1.396-1.888.6-.849 1.054-1.667 1.373-2.445.692-1.688 1.23-4.72
 1.475-5.859.088-.412.309-.348.322-.148.027.419-.237 2.047-.29
 2.383-.436 2.781-.772 4.41-2.009 6.349 2.196-1.358 4.805-3.019
 7.592-3.955C8.846 9.936 5.847 6.85 1.676 4.905 1.037 4.542 0 4.464 0
 4.22c0-.271.781-.06 1.043.007 2.383.596 4.817 2.141 6.601 3.444 2.145
 1.567 4.714 3.967 5.679 5.081.657-.226 2.286-.457 3.696-.496.752-1.58
 2.55-4.018 4.788-5.442.413-.263.842-.594 1.316-.811zm-8.594
 8.071c.423.428.742.934 1.11
 1.398.174-.59.405-1.216.643-1.758-.619.082-1.281.203-1.753.36z" />
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
