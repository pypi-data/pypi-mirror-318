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


class KocIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "koc"

    @property
    def original_file_name(self) -> "str":
        return "koc.svg"

    @property
    def title(self) -> "str":
        return "Koc"

    @property
    def primary_color(self) -> "str":
        return "#F9423A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Koc</title>
     <path d="M23.72
 9.887c-1.313-3.731-5.036-3.932-5.414-3.943-1.667-.036-3.511.541-4.917
 1.906-.568.506-.97 1.095-1.395
 1.719-.426-.636-.828-1.213-1.395-1.719C9.204 6.485 7.36 5.908 5.694
 5.944c-.39.011-4.114.211-5.414 3.943-.46 1.33-.354 3.06.331 4.33.686
 1.46 2.329 2.66 4.066 2.543 1.253-.035 2.624-.824
 3.132-2.107.426-1.141.296-2.377-.685-3.354.024.247.035.6-.213.918-.39.541-1.016.683-1.666.447-.568-.259-.78-.67-.721-1.212.035-.46.413-.812.803-.989.757-.33
 1.454-.164 2.14.483 1.123 1.247 1.253 3.13 1.785 4.567.378 1.177.969
 2.2 2.28 2.495.154.035.32.059.485.047.166 0 .331-.012.485-.047
 1.312-.294 1.903-1.318 2.281-2.495.532-1.436.662-3.32
 1.773-4.567.686-.647 1.383-.812
 2.14-.483.39.177.756.53.803.989.06.541-.153.953-.72
 1.212-.65.236-1.265.094-1.667-.447-.248-.318-.237-.671-.213-.918-.981.977-1.111
 2.213-.686 3.354.509 1.283 1.88 2.072 3.133 2.107 1.725.118
 3.368-1.07 4.054-2.542.674-1.271.78-3.001.32-4.331zm-2.637
 4.449c-.792.694-1.844.894-2.695.506-.508-.248-.886-.683-1.004-1.154.72.718
 2.02 1.071 3.203-.176 0 0
 1.11-1.024.484-2.966-.319-.965-1.489-1.754-2.47-1.86-1.466-.235-2.837.259-3.794
 1.589-1.123 1.73-1.265 3.66-2.092 5.59a.732.732 0 0
 1-.721.448.732.732 0 0
 1-.721-.447c-.816-1.919-.946-3.837-2.08-5.58-.958-1.33-2.341-1.824-3.795-1.588-.98.094-2.163.894-2.47
 1.86-.627 1.941.484 2.965.484 2.965 1.194 1.248 2.483.883
 3.204.177-.119.47-.485.906-1.005
 1.153-.851.389-1.915.177-2.707-.506-1.17-1.153-1.347-2.636-.886-4.001.555-1.66
 2.246-2.484 3.581-2.59 1.584-.141 3.77.824 4.645 2.484.201.376.627
 1.365.627 1.365h2.222s.426-.989.626-1.365c.875-1.648 3.062-2.613
 4.646-2.484 1.335.106 3.026.942 3.581 2.59.485 1.353.307 2.836-.863
 3.99z" />
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
