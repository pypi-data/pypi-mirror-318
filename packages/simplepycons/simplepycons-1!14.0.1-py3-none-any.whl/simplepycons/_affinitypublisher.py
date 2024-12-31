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


class AffinityPublisherIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "affinitypublisher"

    @property
    def original_file_name(self) -> "str":
        return "affinitypublisher.svg"

    @property
    def title(self) -> "str":
        return "Affinity Publisher"

    @property
    def primary_color(self) -> "str":
        return "#891B26"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Affinity Publisher</title>
     <path d="M24 2.344v19.312A2.345 2.345 0 0 1 21.656 24H2.344A2.345
 2.345 0 0 1 0 21.656V2.344A2.345 2.345 0 0 1 2.344 0h19.312A2.345
 2.345 0 0 1 24 2.344Zm-1.758 16.607-9.93-17.193h-1.639L9.75
 3.354l10.91 18.888h.645c.517 0 .937-.42.937-.937v-2.354Zm-6.911
 3.291L7.086 7.967l-1.263 2.187a1.657 1.657 0 0 0 0 1.657c1.512 2.615
 6.025 10.431 6.025 10.431h3.483Zm5.974-20.484h-8.071l9.008
 15.596V2.695a.938.938 0 0 0-.937-.937Zm-10.38 20.484L4.883
 11.781l-3.125 5.411v4.113c0 .517.42.937.938.937h8.229Zm8.812 0L9.289
 4.153 7.598 7.08l8.656 15.162h3.483Z" />
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
