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


class OsfIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "osf"

    @property
    def original_file_name(self) -> "str":
        return "osf.svg"

    @property
    def title(self) -> "str":
        return "OSF"

    @property
    def primary_color(self) -> "str":
        return "#2CB9F1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OSF</title>
     <path d="M12.088 0a2.984 2.984 0 0 0-2.986 2.984 2.984 2.984 0 0
 0 .525 1.68 2.654 2.654 0 0 1 2.482-1.734c1.121 0 2.083.706 2.467
 1.695a2.984 2.984 0 0 0 .496-1.64A2.984 2.984 0 0 0 12.088 0zM5.65
 2.666A2.984 2.984 0 0 0 2.666 5.65 2.984 2.984 0 0 0 5.65 8.635 2.984
 2.984 0 0 0 8.635 5.65 2.984 2.984 0 0 0 5.65 2.666zm12.7 0a2.984
 2.984 0 0 0-2.985 2.984 2.984 2.984 0 0 0 2.985 2.985 2.984 2.984 0 0
 0 2.986-2.985 2.984 2.984 0 0 0-2.986-2.984zm-6.24.764a2.147 2.147 0
 0 0-2.147 2.146 2.147 2.147 0 0 0 2.146 2.147 2.147 2.147 0 0 0
 2.147-2.147 2.147 2.147 0 0 0-2.147-2.146zM9.112 6.04a3.497 3.497 0 0
 1-2.984 3.06 2.147 2.147 0 0 0 1.363.493A2.147 2.147 0 0 0 9.64
 7.447a2.147 2.147 0 0 0-.526-1.406zm5.782.047a2.147 2.147 0 0 0-.489
 1.36 2.147 2.147 0 0 0 2.147 2.146 2.147 2.147 0 0 0 1.355-.489 3.494
 3.494 0 0 1-3.013-3.017zM2.985 9.016A2.984 2.984 0 0 0 0 12a2.984
 2.984 0 0 0 2.984 2.984 2.984 2.984 0 0 0 1.659-.505A2.655 2.655 0 0
 1 2.922 12c0-1.131.719-2.102 1.723-2.479a2.984 2.984 0 0
 0-1.66-.505zm18.03 0a2.984 2.984 0 0 0-1.673.52 2.655 2.655 0 0 1
 1.71 2.474c0 1.12-.705 2.082-1.695 2.467a2.984 2.984 0 0 0
 1.659.507A2.984 2.984 0 0 0 24 12a2.984 2.984 0 0
 0-2.984-2.984zm-15.447.838A2.147 2.147 0 0 0 3.422 12a2.147 2.147 0 0
 0 2.146 2.146A2.147 2.147 0 0 0 7.715 12a2.147 2.147 0 0
 0-2.147-2.146zm12.838.01a2.147 2.147 0 0 0-2.146 2.146 2.147 2.147 0
 0 0 2.146 2.146 2.147 2.147 0 0 0 2.147-2.146 2.147 2.147 0 0
 0-2.147-2.147zM7.492 14.376a2.147 2.147 0 0 0-1.398.518 3.496 3.496 0
 0 1 3.015 3.037 2.147 2.147 0 0 0 .53-1.409 2.147 2.147 0 0
 0-2.147-2.146zm9.06 0a2.147 2.147 0 0 0-2.146 2.146 2.147 2.147 0 0 0
 .492 1.362 3.495 3.495 0 0 1 3.047-2.996 2.147 2.147 0 0
 0-1.392-.512zm-10.902.988a2.984 2.984 0 0 0-2.984 2.985 2.984 2.984 0
 0 0 2.984 2.986 2.984 2.984 0 0 0 2.985-2.986 2.984 2.984 0 0
 0-2.985-2.985zm12.7 0a2.984 2.984 0 0 0-2.985 2.985 2.984 2.984 0 0 0
 2.985 2.986 2.984 2.984 0 0 0 2.986-2.986 2.984 2.984 0 0
 0-2.986-2.985zm-6.35.908a2.147 2.147 0 0 0-2.146 2.147A2.147 2.147 0
 0 0 12 20.566a2.147 2.147 0 0 0 2.146-2.146A2.147 2.147 0 0 0 12
 16.273zm2.268 3.504A2.65 2.65 0 0 1 12 21.067a2.65 2.65 0 0
 1-2.188-1.16 2.734 2.635 0 0 0-.46 1.458A2.734 2.635 0 0 0 12.086
 24a2.734 2.635 0 0 0 2.734-2.635 2.734 2.635 0 0 0-.552-1.588z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/CenterForOpenScience/osf.i
o/blob/de170682924278eba1db9d6e1c50166bf43700e0/website/static/img/cir'''

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
        yield from [
            "Open Science Framework",
        ]
