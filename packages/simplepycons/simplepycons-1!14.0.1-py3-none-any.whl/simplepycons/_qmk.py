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


class QmkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qmk"

    @property
    def original_file_name(self) -> "str":
        return "qmk.svg"

    @property
    def title(self) -> "str":
        return "QMK"

    @property
    def primary_color(self) -> "str":
        return "#333333"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>QMK</title>
     <path d="M6.78 0a.33.33 0 0 1
 .33.33v2.127h1.453V.331c0-.16.114-.293.264-.324L8.894 0h.661a.33.33 0
 0 1 .331.33v2.127h1.452V.331c0-.16.114-.293.265-.324L11.669
 0h.662a.33.33 0 0 1
 .33.33v2.127h1.452V.331c0-.16.114-.293.265-.324L14.445 0h.661a.33.33
 0 0 1 .331.33l-.001 2.127h1.453V.331c0-.16.114-.293.264-.324L17.22
 0h.662a.33.33 0 0 1 .33.33v2.127h.468a2.864 2.864 0 0 1 2.863
 2.863l-.001.467h2.127c.16 0 .293.114.324.265l.007.067v.661a.33.33 0 0
 1-.33.33h-2.128v1.453h2.127c.16 0
 .293.114.324.264l.007.067v.661a.33.33 0 0
 1-.33.331h-2.128v1.452h2.127c.16 0
 .293.114.324.265l.007.066v.662a.33.33 0 0
 1-.33.33h-2.128v1.452h2.127c.16 0
 .293.114.324.265l.007.067v.661a.33.33 0 0
 1-.33.331l-2.128-.001v1.453h2.127c.16 0
 .293.114.324.264l.007.067v.662a.33.33 0 0 1-.33.33h-2.128v.468a2.864
 2.864 0 0 1-2.862 2.863l-.468-.001v2.127a.33.33 0 0
 1-.264.324l-.066.007h-.662a.33.33 0 0
 1-.33-.33l-.001-2.128h-1.453l.001 2.127c0
 .16-.114.293-.264.324l-.067.007h-.661a.331.331 0 0
 1-.331-.33l-.001-2.128h-1.452v2.127a.33.33 0 0
 1-.264.324l-.066.007h-.662a.33.33 0 0
 1-.33-.33l-.001-2.128H9.886v2.127a.33.33 0 0 1-.264.324L9.555
 24h-.661a.331.331 0 0 1-.331-.33v-2.128H7.11v2.127a.33.33 0 0
 1-.33.331h-.662a.331.331 0 0 1-.33-.33l-.001-2.128H5.32a2.864 2.864 0
 0 1-2.863-2.862v-.468H.331a.331.331 0 0 1-.324-.264L0
 17.882v-.662a.33.33 0 0 1
 .33-.33l2.127-.001v-1.453l-2.126.001a.331.331 0 0 1-.324-.264L0
 15.106v-.661a.33.33 0 0 1 .33-.331l2.127-.001v-1.452H.331a.331.331 0
 0 1-.324-.264L0 12.331v-.662a.33.33 0 0 1
 .33-.33l2.127-.001V9.886H.331a.331.331 0 0 1-.324-.264L0
 9.555v-.661a.33.33 0 0 1 .33-.33l2.127-.001V7.11H.331a.331.331 0 0
 1-.324-.263L0 6.78v-.66a.33.33 0 0 1 .33-.331l2.127-.001V5.32A2.864
 2.864 0 0 1 5.32 2.457h.467V.331c0-.16.114-.293.265-.324L6.118
 0h.662Zm9.915 6.275c-.154 0-.278.006-.372.018a.952.952 0 0
 0-.23.053.26.26 0 0 0-.125.088.204.204 0 0 0-.035.115v4.428c0
 .472-.066.902-.2
 1.288-.132.387-.33.718-.592.992-.263.275-.592.49-.988.646-.395.157-.859.238-1.39.244V6.549a.203.203
 0 0 0-.035-.115.26.26 0 0 0-.124-.088.96.96 0 0 0-.235-.053 3.15 3.15
 0 0 0-.368-.018c-.135 0-.252.006-.35.018a1.02 1.02 0 0
 0-.238.053.292.292 0 0 0-.133.088.188.188 0 0
 0-.04.115v7.598c-.531-.012-.996-.093-1.395-.244a2.597 2.597 0 0
 1-.987-.637 2.637 2.637 0 0 1-.584-1 4.2 4.2 0 0
 1-.195-1.324V6.549a.204.204 0 0 0-.036-.115.26.26 0 0
 0-.124-.088.96.96 0 0 0-.234-.053 3.148 3.148 0 0 0-.368-.018c-.147
 0-.27.006-.367.018a.887.887 0 0 0-.23.053.293.293 0 0
 0-.124.088.188.188 0 0 0-.04.115v4.525c0 .697.106 1.314.318
 1.851.213.537.52.99.921 1.36.402.368.892.65 1.47.845.579.195
 1.237.301 1.975.319v2.116a.2.2 0 0 0 .04.124.263.263 0 0 0
 .124.084c.056.02.133.037.23.049.097.012.22.017.367.017.148 0
 .27-.005.368-.017a1.15 1.15 0 0 0
 .235-.049c.059-.02.1-.049.124-.084a.218.218 0 0 0
 .035-.124v-2.116c.726-.018 1.377-.133 1.953-.346a4.17 4.17 0 0 0
 1.47-.903c.404-.39.715-.86.934-1.412.218-.552.327-1.176.327-1.873V6.549a.189.189
 0 0 0-.04-.115.294.294 0 0 0-.124-.088.887.887 0 0 0-.23-.053 3.056
 3.056 0 0 0-.358-.018Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/qmk/qmk.fm/blob/1c3cf365e7'''

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
