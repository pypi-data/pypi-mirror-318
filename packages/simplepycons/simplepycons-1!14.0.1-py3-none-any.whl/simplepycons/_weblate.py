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


class WeblateIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "weblate"

    @property
    def original_file_name(self) -> "str":
        return "weblate.svg"

    @property
    def title(self) -> "str":
        return "Weblate"

    @property
    def primary_color(self) -> "str":
        return "#2ECCAA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Weblate</title>
     <path d="M9.662 3.809c-1.875 1.19-2.81 3.515-2.83 5.795-.014
 2.628.666 5.258 1.988 7.305.936 1.46 2.238 2.715 3.836 3.412a6.942
 6.942 0 005.647-.07c1.997-.927 3.523-2.73 4.463-4.785 1.606-3.518
 1.643-7.724.12-11.295-1.146.458-2.166-.271-2.166-.271s.003
 1.122-1.083 1.685c1.115 2.612 1.088 5.717-.03 8.263-.538 1.225-1.358
 2.365-2.498
 3.01-.917.52-2.04.625-3.052.184-1.342-.585-2.293-1.864-2.89-3.254-.466-1.067-.782-2.447-.802-3.878-.037-1.724.728-3.193
 1.635-3.218.622-.024 1.427.918 1.598 2.435.158 1.543-.177 3.72-1.174
 5.49.677 1.085 1.77 1.98 2.951 1.974 1.386-2.338 1.827-4.911
 1.793-6.987-.02-2.28-.955-4.603-2.83-5.795-1.437-.907-3.173-.948-4.676
 0zM3.278 3.9s-1.018.73-2.163.27c-1.524 3.573-1.488 7.778.12 11.296.94
 2.056 2.465 3.858 4.462 4.785a6.95 6.95 0 005.523.124 9.12 9.12 0
 01-1.75-1.455 11.18 11.18 0
 01-1.267-1.628c-.768-.08-1.498-.482-2.003-.913-1.447-1.213-2.453-3.478-2.632-5.9-.12-1.635.14-3.354.795-4.894C3.276
 5.022 3.278 3.9 3.278 3.9z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/WeblateOrg/graphics/blob/6'''

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
