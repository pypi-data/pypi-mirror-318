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


class BugattiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bugatti"

    @property
    def original_file_name(self) -> "str":
        return "bugatti.svg"

    @property
    def title(self) -> "str":
        return "Bugatti"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bugatti</title>
     <path d="M0 2.978h18.593c.021.004.042.012.063.013.436.019.863.09
 1.279.218 1.459.451 2.507 1.367 3.117 2.772.454 1.046.5 2.259.316
 3.156a4.634 4.634 0 0 1-1.37
 2.482c-.014.014-.027.03-.04.045.021.026.052.04.077.061a4.774 4.774 0
 0 1 1.951
 3.564c.001.021.01.042.014.063v.79c-.005.027-.012.053-.014.08-.004.046-.002.093-.007.14a5.501
 5.501 0 0 1-.21 1.047c-.398 1.278-1.167 2.262-2.336
 2.924-.836.474-1.744.686-2.7.687-6.24.004-12.48.002-18.72.002v-4.74h2.988l.001
 1.738c.134.016 7.226.01
 7.286-.006v-4.668h-3.06v1.425c-.102.019-2.928.014-2.986-.004V8.912h2.986v1.424c.103.019
 3.003.014 3.06-.003V5.976H3V7.51H.008Zm13.753 15.05h4.744c.254 0
 .505-.023.75-.09.77-.21 1.3-.683 1.546-1.447a2.605 2.605 0 0
 0-.007-1.636 2.068 2.068 0 0 0-1.12-1.274 2.553 2.553 0 0
 0-1.092-.239h-4.82zm.003-12.058v4.377h4.397a2.5 2.5 0 0 0
 .723-.103c.678-.203 1.147-.63
 1.376-1.304.145-.428.163-.868.068-1.308-.161-.742-.598-1.251-1.313-1.515a2.711
 2.711 0 0 0-.947-.147Z" />
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
