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


class TheRegisterIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "theregister"

    @property
    def original_file_name(self) -> "str":
        return "theregister.svg"

    @property
    def title(self) -> "str":
        return "The Register"

    @property
    def primary_color(self) -> "str":
        return "#FF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>The Register</title>
     <path d="M22.368 12.858a42.543 42.543 0 0 1-2.612
 1.818c-.893.568-1.683.977-2.378
 1.22-.695.245-1.167.198-1.413-.132-.23-.417-.242-1.028-.028-1.826.21-.802.508-1.628.893-2.485.381-.782.711-1.58.99-2.39.277-.81.412-1.632.4-2.458-.012-.826-.266-1.648-.758-2.47-.433-.67-1.08-1.174-1.94-1.508-.863-.337-1.823-.504-2.883-.492a9.544
 9.544 0 0 0-3.148.58 6.839 6.839 0 0 0-2.23 1.402c-.675.626-1.207
 1.408-1.6 2.345-.134.341-.221.794-.27 1.346a17.953 17.953 0 0 0-.082
 1.49c-.004.444-.008.678-.004.698-.433.298-.925.663-1.481
 1.096-.556.43-1.104.95-1.64 1.552a15.423 15.423 0 0 0-1.437
 1.973c-.393.655-.635 1.155-.727 1.505-.048.143-.008.532.119
 1.183.127.643.457 1.386 1 2.227.545.841 1.418 1.62 2.617
 2.331.012.012.044-.012.09-.067a.925.925 0 0 0 .084-.087 6.701 6.701 0
 0 1-.43-.476c-.261-.302-.515-.699-.757-1.175a2.88 2.88 0 0
 1-.31-1.52c.048-.732.512-1.399 1.394-2.006.885-.61 2.393-1.143
 4.53-1.592.606-.155 1.131-.385
 1.58-.707.448-.314.686-.492.706-.532-.167 1.703.14 3.26.901
 4.653a12.107 12.107 0 0 0 2.537 3.176l9.906-9.878L24
 11.6c-.472.37-1.012.79-1.632 1.258zM9.438
 7.363c-.156.413-.31.826-.466
 1.243-.15.417-.234.651-.246.707.028.048.127.163.282.337.163.171.254.286.282.342.012.1-.044.337-.17.707-.124.37-.374.647-.739.838-.48.18-.929.214-1.346.103-.417-.103-.75-.242-1.008-.413-.254-.175-.388-.266-.396-.286l4.032-4.39.016.142c-.008.035-.087.258-.242.67z"
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
