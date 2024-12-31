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


class WikimediaCommonsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wikimediacommons"

    @property
    def original_file_name(self) -> "str":
        return "wikimediacommons.svg"

    @property
    def title(self) -> "str":
        return "Wikimedia Commons"

    @property
    def primary_color(self) -> "str":
        return "#006699"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wikimedia Commons</title>
     <path d="M9.048 15.203a2.952 2.952 0 1 1 5.904 0 2.952 2.952 0 0
 1-5.904 0zm11.749.064v-.388h-.006a8.726 8.726 0 0 0-.639-2.985 8.745
 8.745 0 0
 0-1.706-2.677l.004-.004-.186-.185-.044-.045-.026-.026-.204-.204-.006.007c-.848-.756-1.775-1.129-2.603-1.461-1.294-.519-2.138-.857-2.534-2.467.443.033.839.174
 1.13.481C15.571 6.996 11.321 0 11.321 0s-1.063 3.985-2.362
 5.461c-.654.744.22.273 1.453-.161.279 1.19.77 2.119 1.49
 2.821.791.771 1.729 1.148 2.556 1.48.672.27 1.265.508
 1.767.916l-.593.594-.668-.668-.668 2.463
 2.463-.668-.668-.668.6-.599a6.285 6.285 0 0 1 1.614
 3.906h-.844v-.944l-2.214 1.27 2.214 1.269v-.944h.844a6.283 6.283 0 0
 1-1.614 3.906l-.6-.599.668-.668-2.463-.668.668
 2.463.668-.668.6.6a6.263 6.263 0 0 1-3.907 1.618v-.848h.945L12
 18.45l-1.27 2.214h.944v.848a6.266 6.266 0 0
 1-3.906-1.618l.599-.6.668.668.668-2.463-2.463.668.668.668-.6.599a6.29
 6.29 0 0
 1-1.615-3.906h.844v.944l2.214-1.269-2.214-1.27v.944h-.843a6.292 6.292
 0 0 1 1.615-3.906l.6.599-.668.668
 2.463.668-.668-2.463-.668.668-2.359-2.358-.23.229-.044.045-.185.185.004.004a8.749
 8.749 0 0 0-2.345 5.662h-.006v.649h.006a8.749 8.749 0 0 0 2.345
 5.662l-.004.004.185.185.045.045.045.045.185.185.004-.004a8.73 8.73 0
 0 0 2.677 1.707 8.75 8.75 0 0 0 2.985.639V24h.649v-.006a8.75 8.75 0 0
 0 2.985-.639 8.717 8.717 0 0 0
 2.677-1.707l.004.004.187-.187.044-.043.043-.044.187-.186-.004-.004a8.733
 8.733 0 0 0 1.706-2.677 8.726 8.726 0 0 0 .639-2.985h.006v-.259z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Commo'''

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
