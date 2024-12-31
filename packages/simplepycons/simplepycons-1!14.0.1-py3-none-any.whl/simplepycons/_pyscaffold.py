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


class PyscaffoldIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pyscaffold"

    @property
    def original_file_name(self) -> "str":
        return "pyscaffold.svg"

    @property
    def title(self) -> "str":
        return "PyScaffold"

    @property
    def primary_color(self) -> "str":
        return "#005CA0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PyScaffold</title>
     <path d="M2.402 2.06C.357 2.06 0 5.626 0
 5.626l5.36.996s-3.65.862-4.227 1.054c.167.456 1.701.623
 1.701.623h5.434c.886 0 1.342-.815 1.342-.815h9.056c.193 0 1.366 0
 1.366 1.582 0 1.583-1.366 1.777-1.366 1.777H7.787c-.175
 0-1.577.258-2.765 1.361h.077v.11h-.184a5.18 5.18 0 00-1.352
 2.327h4.57c.154-.072.27-.11.27-.11h10.208c1.819.003 3.51-.837
 4.466-2.218h-.282v-.11h.331c.523-.907.865-2.176.874-3.068
 0-3.73-2.84-5.527-4.72-5.527h-9.25c-.61-1.192-2.101-1.55-2.101-1.55h-.896l.316
 1.096h-.283v4.02h.283c-.107.367-.212.736-.318
 1.105l-.318-1.106h.261V3.155h-.26l.315-1.096zm.788 1.419a.557.557 0
 01.566.56.553.553 0 01-.561.56c-.747.003-.752-1.117-.005-1.12zm2.019
 8.726h.33v.108h-.33zm.44 0h.33v.108h-.33zm.439
 0h.332v.108h-.331l-.001-.108zm.44 0h.33v.108h-.33zm.44
 0h.33v.108h-.33zm.44 0h.33v.108h-.33zm.768
 0v.108h-.327v-.11c.101.005.22.001.327.002zm.109 0h.33v.108h-.33zm.44
 0h.33v.108h-.33zm.44 0h.33v.108h-.33zm.44 0h.33v.108h-.33zm.44
 0h.33v.108h-.33zm.44 0h.329v.108h-.33l.001-.108zm.439
 0h.33v.108h-.33zm.44 0h.33v.108h-.33zm.44
 0h.329v.108h-.33l.001-.108zm.439 0h.33v.108h-.33zm.44
 0h.33v.108h-.33zm.44 0h.33v.108h-.33zm.44
 0h.329v.108h-.33l.001-.108zm.439 0h.33v.108h-.33v-.11zm.44
 0h.33v.108h-.33v-.11zm.44 0h.33v.108h-.33v-.11zm.439
 0h.33v.108h-.33zm.44 0h.33v.108h-.33zm.44 0h.33v.108h-.33zm.44
 0h.329v.108h-.33l.001-.108zm.439 0h.33v.108h-.33zm.44
 0h.33v.108h-.33zm.44 0h.33v.108h-.33zm.439 0h.33v.108h-.33zm.44
 0h.33v.108h-.33zm.44 0h.33v.108h-.33zm.44
 0h.329v.108h-.33l.001-.108zm.439 0h.33v.108h-.33zm.44
 0h.33v.108h-.33zm.44 0h.33v.108h-.33zm.44
 0h.329v.108h-.33l.001-.108zm.439 0h.33v.108h-.33zm.44
 0h.33v.108h-.33v-.108zM3.52
 14.812c-.015.061-.022.13-.036.193l.277-.192-.241-.001zm.543
 0l-.622.43a7.27 7.27 0 00-.097.765l1.726-1.194zm1.306 0l-2.038
 1.412c-.005.11-.019.208-.019.321 0
 .184.017.351.03.524l3.262-2.256-1.235-.001zm1.532 0L3.354
 17.27c.022.217.057.418.099.615 1.38-.925 2.753-1.89
 4.123-2.838.09-.093.182-.17.273-.233-.314.001-.64-.001-.948-.002zm.404.627l-3.532
 2.445h.992l2.337-1.62c.005-.284.073-.565.2-.825zm-.203 1.037l-2.039
 1.408h1.003l1.149-.795a2.066 2.066 0
 01-.113-.614zm.173.778l-.908.63h.843l.336-.233a1.539 1.539 0
 01-.27-.398zm.397.517l-.163.113h.348c-.064-.041-.119-.055-.185-.113zm-4.186.283c.835
 3.483 4.47 3.888 4.47 3.888h7.856c2.412 0 4.141-3.805
 4.141-3.805-3.864.002-7.729-.007-11.593-.012 0
 0-.092-.018-.224-.071H3.485zm9.045.099l.26
 1h-.231v1.786h.23l-.259.98-.275-.98h.211v-1.787h-.21Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/pyscaffold/pyscaffold/blob'''

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
