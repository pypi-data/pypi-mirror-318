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


class QiitaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qiita"

    @property
    def original_file_name(self) -> "str":
        return "qiita.svg"

    @property
    def title(self) -> "str":
        return "Qiita"

    @property
    def primary_color(self) -> "str":
        return "#55C500"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Qiita</title>
     <path d="M3.57 8.343a3.653 3.653 0 0 0-1.376.269 3.585 3.585 0 0
 0-1.14.738 3.503 3.503 0 0 0-.773 1.102A3.297 3.297 0 0 0 0
 11.814a3.28 3.28 0 0 0 .281 1.357 3.535 3.535 0 0 0 .775 1.107A3.636
 3.636 0 0 0 3.6 15.29a3.731 3.731 0 0 0 .987-.13 3.657 3.657 0 0 0
 .888-.374l.687.698a.579.579 0 0 0 .824 0 .58.58 0 0 0
 0-.817l-.624-.624a3.533 3.533 0 0 0 .613-1.022 3.282 3.282 0 0 0
 .226-1.208 3.297 3.297 0 0 0-.282-1.362 3.488 3.488 0 0
 0-.775-1.102A3.614 3.614 0 0 0 5 8.612a3.657 3.657 0 0 0-1.398-.27
 3.653 3.653 0 0 0-.031 0zm11.306.185v1.484h-.765v1.063h.765v2.142c0
 .419.053.761.159 1.028a1.56 1.56 0 0 0 .433.63 1.511 1.511 0 0 0
 .643.317 2.676 2.676 0 0 0 .694.086h.853v-1.013h-.736a1.25 1.25 0 0
 1-.352-.048.713.713 0 0 1-.291-.169.81.81 0 0 1-.2-.324 1.575 1.575 0
 0 1-.074-.519v-2.13h1.666v-1.063h-1.66V8.528zM9.4 8.856a.69.69 0 0
 0-.69.691.69.69 0 0 0 .69.69.69.69 0 0 0 .691-.69.69.69 0 0
 0-.69-.691zm2.771 0a.69.69 0 0 0-.69.691.69.69 0 0 0 .69.69.69.69 0 0
 0 .691-.69.69.69 0 0 0-.69-.691zm-8.6.538a2.324 2.324 0 0 1 .03 0
 2.35 2.35 0 0 1 .93.187 2.346 2.346 0 0 1 1.264 1.28 2.463 2.463 0 0
 1 .186.957 2.444 2.444 0 0 1-.186.957 2.384 2.384 0 0 1-.506.767
 2.363 2.363 0 0 1-1.688.698 2.324 2.324 0 0 1-.93-.186 2.376 2.376 0
 0 1-.755-.512 2.427 2.427 0 0 1-.699-1.723 2.44 2.44 0 0 1 .699-1.727
 2.384 2.384 0 0 1 .756-.511 2.324 2.324 0 0 1
 .898-.187zm17.648.773a2.69 2.69 0 0 0-1.02.201 2.49 2.49 0 0
 0-.815.552 2.432 2.432 0 0 0-.525.814 2.678 2.678 0 0 0-.186.998
 2.644 2.644 0 0 0 .186.997 2.485 2.485 0 0 0 .525.814 2.436 2.436 0 0
 0 .815.546 2.697 2.697 0 0 0 1.059.2 2.42 2.42 0 0 0 .518-.056 2.524
 2.524 0 0 0 .46-.146 2.426 2.426 0 0 0 .394-.213 2.394 2.394 0 0 0
 .329-.263l.065.53H24v-4.829h-.976l-.068.533a2.498 2.498 0 0
 0-.322-.26 2.25 2.25 0 0 0-.394-.217 2.616 2.616 0 0 0-.462-.145
 2.404 2.404 0 0 0-.521-.056 2.69 2.69 0 0 0-.038
 0zm-12.375.844v4.138h1.113V11.01zm2.77
 0v4.138h1.114V11.01zm9.72.145a1.592 1.592 0 0 1 .024 0 1.557 1.557 0
 0 1 1.098.445 1.495 1.495 0 0 1 .334.495 1.61 1.61 0 0 1 .121.631
 1.632 1.632 0 0 1-.121.64 1.551 1.551 0 0 1-.331.498 1.47 1.47 0 0
 1-.49.324 1.642 1.642 0 0 1-1.207 0 1.502 1.502 0 0 1-.493-.324 1.52
 1.52 0 0 1-.333-.5 1.64 1.64 0 0 1-.122-.638 1.628 1.628 0 0 1
 .12-.637 1.524 1.524 0 0 1 .328-.495 1.474 1.474 0 0 1 .49-.323 1.592
 1.592 0 0 1 .581-.116z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://help.qiita.com/ja/articles/others-bra'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://help.qiita.com/ja/articles/others-bra'''

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
