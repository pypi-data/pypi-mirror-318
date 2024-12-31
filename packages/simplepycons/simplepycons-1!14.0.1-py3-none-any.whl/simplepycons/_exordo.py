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


class ExordoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "exordo"

    @property
    def original_file_name(self) -> "str":
        return "exordo.svg"

    @property
    def title(self) -> "str":
        return "Exordo"

    @property
    def primary_color(self) -> "str":
        return "#DAA449"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Exordo</title>
     <path d="M12 0a12 12 0 00-5.514 1.342l2.01 14.062
 2.033-5.281a.375.375 0 01.334-.24.375.375 0 01.15.023.375.375 0
 01.217.487L9.64 14.529 18.95 2.22a12 12 0 00-3.853-1.81l-.844
 2.327-.318.828a.375.375 0 01-.485.215.375.375 0
 01-.215-.484l.315-.822.812-2.239A12 12 0 0012 0zM5.785 1.736a12 12 0
 00-5.691 8.762l.699.49a.375.375 0 01.09.524.375.375 0
 01-.522.09l-.343-.243A12 12 0 000 12a12 12 0 001.129 5.078.375.375 0
 01.21-.084l6.05-.422-5.213-3.693a.375.375 0 01-.088-.524.375.375 0
 01.28-.158.375.375 0 01.243.069l5.205
 3.691-2.03-14.22zm13.764.934L9.275
 16.252l10.037-2.57-.126-.493a.375.375 0 01.27-.455.375.375 0
 01.075-.011.375.375 0 01.38.279l.128.492 3.951-1.012A12 12 0 0024
 12a12 12 0 00-4.451-9.33zm-7.48 1.607a.375.375 0
 01.156.024l.826.316.826.315a.375.375 0 01.217.484.375.375 0
 01-.485.215l-.826-.315-.828-.314a.375.375 0 01-.217-.484.375.375 0
 01.33-.24zm.13 2.13a.375.375 0 01.155.023.375.375 0
 01.214.484l-.271.711.389.148a.375.375 0 01.216.485.375.375 0
 01-.482.217l-.393-.149-.091.238a.375.375 0 01-.485.215.375.375 0
 01-.215-.484l.09-.236-.56-.215a.375.375 0 01-.217-.485.375.375 0
 01.33-.24.375.375 0 01.154.024l.56.214.276-.71a.375.375 0
 01.33-.24zm11.733 6.864l-3.705.95.127.49a.375.375 0
 01-.27.459.375.375 0 01-.457-.27l-.127-.494-9.785 2.506 4.91
 1.502a.375.375 0 01.248.467.375.375 0 01-.469.25l-4.922-1.504 1.032
 1.17a.375.375 0 01-.034.53.375.375 0 01-.529-.034l-1.328-1.51-.52
 5.567A12 12 0 0012 24a12 12 0
 002.07-.18l-2.441-2.636-.303.265a.375.375 0 01-.53-.035.375.375 0
 01.036-.53l.295-.257-.313-.354a.375.375 0 01.034-.529.375.375 0
 01.252-.094.375.375 0 01.277.127l.312.354.383-.334a.375.375 0
 01.252-.094.375.375 0 01.278.129.375.375 0 01-.036.53l-.373.327 2.729
 2.95a12 12 0 005.164-2.772l-3.264-.998a.375.375 0 01-.25-.469.375.375
 0 01.367-.265.375.375 0 01.102.017l3.654 1.118a12 12 0
 003.237-6.999zM7.465 17.34l-5.912.562a12 12 0 002.728
 3.285l.358-.427a.375.375 0 01.273-.137.375.375 0 01.256.086.375.375 0
 01.049.527l-.344.416a12 12 0 002.5 1.418l.467-5.01-.559.678a.375.375
 0 01-.527.051.375.375 0 01-.05-.527l.76-.922zm-2.541 1.88a.375.375 0
 01.254.087l.681.562.684.563a.375.375 0 01.05.529.375.375 0
 01-.529.05l-.681-.564-.682-.562a.375.375 0 01-.05-.528.375.375 0
 01.273-.136Z" />
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
