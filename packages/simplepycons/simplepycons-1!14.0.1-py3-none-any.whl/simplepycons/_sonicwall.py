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


class SonicwallIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sonicwall"

    @property
    def original_file_name(self) -> "str":
        return "sonicwall.svg"

    @property
    def title(self) -> "str":
        return "SonicWall"

    @property
    def primary_color(self) -> "str":
        return "#FF791A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SonicWall</title>
     <path d="M23.678 10.007a.31.31 0 0 0 .016.62.308.308 0 0 0
 .306-.308.31.31 0 0 0-.302-.312.31.31 0 0 0-.02 0zm.016.043a.27.27 0
 0 1 .27.269.27.27 0 1 1-.27-.27zm-9.503.053l-.614
 1.863-.013.04-.013-.04-.624-1.855h-.619l.986
 2.74h.508l.618-1.788.013-.037.013.037.619
 1.787h.507l.986-2.74h-.603l-.622
 1.856-.015.04-.013-.04-.613-1.863zm-5.48.006v2.743h.258V10.11zm-7.823
 0a1.315 1.315 0 0 0-.038.002c-.481 0-.85.306-.85.712 0
 .41.26.63.898.759.6.12.715.279.715.526 0 .288-.26.49-.631.49a1.228
 1.228 0 0 1-.923-.37l-.02-.02v.313a1.477 1.477 0 0 0 .923.31c.524 0
 .89-.302.89-.738.005-.393-.257-.614-.872-.738-.619-.127-.739-.288-.739-.541
 0-.27.255-.464.608-.464a1.091 1.091 0 0 1
 .759.287l.022.018v-.318a1.315 1.315 0 0
 0-.742-.227zm4.92.002v2.747h.284v-2.081l1.813
 2.08h.063v-2.746h-.272v2.106l-1.828-2.106zm11.672 0l-.642
 1.721c-.637.117-1.051.393-.848.943.278.76 1.549 1.218 1.549
 1.218s-1.285-.801-.613-1.34c.296-.238.819-.414
 1.313-.54l.278.719h.541l-.322-.833c.403-.08.708-.122.708-.122s-.36-.043-.785-.077l-.653-1.69zm2.136
 0v2.721h1.554v-.49h-1.034v-2.231zm2.106
 0v2.721h1.555v-.49H22.24v-2.231zm-17.953.008a1.344 1.344 0 0 0-.042 0
 1.327 1.327 0 0 0-.67.176 1.313 1.313 0 0 0-.491.499 1.377 1.377 0 0
 0-.185.69 1.292 1.292 0 0 0 .397.953 1.318 1.318 0 0 0 .971.395 1.351
 1.351 0 0 0 1.359-1.356 1.307 1.307 0 0 0-.397-.965 1.344 1.344 0 0
 0-.942-.392zm7.3.002a1.381 1.381 0 0 0-.96.392 1.292 1.292 0 0
 0-.4.96 1.377 1.377 0 0 0 .33.923 1.353 1.353 0 0 0 1.077.454 1.516
 1.516 0 0 0 .65-.136 1.477 1.477 0 0 0 .265-.185v-.338a1.16 1.16 0 0
 1-.899.412 1.134 1.134 0 0 1-.823-.325 1.067 1.067 0 0 1-.325-.794
 1.097 1.097 0 0 1 .146-.565 1.073 1.073 0 0 1 .41-.402 1.156 1.156 0
 0 1 .576-.15 1.196 1.196 0 0 1 .515.12 1.132 1.132 0 0 1
 .4.314v-.35a1.477 1.477 0 0 0-.26-.185 1.477 1.477 0 0 0-.66-.145
 1.381 1.381 0 0 0-.041 0zm12.661.009a.11.11 0 0 0-.012
 0h-.162v.37h.094v-.142h.035l.085.142.11-.002-.103-.153a.103.103 0 0 0
 .068-.102.11.11 0 0 0-.115-.113zm-.026.063a.048.048 0 0 1 .046.054c0
 .032-.017.048-.054.048h-.046v-.101h.046a.048.048 0 0 1 .008
 0zm-19.97.178a1.108 1.108 0 0 1 .006 0 1.093 1.093 0 0 1 .548.153
 1.075 1.075 0 0 1 .405.399 1.097 1.097 0 0 1 .143.553 1.12 1.12 0 0
 1-.143.564 1.047 1.047 0 0 1-.4.399 1.108 1.108 0 0 1-.553.145 1.087
 1.087 0 0 1-1.091-1.095 1.119 1.119 0 0 1 .144-.564 1.108 1.108 0 0 1
 .94-.554zm14.015.465l.368.931c-.032 0-.065-.003-.097-.004a7.414 7.414
 0 0 0-.622.01h-.018z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://brandfolder.com/sonicwall/sonicwall-e'''

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
