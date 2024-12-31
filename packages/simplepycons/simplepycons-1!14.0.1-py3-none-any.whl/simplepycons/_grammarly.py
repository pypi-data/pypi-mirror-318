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


class GrammarlyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "grammarly"

    @property
    def original_file_name(self) -> "str":
        return "grammarly.svg"

    @property
    def title(self) -> "str":
        return "Grammarly"

    @property
    def primary_color(self) -> "str":
        return "#027E6F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Grammarly</title>
     <path d="M12 24H.032V12c0-3.314 1.341-6.314 3.504-8.486C5.703
 1.344 8.694 0 12 0c3.305 0 6.297 1.344 8.463 3.514 2.164 2.172 3.505
 5.172 3.505 8.486s-1.338 6.314-3.505 8.486C18.297 22.656 15.305 24 12
 24m2.889-13.137-1.271 2.205h4.418c-.505 2.882-3.018 5.078-6.036
 5.078-3.38 0-6.132-2.757-6.132-6.146S8.618 5.854 12 5.854c1.821 0
 3.458.801 4.584
 2.069l1.143-1.988c-1.493-1.418-3.506-2.29-5.725-2.29-4.6 0-8.332
 3.74-8.332 8.355s3.73 8.354 8.332 8.354c4.603 0 8.332-3.739
 8.332-8.354 0-.387-.029-.765-.079-1.137z" />
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
