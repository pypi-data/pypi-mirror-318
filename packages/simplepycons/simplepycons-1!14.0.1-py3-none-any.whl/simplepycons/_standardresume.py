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


class StandardResumeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "standardresume"

    @property
    def original_file_name(self) -> "str":
        return "standardresume.svg"

    @property
    def title(self) -> "str":
        return "Standard Resume"

    @property
    def primary_color(self) -> "str":
        return "#2A3FFB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Standard Resume</title>
     <path d="M1.524 17.138v-2.093h3.111v2.358c0 1.306.102 2.226.306
 2.76.204.523.587.786 1.149.786.564 0 .934-.217
 1.115-.654.187-.435.281-1.146.281-2.131
 0-.987-.165-1.845-.49-2.573-.326-.736-.845-1.506-1.554-2.305L3.852
 11.5a10.829 10.829 0 0 1-1.74-2.625C1.705 7.97 1.5 6.92 1.5
 5.73c0-1.937.342-3.375 1.028-4.317C3.212.471 4.391 0 6.064 0s2.802.55
 3.39 1.653c.595 1.092.893 2.691.893
 4.797v1.452H7.324v-1.68c0-1.136-.09-1.95-.268-2.438-.18-.498-.525-.745-1.041-.745-.505
 0-.871.186-1.101.56-.22.371-.33.932-.33 1.678 0 .747.114 1.341.342
 1.785.23.445.64 1.014 1.236 1.707l1.775 2.091c.889 1.05 1.56 2.11
 2.007 3.186.457 1.074.685 2.247.685 3.518 0 2.194-.338 3.815-1.016
 4.864C8.938 23.475 7.75 24 6.053 24c-1.69
 0-2.868-.582-3.537-1.746-.66-1.173-.99-2.878-.99-5.117Zm15.849-4.426-1.053-.052v11.073h-3.28V.28h5.422c1.125
 0 1.965.248 2.52.746.555.489.918 1.177 1.09 2.066.18.878.269
 2.034.269 3.464 0 1.422-.138 2.505-.416 3.252a2.405 2.405 0 0 1-1.542
 1.505c.741.143 1.26.69 1.554 1.64.293.95.44 2.932.44 5.943 0
 3.003.042 4.615.123 4.837h-3.28c-.082-.177-.122-2.98-.122-8.407
 0-1.04-.114-1.728-.344-2.066-.228-.346-.69-.53-1.381-.547Zm-1.041-2.824h1.31c.415
 0
 .721-.102.918-.306.204-.206.342-.555.415-1.053.083-.498.123-1.257.123-2.28v-.144c0-1.27-.097-2.1-.294-2.492-.195-.391-.648-.586-1.357-.586h-1.115z"
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
