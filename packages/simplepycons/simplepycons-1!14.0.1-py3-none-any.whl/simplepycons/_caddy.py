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


class CaddyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "caddy"

    @property
    def original_file_name(self) -> "str":
        return "caddy.svg"

    @property
    def title(self) -> "str":
        return "Caddy"

    @property
    def primary_color(self) -> "str":
        return "#1F88C0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Caddy</title>
     <path d="M11.094.47c-.842 0-1.696.092-2.552.288a11.37 11.37 0 0
 0-4.87 2.423 10.632 10.632 0 0 0-2.36 2.826A10.132 10.132 0 0 0 .305
 8.582c-.398 1.62-.4 3.336-.043 5.048.085.405.183.809.31 1.212a11.85
 11.85 0 0 0 1.662 3.729 3.273 3.273 0 0 0-.086.427 3.323 3.323 0 0 0
 2.848 3.71 3.279 3.279 0 0 0 1.947-.346c1.045.51 2.17.864 3.339
 1.04a11.66 11.66 0 0 0 4.285-.155 11.566 11.566 0 0 0 4.936-2.485
 10.643 10.643 0 0 0 2.352-2.894 11.164 11.164 0 0 0 1.356-4.424
 11.214 11.214 0 0 0-.498-4.335c.175-.077.338-.175.486-.293a.444.444
 89.992 0 0 .001 0c.402-.322.693-.794.777-1.342a2.146 2.146 0 0
 0-1.79-2.434 2.115 2.115 0 0
 0-1.205.171c-.038-.043-.078-.086-.113-.13a11.693 11.693 0 0
 0-3.476-2.93 13.348 13.348 0 0 0-1.76-.81 13.55 13.55 0 0
 0-2.06-.613A12.121 12.121 0 0 0 11.093.47Zm.714.328c.345-.004.688.01
 1.028.042a9.892 9.892 0 0 1 2.743.639c.984.39 1.89.958 2.707
 1.632.803.662 1.502 1.45 2.091 2.328.026.039.048.08.07.12a2.12 2.12 0
 0 0-.435 2.646c-.158.114-.97.692-1.634
 1.183-.414.308-.733.557-.733.557l.581.68s.296-.276.665-.638c.572-.562
 1.229-1.233 1.395-1.403a2.122 2.122 0 0 0 1.907.677 11.229 11.229 0 0
 1-.013 4.046 11.41 11.41 0 0 1-1.475 3.897 12.343 12.343 0 0 1-2.079
 2.587c-1.19 1.125-2.633 2.022-4.306 2.531a10.826 10.826 0 0
 1-3.973.484 11.04 11.04 0 0 1-3.057-.652 3.304 3.304 0 0 0
 1.417-2.294 3.275 3.275 0 0 0-.294-1.842c.18-.162.403-.363.656-.6
 1.015-.955 2.353-2.303 2.353-2.303l-.47-.599s-1.63.972-2.801
 1.728c-.307.198-.573.378-.777.517a3.273 3.273 0 0
 0-1.516-.611c-1.507-.198-2.927.672-3.487 2.017a10.323 10.323 0 0
 1-.695-1.078A10.92 10.92 0 0 1 .728 14.8a10.35 10.35 0 0
 1-.2-1.212c-.164-1.653.103-3.258.629-4.754a12.95 12.95 0 0 1
 1.087-2.288c.57-.968 1.248-1.872 2.069-2.656A11.013 11.013 0 0 1
 11.808.797Zm-.147 3.257a3.838 3.838 0 0 0-3.82 3.82v2.36h-.94c-.751
 0-1.377.625-1.377
 1.377v3.8h1.46v-3.718h9.354v6.264H10.02v1.46h6.4c.751 0 1.377-.625
 1.377-1.377v-6.43c0-.751-.626-1.377-1.377-1.377h-.94v-2.36a3.838
 3.838 0 0 0-3.82-3.819zm0 1.46a2.371 2.371 0 0 1 2.36
 2.36v2.36H9.3v-2.36a2.372 2.372 0 0 1 2.36-2.36zm10.141.392a1.253
 1.253 0 0 1 1.296
 1.434c-.049.319-.217.59-.453.78-.266.213-.61.318-.968.264a1.253 1.253
 0 0 1-1.045-1.42 1.255 1.255 0 0 1 1.17-1.058zM5.384 17.425a2.02 2.02
 0 0 1 1.917 1.298c.116.3.159.628.114.967a2.015 2.015 0 0 1-2.249
 1.728 2.016 2.016 0 0 1-1.727-2.25 2.017 2.017 0 0 1 1.945-1.743z" />
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
