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


class LeaderPriceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "leaderprice"

    @property
    def original_file_name(self) -> "str":
        return "leaderprice.svg"

    @property
    def title(self) -> "str":
        return "Leader Price"

    @property
    def primary_color(self) -> "str":
        return "#E50005"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Leader Price</title>
     <path d="M1.836 7.574h-1.1v3.97h2.822v-.965H1.836zM17.08
 9.943h1.794V9.15H17.08v-.636h1.987v-.941H15.99v3.97h3.106v-.936h-2.021v-.665zm-12.075
 0H6.8V9.15H5.005v-.636h1.992v-.941H3.92v3.97h3.106v-.936H5.005zm17.314.217c.492-.208.815-.613.815-1.22v-.01c0-.391-.12-.7-.352-.927-.265-.27-.685-.43-1.293-.43h-1.877v3.971h1.1v-1.201h.483l.8
 1.201h1.27zm-.29-1.153c0 .29-.217.472-.588.472h-.724v-.95h.719c.367 0
 .593.16.593.473zm-8.731-1.433h-1.53v3.97h1.51c1.428 0 2.263-.849
 2.263-1.997v-.01c-.005-1.148-.825-1.963-2.243-1.963zm1.11 1.992c0
 .642-.44 1.004-1.096 1.004h-.448V8.553h.448c.656 0 1.095.367 1.095
 1.004zM11.734 0 5.497 6.238h12.475zm-2.88 7.574-1.68
 3.97h1.149l.28-.704h1.52l.289.704h1.172l-1.679-3.97zm.072
 2.417.444-1.158.439 1.158zm-.781 5.248h.482l.8
 1.202h1.27l-.946-1.385c.492-.207.815-.613.815-1.22v-.01c0-.39-.12-.7-.352-.926-.265-.27-.685-.43-1.293-.43H7.046v3.966h1.1zm0-1.813h.718c.367
 0 .594.159.594.472v.01c0
 .29-.217.473-.589.473h-.723zm-1.54.453v-.01c0-.878-.646-1.394-1.65-1.394h-1.7v3.966h1.1v-1.134H4.9c.984
 0 1.708-.492 1.708-1.428zm-1.1.048c0
 .314-.236.516-.626.516h-.526v-1.046h.516c.396 0
 .637.183.637.52zm6.788-1.457H11.19v3.966h1.104zm2.634 4.091c.695 0
 1.341-.342 1.737-.916l.024-.034-.892-.613-.025.034a1.02 1.02 0 0
 1-1.862-.574 1.02 1.02 0 0 1 1.023-1.018c.338 0
 .651.164.84.444l.024.034.892-.613-.024-.034a2.103 2.103 0 0
 0-1.737-.912 2.108 2.108 0 0 0-2.103 2.104c0 1.153.94 2.098 2.103
 2.098zm3.295-1.056v-.666h1.906v-.791h-1.906v-.637h2.103v-.936h-3.193v3.966h3.218v-.936zM11.735
 24l6.237-6.238H5.497z" />
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
