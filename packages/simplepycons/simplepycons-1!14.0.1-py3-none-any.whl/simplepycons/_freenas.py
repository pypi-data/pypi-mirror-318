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


class FreenasIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "freenas"

    @property
    def original_file_name(self) -> "str":
        return "freenas.svg"

    @property
    def title(self) -> "str":
        return "FreeNAS"

    @property
    def primary_color(self) -> "str":
        return "#343434"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FreeNAS</title>
     <path d="M19.598 2.707h.143c.06 0 .101.01.124.032a.107.107 0 0 1
 .034.083c0 .045-.017.077-.051.097a.307.307 0 0
 1-.153.029h-.098v-.241zm0
 .391h.09l.214.337h.203l-.242-.356v-.008a.29.29 0 0 0
 .161-.081.237.237 0 0 0 .059-.168.254.254 0 0 0-.03-.125.241.241 0 0
 0-.08-.082.349.349 0 0 0-.114-.045.645.645 0 0
 0-.133-.013h-.303v.879h.175v-.338m-.485-.368a.628.628 0 0 1
 .348-.367.688.688 0 0 1 .277-.053.64.64 0 0 1 .625.42.735.735 0 0 1
 .049.27.74.74 0 0 1-.049.271.642.642 0 0 1-.348.366.675.675 0 0
 1-.277.054.646.646 0 0 1-.624-.421.712.712 0 0
 1-.049-.27c0-.095.015-.185.048-.27zm.014.884a.835.835 0 0 0
 .273.179.884.884 0 0 0 .338.064c.12 0 .233-.021.339-.064A.83.83 0 0 0
 20.598 3a.852.852 0 0 0-.249-.613.815.815 0 0
 0-.272-.179c-.105-.043-.218-.064-.339-.064s-.233.021-.338.064a.82.82
 0 0 0-.454.45.838.838 0 0 0-.067.342c0 .125.021.239.067.343a.796.796
 0 0 0 .181.271m-1.864 12.361a3.268 3.268 0 0 1-.931 1.215 3.203 3.203
 0 0 1-2.008.695 3.199 3.199 0 0 1-2.423-1.085 1.989 1.989 0 0
 1-.439-.855 2.223 2.223 0 0
 1-.06-.519c.002-.854.428-1.71.845-2.362.21-.326.418-.602.575-.794l.208.254.036.046a7.499
 7.499 0 0 0 1.126 1.083c.766.597 1.85 1.197 3.126 1.229.012 0
 .023.003.035.004a.172.172 0 0 1 .064 0 .16.16 0 0 1
 .126.189c-.061.33-.158.628-.28.9zm6.719-7.025a5.339 5.339 0 0
 1-.821.905c-.752.664-1.936 1.343-3.649 1.435l-.505.926a.173.173 0 0
 1-.299.008l-.581-.954c-.275.051-.984.168-1.808.168-1.376-.03-1.807-.241-2.263-.532l1.538-2.072-3.297-.764
 4.136-.795c1.208-2.437 1.583-4.521 1.675-5.157-4.638.514-8.102
 1.666-10.329 2.632l-.179.079-.034.014-.249-.241a9.292 9.292 0 0
 0-1.459-.985 9.404 9.404 0 0 0-4.516-1.175 8.05 8.05 0 0
 0-.894.043c-.491.031-.253.153-.194.203.225.184.544.573.753
 1.112.211.541.354 1.27.354 2.254 0
 .275-.012.579-.036.896-.195.362-.376.741-.539 1.132C.311 9.227 0
 10.479 0 11.767c0 2.291.9 4.378 2.181 6.074l.173.262-1.355
 2.7a.063.063 0 0 0 .021.08c.011.007.023.01.035.01a.067.067 0 0 0
 .047-.02l2.117-1.863.248.24a10.1 10.1 0 0 0 6.812 2.63c4.516 0
 8.342-2.953 9.652-7.032l.288-.124a6.314 6.314 0 0 0
 1.132-.555c.684-.424 1.502-1.107
 2.045-2.141.362-.687.604-1.534.604-2.576 0-.163-.006-.33-.018-.502"
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
        return '''https://github.com/freenas/webui/blob/fd668f4'''

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
