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


class CoinbaseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "coinbase"

    @property
    def original_file_name(self) -> "str":
        return "coinbase.svg"

    @property
    def title(self) -> "str":
        return "Coinbase"

    @property
    def primary_color(self) -> "str":
        return "#0052FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Coinbase</title>
     <path d="M4.844 11.053c-.872 0-1.553.662-1.553 1.548s.664 1.542
 1.553 1.542c.889 0 1.564-.667 1.564-1.547
 0-.875-.664-1.543-1.564-1.543zm.006 2.452c-.497 0-.86-.386-.86-.904
 0-.523.357-.909.854-.909.502 0 .866.392.866.91 0
 .517-.364.903-.86.903zm1.749-1.778h.433v2.36h.693V11.11H6.599zm-5.052-.035c.364
 0 .653.224.762.558h.734c-.133-.713-.722-1.197-1.49-1.197-.872
 0-1.553.662-1.553 1.548 0 .887.664 1.543 1.553 1.543.75 0 1.351-.484
 1.484-1.203h-.728a.78.78 0 01-.756.564c-.502 0-.855-.386-.855-.904
 0-.523.347-.909.85-.909zm18.215.622l-.508-.075c-.242-.035-.415-.115-.415-.305
 0-.207.225-.31.53-.31.336 0
 .55.143.595.379h.67c-.075-.599-.537-.95-1.247-.95-.733
 0-1.218.375-1.218.904 0
 .506.317.8.958.892l.508.075c.249.034.387.132.387.316 0
 .236-.242.334-.577.334-.41 0-.641-.167-.676-.42h-.681c.064.581.52.99
 1.35.99.757 0 1.26-.346 1.26-.938 0-.53-.364-.806-.936-.892zM7.378
 9.885a.429.429 0 00-.444.437c0 .254.19.438.444.438a.429.429 0
 00.445-.438.429.429 0 00-.445-.437zm10.167
 2.245c0-.645-.392-1.076-1.224-1.076-.785 0-1.224.397-1.31
 1.007h.687c.035-.236.22-.432.612-.432.352 0 .525.155.525.345 0
 .248-.317.311-.71.351-.531.058-1.19.242-1.19.933 0 .535.4.88
 1.034.88.497 0
 .809-.207.965-.535.023.293.242.483.548.483h.404v-.616h-.34v-1.34zm-.68.748c0
 .397-.347.69-.769.69-.26 0-.48-.11-.48-.34
 0-.293.353-.373.676-.408.312-.028.485-.097.572-.23zm-3.679-1.825c-.386
 0-.71.162-.94.432V9.856h-.693v4.23h.68v-.391c.232.282.56.449.953.449.832
 0 1.461-.656 1.461-1.543 0-.886-.64-1.548-1.46-1.548zm-.103
 2.452c-.497 0-.86-.386-.86-.904 0-.517.369-.909.865-.909.503 0
 .855.386.855.91 0 .517-.364.903-.86.903zm-3.187-2.452c-.45
 0-.745.184-.919.443v-.385H8.29v2.975h.693v-1.617c0-.455.289-.777.716-.777.398
 0 .647.282.647.69v1.704h.692v-1.755c0-.748-.386-1.278-1.142-1.278zM24
 12.503c0-.851-.624-1.45-1.46-1.45-.89 0-1.542.668-1.542 1.548 0
 .927.698 1.543 1.553 1.543.722 0 1.287-.426
 1.432-1.03h-.722c-.104.264-.358.414-.699.414-.445
 0-.78-.276-.854-.76H24v-.264zm-2.252-.23c.11-.414.422-.615.78-.615.392
 0 .693.224.762.615Z" />
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
