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


class AdpIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "adp"

    @property
    def original_file_name(self) -> "str":
        return "adp.svg"

    @property
    def title(self) -> "str":
        return "ADP"

    @property
    def primary_color(self) -> "str":
        return "#D0271D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ADP</title>
     <path d="M15.08584 11.9999a3.13031 3.13031 0 0 1-3.12003
 3.12002h-1.2v-1.37144h1.2a1.74859 1.74859 0 1 0
 0-3.49717h-1.2V8.87987h1.2a3.13031 3.13031 0 0 1 3.12003
 3.12002M8.43436 8.87987v2.53716H6.27434l-.78858
 1.37144H9.8058v-3.9086Zm15.56584 1.9543a4.28575 4.28575 0 0 1-4.28575
 4.28575v2.33145h-3.70289V15.6342a5.36233 5.36233 0 0 1-4.08003
 1.81716H8.43436v-2.33145H5.69148l-1.37144 2.33145H0L6.34291
 6.54842h5.6229a5.59548 5.59548 0 0 1 4.08004
 1.81716V6.54842h3.70289a4.2789 4.2789 0 0 1 4.25146 4.28575m-12.03439
 5.24576a4.09032 4.09032 0 0 0
 3.7029-2.33145h1.74858v2.33145h.96v-2.33145h1.37145a2.91088 2.91088 0
 0 0 2.9143-2.91431 2.94174 2.94174 0 0
 0-2.94859-2.91431H17.383v3.49717h-1.37144a4.11432 4.11432 0 0
 0-4.04575-3.49717H7.16577l-4.76575
 8.16007h1.13144l1.37144-2.33145h4.9029v2.33145zm7.74864-7.20006h-1.37144v1.37144h1.37144a.57943.57943
 0 0 1 .58286.58286.6.6 0 0
 1-.58286.58286h-1.37144v1.37144h1.37144a1.9543 1.9543 0 0 0
 1.9543-1.9543 1.97487 1.97487 0 0 0-1.9543-1.9543 M21.63447
 16.76565a.54858.54858 0 1 1-.54858-.54858.54172.54172 0 0 1
 .54858.54858m.13714 0a.68572.68572 0 1 0-.68572.68572.68572.68572 0 0
 0 .68572-.68572 M21.12018 16.45707a.13714.13714 0 1 1 0
 .2743h-.13715v-.2743zm.17143-.03428a.26057.26057 0 0
 0-.17143-.06857h-.2743v.82286h.10287v-.30857h.13714l.17143.30857h.13714l-.20571-.34286c.03428
 0 .06857-.03429.10286-.06857a.20572.20572 0 0 0 .03428-.13715.192.192
 0 0 0-.03428-.20571" />
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
