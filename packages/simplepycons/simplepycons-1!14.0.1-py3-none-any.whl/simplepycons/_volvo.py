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


class VolvoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "volvo"

    @property
    def original_file_name(self) -> "str":
        return "volvo.svg"

    @property
    def title(self) -> "str":
        return "Volvo"

    @property
    def primary_color(self) -> "str":
        return "#003057"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Volvo</title>
     <path d="M10.873
 12.584h.49l-.001-1.452h-.489v-.322h1.94v.322h-.483v1.451h.449c.415 0
 .687-.274.687-.646h.32v.972h-2.913v-.325zm4.313.327h1.134l.962-1.779h.482v-.322h-1.45v.322h.419l-.701
 1.295-.71-1.295h.51l-.002-.322h-2.104v.322h.482l.978 1.779zM5.073
 10.81H2.968v.322h.481l.98
 1.779h1.133l.962-1.779h.482v-.322h-1.45v.322h.418l-.7
 1.295-.71-1.295h.509v-.322zm3.707-.044c.975 0 1.498.486 1.498 1.096 0
 .618-.494 1.111-1.493 1.111-.999 0-1.497-.493-1.497-1.111
 0-.61.517-1.096
 1.492-1.096zm.017.33c-.333-.005-.527.348-.534.753-.006.39.15.784.506.79.366.007.524-.39.53-.772.008-.405-.168-.764-.502-.77zm10.738-.33c.974
 0 1.497.486 1.497 1.096 0 .618-.493 1.111-1.492 1.111-1
 0-1.498-.493-1.498-1.111 0-.61.518-1.096 1.493-1.096zm-.517
 1.083c-.007.39.15.784.506.79.366.007.524-.39.53-.772.008-.405-.168-.764-.502-.77-.333-.006-.527.347-.534.752zm2.857-6.667L20.656
 6.4A10.26 10.26 0 0 1 22.308 12c0 5.693-4.615 10.308-10.308
 10.308S1.692 17.693 1.692 12 6.307 1.692 12 1.692c2.07 0 3.996.61
 5.611 1.66l1.219-1.219A11.944 11.944 0 0 0 12 0C5.373 0 0 5.373 0
 12s5.373 12 12 12 12-5.373
 12-12c0-2.533-.785-4.882-2.125-6.818zM18.036.472v.337c.728.394
 1.413.859 2.047 1.382l-1.71 1.71a10.29 10.29 0 0 1 1.735
 1.732l1.708-1.708c.524.636.989 1.322 1.384 2.038h.328V.473h-5.492z"
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
        return '''https://www.media.volvocars.com/global/en-gb/'''

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
