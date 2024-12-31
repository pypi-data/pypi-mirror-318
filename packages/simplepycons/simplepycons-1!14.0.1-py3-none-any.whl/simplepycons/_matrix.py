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


class MatrixIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "matrix"

    @property
    def original_file_name(self) -> "str":
        return "matrix.svg"

    @property
    def title(self) -> "str":
        return "Matrix"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Matrix</title>
     <path d="M.632.55v22.9H2.28V24H0V0h2.28v.55zm7.043
 7.26v1.157h.033c.309-.443.683-.784 1.117-1.024.433-.245.936-.365
 1.5-.365.54 0 1.033.107 1.481.314.448.208.785.582 1.02
 1.108.254-.374.6-.706 1.034-.992.434-.287.95-.43 1.546-.43.453 0
 .872.056
 1.26.167.388.11.716.286.993.53.276.245.489.559.646.951.152.392.23.863.23
 1.417v5.728h-2.349V11.52c0-.286-.01-.559-.032-.812a1.755 1.755 0 0
 0-.18-.66 1.106 1.106 0 0
 0-.438-.448c-.194-.11-.457-.166-.785-.166-.332 0-.6.064-.803.189a1.38
 1.38 0 0 0-.48.499 1.946 1.946 0 0 0-.231.696 5.56 5.56 0 0
 0-.06.785v4.768h-2.35v-4.8c0-.254-.004-.503-.018-.752a2.074 2.074 0 0
 0-.143-.688 1.052 1.052 0 0
 0-.415-.503c-.194-.125-.476-.19-.854-.19-.111
 0-.259.024-.439.074-.18.051-.36.143-.53.282-.171.138-.319.337-.439.595-.12.259-.18.6-.18
 1.02v4.966H5.46V7.81zm15.693 15.64V.55H21.72V0H24v24h-2.28v-.55z" />
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
